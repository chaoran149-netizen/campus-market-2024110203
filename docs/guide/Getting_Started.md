Getting Started

Campus Market Seed 使用指南

⸻

1. 文档说明

本指南介绍如何开始使用 Campus Market Seed。

如果尚未完成开发环境配置，请先阅读：

docs/guide/Environment_Setup.md

完成环境配置后，再继续本指南。

⸻

2. 获取项目

克隆课程种子仓库：

git clone <课程仓库地址>
cd campus-market-seed

⸻

3. 切换 Node.js 环境

项目根目录提供：

.nvmrc

执行：

nvm use

如果当前电脑尚未安装对应版本的 Node.js：

nvm install
nvm use

确认版本：

node -v

⸻

4. 安装项目依赖

执行：

pnpm install

等待依赖安装完成。

查看 pnpm 版本：

pnpm -v

⸻

5. 启动项目

执行：

pnpm dev

浏览器访问：

http://localhost:5173

若页面显示：

项目启动成功

说明项目已经能够正常运行。

⸻

6. 浏览项目结构

建议首先浏览项目目录：

src/
docs/
scripts/
public/

重点了解：

src/
├── api
├── components
├── router
├── stores
├── views
├── App.vue
└── main.ts

以及：

docs/
├── ai
├── evidence
└── guide

理解各目录的用途，为后续项目开发做好准备。

⸻

7. 阅读课程文档

开始正式开发前，建议阅读：

* 《实训方案》
* 《需求分析》
* 《技术架构》
* 《实训计划》

上述文档位于《校园轻集市项目指导书》中。

⸻

8. AI 协作规范

本课程鼓励合理使用 AI Coding 工具辅助开发。

在整个项目开发过程中，应记录：

* 提出的 Prompt；
* AI 给出的建议；
* 自己最终采用的方案；
* 对 AI 输出的修改与验证过程。

详细要求请阅读：

docs/ai/AI_Collaboration_Card.md

⸻

9. 过程性证据

课程采用过程性评价。

请根据每天的实验任务，及时填写：

docs/evidence/

中的对应 Evidence 文档。

⸻

10. Git 提交建议

建议每完成一个独立功能后及时提交一次代码。

例如：

chore: initialize project
docs: complete Day1 evidence
feat: implement login page
fix: resolve router issue

保持良好的 Git 提交习惯，有助于项目管理与课程评价。

⸻

11. 下一步

完成以上准备工作后，请按照教师发布的《校园轻集市项目指导书》中对应日期的：

* 实验手册

开始当天的项目实践。

祝你顺利完成《校园轻集市》项目开发！