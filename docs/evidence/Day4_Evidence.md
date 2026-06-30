# Day4 Evidence — 发布表单与数据新增

## 1. 今日完成内容

本日完成了"校园轻集市"的**发布表单**设计、**表单校验**和**数据新增**功能。在 PublishView.vue 中实现了基于发布类型的动态表单切换（支持二手交易、失物招领、拼单搭子、跑腿委托四类业务），为每类业务编写了专属字段和基础校验规则，使用 Axios POST 向 JSON Server 提交数据，新增成功后给出反馈并自动跳转到对应列表页。同时创建了 FormField.vue 通用表单项组件，为四个 API 模块补充了 create 方法。

## 2. 发布类型与字段设计

| 发布类型 | 对应数据集合 | 关键字段 | 设计理由 |
|----------|-------------|----------|----------|
| 二手交易 | trades | title、category、price、condition、location、description | 商品需要展示名称、分类、价格和成色，location 说明交易地点 |
| 失物招领 | lostFounds | title、type、itemName、location、time、description、contact | type 区分丢失/拾取，itemName+location+time 定位物品信息 |
| 拼单搭子 | groupBuys | title、type、targetCount、deadline、location、description | targetCount 是拼单核心，deadline 标注截止时间 |
| 跑腿委托 | errands | title、taskType、reward、pickupLocation、deliveryLocation、deadline、description | 取件+送达双地点是跑腿特有需求，reward 标注酬劳 |

通用字段（标题、校区、描述）对所有类型共用，采取 `reactive` 响应式对象统一管理，避免重复代码。专属字段通过 `publishType` 变量 + `v-if` 条件渲染动态显示。

## 3. 表单校验规则

| 校验字段 | 适用类型 | 校验规则 | 错误提示 |
|----------|----------|----------|----------|
| title | 全部 | 不能为空 | "请输入标题" |
| description | 全部 | 不能为空 | "请输入描述" |
| price | 二手交易 | 必须 > 0 | "请输入有效的价格" |
| location | 二手交易 / 失物招领 | 不能为空 | "请输入交易地点" / "请输入丢失/拾取地点" |
| itemName | 失物招领 | 不能为空 | "请输入物品名称" |
| time | 失物招领 | 不能为空 | "请输入时间" |
| targetCount | 拼单搭子 | 必须 >= 2 | "目标人数至少为2" |
| deadline | 拼单搭子 / 跑腿委托 | 不能为空 | "请输入截止时间" |
| reward | 跑腿委托 | 必须 > 0 | "请输入有效的酬劳" |
| pickupLocation | 跑腿委托 | 不能为空 | "请输入取件地点" |

校验通过 `validate()` 函数集中执行，返回布尔值。校验错误通过 `errors` 对象存储，逐字段绑定到 FormField 组件的 `error` prop 上显示。

## 4. AI 协作记录

- **使用的 AI 工具**：Opencode
- **核心提示词**：输入了 Day4 实验手册全文，要求 AI 完成发布表单设计、校验和数据提交。
- **AI 生成了哪些内容**：
  - AI 为四个 API 模块各补充了 POST 方法（createTrade / createLostFound / createGroupBuy / createErrand）
  - AI 生成了 FormField.vue 通用表单项组件
  - AI 重写了 PublishView.vue，包含类型切换、四种专属字段、校验逻辑、POST 提交和反馈跳转
- **AI 生成内容中有哪些不合理之处**：
  1. groupBuy 的 create 方法遗漏了 `currentCount` 字段，db.json 已有此字段，缺少会导致新数据不一致。人工补充 `currentCount: 1`
  2. lostFound 的 time 字段使用了 `<input type="datetime-local">`，但 db.json 中 time 是字符串格式（如 "2026-06-28 12:00"），格式不匹配。人工改回普通 text 输入
  3. 初始方案将所有校验错误汇总在表单顶部显示，不够直观。人工改为每个 FormField 独立显示对应字段的错误信息

## 5. 人工调整内容

| 调整项 | 原因 |
|--------|------|
| groupBuy 创建时补充 `currentCount: 1` | db.json 已有此字段，新增数据必须包含 |
| lostFound time 从 datetime-local 改回 text | 保持与 db.json 已有数据格式一致 |
| 校验错误改为逐字段显示 | 用户体验更好，能一眼定位问题字段 |
| 切换发布类型时自动清除错误信息 | 避免残留上一类型的校验错误 |
| 添加 `submitting` 状态控制按钮禁用 | 防止用户重复点击提交 |
| 添加 `resetForm()` 重置按钮 | 方便测试和多条数据连续发布 |
| errand 补充 `deliveryLocation` 字段 | 跑腿任务需要取件+送达两个地点 |
| 删除复杂登录逻辑 | Day4 不需要，使用固定发布人 `"当前用户"` |
| 删除真实图片上传逻辑 | Day4 不需要，字段暂时留空 |
| 发布人使用固定值 `"当前用户"` | 当前暂无用户系统，后续 Day5 可结合 Pinia |

## 6. 测试记录

**测试时间**：2026-06-29 10:00

**测试流程**：
1. 浏览器打开 http://localhost:5173，点击导航"发布"
2. 选择发布类型为"二手交易"
3. 填写标题："测试商品-证据卡验证"
4. 选择分类："数码电子"，填写价格：99，成色："九成新"，交易地点："图书馆"
5. 选择校区："主校区"，填写描述
6. 点击"发布到集市"按钮
7. 页面显示绿色提示："发布成功！正在跳转…"
8. 自动跳转到 `/trade` 页面，列表中出现新增的商品

**API 验证**：通过 PowerShell 直接 POST 到 `http://localhost:3001/trades`，返回状态码 **201 Created**，确认 JSON Server 写入成功。

## 7. 遇到的问题与解决方法

**问题**：PublishView.vue 使用 `<script setup lang="ts">` 定义组件逻辑后，尝试用额外的 `<script lang="ts">` 定义 `typeOptions` 常量数组供模板使用。编译时出现 TypeScript 类型错误。

**解决**：Vue 3 支持同一 SFC 中两个 `<script>` 块共存。将 `typeOptions` 放到第二个不带 setup 的 `<script lang="ts">` 块中声明，模板可正常访问。编译通过（`pnpm run build-only` 验证 130 个模块无错误）。

**问题**：发布表单切换类型后，前一个类型的校验错误残留。例如先在"二手交易"触发价格为空错误，再切换到"失物招领"时错误提示依然显示。

**解决**：在 `watch(publishType, ...)` 中调用 `clearErrors()`，切换类型时自动清除所有校验错误和反馈信息。

## 8. 今日反思

发布表单、表单校验和数据新增让项目从"只读的数据展示"进入"可写的用户交互"阶段。数据新增是完整 Web 应用闭环的关键一环——用户不只是浏览信息，还能贡献内容。表单校验看似简单，却是前端交互体验的基础：没有校验，用户提交无效数据后只能在列表页发现数据不一致；有了校验，问题在输入阶段就被拦截。Day4 建立的"选择类型 → 填写字段 → 校验 → 提交 → 反馈 → 跳转"流程，是后续 Day5 状态管理（记录当前用户发布）、Day6 交互优化（加载状态、错误重试）和 Day7 综合验收的基础。

---

### 本日交付物清单

| 交付物 | 路径 | 状态 |
|--------|------|------|
| 发布页面 | `src/views/PublishView.vue` | ✓ 类型切换+校验+POST提交+反馈+跳转 |
| 表单项组件 | `src/components/FormField.vue` | ✓ 已创建 |
| 4 个 API POST 方法 | `src/api/{trade,lostFound,groupBuy,errand}.ts` | ✓ 已补充 |
| POST 接口验证 | `POST /trades` → 201 Created | ✓ 测试通过 |
| 构建验证 | `pnpm run build-only` | ✓ 130 模块通过 |
| Day4 证据卡 | `docs/evidence/Day4_Evidence.md` | ✓ 本文档 |
