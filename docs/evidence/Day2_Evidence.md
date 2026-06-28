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

| 项目 | 内容 |
|------|------|
| AI 工具 | Opencode |
| AI 完成的任务 | 创建 5 个新视图页面（TradeView、LostFoundView、GroupBuyView、ErrandView、UserCenterView）；创建 3 个布局组件（AppLayout、AppHeader、AppNav）；重写路由配置文件；重构 App.vue 使用布局组件 |
| 人工检查内容 | ① 检查每个新页面的业务场景是否符合"校园轻集市"主题 ② 确认路由器路由路径与导航按钮的 `to` 属性一致 ③ 验证 `UserCenterView.vue` 中 `menus` 变量定义在 `<script setup>` 内而非额外 `<script>` 块 ④ 确认全局 CSS 变量和 doodle 风格覆盖所有组件 ⑤ 运行 `pnpm run build-only` 验证编译通过、无报错 |
| 修改内容 | 修正 UserCenterView.vue 的 `<script>` 标签结构；调整 App.vue 去除冗余的内联导航逻辑；确认布局组件使用插槽而非硬编码内容 |

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
