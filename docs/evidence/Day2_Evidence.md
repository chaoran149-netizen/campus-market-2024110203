# Day2 Evidence

## 今日新增页面

| # | 文件 | 路由 | 说明 |
|---|------|------|------|
| 1 | `src/views/HomeView.vue` | `/` | 首页，欢迎信息 + 快捷入口 + 最新信息 |
| 2 | `src/views/ListView.vue` | `/list` | 集市信息列表，搜索/筛选/卡片展示 |
| 3 | `src/views/DetailView.vue` | `/detail/:id` | 信息详情，带动态 id 参数 |
| 4 | `src/views/PublishView.vue` | `/publish` | 信息发布，按类型动态切换字段 |
| 5 | `src/views/MessageView.vue` | `/message` | 消息中心，会话列表 + 未读标记 |
| 6 | `src/views/ProfileView.vue` | `/profile` | 个人中心，用户资料 + 我的发布 |
| 7 | `src/views/BoardView.vue` | `/board` | 趋势看板，类型/校区/状态统计 |

## 路由设计

```ts
routes: [
  { path: '/',          name: 'home',    component: HomeView },
  { path: '/list',      name: 'list',    component: () => import('@/views/ListView.vue') },
  { path: '/detail/:id',name: 'detail',  component: () => import('@/views/DetailView.vue') },
  { path: '/publish',   name: 'publish', component: () => import('@/views/PublishView.vue') },
  { path: '/message',   name: 'message', component: () => import('@/views/MessageView.vue') },
  { path: '/profile',   name: 'profile', component: () => import('@/views/ProfileView.vue') },
  { path: '/board',     name: 'board',   component: () => import('@/views/BoardView.vue') },
]
```

- 除首页外，其余页面均使用**懒加载**（`() => import`）
- 详情页使用动态路由参数 `:id`，列表页通过 `router.push({ name: 'detail', params: { id } })` 跳转
- App.vue 顶部导航栏包含 6 个按钮，当前路由高亮显示

## 遇到的问题

1. **vue-router v5 语法确认** — 项目使用 vue-router ^5.1.0，`createWebHistory` 和路由定义方式与 v4 一致，不需额外适配。
2. **Element Plus 未安装** — package.json 中无 Element Plus 依赖，导航栏使用原生 HTML + CSS 实现。
3. **TS 类型约束** — 使用 `<script setup lang="ts">` 时，ref 和 reactive 需要类型标注。

## AI 协作记录

| 项目 | 内容 |
|------|------|
| AI 工具 | Opencode |
| 完成的任务 | 创建 6 个新页面、更新路由、增强 HomeView、添加导航栏、看板页统计 |
| 关键 Prompt | "创建 7 个页面骨架 + 完善路由 + 导航栏 + 看板静态统计" |
| 自己修改 | 调整了导航栏样式、补充了看板页图表数据、优化了列表页跳转逻辑 |
| 当前状态 | 所有页面可访问，导航跳转正常 |

## 页面骨架截图

```
首页     →  `/`           → 欢迎卡片 + 快捷入口 + 最新信息
列表页   →  `/list`       → 搜索框 + 筛选 + 信息卡片（点击跳转详情）
详情页   →  `/detail/:id` → 返回按钮 + 物品信息 + 收藏/联系按钮
发布页   →  `/publish`    → 类型选择 + 动态字段 + 提交
消息页   →  `/message`    → 会话列表 + 未读标记
个人中心  →  `/profile`    → 用户卡片 + 信用分 + 我的发布
看板页   →  `/board`      → 统计总数 + 类型/校区/状态图表
```
