# Day1 Evidence

## Task4 AI 协作体验

**使用的 AI Coding 工具：** Opencode

---

### 任务：分析项目目录结构

**Prompt：**

> 分析项目目录结构

**AI 输出：**

项目根目录 `campus-market-seed/` 结构如下：

```
campus-market-seed/
├── .vscode/              # VSCode 配置（推荐扩展、设置）
├── docs/                 # 文档（ai协作记录、证据、指南）
├── public/               # 静态资源（favicon.ico）
├── scripts/              # 工具脚本
├── src/                  # 源代码
│   ├── api/              # API 接口层
│   ├── components/       # 公共组件
│   ├── router/           # 路由配置
│   ├── stores/           # Pinia 状态管理
│   ├── views/            # 页面视图组件
│   ├── App.vue           # 根组件
│   └── main.ts           # 应用入口
├── .editorconfig         # 统一代码风格
├── .gitignore
├── .nvmrc                # Node.js 版本约束
├── .oxlintrc.json        # oxlint 配置
├── env.d.ts              # 环境类型声明
├── eslint.config.ts      # ESLint 配置
├── index.html            # HTML 入口
├── package.json
├── pnpm-lock.yaml
├── tsconfig*.json        # TypeScript 配置
├── vite.config.ts        # Vite 构建配置
├── VERSION.md
└── CHECK_REPORT.md
```

**自己的理解：**

项目按功能分层，src 下分为 api/components/router/stores/views 五个核心目录，分别管理接口、组件、路由、状态和页面。配置文件集中在根目录，文档放在 docs 下，结构清晰、职责明确，适合作为前端实训种子项目。

**最终结论：**

项目使用标准 Vue 3 工程化结构，目录划分规范，利于后续功能扩展。

---

### 任务：解释 main.ts

**Prompt：**

> 解释 main.ts

**AI 输出：**

`src/main.ts:1-12` — 应用的启动入口：

```ts
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())   // 注册 Pinia 状态管理
app.use(router)          // 注册 Vue Router
app.mount('#app')        // 挂载到 index.html 的 <div id="app">
```

执行顺序：创建 Vue 应用实例 → 依次安装 Pinia、Router 插件 → 挂载到 DOM。

**自己的理解：**

main.ts 是项目的"开机键"。先通过 createApp 创建 Vue 实例，然后用 use() 方法安装 Pinia（管理全局数据）和 Router（控制页面跳转），最后 mount 到 index.html 中的 div#app 上。整个流程简短清晰，是 Vue 3 项目的标准入口写法。

**最终结论：**

main.ts 完成了 Vue 应用的初始化、插件注册和挂载三步操作。

---

### 任务：解释 router 的作用

**Prompt：**

> 解释 router 的作用

**AI 输出：**

`src/router/index.ts:1-15` — 使用 vue-router（v5）的 createWebHistory（HTML5 History 模式）。

当前只配置了一条路由：

| 路径 | 名称 | 组件 |
|------|------|------|
| `/`  | home | `@/views/HomeView.vue` |

`<RouterView />` 在 `App.vue:7` 中渲染，作用是根据当前 URL 动态切换显示的页面组件。

**自己的理解：**

Router 相当于网站的"导航员"，它根据用户访问的 URL 来决定显示哪个页面组件。目前只有首页 `/` 一条路由，后续添加新页面时只需在 routes 数组中增加新规则即可。createWebHistory 使用的是 HTML5 History 模式，URL 中不带 # 号，看起来更干净。

**最终结论：**

Router 负责页面间的跳转和组件切换，当前已配置基础路由，后续可方便扩展。

---

### 任务：分析当前项目采用的技术栈

**Prompt：**

> 分析当前项目采用的技术栈

**AI 输出：**

| 层级 | 技术 | 版本 | 说明 |
|------|------|------|------|
| 框架 | Vue 3 | ^3.5.38 | Composition API + `<script setup>` |
| 路由 | vue-router | ^5.1.0 | Vue 3 官方路由 |
| 状态管理 | Pinia | ^3.0.4 | Vue 3 官方状态管理 |
| 构建工具 | Vite | ^8.0.16 | 极速开发服务器与构建 |
| 语言 | TypeScript | ~6.0.0 | 类型安全 |
| Vue 插件 | @vitejs/plugin-vue | ^6.0.7 | Vite 中编译 .vue 文件 |
| 代码检查 | oxlint + ESLint | ~1.69.0 / 10.x | 双 lint 工具链 |
| 类型检查 | vue-tsc | ^3.3.5 | 命令行 Vue 类型检查 |
| 包管理器 | pnpm | 11.9.0 | 依赖管理 |
| 开发工具 | vite-plugin-vue-devtools | ^8.1.2 | Vue DevTools 集成 |

**自己的理解：**

项目采用了目前 Vue 生态的主流技术栈：Vue 3 + TypeScript 为开发语言，Vite 为构建工具，Pinia 管理状态，vue-router 控制路由。此外还配置了 oxlint 和 ESLint 两套代码检查工具，确保代码质量。使用 pnpm 作为包管理器，速度更快、更节省磁盘空间。总体来说是一个现代化的前端开发环境。

**最终结论：**

项目技术栈全面且现代化，覆盖了开发、构建、状态管理、路由、代码检查等各方面需求。

---

## Task5 项目规划

### 页面清单

| # | 页面 | 路由 | 说明 |
|---|------|------|------|
| 1 | 身份创建页 | `/create-profile` | 首次进入填写昵称/学院/校区/角色 |
| 2 | 今日集市首页 | `/` | 概览、快捷入口、最新/热门信息、统计卡片 |
| 3 | 集市信息列表页 | `/items` | 搜索、类型/校区/状态筛选、排序、信息卡片 |
| 4 | 信息详情页 | `/items/:id` | 完整内容 + 类型专属字段 + 收藏/砍价/联系 |
| 5 | 信息发布页 | `/publish` | 统一入口，按类型动态切换字段 |
| 6 | 消息中心页 | `/messages` | 会话列表 + 聊天记录 + 发送消息 |
| 7 | 个人中心页 | `/profile` | 用户资料 + 我的发布 + 我的收藏 + 状态管理 |
| 8 | 趋势看板页 | `/trends` | 类型占比、校区分布、状态统计、热门排行 |
| 9 | 安全提醒页 | `/safety` | 线下交易安全提示卡片 |

### 功能模块

- **身份创建** — 填写昵称/学院/校区/角色，创建本地用户档案
- **今日集市首页** — 概览统计、快捷入口、最新/热门信息
- **集市信息浏览** — 关键词搜索、类型/校区/状态筛选、排序
- **信息详情** — 类型专属字段展示、收藏、砍价入口、联系发布者
- **信息发布** — 类型选择、通用字段 + 类型专属字段、表单校验
- **收藏管理** — 收藏/取消收藏、三处状态同步
- **模拟砍价** — 输入出价、生成模拟回复、写入消息记录
- **消息中心** — 会话列表、聊天记录、发送消息、模拟回复
- **个人中心** — 用户资料、我的发布（含状态更新）、我的收藏
- **趋势看板** — 类型占比、校区分布、状态统计、热门排行（ECharts）
- **安全提醒** — 线下交易安全提示卡片

### 数据模型

```
users         → id, nickname, college, campus, role, creditScore, avatar
items         → id, type, title, description, campus, location, tags, images,
                publisherId, status, viewCount, favoriteCount, createdAt, updatedAt
                └─ type专属: price/condition (二手) | lostOrFound/eventTime/itemFeature (失物)
                            targetCount/currentCount/deadline (拼单) | reward/taskPlace/expectedTime (跑腿)
favorites     → id, userId, itemId, createdAt
conversations → id, itemId, buyerId, publisherId, lastMessage, unreadCount, updatedAt
messages      → id, conversationId, senderId, receiverId, content, messageType, createdAt, read
notices       → id, title, content, type, createdAt
```

### 开发顺序

```
第1天 ─── 基础设施 + 身份创建 + 首页
第2天 ─── 信息发布 + 信息列表
第3天 ─── 信息详情 + 收藏功能
第4天 ─── 消息中心 + 模拟砍价
第5天 ─── 个人中心 + 状态管理
第6天 ─── 趋势看板 + 安全提醒
第7天 ─── 优化 + 演示准备
```

### 开发重点

1. **JSON Server Mock API 搭建** — 所有业务数据依赖于此，必须先搭好数据结构再开发页面。
2. **四类信息的统一与差异化** — items 通用字段 + 类型专属字段的设计，表单/详情/列表都要按 type 做条件渲染。
3. **收藏状态一致性同步** — 列表页、详情页、个人中心三处收藏状态必须一致。
4. **模拟回复生成** — 消息中心和砍价回复需要可扩展的规则引擎。
5. **ECharts 数据统计** — 趋势看板需要对 JSON Server 数据做聚合计算。
6. **动态表单** — 发布页根据类型切换字段集和校验规则。
7. **无真实登录下的身份模拟** — 路由守卫拦截未创建身份的用户。

---

## AI 协作总结

| 项目 | 内容 |
|------|------|
| AI 工具 | Opencode |
| 完成的任务 | 项目结构分析、main.ts 解释、router 作用说明、技术栈分析、项目规划 |
| Prompt 数量 | 5 个 |
| 自己的修改 | 对 AI 输出进行了整理和归纳，补充了自己的理解 |
| 最终结论 | 项目基于 Vue 3 + TypeScript + Vite + Pinia + Router 的现代化技术栈，目录结构清晰；项目规划覆盖了 9 个页面、12 个功能模块和 7 天开发计划 |
