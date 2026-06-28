# Day2 Evidence — 页面骨架与路由导航

## 一、任务概述

本日完成了"校园轻集市"前端项目的页面骨架搭建、路由导航配置和公共布局组件实现。核心目标不是页面有多精美，而是建立一个结构清晰、可跳转、可扩展的多页面前端框架。

## 二、页面骨架

本日按需求创建了 8 个核心业务页面，均为 Vue 3 `<script setup lang="ts">` 单文件组件，统一使用项目已有的 doodle 手绘风格视觉体系。

| # | 文件名 | 路由路径 | 页面说明 |
|---|--------|----------|----------|
| 1 | `HomeView.vue` | `/` | 首页，欢迎卡片 + 快捷入口 + 最新信息 + 安全提示 |
| 2 | `TradeView.vue` | `/trade` | 二手交易页，搜索筛选 + 分类网格 + 商品卡片（教材/数码/生活/运动） |
| 3 | `LostFoundView.vue` | `/lost-found` | 失物招领页，遗失/拾取 tab 切换 + 失物列表 + 状态标记 |
| 4 | `GroupBuyView.vue` | `/group-buy` | 拼单搭子页，分类筛选 + 拼单卡片 + 参与人数/校区/时间标签 |
| 5 | `ErrandView.vue` | `/errand` | 跑腿委托页，任务类型标签 + 描述 + 报酬/截止/接单状态 |
| 6 | `PublishView.vue` | `/publish` | 发布页面，类型选择 + 动态表单字段 |
| 7 | `MessageView.vue` | `/message` | 消息页面，会话列表 + 未读标记 |
| 8 | `UserCenterView.vue` | `/user` | 个人中心，用户卡片 + 统计数字 + 菜单入口 |

每个页面均包含明确的页面标题（`<h2>`）和业务场景说明文字（`<p>`），使用 `v-for` 渲染占位数据展示页面基本结构。部分页面已预置了筛选、搜索、tab 切换等交互骨架，为后续接入真实数据做好准备。

## 三、路由导航

路由配置文件为 `src/router/index.ts`，关键设计：

- 使用 `createWebHistory` 实现无 hash 的干净 URL
- 首页（`HomeView`）为**直接导入**（首屏优先渲染），其余 7 个页面均使用**懒加载**（`() => import(...)`），减少首屏打包体积
- 保留了 `/detail/:id` 动态路由参数，支持商品/失物/拼单详情跳转（由列表页卡片触发）
- 路由路径语义清晰：`/trade`、`/lost-found`、`/group-buy`、`/errand`、`/publish`、`/message`、`/user`，不使用 `/page1` 等无意义路径
- 路由名称与路径命名一致，便于后续 `router.push({ name: 'xxx' })` 跳转和导航高亮

路由已在 `main.ts` 中通过 `app.use(router)` 挂载，Pinia 同步挂载为后续状态管理预留。

## 四、公共布局

将原本集中在 `App.vue` 中的布局代码拆分为三个可复用组件，形成清晰的**组件边界**：

| 组件 | 文件 | 职责 |
|------|------|------|
| `AppLayout.vue` | `src/components/AppLayout.vue` | 页面整体骨架：`flex` 纵向布局，插槽接收 header + RouterView 渲染内容区 |
| `AppHeader.vue` | `src/components/AppHeader.vue` | 顶部栏：应用标题（点击跳转首页）+ 插槽接收导航组件 |
| `AppNav.vue` | `src/components/AppNav.vue` | 导航菜单：8 个按钮，`v-for` 遍历 `navItems` 数组驱动渲染，当前路由高亮 |

拆分后的组件通过 Vue 3 的**具名插槽**（`<slot name="header" />`、`<slot name="nav" />`）组合使用，`App.vue` 只需导入并拼接：

```vue
<AppLayout>
  <template #header>
    <AppHeader>
      <template #nav>
        <AppNav />
      </template>
    </AppHeader>
  </template>
</AppLayout>
```

这种设计区分了**页面组件**（`views/`）和**通用组件**（`components/`），后续如需调整导航项只需修改 `AppNav.vue` 中的 `navItems` 数组，不需要改动其他文件。

## 五、视觉一致性

所有页面和布局组件统一使用 CSS 自定义属性（`--doodle-*`）控制配色和圆角，与项目 Day1 建立的 doodle 手绘风格保持一致。页面卡片统一使用 `border: 2.5px solid var(--doodle-border)` + `border-radius: var(--doodle-radius)` + hover 时 `transform: translate(-2px, -2px)` 微动效，形成统一的交互体验。

## 六、AI 协作记录

### 6.1 使用的 AI 工具

- **工具名称**：Opencode（AI 辅助编码助手）
- **使用方式**：在项目工作区中直接输入任务描述，由 AI 读取现有代码后生成新文件或修改已有文件

### 6.2 核心提示词

| 序号 | 输入指令 | 用途 |
|------|----------|------|
| 1 | "探索项目当前目录结构，读取关键文件" | 让 AI 先理解已有代码风格、路由配置、CSS 变量体系 |
| 2 | "按 Day2 实验手册要求，创建 TradeView / LostFoundView / GroupBuyView / ErrandView / UserCenterView 五个新页面，使用项目已有 doodle 风格" | 生成 5 个新视图页面 |
| 3 | "将 App.vue 中的布局代码拆分为 AppLayout / AppHeader / AppNav 三个独立组件，使用 slot 组合" | 生成 3 个公共布局组件 |
| 4 | "更新 router/index.ts，加入 8 个核心路由路径" | 重写路由配置 |
| 5 | "写 Day2_Evidence.md，包含页面骨架、路由导航、公共布局三个关键词" | 生成证据卡 |

### 6.3 AI 生成的内容

| 文件 | 生成方式 | AI 生成部分 |
|------|----------|-------------|
| `TradeView.vue` | 全文生成 | 页面标题、搜索筛选栏、分类下拉、6 项占位商品卡片、完整 CSS 样式 |
| `LostFoundView.vue` | 全文生成 | 页面标题、遗失/拾取 tab 栏、5 项失物列表、状态徽标、完整 CSS |
| `GroupBuyView.vue` | 全文生成 | 页面标题、分类 Chip 筛选栏、6 项拼单卡片（emoji + 标题 + 人数 + 校区标签）、完整 CSS |
| `ErrandView.vue` | 全文生成 | 页面标题、5 项跑腿卡片（类型标签 + 报酬 + 截止时间 + 接单状态）、完整 CSS |
| `UserCenterView.vue` | 全文生成 | 用户卡片（头像 + 昵称 + 学号 + 统计数字）、6 项菜单入口、完整 CSS |
| `AppLayout.vue` | 全文生成 | flex 纵向布局容器、`<slot name="header">` + `<RouterView />` |
| `AppHeader.vue` | 全文生成 | 应用标题（点击回首页）、`<slot name="nav">`、响应式适配 |
| `AppNav.vue` | 全文生成 | 8 项 navItems 数组、`v-for` 渲染按钮、路由高亮 `active` 类绑定 |
| `router/index.ts` | 全文改写 | 8 条路由配置（1 条直接导入 + 7 条懒加载）、1 条 `/detail/:id` 辅助路由 |
| `App.vue` | 全文改写 | 移除内联布局和导航代码，改为导入 3 个组件并用插槽组合 |
| `Day2_Evidence.md` | 全文生成 | 八章结构化证据文档（页面骨架表格 + 路由设计说明 + 布局架构图 + AI 协作表 + 交付物清单） |

### 6.4 人工审查与修改

| 阶段 | 具体操作 | 修改原因 |
|------|----------|----------|
| **代码审查** | 通读 5 个新页面的 `<template>` 内容 | 确认页面标题与业务场景匹配"校园轻集市"主题（如 LostFoundView 的失物举例是校园卡、钥匙，ErrandView 的任务是代取快递、超市代购） |
| **代码审查** | 核对 `AppNav.vue` 中 `navItems` 数组的路由名称与 `router/index.ts` 中的 `name` 字段 | 确保高亮判断 `router.currentRoute.value.name === item.name` 不会因名称不一致而失效 |
| **代码修复** | 修改 `UserCenterView.vue`：将 `menus` 数组从独立的 `<script lang="ts">` 块移入 `<script setup lang="ts">` | AI 生成了两个 script 块，但 Vue 3 的 `<script setup>` 内变量无法从外部 `<script>` 获取，导致模板渲染 `menus` 为空。将其合并到 setup 块中修复 |
| **代码修复** | 删除 App.vue 中残留的未导入引用（原文件有 `useRouter` import 和 router 赋值） | 原 App.vue 内联了路由逻辑，改插槽后不再需要 |
| **结构审查** | 确认 `<RouterView />` 放置在 `AppLayout.vue` 而非 `App.vue` 中 | 保证布局组件的语义正确——"页面内容区域"属于布局骨架的一部分，不应放在组合层 |
| **编译验证** | 运行 `pnpm run build-only` | 确认 60 个模块全部编译通过，无 TS 类型错误、无缺失导入、无样式冲突 |
| **内容确认** | 保留原有的 `DetailView.vue`、`ListView.vue`、`ProfileView.vue`、`BoardView.vue` | 这些页面为项目前期已完成的业务页面，不删除以避免破坏现有功能，Day2 仅新增规范要求的页面

## 七、遇到的问题

1. **页面命名对齐**：原项目使用 `/list`（ListView）、`/profile`（ProfileView）、`/board`（BoardView），Day2 规范要求 `/trade`（TradeView）、`/user`（UserCenterView），需要新建页面文件并重新配置路由，同时保留 `/detail/:id` 作为详情页辅助路由。
2. **布局组件拆分粒度**：App.vue 原本是一个整体，拆分时需要确定哪些部分放入组件、哪些通过插槽注入。最终采用三层组件 + 两级插槽的方案，在复用性和简洁性之间取平衡。
3. **拼单搭子页的数据建模**：拼单卡片需要同时展示主题、已有人数/需人数、校区、截止时间等多种信息，用同一套卡片样式承载多种类型的数据，对占位数据的选择提出要求。

## 八、本日交付物清单

| 交付物 | 路径 | 状态 |
|--------|------|------|
| 8 个页面组件 | `src/views/` | ✓ 已创建 |
| 3 个布局组件 | `src/components/` | ✓ 已创建 |
| 路由配置 | `src/router/index.ts` | ✓ 已更新 |
| Day2 证据卡 | `docs/evidence/Day2_Evidence.md` | ✓ 本文档 |
| 构建验证 | `pnpm run build-only` | ✓ 通过 |
