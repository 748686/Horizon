# AI 博主 Horizon 雷达：待完成项

已准备：`data/config.ai-blogger.json`、`profiles/ai-creator/` 以及 GitHub Actions 工作流 `.github/workflows/ai-blogger-radar.yml`。

## 默认方案

- **日报语言**：中文；每天 08:20（Asia/Shanghai）尝试执行。
- **内容范围**：模型/产品变化、行业信号、开源工具与研究社区；最多 12 条，按类别配额避免单一来源淹没日报。
- **默认模型**：DeepSeek `deepseek-chat`，密钥只通过 `DEEPSEEK_API_KEY` 注入，不写进仓库。
- **来源**：Hacker News、MachineLearning / LocalLLaMA、GitHub Releases、GitHub Trending RSS、Hugging Face Blog、OSS Insight、Google News。X 和 Telegram 默认关闭，避免在未授权或未确认信源前引入额外密钥/噪音。
- **发布**：生成 Markdown 并部署到 GitHub Pages 的 `gh-pages` 分支；不会部署 CloudBase。

## 仍需你提供或亲自完成的安全步骤

1. **GitHub 仓库**：请 Fork `Thysrael/Horizon` 到你的 GitHub 账户，然后把 Fork URL 发给我；或者把你已创建的目标仓库 URL 发来。
2. **模型密钥**：推荐在 Fork 的 **Settings → Secrets and variables → Actions** 中新增 `DEEPSEEK_API_KEY`。不要把密钥发到聊天中。若你想用 OpenAI、Claude、Gemini、MiniMax 或通义千问，请告诉我服务商和模型名，我会替换配置和工作流的环境变量名。
3. **验证工作流**：在 Actions 页面手动运行 `AI Blogger Horizon Radar`。成功后，在 Settings → Pages 中将 Source 设为 `Deploy from a branch`，选择 `gh-pages` / `root`。
4. **可选推送**：如需日报到飞书、钉钉、Slack 或 Discord，请提供目标平台和机器人 Webhook（建议你自行添加为 `HORIZON_WEBHOOK_URL` secret，而不是粘贴到聊天）。

## 首次验收

- GitHub Actions 的 `Generate daily briefing` 成功；
- `gh-pages` 分支出现当天 Markdown；
- Pages URL 能打开；
- 当天日报不超过 12 条，且每条含“摘要”；高分条目还应出现“可做角度”。

> 工作流已启用，但只有仓库配置了 `DEEPSEEK_API_KEY` 后才能成功生成日报；仓库中没有创建 `.env` 文件。
