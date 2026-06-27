Environment Setup

《校园轻集市》课程开发环境配置指南

⸻

1. 文档说明

本指南用于配置《校园轻集市》课程所需的开发环境。

开发环境通常只需配置一次，后续所有课程项目均可复用。

完成本指南后，请继续阅读：

docs/guide/Getting_Started.md

开始项目实践。

⸻

2. 为什么需要统一开发环境？

软件工程项目通常由多人协作完成。

如果开发人员使用不同版本的 Node.js、不同的包管理器或不同的开发工具，可能会导致：

* 项目无法启动；
* 依赖安装失败；
* 编译结果不一致；
* 运行结果不同；
* 难以定位和解决问题。

因此，本课程采用统一的开发环境基线（Course Development Baseline），保证所有同学在相同的软件环境下完成项目开发。

⸻

3. 课程开发环境基线

本项目通过以下配置共同约束开发环境。

配置	作用
.nvmrc	声明项目要求的 Node.js 版本
package.json 中的 packageManager	声明项目使用的包管理器及版本
.editorconfig	统一代码缩进、编码及换行格式
.vscode/settings.json	推荐统一 VS Code 配置
.gitignore	统一版本管理规则

上述配置属于课程基础设施，请勿随意修改。

⸻

4. 推荐开发软件

建议使用以下开发环境完成本课程。

软件	推荐版本	用途
Git	最新稳定版	版本管理
nvm	最新稳定版	Node.js 版本管理
Node.js	24.12.0 或以上	JavaScript 运行环境
pnpm	11.x	项目依赖管理
VS Code	最新稳定版	代码编辑器
AI Coding 工具	自行选择	AI 辅助开发

推荐 AI Coding 工具包括：

* GitHub Copilot
* Cursor
* Trae
* Opencode
* 通义灵码

教师不限制 AI 工具选择，但要求记录 AI 协作过程。

⸻

5. 配置开发环境

建议按照以下顺序完成开发环境配置。

（1）安装 Git

安装完成后，执行：

git --version

确认 Git 已正确安装。

⸻

（2）安装 nvm

安装完成后，执行：

nvm --version

确认 nvm 已正确安装。

⸻

（3）安装课程要求的 Node.js

执行：

nvm install 24.12.0

设置默认版本：

nvm alias default 24.12.0

切换至课程要求的版本：

nvm use 24.12.0

验证：

node -v

应输出：

v24.12.0

⸻

（4）启用包管理器

本课程使用 pnpm 管理项目依赖。

项目已经在 package.json 中声明：

"packageManager": "pnpm@11.9.0"

首次配置时，建议启用 Corepack：

corepack enable
corepack prepare pnpm@11.9.0 --activate

验证：

pnpm -v

应输出：

11.9.0

⸻

（5）配置镜像源（推荐）

为了提高依赖下载速度，建议配置国内镜像：

pnpm config set registry https://registry.npmmirror.com

验证：

pnpm config get registry

应输出：

https://registry.npmmirror.com

⸻

（6）安装 VS Code

建议安装最新版 VS Code。

推荐启用：

* 自动保存；
* 保存时自动格式化；
* TypeScript 支持；
* ESLint 支持。

⸻

（7）安装推荐插件

建议安装：

* Vue - Official
* ESLint
* GitLens
* Markdown All in One
* Error Lens

根据所使用的 AI Coding 工具安装对应插件。

⸻

6. 环境验证

完成以上配置后，执行：

git --version
nvm --version
node -v
pnpm -v

若均能正确输出版本信息，则说明开发环境已准备完成。

⸻

7. 常见问题

Node.js 版本错误

执行：

nvm use

即可切换至课程要求的 Node.js 版本。

⸻

pnpm 版本错误

执行：

corepack prepare pnpm@11.9.0 --activate

重新打开终端即可。

⸻

无法安装依赖

检查镜像配置：

pnpm config get registry

确认网络连接正常后重新执行：

pnpm install

⸻

8. 下一步

开发环境准备完成后，请继续阅读：

docs/guide/Getting_Started.md

开始 Day1 的项目实践。