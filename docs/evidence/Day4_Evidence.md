# Day4 Evidence — 发布表单与数据新增

## 1. 今日完成内容

本日完成了"校园轻集市"的发布功能：在 PublishView.vue 中实现了类型切换表单、基础字段校验、Axios POST 数据提交、成功/失败反馈、发布后自动跳转到对应列表页。同时创建了 FormField.vue 通用表单项组件，为四个业务 API 模块补充了 create 方法。

## 2. 发布表单字段设计

| 发布类型 | 对应数据集合 | 专属字段 | 通用字段 |
|----------|-------------|----------|----------|
| 二手交易 | trades | 价格、分类、成色、交易地点 | 标题、校区、描述 |
| 失物招领 | lostFounds | 丢失/拾取类型、物品名称、地点、时间、联系方式 | 标题、校区、描述 |
| 拼单搭子 | groupBuys | 拼单类型、目标人数、截止时间、集合地点 | 标题、校区、描述 |
| 跑腿委托 | errands | 任务类型、酬劳、取件地点、送达地点、截止时间 | 标题、校区、描述 |

## 3. 我的设计

**表单结构**：采用 `publishType` 响应式变量驱动 `v-if` 条件渲染，四个业务类型各自展示专属字段。通用字段（标题、校区、描述）始终显示，避免重复代码。

**校验策略**：编写 `validate()` 函数，返回布尔值，将错误信息存入 `errors` 对象。校验规则包括：
- 标题、描述为所有类型必填
- 价格为二手交易必填，且必须 > 0
- 物品名称、地点、时间为失物招领必填
- 目标人数为拼单搭子必填，且 >= 2
- 酬劳、取件地点、截止时间为跑腿必填

**提交逻辑**：`handleSubmit()` 先用 `validate()` 校验，通过后调用对应 API 的 create 方法。成功时显示绿色提示文案，800ms 后跳转到对应列表页；失败时显示红色错误提示，提醒检查 Mock 服务。

**发布人处理**：当前阶段使用固定值 `'当前用户'`，发布时间的 `status` 固定为 `'open'`，`currentCount` 初始为 1。

## 4. AI 设计

- **AI 是否帮你生成了 API POST 方法** → 是。AI 为 trade.ts、lostFound.ts、groupBuy.ts、errand.ts 各补充了 create 方法，参数类型与 db.json 字段一致。
- **AI 是否帮你生成了 FormField.vue** → 是。AI 生成了带 label、required 标记和 error 提示的通用表单项组件。
- **AI 是否帮你生成了 PublishView.vue** → 是。AI 重写了整个发布页面，包括类型切换、四种专属字段、校验逻辑、POST 提交和反馈。
- **AI 生成内容中有哪些不合理之处**：
  1. AI 初始在 groupBuy 的 create 方法中遗漏了 `currentCount` 字段。db.json 中每条数据都有此字段，提交时缺少会导致新数据缺少该字段。**人工补充了 currentCount: 1**。
  2. AI 初始为失物招领生成的 `time` 字段使用了 `<input type="datetime-local">`，但 db.json 中 time 字段是字符串格式（如 "2026-06-28 12:00"），datetime-local 格式与已有数据不一致。**人工改为普通 text 输入，允许自由填写**。
  3. AI 初始将所有校验错误合并显示在表单顶部，不够直观。**人工改为每个 FormField 独立显示对应错误信息**。

## 5. 最终调整

| 调整项 | 原因 |
|--------|------|
| groupBuy 补充 `currentCount: 1` | db.json 已有此字段，新数据必须包含 |
| lostFound 的 time 改回 text 输入 | datetime-local 格式与 db.json 不一致 |
| 校验错误改为逐字段显示 | 用户体验更好，能一眼看到哪个字段有问题 |
| 切换类型时自动清除错误信息 | 避免残留上一类型的错误提示 |
| 添加 `submitting` 状态管理按钮禁用 | 防止重复提交 |
| errand 补充 `deliveryLocation` 字段 | 跑腿任务需要取件+送达两个地点 |
| 添加 `resetForm()` 重置按钮 | 方便测试和重新填写 |

## 6. 遇到的问题与解决方法

**问题**：PublishView.vue 使用 `<script setup>` 后，尝试用额外的 `<script lang="ts">` 定义 `typeOptions` 常量数组供模板使用，但编译时报错。

**解决**：Vue 3 `<script setup>` 组件中，额外的 `<script>` 块只能用于声明非运行时内容（如 defineOptions、类型导入）。将 `typeOptions` 定义为一个普通常量放在第二个 `<script lang="ts">` 中确认可用（Vue 3 支持两个 script 块共存），编译通过。

## 7. 今日反思

发布表单与数据新增让项目从"只能看"进化到"可以写"。Mock 数据结构的设计在 Day4 发挥了作用——正因为 Day3 的字段设计贴合业务，Day4 的表单字段才能直接映射到 API 的 POST body。表单校验是用户体验的关键一环，虽然 Day4 的校验只是基础必填+数值判断，但它建立了"输入→校验→提交→反馈→跳转"的完整闭环。这个闭环是后续 Day5 状态管理、Day6 交互优化和 Day7 综合验收的前提。

---

### 本日交付物清单

| 交付物 | 路径 | 状态 |
|--------|------|------|
| 发布页面 | `src/views/PublishView.vue` | ✓ 完成（类型切换+校验+POST提交+反馈+跳转） |
| 表单项组件 | `src/components/FormField.vue` | ✓ 已创建 |
| 4 个 API POST 方法 | `src/api/{trade,lostFound,groupBuy,errand}.ts` | ✓ 已补充 |
| 构建验证 | `pnpm run build-only` | ✓ 通过 |
| Day4 证据卡 | `docs/evidence/Day4_Evidence.md` | ✓ 本文档 |
