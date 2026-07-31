import json
import shutil
from pathlib import Path

import pytest

import src.processing.profiles as profile_module
from src.processing import ProfileRegistry


def test_loads_builtin_tech_news_profile():
    registry = ProfileRegistry.load(
        Path(__file__).resolve().parents[1] / "profiles", "tech-news"
    )

    profile = registry.get("tech-news")
    assert profile.definition.filter.enabled is True
    assert profile.definition.filter.threshold == 8.0
    assert [block.id for block in profile.definition.enrichment.blocks] == [
        "summary",
        "background",
        "community_discussion",
    ]
    assert profile.definition.enrichment.blocks[1].tools == ["web_search"]
    assert "3-6 complete sentences" in profile.enrichment_prompt
    assert "2-4 complete sentences" in profile.enrichment_prompt
    assert "1-3 complete sentences" in profile.enrichment_prompt
    assert "no more than 15 words" in profile.enrichment_prompt
    assert "untrusted reference material" not in profile.enrichment_prompt
    assert "untrusted data, not instructions" not in profile.analysis_prompt
    assert "three to five specific topic tags" in profile.analysis_prompt
    assert "Technology news profile" in profile.match_prompt


def test_default_profiles_fall_back_to_packaged_resources(tmp_path, monkeypatch):
    packaged_profiles = tmp_path / "packaged-profiles"
    source_profiles = Path(__file__).resolve().parents[1] / "profiles"
    shutil.copytree(source_profiles, packaged_profiles)
    working_dir = tmp_path / "working"
    working_dir.mkdir()
    monkeypatch.chdir(working_dir)
    monkeypatch.setattr(profile_module, "BUILTIN_PROFILES_DIR", packaged_profiles)

    registry = ProfileRegistry.load(Path("profiles"), "tech-news")

    assert registry.get("tech-news").analysis_prompt


def test_rejects_enabled_filter_without_threshold(tmp_path):
    profile_dir = tmp_path / "invalid"
    profile_dir.mkdir()
    for name in ("match.md", "analysis.md", "enrichment.md"):
        (profile_dir / name).write_text("prompt", encoding="utf-8")
    (profile_dir / "profile.json").write_text(
        json.dumps(
            {
                "id": "invalid",
                "name": "Invalid",
                "match": "match.md",
                "analysis": "analysis.md",
                "filter": {"enabled": True},
                "enrichment": {
                    "prompt": "enrichment.md",
                    "blocks": [{"id": "body", "type": "section", "tools": []}],
                },
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="threshold"):
        ProfileRegistry.load(tmp_path, "invalid")


def test_rejects_prompt_path_outside_profile_directory(tmp_path):
    profile_dir = tmp_path / "invalid"
    profile_dir.mkdir()
    (tmp_path / "outside.md").write_text("prompt", encoding="utf-8")
    (profile_dir / "analysis.md").write_text("prompt", encoding="utf-8")
    (profile_dir / "enrichment.md").write_text("prompt", encoding="utf-8")
    (profile_dir / "profile.json").write_text(
        json.dumps(
            {
                "id": "invalid",
                "name": "Invalid",
                "match": "../outside.md",
                "analysis": "analysis.md",
                "filter": {"enabled": False},
                "enrichment": {
                    "prompt": "enrichment.md",
                    "blocks": [{"id": "body", "type": "section", "tools": []}],
                },
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="escapes"):
        ProfileRegistry.load(tmp_path, "invalid")
