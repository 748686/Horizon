---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> 从 46 条内容中筛选出 18 条重要资讯。

---

**科技新闻**
1. [Stateless MCP 2.0 发布，重燃作者兴趣并催生两个工具](#item-tech-news-1) ⭐️ 9.0/10
2. [DeepSeek-V4-Flash-0731：304B 参数的高性价比新模型](#item-tech-news-2) ⭐️ 8.0/10
3. [Arch Linux 禁用 AUR 软件包领养功能](#item-tech-news-3) ⭐️ 8.0/10
4. [MiniMax H3 多模态视频模型将于 8 月 3 日开源](#item-tech-news-4) ⭐️ 8.0/10
5. [德国法院裁定 AI 音乐公司 Suno 侵犯版权](#item-tech-news-5) ⭐️ 8.0/10
6. [电梯调度算法、权衡与真实行为](#item-tech-news-6) ⭐️ 7.0/10
7. [Hugging Face 遭入侵：可重用认证密钥成入口](#item-tech-news-7) ⭐️ 7.0/10
8. [开源权重革命：Simon Willison 谈最新模型趋势](#item-tech-news-8) ⭐️ 7.0/10
9. [法官质疑 Anthropic 风险认定，考虑永久撤销禁令](#item-tech-news-9) ⭐️ 7.0/10
10. [OpenAI 封禁柬埔寨诈骗团伙 ChatGPT 账号网络](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [纽约州起诉 Kalshi：称其运营“非法赌博业务”](#item-finance-news-1) ⭐️ 9.0/10
2. [AI 对冲基金“情境感知”因动量崩溃被迫平仓，资产从 450 亿美元缩水至约 100 亿美元](#item-finance-news-2) ⭐️ 8.0/10
3. [美国拟对留学生毕业后工作收取 10 万美元 OPT 费用](#item-finance-news-3) ⭐️ 8.0/10
4. [美股午盘异动：亚马逊、苹果、Reddit、GoDaddy 等因财报或指引大幅波动](#item-finance-news-4) ⭐️ 7.0/10
5. [美联储三位官员反对维持利率，主张立即加息以抗通胀](#item-finance-news-5) ⭐️ 7.0/10
6. [盘前综述：科技与生物科技股因财报及 FDA 消息大幅波动](#item-finance-news-6) ⭐️ 7.0/10
7. [五部门启动婚介机构乱象专项整治行动](#item-finance-news-7) ⭐️ 7.0/10

**科技博客**
1. [共同设计注意力机制：为长上下文推理提速](#item-tech-blog-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Stateless MCP 2.0 发布，重燃作者兴趣并催生两个工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.0/10

Model Context Protocol 推出 2.0 版（Stateless MCP），正式规范为 2026-07-28 版。新规范将原先需要两次 HTTP 请求（initialize 获取 Mcp-Session-Id 后再调用工具）的流程，缩减为一次带 MCP-Protocol-Version 与 Mcp-Method 等头部的请求，省去服务端会话状态，更利于构建可扩展 Web 应用。Simon Willison 认为这是 MCP 自 2024 年 11 月由 Anthropic 推出以来最重大变化，也降低了客户端与服务器实现难度；他本周用该规范构建了 mcp-explorer 与 datasette-mcp 两个项目。mcp-explorer 是可用 uvx 运行的 stateless Python CLI 工具，用于列举、检查和调用 MCP 工具；datasette-mcp 是 Datasette 插件，为实例增加 /-/mcp 端点，提供 list\_databases、get\_database\_schema、execute\_sql 三个工具，目前 execute\_sql 为只读。

rss · Simon Willison · 7月31日 23:13

**「背景」** MCP 是 Anthropic 于 2024 年 11 月推出的开放协议，旨在标准化 LLM agent 接入外部工具的方式。2025 年它被广泛采用，但后来 Skills 等方案让带终端和 curl 的 agent 能更灵活地完成许多任务，使 MCP 关注度下降；Stateless MCP 通过去除会话状态和简化请求流程，重新降低了实现与审计门槛。

**「影响」** 对 MCP 客户端和服务器开发者来说，新规范减少了 session 维护、路由同会话到同一后端等负担，使 MCP 更容易嵌入无状态 Web 服务和轻量级 CLI 工具。作者指出，相比给 agent 开放 shell 和联网能力，MCP 工具更易审计和控制，也适合在笔记本电脑上运行的小模型驱动；datasette-mcp 已让 ChatGPT/Claude 等能对托管 Datasette 实例执行只读 SQL。

**标签**: `#MCP`, `#Model Context Protocol`, `#AI agents`, `#protocols`, `#software engineering`

---

<a id="item-tech-news-2"></a>
### [DeepSeek-V4-Flash-0731：304B 参数的高性价比新模型](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 于 2026 年 7 月 31 日发布 DeepSeek-V4-Flash-0731，这是其 V4 系列的最新模型，参数量为 3040 亿（Hugging Face 上约 167GB），官方称其智能体能力大幅增强。Artificial Analysis 评估其性能超过 4280 亿参数的 MiniMax M3；API 定价为每百万输入 token 0.14 美元、每百万输出 token 0.27 美元，按 Intelligence Index 与单任务成本计算，可能是目前性价比最高的模型之一（图中约 50 分、每任务约 0.028 美元）。Simon Willison 通过 OpenRouter 实测发现，默认推理级别生成“鹈鹕骑自行车”图像效果不佳，而设置 \`reasoning\_effort high\` 后质量明显改善，说明高推理强度对该类生成任务很重要。

rss · Simon Willison · 7月31日 23:59

**「背景」** DeepSeek 是一家以开放权重模型著称的中国 AI 实验室，其 V4 系列是 2026 年发布的最新模型家族。与密集模型不同，DeepSeek 的“Flash”型号采用稀疏混合专家（MoE）架构，虽然总参数量约为 300B（来源口径在 284B 到 304B 之间），但每次推理只激活约 13B 参数，从而在较低成本下获得较强性能。该模型已在 Hugging Face 开放权重，并通过 OpenRouter 和 DeepInfra 等平台提供 API，便于开发者直接比较和调用。

**「影响」** 对开发者与 AI 应用团队而言，该模型以极低 API 价格提供接近头部模型的智能水平，可能显著降低智能体与文本生成类应用的成本；但需要留意默认参数并不总能达到最佳输出，图像生成等任务应显式调高推理强度，且本地部署需约 167GB 存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek-ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash-0731">DeepSeek V 4 Flash 0731 - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://deepinfra.com/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek-ai/ DeepSeek - V 4 - Flash - 0731 - Demo - DeepInfra</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI model`, `#agentic AI`, `#language models`, `#open source`

---

<a id="item-tech-news-3"></a>
### [Arch Linux 禁用 AUR 软件包领养功能](https://lwn.net/Articles/1086489/) ⭐️ 8.0/10

Arch Linux DevOps 团队宣布，由于“当前大量恶意软件包领养及通过 AUR 进行的后续提交”，已禁用对 AUR 孤儿软件包的领养功能。恶意负载是一个远程访问木马（RAT），它通过 Tor 网络接收命令，并尝试上传大量用户数据。此前项目在 6 月暂停了新账户注册，7 月 13 日重新开放，但新增的限制“微小且显然无效”。攻击者利用新账户领养孤儿包并推送恶意更新，从而在用户系统上安装恶意软件。这一事件凸显了 AUR 的供应链风险，影响系统管理员和依赖 AUR 的软件工程师。

rss · LWN.net · 7月31日 13:38

**「背景」** Arch Linux 用户仓库（AUR）允许用户提交软件包，而无人维护的“孤儿软件包”可由其他用户接手维护并推送更新。2025 年 6 月，Arch Linux 曾因攻击者创建新账户恶意接管孤儿软件包并推送恶意更新而暂停新账户注册，7 月 13 日重新开放并增加了限制，但这些限制似乎未能有效阻止后续攻击。此次事件中，攻击者通过恶意接管和提交将名为 CHAOS 的远程访问木马（RAT）植入多个 AUR 软件包，该木马通过 Tor 网络接收命令并尝试窃取用户数据。

**「影响」** 曾安装被恶意领养软件包的用户可能已感染该 RAT 并面临数据泄露风险；禁用领养功能会暂停孤儿包的维护流程，依赖 AUR 获取软件或更新的开发者可能因此受到影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1086489/">Arch Linux disables AUR package adoption [LWN.net]</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/arch-linux-pulls-aur-packages-that-installed-chaos-rat-malware/">Arch Linux pulls AUR packages that installed Chaos RAT malware</a></li>
<li><a href="https://archlinux.org/news/active-aur-malicious-packages-incident/">Arch Linux - News: Active AUR malicious packages incident</a></li>

</ul>
</details>

**标签**: `#security`, `#Arch Linux`, `#AUR`, `#malware`, `#supply chain`

---

<a id="item-tech-news-4"></a>
### [MiniMax H3 多模态视频模型将于 8 月 3 日开源](https://modelscope.cn/models/MiniMax/MiniMax-H3) ⭐️ 8.0/10

MiniMax 宣布其新一代通用多模态视频模型 H3 将于 2026 年 8 月 3 日在魔搭社区开源发布。该模型原生支持文本、图像、音频和视频的理解与生成，可综合解析人物、动作、声音、情感、镜头语言及创作意图，并自然融合多种参考素材进行连贯创作。模型具备多维度精准编辑控制能力，面向影视、广告、品牌、电商与游戏等商业场景，可生成包含字幕、品牌信息、特效、产品展示及 UI 动态演示在内的多样化内容。目前该消息为前瞻性预告，尚未提供技术细节或实际发布验证。

telegram · zaihuapd · 7月31日 12:37

**「背景」** MiniMax H3 是 MiniMax 推出的新一代通用多模态生成模型，能够将文本、图像、视频和音频作为同一创作上下文进行联合理解，并生成最高 2K 分辨率、时长 15 秒、带原生立体声的视频。该模型采用开放权重（open-weights）形式发布，与常见仅限 API 的视频生成模型不同，允许社区直接获取模型权重。此次公告称其将于 2026 年 8 月 3 日在魔搭社区开源，因而属于开放生态发布事件。

**「影响」** 如果该开源计划如期实现，多模态视频生成与编辑能力有望以更低门槛进入开发者和创作者的工作流，为影视、广告、电商等商业应用提供新的工具选项。但实际影响取决于发布时的模型能力、许可证条款和性能表现，目前仍存在不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H3 - Open-Weights General-Purpose Multimodal Video ...</a></li>
<li><a href="https://minimaxh3.ai/">MiniMax H3 AI Video Generator: Create Videos with Sound</a></li>

</ul>
</details>

**标签**: `#MiniMax`, `#multimodal`, `#video model`, `#open source`, `#AI`

---

<a id="item-tech-news-5"></a>
### [德国法院裁定 AI 音乐公司 Suno 侵犯版权](https://www.dw.com/en/german-court-rules-that-ai-music-firm-suno-violated-copyrights/a-78152227) ⭐️ 8.0/10

德国慕尼黑地区法院于周五裁定，美国 AI 音乐公司 Suno 侵犯版权，须披露通过侵权所得利润并支付数额待定的赔偿。Suno 表示不认同判决，将评估包括上诉在内的所有选项。该诉讼由德国音乐版权集体管理组织 GEMA 于 2025 年 1 月提起，指控 Suno 未经许可和补偿，用受版权保护的音乐训练其 AI 模型。庭审中 GEMA 演示了由 Suno 生成的歌曲与原作品高度相似。这是全球首批检验版权法如何适用于 AI 音乐训练的重大案件之一，GEMA 代表德国逾 9.5 万名音乐人及全球超 200 万名权利持有人。

telegram · zaihuapd · 7月31日 13:11

**「背景」** Suno 是一家提供 AI 音乐生成服务的公司，其模型需要使用大量已有音乐录音进行训练。GEMA 是德国的音乐作品集体管理组织，代表作曲家、词作者和出版商的权益。本案的核心争议在于，未经明确许可使用受版权保护的音乐训练 AI 模型是否构成侵权，而此次判决可能为德国未来 AI 训练行为的合法性设定先例。

**「影响」** 对 Suno 而言，该判决要求其披露利润并支付赔偿（具体金额待定），且可能面临上诉，这构成直接的法律与财务风险。该判决同时强化了 GEMA 的谈判地位，可能促使 AI 音乐公司在德国乃至更广范围寻求版权授权，但最终影响仍取决于后续上诉结果。

**标签**: `#AI`, `#copyright`, `#music`, `#legal`, `#Suno`

---

<a id="item-tech-news-6"></a>
### [电梯调度算法、权衡与真实行为](https://john.fun/elevators) ⭐️ 7.0/10

《Elevators》一文由 Jrh0203 发布在 john.fun，探讨了电梯调度算法及其权衡，并通过模拟与比较分析真实世界中的电梯行为。文章指出不同算法（如 SCAN/LOOK 与目的地派送）在不同条件下表现各异，其中目的地派送在随机目的地模拟中表现较差，但真实建筑中常见的成组同层出行模式可能改变这一结论。该内容在 Hacker News 上引发了软件工程师和系统思考者的广泛讨论，包括将电梯调度类比为磁盘调度算法。整体上这是一篇高价值的技术文章，但并非突破性或范式转变的进展。

hackernews · Jrh0203 · 7月31日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49124218)

**「背景」** 电梯调度算法决定多台电梯如何响应楼层召唤，常见方案包括 SCAN、LOOK、Otis 专有的 RSR 以及目的地派梯系统（用键盘输入目标楼层取代上下按钮）。SCAN 也被称为电梯算法或电梯调度算法，其思路与磁盘调度中的 SCAN 算法相通：磁盘寻道类似一台绕轴展开的长电梯。本文通过模拟比较这些算法的行为与取舍，社区讨论中常将电梯调度与磁盘调度（如 LOOK）进行类比。

**「社区讨论」** 评论者将电梯调度与硬盘 SCAN/LOOK 磁盘调度算法类比，并指出目的地派送表现不佳可能是随机目的地模拟造成的假象，真实建筑中的常见模式（如同层员工群体同时前往同一楼层）会改变算法效果。还有人分享了 Elevator Saga 游戏和开发 Sky Lobby 游戏时选择 LOOK 算法的经验，并提到用户经常同时按上下按钮这一现实问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://elsolitario.org/en/2026/07/31/elevator-algorithms-scan-look-rsr/">Elevator Algorithms: SCAN, LOOK, and RSR Explained</a></li>
<li><a href="https://dev.to/thesaltree/elevator-scheduling-algorithms-fcfs-sstf-scan-and-look-2pae">Elevator Scheduling Algorithms: FCFS, SSTF, SCAN, and LOOK SCAN (Elevator) Disk Scheduling Algorithms - GeeksforGeeks Traditional and Real-Time Elevator Scheduling Algorithms Diving into Go: Implementing Classic Elevator Scheduling ... The Elevator Problem: Scheduling and Load Balancing elevator algorithm — Visual Explainer | Vectree</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/scan-elevator-disk-scheduling-algorithms/">SCAN (Elevator) Disk Scheduling Algorithms - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#elevator algorithms`, `#scheduling`, `#simulation`, `#software engineering`, `#systems`

---

<a id="item-tech-news-7"></a>
### [Hugging Face 遭入侵：可重用认证密钥成入口](https://tailscale.com/blog/hugging-face-intrusion) ⭐️ 7.0/10

Tailscale 发布事件分析，解释 Hugging Face 入侵事件中攻击者利用一枚可重用的 Tailscale 认证密钥进入其 tailnet，并非利用 Tailscale 产品漏洞。该密钥被复制到外部沙箱并在数天内注册了 181 个 CI 节点，获得 CI 节点身份标签所对应的访问权限。事件中涉及的 136 个凭证中包括这一枚可重用密钥；Tailscale 强调没有漏洞被利用，但作为安全工具仍将此视为自身入侵并承担责任。此事件显示长期有效的可重用认证密钥和缺乏来源或目标绑定的访问控制是实际风险，也暴露了相关告警机制的不足。

hackernews · bluehatbrit · 7月31日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49127306)

**「背景」** Tailscale 是一种基于 WireGuard 的网格 VPN，通过 tailnet 将设备组成私有网络；认证密钥用于允许新节点加入，并可设置为一次性或可重用。Hugging Face 是 AI 模型托管平台，此前披露了安全事件；本次风波的核心并非 VPN 被攻破，而是认证凭证被盗用。

**「影响」** 使用 Tailscale 等网格 VPN 的组织应审查认证密钥的生命周期和复用策略，将 CI 等动态节点的密钥绑定来源或目的地，并配置异常节点注册告警；否则类似可重用密钥泄露可能绕过网络边界，扩大攻击面。

**「社区讨论」** 评论者态度不一，有人赞赏 Tailscale 透明处理并认为道歉令人满意，也有人觉得这是巧妙营销。技术讨论集中在告警机会：用可重用密钥在几天内注册 181 个节点应触发提醒，且密钥应按来源或目标进行范围限制，例如仅在带有 ci\_node 属性的机器上使用。

**标签**: `#security`, `#tailscale`, `#hugging-face`, `#credential-management`, `#postmortem`

---

<a id="item-tech-news-8"></a>
### [开源权重革命：Simon Willison 谈最新模型趋势](https://simonwillison.net/2026/Jul/31/oxide-and-friends/#atom-everything) ⭐️ 7.0/10

Simon Willison 于周一参加 Oxide and Friends 播客，与 Bryan Cantrill 和 Adam Leventhal 讨论近期开源权重模型的激增，重点提到 Kimi K3 证明开源权重模型能与专有前沿模型正面竞争。他们还谈到 OpenAI 遭遇的意外网络安全攻击，以及几乎所有 AI 重要人物签署的《开放式权重与美国 AI 领导力》公开信，唯一显著例外是 Anthropic。Willison 指出，由于几天后 DeepSeek V4 Flash 0731 发布和 Anthropic 自身的尴尬网络安全事件发生，这期对话已经过时。节目还涉及 Golden Gate Claude、Zizians、阿拉米达野生火鸡袭击、苏联马尔堡病毒研究和铅犯罪假说等话题。他们回顾了 1 月的预测，并新增预测：今年年底前教宗会说一些关于开放模型的话。

rss · Simon Willison · 7月31日 21:33

**「背景」** 开源权重模型是指公开模型权重、允许本地运行和微调的大语言模型，区别于仅通过 API 提供的封闭前沿模型。2026 年 7 月底，Kimi K3 等模型展示了开源权重路线可与专有模型竞争，促使微软等机构发布关于开源权重与美国 AI 领导力的公开信，几乎所有主要 AI 公司签署，而 Anthropic 未签署。

**「影响」** 对于依赖本地 LLM 部署的开发者，节目中讨论的 Kimi K3 表现以及节目录制后发布的 DeepSeek V4 Flash 0731，进一步表明开源权重模型可作为封闭 API 之外的有力替代。Anthropic 未签署公开信这一事实，也凸显出企业在开源权重安全问题上的立场分歧，可能影响开发者对模型提供方的选择与合规评估。

**标签**: `#open-weights`, `#AI`, `#podcast`, `#LLM`, `#industry-news`

---

<a id="item-tech-news-9"></a>
### [法官质疑 Anthropic 风险认定，考虑永久撤销禁令](https://techcrunch.com/2026/07/30/judge-says-trump-admin-still-lacks-evidence-for-anthropic-supply-chain-risk-label/) ⭐️ 7.0/10

美国联邦地区法官 Rita Lin 在周四听证会上表示，特朗普政府仍未提供足够证据，证明将 Anthropic 列为“供应链风险”并禁止联邦政府使用其 AI 技术的决定合理，她正考虑永久撤销禁令。政府因 Anthropic 公开批评国防部而实施封禁，Lin 称这一逻辑“非常令人不安”，可能开创报复与政府意见不合的联邦承包商的先例，并指出案卷记录“在某些方面对政府而言变得更糟了”。争端源于 Anthropic 与国防部合同谈判破裂：Anthropic 要求其 AI 不用于大规模监控或致命武器决策，国防部则认为私营企业不应规定军方如何使用技术。Anthropic 于 3 月提起两起诉讼，Lin 此前已临时叫停封禁，目前正考虑是否永久撤销；政府律师称计划在 9 月 30 日前完成停用 Anthropic 产品。该案涉及 AI 治理、政府合同、言论自由与行政权力边界，但属于法律程序进展而非技术突破。

telegram · zaihuapd · 7月31日 08:00

**「背景」** 美国联邦采购制度允许政府以“供应链风险”为由限制特定公司的产品，但该案的核心争议在于，政府是否能因承包商公开批评国防部而将其列入风险名单并禁止使用。Anthropic 与国防部就 AI 军事用途的合同条款未能达成一致，随后于 3 月提起诉讼，挑战封禁决定。

**「影响」** 若法官作出永久禁令，Anthropic 与联邦机构的合同关系可能恢复，且政府以企业公开表态作为封禁理由将更难成立；反之，若政府胜诉，AI 公司在国防合同中坚持人权与武器使用限制条款时可能面临更大压力。目前法院尚未作出最终裁定，这些影响仍未确定。

**标签**: `#Anthropic`, `#AI regulation`, `#US government`, `#supply chain`, `#legal`

---

<a id="item-tech-news-10"></a>
### [OpenAI 封禁柬埔寨诈骗团伙 ChatGPT 账号网络](https://openai.com/index/disrupting-malicious-uses-of-ai-criminal-scam-operation/) ⭐️ 7.0/10

OpenAI 于 2026 年 8 月 4 日（原文如此，后改为 7 月 31 日）宣布，封禁了一个疑似位于柬埔寨波贝市的 ChatGPT 账号网络。该团伙利用 ChatGPT 同时开展投资诈骗、杀猪盘、赌博和冒充执法人员等多类骗局，并生成虚假人设、翻译与受害者的对话、伪造护照和法律文书图片。OpenAI 根据 WhatsApp 提供的线索展开调查，已与行业伙伴和有关部门共享威胁信息。部分账号还生成过疑似涉及人口贩运和强迫劳动的内容，例如以机票住宿为饵在波贝招聘“聊天员”，与公开报道中东南亚犯罪集团诱拐劳工的情况吻合。OpenAI 表示该网络可能与数百名目标接触，单个受害者损失数千美元，但具体金额无法核实。

telegram · zaihuapd · 7月31日 23:41

**「背景」** “杀猪盘”是一种以建立情感关系为基础的诈骗手法，骗子先打造虚假人设取得受害者信任，再诱导其投资或转账，得手后失联；此类骗局常由东南亚有组织犯罪团伙运营，成员会通过社交媒体和聊天应用大量物色目标。AI 服务的兴起使诈骗团伙能够低成本生成可信文案、伪造身份和翻译对话，从而扩大攻击规模并提高欺骗性。

**「影响」** 对相关诈骗团伙而言，账号封禁会中断其现有 ChatGPT 账号和配套的内容生成流程，迫使其更换工具或投入更多资源绕过检测；对行业而言，OpenAI 与 WhatsApp 及行业伙伴共享情报，可能帮助平台识别关联账号并阻止类似滥用，但具体威慑效果尚不确定。

**标签**: `#AI safety`, `#OpenAI`, `#ChatGPT misuse`, `#scam`, `#policy`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [纽约州起诉 Kalshi：称其运营“非法赌博业务”](https://www.cnbc.com/2026/07/31/new-york-sues-kalshi-claims-it-is-illegal-gambling-operation.html) ⭐️ 9.0/10

纽约州于 7 月 31 日对预测市场平台 Kalshi 提起诉讼，指控其未向州博彩委员会注册，构成“非法赌博经营”。州检察长詹乐霞和州长霍楚尔要求法院永久禁止 Kalshi 运营，并寻求向用户退款、每次体育博彩要约罚款 10 万美元、以及按违法所得的三倍处罚，州方估计总额可能达 360 亿美元。Kalshi 总部位于纽约市，公司在联邦法院已与纽约州及商品期货交易委员会（CFTC）陷入管辖权争议。

rss · CNBC Finance · 7月31日 15:31

**「名词解释」** 预测市场是让用户就“某事件是否发生”下注的平台，例如选举或体育比赛结果；纽约州认为这类体育合约等同于体育博彩，应受州法规管，而 Kalshi 和联邦监管机构 CFTC 则认为它们是“互换合约”，由联邦专属监管。简单说，争议核心是“谁有权监管预测市场”。

**「潜在影响」** 若法院支持纽约州，Kalshi 可能被迫暂停或大幅调整在纽约乃至全美的体育类预测产品，并面临巨额罚款和赔偿，其用户也可能无法继续使用相关功能；同时，这一案件可能影响其他预测市场平台的合法性和监管方向。目前法院尚未作出最终裁决，实际后果仍不确定。

**标签**: `#prediction markets`, `#regulation`, `#lawsuit`, `#CFTC`, `#New York`

---

<a id="item-finance-news-2"></a>
### [AI 对冲基金“情境感知”因动量崩溃被迫平仓，资产从 450 亿美元缩水至约 100 亿美元](https://www.cnbc.com/2026/07/31/why-leopold-aschenbrenner-situational-awareness-hedge-fund-imploded.html) ⭐️ 8.0/10

Leopold Aschenbrenner 旗下的 AI 主题对冲基金“情境感知”（Situational Awareness）在经历一场历史性的动量崩溃后迅速崩盘：其管理资产从约 450 亿美元缩水至约 100 亿美元，并将公开交易的股票持仓折价出售给 Citadel。该基金同时押注 AI 基础设施股上涨和软件股下跌，但两类头寸同时亏损，触发保证金追缴和强制平仓。

rss · CNBC Finance · 7月31日 16:14

**「关键概念解释」** “动量崩溃”指原本持续上涨的股票突然集体大幅下跌，导致依赖趋势的量化策略在极短时间内遭受巨大损失。这里还涉及“保证金追缴”：基金用借来的钱放大投资（即杠杆），当持仓市值下降时，券商要求追加现金担保，基金被迫卖出更多持仓来筹集资金，从而进一步压低股价，形成“去杠杆螺旋”。

**「影响」** 受此事件影响，AI 基础设施股票此前数周大幅波动，但在最大强制卖家退出后出现反弹；不过并非所有人都认为抛售已结束，知名投资者 Michael Burry 反而在市场反弹时增加了对 AI 相关股票的看跌押注。这一案例也警示了使用高杠杆的投资者：即使大盘看似平稳，集中的杠杆策略也可能迅速崩盘。

**标签**: `#hedge fund`, `#AI stocks`, `#momentum crash`, `#margin call`, `#leverage`

---

<a id="item-finance-news-3"></a>
### [美国拟对留学生毕业后工作收取 10 万美元 OPT 费用](https://www.bloomberg.com/news/articles/2026-07-30/trump-weighs-100-000-fee-for-foreign-students-to-work-post-grad) ⭐️ 8.0/10

特朗普政府正考虑向国际学生收取 10 万美元费用，以获准毕业后留美工作，这笔费用针对“选择性实践培训”（OPT）项目。知情人士称，去年秋季有近 30 万国际学生持 OPT 留美；白宫官员表示暂无即将出台的政策变化，但未否认正在讨论。此前政府已将学生签证居留期限缩短为四年，并曾推动对 H-1B 签证收取同等费用，但该费用在 2026 年 6 月被联邦法官裁定违法，政府正在上诉。

telegram · zaihuapd · 7月31日 09:00

**「关键概念」** OPT 全称“选择性实践培训”（Optional Practical Training），是允许持 F-1 学生签证的国际学生在毕业后留美工作最长 12 个月的项目，STEM 专业可再延长 24 个月。10 万美元费用是拟议中的额外收费，并非已正式实施的政策。

**「影响」** 若该费用落地，最直接受影响的将是依赖 OPT 留美工作的约 30 万国际毕业生，以及聘用这些毕业生的科技、金融等行业企业，后者的用人成本可能明显上升；依赖国际学生学费的高校也可能因生源减少而受损。不过，该提案仍在讨论阶段，且类似 H-1B 收费已遭法院否决，因此实际实施时间和形式仍有较大不确定性。

**标签**: `#immigration-policy`, `#higher-education`, `#tech-industry`, `#labor-market`, `#visa`

---

<a id="item-finance-news-4"></a>
### [美股午盘异动：亚马逊、苹果、Reddit、GoDaddy 等因财报或指引大幅波动](https://www.cnbc.com/2026/07/31/stocks-making-the-biggest-moves-midday-aapl-amzn-rddt-gddy-iesc.html) ⭐️ 7.0/10

截至 2026 年 7 月 31 日午盘，多只个股因财报和公司指引出现大幅波动：亚马逊大涨 15%，云业务收入同比增长 37%、超出预期；苹果下跌逾 9%，尽管 iPhone 销售额增长 22%；Reddit 跌 22%，因来自谷歌的搜索推荐流量“不稳”；GoDaddy 跌 20%，因全年指引不及华尔街预期；Replimune 涨逾 94%，因美国食品药品监督管理局（FDA）顾问委员会支持其皮肤癌药物 RP1 的试验结果。这些大多是市场对业绩数字和公司未来展望的直接反应。

rss · CNBC Finance · 7月31日 17:42

**「关键概念」** “指引”（guidance）指公司自己给出的未来收入、利润等业绩预测；当指引高于或低于华尔街分析师的普遍预期，股价常会迅速反应。文中“同比增长 37%”指与去年同期相比增长 37%，这种比较可以排除季节性因素，更直观地看出业务是否加速。

**「影响」** 最直接的影响是这些公司的股东在午盘看到市值大幅变动；例如亚马逊云业务加速增长可能利好云计算相关产业链，但单日涨跌并不代表长期趋势。对普通消费者来说，这些财报变化短期内通常不会直接改变商品或服务价格，除非后续公司调整投资、定价或经营策略。

**标签**: `#Earnings`, `#Stock Movers`, `#Cloud Computing`, `#FDA Approval`, `#Guidance`

---

<a id="item-finance-news-5"></a>
### [美联储三位官员反对维持利率，主张立即加息以抗通胀](https://www.cnbc.com/2026/07/31/fed-officials-who-voted-to-hike-rates-say-action-is-needed-now-against-inflation.html) ⭐️ 7.0/10

在 2026 年 7 月的美联储会议上，三位地方联储行长——克利夫兰的哈马克、明尼阿波利斯的卡什卡利和达拉斯的洛根——公开反对委员会维持利率不变的决定，主张现在加息以抑制通胀。其余九名投票委员同意将联邦基金利率目标区间保持在 3.5%-3.75%不变。美联储主席沃什投了支持票，但也表示通胀仍需回落到 2%目标。

rss · CNBC Finance · 7月31日 14:35

**「名词解释」** 联邦公开市场委员会\(FOMC\)是美联储制定利率的机构；委员投“反对票”表示不同意多数派的决定，不代表立刻改变政策。这三位官员担心通胀已经高于 2%目标超过五年，拖延会让物价上涨更难控制。

**「可能影响」** 由于本次会议决定维持利率不变，家庭和企业的贷款成本不会立即变化；但如果未来加息，房贷、车贷和信用卡等浮动利率借款的利息可能上升。

**标签**: `#Federal Reserve`, `#monetary policy`, `#inflation`, `#interest rates`, `#FOMC`

---

<a id="item-finance-news-6"></a>
### [盘前综述：科技与生物科技股因财报及 FDA 消息大幅波动](https://www.cnbc.com/2026/07/31/stocks-making-the-biggest-moves-premarket-repl-cvx-aapl-amzn-mrna.html) ⭐️ 7.0/10

在最新财报和监管消息公布后，多只股票在盘前交易中大幅波动。Replimune 因 FDA 顾问委员会投票支持其皮肤癌药物 RP1 而大涨超 130%，Wedbush 随即上调其评级；Amazon 因云业务收入同比增 37%、超过市场预期且创 18 个季度最快增速而涨逾 11%；Apple 尽管 iPhone 销售增长 22%、整体营收好于预期，股价仍跌逾 7%。此外，诺和诺德因三期试验失败跌逾 10%，Chevron 净利润为 121 亿美元、同比增近 400%，Moderna 虽然二季度业绩好于预期仍跌逾 4%。

rss · CNBC Finance · 7月31日 12:30

**「解读」** “盘前”指美股正式开盘前的交易时段，价格会快速反映隔夜财报、监管和新闻消息；“同比”意思是与去年同期相比。文中提到的 FDA 顾问委员会投票是独立专家对药品证据的评估意见，虽不具最终法律效力，但通常是 FDA 审批决定的重要参考。

**「影响」** 对持有这些个股的投资者来说，盘前价格波动直接影响持仓市值；对相关患者而言，Replimune 获专家支持可能增加疗法获批希望，而诺和诺德三期失败则意味着该药在心血管领域的前景受挫。最终影响仍取决于 FDA 正式决定、后续临床结果和监管审查，不应视为确定的投资或治疗结论。

**标签**: `#premarket movers`, `#corporate earnings`, `#FDA decision`, `#biotech`, `#technology`

---

<a id="item-finance-news-7"></a>
### [五部门启动婚介机构乱象专项整治行动](https://www.peopleapp.com/column/30052813314-500007628513) ⭐️ 7.0/10

民政部会同中央网信办、工业和信息化部、公安部、市场监管总局，于 2026 年 7 月 28 日联合印发工作方案，并于 7 月 30 日召开电视电话会议，部署整治婚介机构乱象专项行动。行动从 2026 年 7 月持续至 2027 年 2 月，聚焦虚假营销、“婚托”欺诈、收费管理混乱、个人信息泄露滥用等七类重点问题。

telegram · zaihuapd · 7月31日 14:00

**「关键词解释」** 婚介机构乱象是指婚介机构在提供相亲、婚恋介绍服务时出现的虚假宣传、雇人冒充相亲对象、违规收费、泄露客户个人信息等问题。专项行动是政府部门集中一段时间开展检查、处罚和规范，目的是通过查处违规行为、曝光典型案例，推动行业整改。

**「影响」** 这项行动可能让使用婚介服务的消费者在虚假宣传和乱收费方面得到更多保护，也可能减少个人信息被泄露的风险。对婚介机构而言，不合规经营会面临更严格的检查和处罚，但实际效果还要看各地落实和执法力度。

**标签**: `#regulation`, `#marriage agencies`, `#consumer protection`, `#China`, `#policy`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [共同设计注意力机制：为长上下文推理提速](https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/) ⭐️ 8.0/10

rss · NVIDIA Inference Performance Blog · 7月31日 22:16

**「背景」** 随着智能体与长上下文负载普及，注意力在推理耗时中的占比持续上升。作者认为，注意力的架构设计本身——而非仅仅实现优化——越来越成为决定推理性能的关键，并据此分析如何在 NVIDIA GPU 上共同设计模型注意力。

**「方案」** 作者从 GEMM 形状算术和 FP8 测量出发，区分了 prefill 与 decode 的瓶颈：prefill 的 GEMM-M 是大规模 ISL×G，受计算限制；decode 每步只产生 G 的小 GEMM，受 KV 缓存读带宽限制。由此得到四项协同设计准则：第一，组大小 G 对 prefill 几乎无影响，但解码的算术强度约等于 2G，因此应尽量提高 G（并结合投机解码）；第二，头维度不改变算术强度，但 Hsz=64 仍需付 128 宽 tile 的代价，Hsz≥512 接近 TMEM 上限，128 或 256 最划算，较大头维度还能摊销 prefill 的 softmax；第三，序列长度成本不对称，prefill 随 ISL² 增长、decode 随 KVSL 线性增长，应通过 KV 缓存压缩、稀疏/滑窗注意力或混合架构减少有效 KV 状态；第四，张量并行会切分 KV 头，应保持 TP≤KH，否则会复制 KV 状态，少数 KV 头的模型可用 ADP/KVP 加 EP 的 Wide EP 或 Helix 并行。

**「启示」** 作者的核心结论是：注意力推理性能可以通过架构层面的协同设计显著改善。模型开发者把组大小、头维度、KV 状态与并行策略作为一个整体来权衡，就能在相同硬件上提升吞吐与交互性。

**标签**: `#attention mechanisms`, `#inference optimization`, `#GPU performance`, `#GQA`, `#model co-design`

---