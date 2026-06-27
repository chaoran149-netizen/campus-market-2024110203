Campus Market Seed

《校园轻集市》AI 辅助前端工程实践课程种子仓库

⸻

项目简介

Campus Market Seed 是《校园轻集市》课程的统一种子仓库（Seed Repository）。

本仓库不仅提供 Vue 3 前端项目模板，还包含课程文档、开发规范、AI 协作规范、过程性证据模板以及自动检测框架，为整个实训提供统一的开发基础。

本仓库是所有同学开展项目实践的起点。

⸻

项目目标

通过本课程，你将完成一个基于 Vue 3 的校园轻集市前端项目，并体验真实的软件工程开发流程。

课程重点包括：

* Vue 3 工程化开发
* Git 版本管理
* AI Coding 协作开发
* 软件工程规范
* 过程性证据管理
* 项目验收与自动检测

⸻

快速开始

首次使用本仓库，请按照以下顺序阅读文档：

README.md
    │
    ▼
docs/guide/Environment_Setup.md
    │
    ▼
docs/guide/Getting_Started.md

随后执行：

git clone <课程仓库地址>
cd campus-market-seed
nvm use
pnpm install
pnpm dev

浏览器访问：

http://localhost:5173

如果页面显示：

项目启动成功

说明开发环境已经配置完成。

⸻

项目结构

campus-market-seed
├── docs
│   ├── ai              # AI 协作规范
│   ├── evidence        # 每日过程证据
│   └── guide           # 学生使用指南
├── scripts             # 自动检测工具
├── src                 # 项目源码
└── CHECK_REPORT.md     # 自动检测报告（后续版本启用）

⸻

文档导航

文档	说明
docs/guide/Environment_Setup.md	配置课程开发环境
docs/guide/Getting_Started.md	Day1 快速开始指南
docs/ai/AI_Collaboration_Card.md	AI 协作记录规范
docs/evidence/	每日过程性证据模板

⸻

技术栈

* Vue 3
* TypeScript
* Vite
* Vue Router
* Pinia
* ESLint
* Oxlint

⸻

开发规范

在整个实训过程中，请遵循以下要求：

* 使用 Git 管理项目开发过程；
* 每完成一个独立功能及时提交 Commit；
* 合理使用 AI Coding 工具辅助开发；
* 保留 AI 协作记录；
* 每天完成对应的 Evidence；
* 保持项目始终能够正常运行。

⸻

后续版本

后续版本将逐步提供：

* 自动检测工具（Check Engine）
* 自动评分报告
* Git 提交分析
* AI 协作分析
* 教师验收工具

⸻

License

本仓库仅用于《校园轻集市》课程教学与实践。