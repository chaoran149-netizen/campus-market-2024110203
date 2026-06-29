# Day3 Evidence — Mock 数据建模与列表渲染

## 一、任务概述

本日完成了"校园轻集市"项目从静态页面到数据驱动页面的关键转变。通过设计 Mock 数据模型、搭建 JSON Server 模拟后端、封装 Axios 请求模块、创建通用列表组件，四个核心业务页面（二手交易、失物招领、拼单搭子、跑腿委托）已全部接入了模拟接口，页面内容由 API 数据驱动渲染。

## 二、Mock 数据模型设计

### 2.1 我的设计

在动手写 `db.json` 之前，我先梳理了四个业务场景的数据需求：

| 业务 | 核心字段 | 设计思路 |
|------|----------|----------|
| 二手交易 | title, price, category, condition, campus, location, publisher, publishTime, status | 商品信息 + 交易状态（open/closed）区分可买和已售 |
| 失物招领 | title, type, itemName, location, time, description, contact, status | 用 type 字段区分 lost/found，status 标记是否找回 |
| 拼单搭子 | title, type, targetCount, currentCount, deadline, location, campus, status | 目标人数和当前人数的差值驱动进度条，deadline 标注时效 |
| 跑腿委托 | title, taskType, reward, pickupLocation, deliveryLocation, description, deadline, status | 取件/送达双地点，status 区分 open/taken/done |

每类数据不少于 5 条（实际 trades 8 条、lostFounds 7 条、groupBuys 7 条、errands 7 条）。数据内容贴近真实校园场景：名字使用"李同学/王同学"、"主校区/东校区/西校区"、"图书馆/二食堂/信息楼" 等真实校园语境，避免出现与项目无关的测试占位文字。

### 2.2 AI 设计对比

AI（Opencode）根据提示词"为校园轻集市设计 db.json，包含二手交易、失物招领、拼单搭子、跑腿委托四组数据"生成了数据结构。

- **AI 的优点**：字段命名统一使用 camelCase；每类数据都包含了 status 状态字段；数据量充足（7-8 条/类）；数据内容贴近校园场景，描述具体（如"菜鸟驿站取三个包裹"而非"任务1"）。
- **AI 的问题**：初始方案在 errands 中缺少 `taskType` 的具体分类值，AI 生成了过于宽泛的 "task-1" "task-2" 等占位类型，我将其改为"取快递/代购/打印/取餐/维修/搬运/代办"七种校园真实任务类型。
- **最终调整**：补充了 taskType 的具体分类；统一了所有数据集的 status 枚举值（open/closed/taken/done）；为每类数据增加了至少 6 条的规模；确保所有字段名在 API 模块和组件中能一一对应。

## 三、JSON Server 配置

在项目根目录创建 `db.json`，并在 `package.json` 的 scripts 中添加：

```
"mock": "json-server --watch db.json --port 3001"
```

启动后确认四个端点均可正常访问：

| 端点 | 响应 |
|------|------|
| `GET /trades` | 8 条二手交易数据 |
| `GET /lostFounds` | 7 条失物招领数据 |
| `GET /groupBuys` | 7 条拼单搭子数据 |
| `GET /errands` | 7 条跑腿委托数据 |

## 四、Axios 请求封装与 API 模块

创建了分层请求架构：

```
src/api/
├── http.ts          → Axios 实例（baseURL: http://localhost:3001, timeout: 5000）
├── trade.ts         → getTrades() / getTradeById(id)
├── lostFound.ts     → getLostFounds() / getLostFoundById(id)
├── groupBuy.ts      → getGroupBuys() / getGroupBuyById(id)
└── errand.ts        → getErrands() / getErrandById(id)
```

API 模块遵循"一个业务一个文件"原则，视图组件只需导入对应模块的方法即可，避免了所有请求逻辑堆在页面中。本阶段未引入 JWT、权限拦截、错误码处理等过度设计。

## 五、列表渲染

### 5.1 通用组件

创建了两个可复用组件：

| 组件 | 位置 | 用途 |
|------|------|------|
| `ItemCard.vue` | `src/components/` | 根据 `type` prop 渲染不同业务卡片（trade/lostFound/groupBuy/errand），每种类型有独立的 UI 布局和微交互 |
| `EmptyState.vue` | `src/components/` | 数据为空时显示友好提示（📭 暂无数据） |

### 5.2 页面数据驱动改造

四个核心页面全部从硬编码占位数据改为 API 请求驱动：

| 页面 | API 方法 | 渲染方式 | 特殊逻辑 |
|------|----------|----------|----------|
| `TradeView.vue` | `getTrades()` | `v-for` + `ItemCard` | 分类筛选（教材/数码/生活/运动） |
| `LostFoundView.vue` | `getLostFounds()` | `v-for` + `ItemCard` | type 字段驱动 tab 切换（失/拾） |
| `GroupBuyView.vue` | `getGroupBuys()` | `v-for` + `ItemCard` | currentCount/targetCount 驱动进度条 |
| `ErrandView.vue` | `getErrands()` | `v-for` + `ItemCard` | taskType + status 驱动标签与圆点 |

每个页面均包含 `loading` 状态管理和 `EmptyState` 空数据处理。`HomeView.vue` 的"最新发布"区域也改为从 `/trades` 接口截取前 4 条渲染。

## 六、AI 协作记录

| 项目 | 内容 |
|------|------|
| AI 工具 | Opencode |
| 核心提示词 | ① "为校园轻集市设计 db.json，包含二手交易/失物招领/拼单搭子/跑腿委托四组数据" ② "创建 Axios 封装和 4 个业务 API 模块" ③ "创建 ItemCard.vue 通用列表卡片组件，用 type 区分四种业务" |
| AI 生成内容 | db.json 数据文件（4 集合 × 7-8 条）、4 个 API 模块文件、ItemCard.vue、EmptyState.vue、4 个视图页面的数据请求改造 |
| 人工审查与修改 | ① 补充 errands 中 taskType 的具体分类值（"取快递"等替代 "task-1"）② 统一 status 枚举值为 open/closed/taken/done ③ 验证 API 模块的 import 路径与 src/api/ 目录一致 ④ 确认 ItemCard.vue 中 type prop 的类型定义与视图传入一致 ⑤ 启动 JSON Server 验证四个端点均可返回数据 ⑥ 运行 `pnpm run build-only` 验证编译通过 |

## 七、遇到的问题与解决

1. **errands 字段设计**：AI 初始方案使用了单一 `location` 字段，但跑腿任务需要取件和送达两个地点。修改为 `pickupLocation` + `deliveryLocation` 双字段。
2. **ItemCard 类型安全**：Vue 3 的 `defineProps` 泛型支持 `Record<string, unknown>` 但在模板中访问属性需要 `data.title` 写法，确认传递的 `:data` prop 对象字段与组件内使用的字段一致。
3. **JSON Server 端口分离**：确保前端 Vite 服务（5173）和 Mock 服务（3001）端口不冲突，axios baseURL 写对。

## 八、本日交付物清单

| 交付物 | 路径 | 状态 |
|--------|------|------|
| Mock 数据文件 | `db.json` | ✓ created (4 集合 29 条) |
| Axios 实例 | `src/api/http.ts` | ✓ created |
| 4 个业务 API 模块 | `src/api/{trade,lostFound,groupBuy,errand}.ts` | ✓ created |
| 列表卡片组件 | `src/components/ItemCard.vue` | ✓ created |
| 空状态组件 | `src/components/EmptyState.vue` | ✓ created |
| 数据渲染页面 | TradeView/LostFoundView/GroupBuyView/ErrandView | ✓ updated |
| JSON Server 验证 | `GET /trades /lostFounds /groupBuys /errands` | ✓ passed |
| 构建验证 | `pnpm run build-only` | ✓ passed |
| Day3 证据卡 | `docs/evidence/Day3_Evidence.md` | ✓ 本文档 |
