# Chinese Natural-Language Routing

用户用中文自然语言表达需求时，先读本文件，不要先要求用户记斜杠命令。若说法能明确映射到命令，直接执行，并用一句话说明解释出的命令，例如：`我把你的需求理解为 /paper-analyze：分析往年题并反推复习重点。`

## 按意图类匹配，不要按字面整句匹配

下面的路由表是**示例**，不是穷举白名单。真实用户的说法千变万化（"老师圈的范围""考纲重点""划的考点""期末就考这些"都指向同一意图），不要因为某句话没逐字出现在表里就放弃路由。**先把用户这句话归到下面某个意图类，再走对应命令**；表里的句子只是每个意图类的代表样本。

| 意图类（用户想做什么） | Route |
|---|---|
| 标注/提取"某来源说了哪些是重点/范围"（老师强调、考纲、复习提纲、星标页） | `/teacher-emphasis` |
| 从往年题/样卷/题库反推考什么、押重点 | `/paper-analyze`（押重点再接 `/plan`） |
| 把答案/解法拿来按考试标准判分、找扣分点 | `/grade` |
| 把做错的题沉淀、归类、建本 | `/wrong-note` |
| 要同类/变式题练某个薄弱点 | `/fix`；泛泛刷题用 `/quiz` |
| 摄取/整理课件、PPT、PDF、笔记 | `/materials` |
| 把资料沉淀成可累积、可互链的知识库 | `/wiki` / `/wiki-ask` / `/wiki-lint` |
| 排复习计划、定每天学什么、问"今天学啥" | `/plan` / `/dashboard` / `/review-due` |
| 时间紧、求救、挂科边缘、明天考 | `/cram`（保留最小诊断与错题修复） |
| 不知道自己哪不会、想先测水平 | `/diagnose` |
| 只有课程名、没资料、求先查资料 | `/materials` with material retrieval |
| 让学生当老师/角色互换/你做题我批改 | `/peer-quiz` |
| 看看自己考试准备够不够/就绪度/能考几分 | `/readiness` |
| 考试策略/考前流程/考场怎么做/卡题怎么办 | `/exam-routine` |
| 信心校准/高信心错题/过度自信检测 | `/calibrate` |
| 复盘反思/今天学了什么/齐默曼 | `/reflect` |
| 只练变式题/混合题/迁移题/基础会了想提高 | `/transfer` |
| 多门课怎么安排/期末周排计划/一周考N门 | `/plan` (multi-course scheduling) |

归类不唯一或置信度低时，按下方"路由规则"的单问题澄清；不要默认拒绝或要求用户改用英文命令。

## 直接路由表（代表样本，非白名单）

| 用户说法 | Route |
|---|---|
| 老师说这些是重点 | `/teacher-emphasis` |
| 这些是老师划的重点 | `/teacher-emphasis` |
| 老师画了重点 | `/teacher-emphasis` |
| 老师上课强调了这些 | `/teacher-emphasis` |
| 复习提纲里哪些最重要 | `/teacher-emphasis -> /plan` |
| 帮我看往年题怎么复习 | `/paper-analyze` |
| 分析这套卷子 | `/paper-analyze` |
| 看看这几年都考什么 | `/paper-analyze` |
| 根据往年题押重点 | `/paper-analyze -> /plan` |
| 根据题库出复习计划 | `/paper-analyze -> /plan` |
| 整理错题 | `/wrong-note` |
| 做个错题本 | `/wrong-note` |
| 把这题加入错题本 | `/wrong-note` |
| 我这题哪里错了 | `/grade` |
| 帮我批改答案 | `/grade` |
| 按考试标准扣分 | `/grade` |
| 给我出几道类似题 | `/fix` or `/quiz` |
| 出几道同类型变式 | `/fix` |
| 我想刷题 | `/quiz` |
| 随机抽查我 | `/quiz` |
| 这章我总是错 | `/fix` |
| 我没时间了先做什么 | `/cram -> /dashboard` |
| 帮我背这个 | `/quiz` with recitation-coach mode |
| 我已经会了，别提示我 | `/quiz` with `test` scaffold level |
| 模拟一套期末卷 | `/mock` |
| 来一次限时模拟 | `/mock` |
| 今天该复习什么 | `/review-due` or `/dashboard` |
| 今天先学哪一章 | `/dashboard -> /plan` |
| 给我一个复习仪表盘 | `/dashboard` |
| 把知识库资料变成计划 | `/materials -> /source-map -> /plan` |
| 把这些资料变成复习计划 | `/materials -> /source-map -> /plan` |
| 把资料整理成知识库 | `/wiki` |
| 建一个课程 wiki | `/wiki` |
| 把课件沉淀成知识百科 | `/wiki` |
| 在知识库里查一下这个 | `/wiki-ask` |
| 根据知识库回答我 | `/wiki-ask` |
| 检查一下知识库有没有遗漏 | `/wiki-lint` |
| 知识库哪里有断链或缺口 | `/wiki-lint` |
| 整理这些课件 | `/materials` |
| 帮我读一下 PPT | `/materials` |
| 帮我读一下 PDF | `/materials` |
| 根据笔记整理考点 | `/materials -> /map` |
| 做考前速记 | `/last-page` |
| 最后一页复习 | `/last-page` |
| 生成复习 PPT | `/last-page -> /ppt` |
| 做一个考前速记 PPT | `/last-page -> /ppt` |
| 做阶段复盘报告 | `/dashboard -> /report` |
| 我还有三天考试，救一下 | `/cram` |
| 明天考试，怎么抢分 | `/cram` |
| 挂科边缘，先复习什么 | `/cram -> /diagnose` |
| 帮我复习知识库里的这门课 | `/profile -> /materials -> /source-map` |
| 建一个课程主页 | `/profile` with ima-note |
| 帮我建课程档案 | `/profile` |
| 我不知道自己哪里不会 | `/diagnose` |
| 先测一下我的水平 | `/diagnose` |
| 这门课怎么复习 | `/profile -> /diagnose -> /plan` |
| 没资料怎么复习 | `/profile -> /materials` with material retrieval |
| 我只有课程名 | `/profile -> /materials` with material retrieval |
| 没有课件先帮我整理 | `/materials` with material retrieval |
| 先帮我查一下这门课资料 | `/materials` with material retrieval |
| 做个知识图谱 | `/map` |
| 梳理知识框架 | `/map` |
| 闭卷怎么背 | `/paper -> /plan` |
| 开卷怎么整理资料 | `/paper -> /last-page` |
| 半开卷带什么纸 | `/paper -> /last-page` |
| 机考怎么练 | `/profile -> /quiz` with coding or OJ focus |
| OJ 怎么刷 | `/quiz` with coding focus |
| 实验考怎么准备 | `/lab -> /plan` |
| 实验报告哪里容易扣分 | `/lab -> /grade` |
| 口试怎么准备 | `/oral` |
| 模拟老师问我 | `/oral` |
| 用苏格拉底方式问我 | `/socratic` |
| 别直接讲，问我问题 | `/socratic` |
| 用费曼法检查我 | `/feynman` |
| 我来讲你来挑错 | `/feynman` |
| 给我画图解释 | `/visual` |
| 做个流程图 | `/visual` |
| 写个代码演示 | `/code-demo` |
| 跑个例子给我看 | `/code-demo` |
| 生成 Anki 卡片 | `/flashcards` |
| 生成 Quizlet 表格 | `/flashcards` |
| 做背诵卡 | `/flashcards` |
| 下次提醒我复习 | `/review-due` plus opt-in reminder handling |
| 每天给我知识归纳 | `/review-due` plus opt-in digest handling |
| 你来做题我来批改 | `/peer-quiz` |
| 角色互换，你当学生 | `/peer-quiz` |
| 让我当老师考你 | `/peer-quiz` |
| 我考试准备好了吗 | `/readiness` |
| 考试就绪度怎么样 | `/readiness` |
| 能考多少分 | `/readiness` (with disclaimer) |
| 考前做什么 | `/exam-routine` |
| 考试策略 | `/exam-routine` |
| 卡题了怎么办 | `/exam-routine` |
| 测一下我的信心准不准 | `/calibrate` |
| 高信心错题 | `/calibrate` |
| 今天复盘一下 | `/reflect` |
| 总结反思 | `/reflect` |
| 做变式题 | `/transfer` |
| 换个方式考同一个知识点 | `/transfer` |
| 我基础题都会了 | `/transfer` |
| 一周考好几门怎么安排 | `/plan` (multi-course scheduling) |
| 期末周多门课排个计划 | `/plan` (multi-course scheduling) |

## 中文命令别名

用户输入中文别名时，视为等效英文命令直接执行。以下是完整映射：

| 中文别名 | 等效命令 |
|----------|----------|
| `/建档` | `/profile` |
| `/资料` | `/materials` |
| `/来源图` | `/source-map` |
| `/诊断` | `/diagnose` |
| `/考卷` | `/paper` |
| `/分析真题` | `/paper-analyze` |
| `/划重点` | `/teacher-emphasis` |
| `/实验` | `/lab` |
| `/百科` | `/wiki` |
| `/百科问` | `/wiki-ask` |
| `/百科检查` | `/wiki-lint` |
| `/计划` | `/plan` |
| `/图谱` | `/map` |
| `/一页纸` | `/last-page` |
| `/仪表盘` | `/dashboard` |
| `/刷题` | `/quiz` |
| `/模考` | `/mock` |
| `/口试` | `/oral` |
| `/批改` | `/grade` |
| `/修复` | `/fix` |
| `/抢答` | `/group-quiz` |
| `/互教` | `/peer-quiz` |
| `/迁移` | `/transfer` |
| `/校准` | `/calibrate` |
| `/讲解` | `/explain` |
| `/追问` | `/socratic` |
| `/费曼` | `/feynman` |
| `/图示` | `/visual` |
| `/视频` | `/video` |
| `/演示` | `/code-demo` |
| `/到期复习` | `/review-due` |
| `/错题本` | `/wrong-note` |
| `/闪卡` | `/flashcards` |
| `/总结` | `/summary` |
| `/反思` | `/reflect` |
| `/恢复` | `/resume` |
| `/报告` | `/report` |
| `/幻灯片` | `/ppt` |
| `/就绪度` | `/readiness` |
| `/临场` | `/exam-routine` |
| `/冲刺` | `/cram` |
| `/模式` | `/mode` |
| `/帮助` | `/help` |

识别到中文别名后，按对应英文命令的正常流程执行（加载 primary reference、走完整工作流）。回复中仍显示中文说明，如：`执行 /刷题（quiz）：自适应刷题，按表现升降难度。`

## 路由规则

### 核心原则：用户不需要记命令

模型必须主动判断用户意图并执行，不要期望用户记住或输入斜杠命令。用户可以用中文别名、英文命令或直接用自然语言说需求，三种方式等效。

### 置信度分级路由

| 置信度 | 行为 |
|--------|------|
| **≥ 0.8（高）** | 直接执行，开头一句话说明：`我把你的需求理解为 /grade：按考试标准批改。` |
| **0.5–0.8（中）** | 呈现 2-3 个最可能的命令选项（带中文说明），让用户选数字或继续说 |
| **< 0.5（低）** | 问一个紧凑的澄清问题，附带最可能方向的提示 |

中置信度时的选项格式：

```markdown
我理解你可能想：
1. `/quiz` — 自适应刷题，按表现升降难度
2. `/fix` — 针对薄弱点做修复练习
3. `/diagnose` — 先测整体水平再决定

选一个数字，或继续说你想做什么。
```

### 主动推荐下一步

每轮任务完成后，在输出末尾推荐 2-3 个下一步命令，**必须基于当前复习进度和状态**，不得随机推荐：

```markdown
📌 推荐下一步（基于当前状态）：
→ /fix 极限证明 — 刚才踩点只得 4/10，需要修复
→ /review-due — 你有 3 个主题今天到期，再不复习会遗忘
→ /readiness — 距考试还有 5 天，看看整体就绪度
```

每个推荐必须带**具体理由**（"因为刚才…""你的…状态是…"），不能只列命令名。2-3 个选项应覆盖不同维度（修复 + 进度 + 到期等），不要都指向同一类动作。连续 3 轮同类任务后至少一个推荐换模式。详细推荐信号表见 `SKILL.md` → Intelligent Routing → 主动推荐下一步。

### 其他规则

- 中文请求能明确映射时直接执行，不要让用户先选命令。
- 如果一句话包含多个动作，按”资料 -> 画像/地图 -> 计划 -> 练习 -> 批改 -> 修复 -> 复习追踪”的顺序拆成工作流，并先执行最有用的一步。
- 在 ima 中，用户提到 知识库、笔记、课程主页、错题本、老师划重点、往年题、报告、PPT 时，优先使用 note/knowledge-base 工作流。
- 如果短语暗示多步骤任务，在 ima 中创建 `task_plan`，然后执行第一个能产生学习价值的步骤。
- 用户处于明显考前高压场景（明天考试、三天冲刺、挂科边缘）时，默认 `/cram`，但保留最小诊断和错题修复，不只给安慰或大纲。
- 用户要求主动提醒或每日/每周知识归纳时，必须走 `references/opt-in-reminders.md`；不要默认开启后台提醒。
- 用户没有外部资料或只给课程名时，必须走 `references/material-retrieval.md`，先检索或生成可复制查询词，再输出低置信复习框架。
