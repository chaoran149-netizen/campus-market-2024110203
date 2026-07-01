# Day5 Evidence

## 状态管理设计

| 项目 | 内容 |
|------|------|
| 状态管理工具 | Pinia |
| Store 数量 | 2 个 |
| 用户 Store | `src/stores/user.ts` |
| 收藏 Store | `src/stores/favorite.ts` |

### Store 设计

**userStore**

| 属性/方法 | 说明 |
|-----------|------|
| `user` (state) | 当前用户信息（昵称、学院、校区、角色、信用分、头像） |
| `displayName` (getter) | 用户昵称 |
| `initial` (getter) | 昵称首字符（用于头像） |
| `updateUser(partial)` (action) | 更新用户信息 |
| `resetUser()` (action) | 重置为默认用户 |

**favoriteStore**

| 属性/方法 | 说明 |
|-----------|------|
| `favorites` (state) | 收藏列表 |
| `count` (getter) | 收藏数量 |
| `addFavorite(item)` (action) | 添加收藏 |
| `removeFavorite(id)` (action) | 取消收藏 |
| `toggleFavorite(item)` (action) | 切换收藏状态 |
| `isFavorited(id)` (action) | 判断是否已收藏 |

### 状态边界

| 数据 | 是否入 Store | 原因 |
|------|-------------|------|
| 当前用户信息 | ✅ 是 | 导航栏、发布页、个人中心等多处使用 |
| 收藏列表 | ✅ 是 | 列表页和个人中心需要共享 |
| 表单输入框内容 | ❌ 否 | 仅属于当前页面 |
| 表单校验错误 | ❌ 否 | 仅属于当前表单 |
| 列表数据 | ❌ 否 | 从接口获取，存放在页面组件 |
| 未读消息数 | ⬜ 暂未 | 后续可扩展 |

### 跨页面使用情况

| 页面 | 使用的 Store |
|------|-------------|
| AppHeader.vue | userStore（显示当前用户头像和昵称） |
| PublishView.vue | userStore（发布人自动读取） |
| TradeView.vue | favoriteStore（收藏/取消收藏按钮） |
| UserCenterView.vue | userStore + favoriteStore（资料展示 + 收藏列表） |

### 测试记录

| 测试项 | 结果 |
|--------|------|
| 导航栏显示用户信息 | ✅ 显示"校园用户"及头像首字 |
| 发布页显示发布人 | ✅ 提示栏显示当前用户昵称 |
| 二手交易页收藏按钮 | ✅ 点击切换，红色实心/空心 |
| 个人中心展示收藏数量 | ✅ 统计数实时更新 |
| 个人中心收藏列表 | ✅ 展示收藏内容，支持取消 |
| TypeScript 类型检查 | ✅ 通过（vue-tsc --noEmit） |
| Vite 构建 | ✅ 通过 |

### AI 协作记录

| 项目 | 内容 |
|------|------|
| AI 工具 | Opencode |
| AI 辅助生成 | userStore 和 favoriteStore 的结构设计、TradeView 收藏按钮集成、UserCenterView 收藏展示 |
| 人工调整 | Store 的状态命名优化、增加类型接口、PublishView 发布人字段替换为 Store 读取、菜单项添加跳转 action |
| 设计原则 | 只把跨页面共享的状态放入 Store；表单临时数据和接口列表数据保留在页面组件中 |

### 后续改进

- 收藏数据目前仅存内存，刷新后会丢失，可结合 localStorage 做持久化
- 可扩展消息未读数为 Store（messageStore）
- UserCenterView 中"我的发布"可通过筛选接口数据实现
