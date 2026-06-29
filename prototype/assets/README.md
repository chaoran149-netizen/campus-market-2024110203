# 校园轻集市 HTML 原型

## 文件结构

```
prototype/
├── assets/
│   ├── common.css          # 公共样式（布局、卡片、颜色等）
│   └── UX_ANALYSIS.md      # UX 分析与产品规划文档
├── index.html              # 原型入口页（所有页面链接导航）
├── home.html               # 首页
├── category.html           # 分类浏览/搜索页
├── item-detail.html        # 二手商品详情页
├── lost-detail.html        # 失物招领详情页
├── group-detail.html       # 拼单搭子详情页
├── task-detail.html        # 跑腿委托详情页
├── publish.html            # 发布选择页
├── publish-item.html       # 发布二手商品
├── publish-lost.html       # 发布失物招领
├── publish-group.html      # 发布拼单搭子
├── publish-task.html       # 发布跑腿委托
├── messages.html           # 消息列表
├── chat.html               # 聊天详情
├── profile.html            # 个人中心
├── my-posts.html           # 我的发布
├── favorites.html          # 我的收藏
├── settings.html           # 账号设置
├── login.html              # 登录
├── register.html           # 注册
├── admin-dashboard.html    # 管理端首页
└── admin-review.html       # 信息审核页
```

## 设计规范

| 项目 | 值 |
|------|-----|
| **主色** | #409eff（清爽蓝） |
| **成功色** | #67c23a |
| **警告色** | #e6a23c |
| **危险色** | #f56c6c |
| **背景色** | #f5f7fa（浅灰白） |
| **卡片背景** | #ffffff（白色） |
| **卡片圆角** | 8px / 12px |
| **阴影** | 0 2px 12px rgba(0,0,0,0.06) |
| **最大内容宽度** | 1280px |
| **详情页布局** | 主内容 + 右侧 320px 侧边栏 |
| **表单页布局** | 主表单 + 右侧 320px 提示栏 |
| **管理端布局** | 左侧 240px 菜单 + 右侧内容区 |

## 技术栈

- **HTML5** — 页面结构
- **Tailwind CSS CDN** — 原子化样式
- **Vue 3 CDN** — 响应式数据和组件
- **Element Plus CDN** — UI 组件库
- **Element Plus Icons CDN** — 图标库

## 打开方式

直接用浏览器打开 `index.html`，点击入口卡片即可跳转到各页面。所有页面为独立 HTML，无需构建工具。

## 迁移建议

后续迁移到 Vue3 + Vite + TypeScript 项目时：
1. 将每个 HTML 中的 Vue 组件拆分为 `.vue` 单文件组件
2. 公共样式移至全局 CSS 文件
3. 数据逻辑移至 Pinia stores
4. 路由配置移至 `router/index.ts`
5. API 调用移至 `src/api/` 目录
