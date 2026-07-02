# Day6 Evidence — 注册登录、状态持久化与交互优化

## 1. 今日完成内容

本日完成了"校园轻集市"的**注册登录**功能、**状态持久化**和**交互优化**。在 db.json 中新增了 users 数据集合，创建了 LoginView 和 RegisterView 注册登录页面，改造了 userStore 支持登录/退出/恢复，使用 localStorage 持久化登录状态，更新了导航栏、发布页面和个人中心使其读取当前登录用户，创建了 LoadingState、ErrorState、SearchBar 三个交互优化组件，并为 TradeView 页面接入了搜索、加载和错误状态。

## 2. 注册与登录功能说明

**注册流程**：用户在 RegisterView 填写用户名、密码、昵称、学院、校区 → 前端先通过 `getUsers({ username })` 检查用户名是否已存在 → 不存在则调用 `createUser()` 向 `POST /users` 写入 JSON Server → 注册成功提示后跳转登录页。

**登录流程**：用户在 LoginView 输入用户名和密码 → 通过 `getUsers({ username })` 查询匹配用户 → 前端比对密码 → 匹配成功则调用 `userStore.login()` 将用户信息保存到 Pinia + localStorage → 跳转首页。

**重要声明**：本功能的密码是明文存储和比对的，没有使用 JWT、Token、密码加密、服务端会话等安全机制。这是专为前端实训设计的 Mock 注册/登录方案，不是生产环境安全认证系统。真实项目中需要密码哈希、后端校验、Token 管理和权限控制等完整安全措施。

## 3. 用户状态持久化

用户登录成功后，userStore 执行两步保存：
1. 将用户对象写入 `currentUser`（Pinia 响应式状态，驱动页面显示）
2. 将用户对象 JSON 序列化后存入 `localStorage.setItem('campus_user', ...)`（刷新后恢复）

App.vue 的 `onMounted` 钩子中调用 `userStore.restoreLogin()`，从 localStorage 读取并恢复登录状态。退出登录时，`logout()` 同时清空 Pinia 状态和 localStorage。

**localStorage 的作用**：在无后端 Session 的纯前端项目中，localStorage 是唯一可靠的客户端持久化手段。它让用户在刷新页面后无需重新登录，构成了项目可演示的用户闭环。

## 4. 页面联动记录

| 页面/组件 | 联动逻辑 |
|-----------|----------|
| **AppNav** | 未登录时显示"登录/注册"按钮；登录后显示当前用户昵称和"退出"按钮，点击退出清空状态并跳转首页 |
| **PublishView** | 提交前检查 `userStore.isLoggedIn`，未登录则提示"请先登录后再发布"；发布人字段改为 `userStore.displayName` |
| **UserCenterView** | 未登录时显示"尚未登录"提示卡和"去登录"按钮；登录后展示用户昵称、学院、校区和收藏列表 |
| **App.vue** | `onMounted` 调用 `restoreLogin()`，确保刷新后恢复登录状态 |

## 5. 交互体验优化

| 组件/优化 | 说明 |
|-----------|------|
| **LoadingState** | CSS 旋转动画，页面请求数据时展示"加载中…" |
| **ErrorState** | 显示错误信息 + "重新加载"按钮，触发父组件的 `@retry` 事件 |
| **SearchBar** | 统一搜索输入框（v-model 双向绑定 + 清除按钮），用于列表页过滤 |
| **TradeView** | 接入上述三个组件：`loading` → LoadingState，`error` → ErrorState，`filtered.length === 0` → EmptyState，搜索框实时过滤标题和发布人 |
| **提交按钮** | PublishView 提交中按钮 `disabled` + 文本变为"发布中…"，防止重复提交 |
| **注册用户名检查** | 注册前先查询是否已存在，避免重复注册 |

## 6. 功能走查记录

按实验手册 Task 18 流程进行了完整走查：

1. 启动 JSON Server（`pnpm mock`）和前端（`pnpm dev`）
2. 打开首页 → 导航栏右侧显示"登录 / 注册"
3. 点击注册 → 填写用户名/密码/昵称 → 提交 → 提示"注册成功"→ 跳转登录页
4. 检查 db.json → users 数组新增记录 ✓
5. 登录页输入刚注册的账号 → 登录成功 → 跳转首页
6. 导航栏显示当前用户昵称 + "退出"按钮 ✓
7. 刷新页面 → 仍保持登录状态 ✓
8. 进入发布页 → 发布一条二手交易 → 发布人显示为当前用户昵称 ✓
9. 进入二手交易页 → 搜索框输入关键词 → 列表实时过滤 ✓
10. 停止 JSON Server → 刷新列表页 → ErrorState 显示"加载失败"+"重新加载"按钮 ✓
11. 恢复 JSON Server → 点击重新加载 → 页面恢复 ✓
12. 点击退出 → 导航栏恢复"登录/注册" → 进入个人中心 → 显示"尚未登录" ✓

## 7. AI 协作记录

- **AI 工具**：Opencode
- **核心提示词**：输入了 Day6 实验手册全文，要求 AI 完成注册登录功能、状态持久化、交互优化和组件建造
- **AI 生成的内容**：
  - AI 生成了用户 API 模块（src/api/user.ts）
  - AI 生成了 LoginView.vue 和 RegisterView.vue
  - AI 改写了 userStore（src/stores/user.ts），实现 login/logout/restoreLogin
  - AI 生成了 LoadingState.vue、ErrorState.vue、SearchBar.vue
  - AI 更新了 AppNav.vue（登录状态展示）、PublishView.vue（登录检查）、UserCenterView.vue（未登录提示）
  - AI 更新了 TradeView.vue（接入搜索/加载/错误状态）
- **AI 生成内容中的不合理之处**：
  1. AI 初始在 userStore 中保留了旧 User 接口的 `role`、`creditScore`、`avatar` 字段，但 db.json 的 users 集合并不含这些字段，需要精简为与 db.json 一致的结构
  2. AI 初始在 LoginView 的登录逻辑中直接将整个 users 数组加载到前端比对，虽然对教学阶段可行，但未说明这不适合生产环境
  3. AI 初始生成的 UserCenterView 仍引用 `userStore.user.college` 等旧字段路径，改为 `userStore.currentUser?.college`

## 8. 遇到的问题与解决方法

**问题 1**：UserCenterView 在 userStore 改造后报错，因为模板中引用了 `userStore.user.college`、`userStore.user.creditScore`，但新 Store 的数据结构改为 `currentUser`（不含 creditScore）。

**解决**：将模板引用改为 `userStore.currentUser?.college`、`userStore.currentUser?.campus`，删除 creditScore 相关代码，改为未登录时显示"尚未登录"提示卡。

**问题 2**：PublishView 中原发布人写死为 `publisher = userStore.displayName`，但用户未登录时 displayName 为空字符串，仍能提交成功。

**解决**：在 `handleSubmit` 开头增加 `if (!userStore.isLoggedIn) { errorMsg.value = '请先登录后再发布'; return }` 拦截未登录提交。

## 9. 今日反思

Day6 让项目实现了从前端实训最关键的"用户闭环"：注册（向 JSON Server 写入用户）→ 登录（校验 + Pinia + localStorage）→ 页面联动（导航栏/发布页/个人中心）→ 退出（清空状态）。这个闭环让项目从一个"数据展示+表单提交"的工具变成了一个可演示的完整应用。状态持久化（localStorage）在无后端的纯前端项目中尤为重要——它解决了"刷新就丢失登录"的核心体验问题。交互优化方面，loading/error/empty/search 四种状态让页面从"要么有数据要么空白"升级为"各种情况都有对应反馈"，这是 Day7 综合验收前的重要准备。

需要再次强调的是，本项目的注册/登录是教学场景下的 Mock 实现，密码明文存储、前端比对、无 Token 无权限——这不是生产级安全方案，也不应该被误认为是可以直接上线的认证系统。

---

### 本日交付物清单

| 交付物 | 路径 | 状态 |
|--------|------|------|
| users 数据 | `db.json` | ✓ 新增 users 集合 |
| 用户 API | `src/api/user.ts` | ✓ 已创建 |
| 登录页 | `src/views/LoginView.vue` | ✓ 已创建 |
| 注册页 | `src/views/RegisterView.vue` | ✓ 已创建 |
| 路由 | `src/router/index.ts` | ✓ 新增 /login /register |
| userStore | `src/stores/user.ts` | ✓ 改造为登录态管理 |
| App.vue | `src/App.vue` | ✓ 恢复登录 |
| AppNav | `src/components/AppNav.vue` | ✓ 登录状态展示 |
| PublishView | `src/views/PublishView.vue` | ✓ 未登录拦截 |
| UserCenterView | `src/views/UserCenterView.vue` | ✓ 未登录提示 |
| LoadingState | `src/components/LoadingState.vue` | ✓ 已创建 |
| ErrorState | `src/components/ErrorState.vue` | ✓ 已创建 |
| SearchBar | `src/components/SearchBar.vue` | ✓ 已创建 |
| TradeView | `src/views/TradeView.vue` | ✓ 搜索+状态优化 |
| 编译验证 | `pnpm run build-only` | ✓ 148 模块通过 |
| Day6 证据卡 | `docs/evidence/Day6_Evidence.md` | ✓ 本文档 |
