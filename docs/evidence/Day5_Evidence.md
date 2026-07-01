# Day5 Evidence — 状态管理与用户中心

## 1. 今日完成内容

今天完成了 Pinia 状态管理的引入和用户中心功能的初步实现，主要包括：
- 创建了 `src/stores/user.ts`，管理当前模拟用户状态（昵称、学院、校区、信用分等）
- 创建了 `src/stores/favorite.ts`，管理收藏列表的增删和状态判断
- 更新了 `AppHeader.vue`，在导航栏右上角读取 userStore 展示头像和昵称
- 更新了 `PublishView.vue`，发布人字段从硬编码改为从 userStore 动态读取
- 更新了 `TradeView.vue`，在二手交易列表每行增加收藏按钮
- 重写了 `UserCenterView.vue`，展示用户资料、信用分、收藏数量和收藏列表
- 填写了本日的证据记录

## 2. Store 设计说明

| Store 文件 | 管理内容 | 主要状态 | 主要方法 |
|---|---|---|---|
| `src/stores/user.ts` | 当前模拟用户信息 | `user`（昵称、学院、校区、角色、信用分） | `updateUser(partial)`、`resetUser()` |
| `src/stores/favorite.ts` | 收藏列表状态 | `favorites`（对象数组） | `addFavorite(item)`、`removeFavorite(id)`、`toggleFavorite(item)`、`isFavorited(id)` |

userStore 使用 Vue 3 的 `computed` 派生了两个 getter：
- `displayName` — 返回用户昵称，发布页面和导航栏直接使用
- `initial` — 返回昵称的首字符，用于圆形头像展示

favoriteStore 的核心是 `toggleFavorite` 方法，先通过 `isFavorited(id)` 判断当前是否已收藏，再决定调用 `addFavorite` 或 `removeFavorite`，实现了收藏/取消收藏的切换逻辑。

## 3. 状态边界说明

这是本日最重要的设计决策——理解哪些数据属于跨页面共享状态，哪些数据只属于单个页面组件内部。

**放入 Store 的数据：**

| 数据 | 原因 |
|------|------|
| 当前用户信息 | 导航栏、发布页、个人中心都需要读取，至少有 3 处以上的使用点 |
| 收藏列表 | 列表页（收藏按钮状态判断）和个人中心（收藏列表展示）都需要读写 |

**不放 Store 的数据：**

| 数据 | 原因 |
|------|------|
| 表单输入框内容 | 只属于发布页组件内部，不与其他页面共享 |
| 表单校验错误信息 | 生命周期绑定在当前表单提交流程中，跨页面无意义 |
| 列表页的接口数据 | 从 JSON Server 获取，存放在页面组件的 ref 中，无需全局共享 |
| 搜索关键词和筛选条件 | 属于单个页面的临时交互状态 |

边界划分直接体现了状态管理的根本价值——不是把一切数据都塞进 Pinia，而是把多处用、多处改的状态统一管理。如果所有数据都放入 Store，Store 会膨胀为一个大对象，失去可维护性。

## 4. 页面使用记录

| 页面/组件 | 使用的 Store | 使用方式 |
|-----------|-------------|----------|
| AppHeader.vue | userStore | 读取 displayName 显示昵称，读取 initial 显示头像首字 |
| PublishView.vue | userStore | handleSubmit 中读取 userStore.displayName 作为发布人 |
| TradeView.vue | favoriteStore | 列表每行渲染收藏按钮，调用 isFavorited 判断状态，toggleFavorite 切换 |
| UserCenterView.vue | userStore + favoriteStore | 资料区读取 userStore，收藏数量由 count 派生，收藏列表支持取消 |

## 5. AI 协作记录

- 使用的 AI 工具：Opencode
- 核心提示词：提供了完整的 Day5 实验手册，要求创建 userStore 和 favoriteStore
- AI 生成的内容：
  - `stores/user.ts` 和 `stores/favorite.ts` 的完整结构，包含 state、getter、action
  - PublishView.vue 中替换发布人字段为 Store 读取的方案
  - TradeView.vue 中收藏按钮的 UI 结构和样式
  - UserCenterView.vue 中收藏列表的数据渲染
- 潜在问题：
  - AI 最初建议把列表数据也放入 Store，与状态边界原则不一致
  - 收藏数据结构包含 type 字段用于区分四类业务，当前仅二手交易使用
  - AI 未主动提出需要在发布页面添加发布人提示，由人工补充

## 6. 人工调整内容

| 调整项 | 说明 |
|--------|------|
| 删除复杂登录系统 | AI 可能倾向于生成 login/logout/JWT/路由守卫等完整认证系统，全部删除 |
| 拆分 Store | 将用户和收藏分为两个独立 Store，而非合并在一个 appStore 中 |
| 状态命名优化 | 将 currentUser 简化为 user，isSignedIn 改为 isLoggedIn |
| 收藏数据结构 | 将 timestamp 改为 addedAt，增加 campus 和 price 字段 |
| 发布页提示 | 添加了发布人提示区域（publisher-hint），让用户清楚看到发布身份 |
| 收藏按钮 UI | 调整为圆形红色心形按钮，样式符合常见收藏 UI 模式 |
| UserCenterView | 增加我的收藏独立区域，支持取消操作，增加空状态提示 |

## 7. 测试记录

| 测试项 | 操作步骤 | 预期结果 | 实际结果 |
|--------|----------|----------|----------|
| 导航栏用户信息 | 打开任意页面 | 右上角显示校园用户及蓝色头像首字校 | 通过 |
| 发布页发布人 | 进入发布页 | 发布人提示栏显示校园用户 | 通过 |
| 二手交易页收藏 | 进入 /trade，点击收藏按钮 | 按钮空心变实心红心，再次点击恢复空心 | 通过 |
| 个人中心收藏数量 | 收藏几件商品后进入 /user | 收藏统计数字随收藏数量变化 | 通过 |
| 个人中心收藏列表 | 有收藏时进入 /user | 展示商品标题、校区、价格，每项有取消按钮 | 通过 |
| 取消收藏 | 在个人中心点击取消按钮 | 该条目从列表消失，数量减 1 | 通过 |
| TypeScript 类型检查 | 执行 vue-tsc --noEmit | 无报错 | 通过 |
| Vite 生产构建 | 执行 vite build | 构建成功 | 通过 |

## 8. 遇到的问题与解决方法

**问题 1：收藏按钮点击后无反应**

最初在 TradeView.vue 中把 ItemCard 放在 router-link 内部，导致点击收藏按钮时事件冒泡触发了路由跳转。解决方法是用 div 包裹 ItemCard，把收藏按钮放在 ItemCard 外部独立渲染，同时用 @click.stop 阻止冒泡。

**问题 2：刷新后收藏数据丢失**

这是预期行为——Day5 的收藏数据保存在 Pinia 内存中，刷新页面后会丢失。这不是 Bug，是当前设计阶段的已知限制。后续可通过 localStorage 或后端接口实现持久化。

**问题 3：UserCenterView 中收藏数量不响应变化**

最初收藏统计数字用了硬编码 5，没有从 favoriteStore.count 读取。修正后统计数由 computed 派生，与收藏列表实时联动。

## 9. 今日反思

Day5 的核心收获在于理解了 Pinia 不是为了让代码看起来更高级，而是解决一个非常实际的问题：当项目从 Day2—Day4 的单页面功能逐步扩展为多页面协同工作时，很多数据（如用户信息、收藏列表）确实需要在不同页面之间共享。如果不引入状态管理，就只能通过 props 层层传递或者每次都从接口重新请求，前者会让组件耦合严重，后者会造成不必要的网络请求。

通过今天的实战，最深刻的感受是状态边界这个概念——不是所有数据都适合放进 Store。表单内容、校验错误、搜索框关键词这些数据只属于当前页面，放进 Store 反而会让 Store 膨胀、代码更难维护。只有真正跨页面共享的状态才值得集中管理。

另外，用户中心是多个 Store 的交汇点——它同时使用了 userStore（展示资料）和 favoriteStore（展示收藏），这恰好验证了 Day5 标题的含义：状态管理是从页面功能实现走向前端应用组织的关键一步。后续 Day6 如果需要扩展消息未读数、通知状态等，也可以遵循同样的原则新建独立的 Store。
