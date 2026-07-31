import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from src.ai.enricher import ContentEnricher
from src.models import (
    ClassificationResult,
    ContentAnalysis,
    ContentBlock,
    ContentItem,
    ProcessingResult,
    SourceType,
)
from src.processing import ProfileRegistry
from src.processing.tools import ToolResult


PROFILES = ProfileRegistry.load(
    Path(__file__).resolve().parents[1] / "profiles", "tech-news"
)


def make_item() -> ContentItem:
    return ContentItem(
        id="rss:test:item",
        source_type=SourceType.RSS,
        title="A technical release",
        url="https://example.com/item",
        content="A project released a new architecture.",
        published_at=datetime.now(timezone.utc),
        profile="tech-news",
        processing=ProcessingResult(
            classification=ClassificationResult(
                profile="tech-news", method="source_override"
            ),
            analysis=ContentAnalysis(
                score=8.5,
                reason="Important release",
                summary="A new architecture was released.",
                tags=["systems"],
            ),
        ),
    )


class FakeTools:
    names = {"web_search"}

    async def execute(self, request_id, block_id, tool, arguments):
        assert block_id == "background"
        assert tool == "web_search"
        assert arguments == {"query": "project architecture"}
        return ToolResult(
            request_id=request_id,
            block_id=block_id,
            tool=tool,
            results=[
                {
                    "title": "Project documentation",
                    "url": "https://docs.example.com/project",
                    "text": "Architecture background.",
                }
            ],
        )


def test_enrichment_generates_blocks_and_validated_sources():
    responses = iter(
        [
            json.dumps(
                {
                    "tool_requests": [
                        {
                            "block_id": "background",
                            "tool": "web_search",
                            "arguments": {"query": "project architecture"},
                            "purpose": "Explain the existing architecture",
                        }
                    ]
                }
            ),
            json.dumps(
                {
                    "title": "新架构发布",
                    "lead": "",
                    "blocks": [
                        {
                            "id": "summary",
                            "type": "section",
                            "role": "summary",
                            "title": "摘要",
                            "content": "项目发布了新的架构，它改变了系统设计，并采用了新的边界。",
                            "source_refs": [],
                        },
                        {
                            "id": "background",
                            "type": "section",
                            "role": "background",
                            "title": "未隔离的背景",
                            "content": "这个版本应被丢弃。",
                            "source_refs": [],
                        },
                    ],
                }
            ),
            json.dumps(
                {
                    "title": "",
                    "lead": "",
                    "block": {
                        "id": "background",
                        "type": "section",
                        "role": "background",
                        "title": "背景",
                        "content": "旧架构的背景信息。",
                        "source_refs": ["tool-1-1"],
                    },
                }
            ),
        ]
    )
    requests = []

    async def complete(**kwargs):
        requests.append(kwargs)
        return next(responses)

    item = make_item()
    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["zh"],
        tools=FakeTools(),
    )
    asyncio.run(enricher._enrich_item(item))

    artifact = item.processing.artifacts["zh"]
    assert artifact.title == "新架构发布"
    assert [block.id for block in artifact.blocks] == [
        "summary",
        "background",
    ]
    assert artifact.blocks[-1].title == "背景"
    assert artifact.sources[0].url == "https://docs.example.com/project"
    assert len(requests) == 3
    assert "explicitly mentioned in the item" in requests[0]["system"]
    assert "Treat the source item as the primary account" in requests[1]["system"]
    assert "Treat the source item as the primary account" in requests[2]["system"]
    assert "https://docs.example.com/project" not in requests[1]["user"]
    assert "https://docs.example.com/project" in requests[2]["user"]


def test_enrichment_rejects_tool_on_unapproved_block():
    async def complete(**kwargs):
        return json.dumps(
            {
                "tool_requests": [
                    {
                        "block_id": "summary",
                        "tool": "web_search",
                        "arguments": {"query": "unapproved"},
                        "purpose": "Rewrite the news",
                    }
                ]
            }
        )

    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["zh"],
        tools=FakeTools(),
    )

    with pytest.raises(ValueError, match="not allowed"):
        asyncio.run(enricher._enrich_item(make_item()))


def test_enrichment_rejects_malformed_tool_plan():
    async def complete(**kwargs):
        return "[]"

    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["zh"],
        tools=FakeTools(),
    )

    with pytest.raises(ValueError, match="tool plan"):
        asyncio.run(enricher._enrich_item(make_item()))


def test_enrichment_rejects_cross_block_source_reference():
    block = ContentBlock(
        id="summary",
        type="section",
        role="summary",
        title="News",
        content="Content",
        source_refs=["tool-1-1"],
    )
    tool_result = ToolResult(
        request_id="tool-1",
        block_id="background",
        tool="web_search",
        results=[
            {
                "title": "Source",
                "url": "https://example.com/source",
                "text": "Context",
            }
        ],
    )

    with pytest.raises(ValueError, match="unknown source refs"):
        ContentEnricher._validate_blocks(
            [block], PROFILES.get("tech-news"), [tool_result]
        )


def test_enrichment_batch_raises_when_an_item_fails():
    async def complete(**kwargs):
        raise RuntimeError("AI unavailable")

    item = make_item()
    enricher = ContentEnricher(
        SimpleNamespace(complete=complete),
        PROFILES,
        ["zh"],
        tools=FakeTools(),
    )

    async def fail_enrichment(failed_item):  # type: ignore[no-untyped-def]
        raise RuntimeError("AI unavailable")

    enricher._enrich_item = fail_enrichment  # type: ignore[method-assign]

    with pytest.raises(RuntimeError, match=item.id):
        asyncio.run(enricher.enrich_batch([item]))
