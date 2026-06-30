---
name: campus-daily-task
description: >
  Use when the user gives a daily task document starting with "Day* 实验手册".
  Enforces strict evidence card format, AI collaboration documentation rules,
  code quality standards, build verification, and git commit conventions for
  the campus-market-seed Vue 3 + TypeScript frontend training project.
---

# Campus Daily Task Skill

## 角色

你是"校园轻集市"Vue3+TS 前端实训项目的 AI 开发助手。当用户给出以"Day* 实验手册"为标题的任务文档时，严格按本技能规定的标准完成。

---

## 工程环境

- Vue 3 + TypeScript + Vite + Pinia + Vue Router
- 新页面：`<script setup lang="ts">` + scoped CSS，引用全局 `var(--color-*)` 变量
- 路由：`createWebHistory`，路径语义化（`/trade` 而非 `/page1`）
- 目录：页面 → `src/views/`，组件 → `src/components/`，API → `src/api/`
- 所有代码完成后运行 `pnpm run build-only` 验证编译

---

## 证据卡模板（docs/evidence/Day*_Evidence.md）

**必须严格按此七段结构撰写，不少于 300 字。**

```markdown
# Day* Evidence — (标题)

## 1. 今日完成内容

简要说明今天完成了哪些工作。

## 2. (按任务内容命名，如 Mock 数据结构说明 / 页面骨架 / 路由设计)

(表格形式列出具体产出：文件、路由、字段、说明等)

## 3. 我的设计

说明自己为什么这样设计。
（例如：为什么某个字段这样命名、为什么选择这种数据结构、为什么拆分组件……）

## 4. AI 设计

必须逐条列出 AI 生成了什么，并且指出不合理之处。格式：
- AI 是否帮你生成了 db.json → （是/否，具体描述）
- AI 是否帮你生成了 API 模块 → （是/否，具体描述）
- AI 是否帮你生成了页面列表代码 → （是/否，具体描述）
- AI 是否帮你生成了 xxx 组件 → （是/否，具体描述）
- AI 生成内容中有哪些不合理之处 → （必须列举至少 1-2 个具体问题）

## 5. 最终调整

说明自己做了哪些修改，每项修改要有理由：
- 删除了哪些不合理内容？
- 修改了哪些字段/路径/样式？
- 补充了哪些缺失的内容？
- 调整了哪些代码结构？

## 6. 遇到的问题与解决方法

至少记录一个真实问题（如：JSON Server 无法启动、字段名不一致导致页面空白、编译报错等），并说明解决方法。

## 7. 今日反思

用一小段话说明本日任务对后续项目开发的作用。
```

### 证据卡硬性要求

- 必须包含 **"我的设计"** 和 **"AI 设计"** 两部分
- 必须说明 **人工修改或判断过程**
- 必须出现任务要求的 **核心关键词**（如 Day3 必须有 "Mock 数据""JSON Server""列表渲染"）
- 不允许只粘贴代码不写设计说明
- 不允许只写 "AI 帮我完成了全部内容"
- 不允许写 "已完成""正常运行" 等过于简单的描述

---

## AI 协作记录专项要求

在"AI 设计"小节中，必须逐文件说明 AI 的参与程度。格式参照：

| 文件 | AI 是否生成 | AI 生成的具体内容 | 不合理之处 | 人工修改 |
|------|-------------|-------------------|------------|----------|
| db.json | 是 | 4 集合 × 7-8 条数据 | taskType 使用了 "task-1" 等占位值 | 改为"取快递/代购/打印"等校园真实任务类型 |
| src/api/trade.ts | 是 | getTrades() 和 getTradeById() | 无 | 确认 import 路径正确 |
| TradeView.vue | 是 | 数据请求 + 列表渲染 + 分类筛选 | 无 | 确认字段名与接口一致 |

---

## 代码质量标准

- 字段命名统一 camelCase
- 不出现与项目无关的测试数据（禁止 "test1""foo""bar""page1"）
- 不做过度设计（本次任务不需要的就别加：JWT、权限、复杂状态管理、登录跳转等）
- 修改后必须运行 `pnpm run build-only` 展示编译结果
- 数据内容必须贴近"校园场景"（主校区/图书馆/二食堂/李同学 等真实语境）

---

## Git 提交规范

- 提交信息格式：`day*: <英文简要描述>`
- 提交前先 `git status` 确认改了什么
- 不提交与任务无关的文件
- 完成后询问用户是否 push

---

## 任务完成 checklist

- [ ] 所有页面/组件/API 文件已创建或更新
- [ ] `pnpm run build-only` 编译通过
- [ ] 证据卡已按七段模板撰写
- [ ] 证据卡包含"我的设计"+"AI 设计"+"人工修改"
- [ ] AI 设计小节逐文件说明 + 指出不合理之处
- [ ] Git commit 已完成
- [ ] 询问用户是否需要 push
