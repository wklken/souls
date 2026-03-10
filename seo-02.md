# Souls 网站 SEO 分析报告 (Codex 分析)

**分析日期**: 2026-03-09  
**分析工具**: acpx codex + web_fetch  
**目标站点**: https://agent-souls.com/  

---

## 一、页面抓取与分析

### 1.1 首页分析

**URL**: https://agent-souls.com/

| SEO 要素 | 现状 | 评估 |
|---------|------|------|
| Title | "Souls - Souls" | ❌ 重复冗余，无关键词 |
| Meta Description | 缺失 | ❌ 严重缺失 |
| H1 | 未明确识别 | ⚠️ 需检查 |
| 主要内容 | "与历史对话，让思想碰撞；与角色对话，让故事映照当下；与专家对话，让能力不断进化" | ✅ 有吸引力但缺乏关键词优化 |
| 关键词密度 | "AI" 未出现，"历史人物" 未出现 | ❌ 核心关键词缺失 |

**页面统计信息**:
- 收录人物: 212 位（200 历史人物 + 4 虚构角色 + 8 专家角色）
- 已添加 AI 生成免责声明 ✅

### 1.2 分类页分析

**URL**: https://agent-souls.com/real_world

| SEO 要素 | 现状 | 评估 |
|---------|------|------|
| Title | "真实世界 - Souls" | ⚠️ 过于简单，缺少关键词 |
| Meta Description | 缺失 | ❌ 缺失 |
| H1 | "真实世界" | ⚠️ 应包含更多关键词如"历史人物" |
| 内容结构 | 人物列表 + tags | ✅ 结构清晰 |

**关键词覆盖情况**:
- 页面包含丰富的人物标签（tags）：
  - 哲学相关：形而上学、伦理学、逻辑学、启蒙运动
  - 历史相关：三国、明朝、东汉、唐代
  - 领域相关：天文学、物理学、医学、文学

### 1.3 详情页分析

**URL**: https://agent-souls.com/real_world/zhuge_liang/

| SEO 要素 | 现状 | 评估 |
|---------|------|------|
| Title | "诸葛亮 (Zhuge Liang) - Souls" | ⚠️ 包含人名但缺少"AI"、"Prompt"等词 |
| Meta Description | 缺失 | ❌ 严重缺失 |
| H1 | 未明确 | ⚠️ 需检查 HTML 结构 |
| 内容质量 | 非常丰富（2000+字） | ✅ 内容详实 |
| 关键词覆盖 | 诸葛亮、三国、北伐、出师表 | ✅ 自然覆盖 |
| 结构化 | 核心身份、核心智慧、灵魂画像、信念、性格、对话风格 | ✅ 层次分明 |

**内容亮点**:
- "核心智慧 (Core Stone)" - 独特的内容架构
- 详细的对话风格指南
- 边界与约束说明
- 关键关系网络

### 1.4 技术 SEO 检查

#### robots.txt
```
Sitemap: https://agent-souls.com/sitemap.xml
```

**评估**: 
- ✅ 包含 sitemap 引用
- ⚠️ 过于简单，建议添加 User-agent 规则和 Disallow 路径

#### sitemap.xml
- ✅ 格式正确，使用标准 urlset schema
- ✅ 包含所有 soul 详情页 URL
- ⚠️ 缺少 `lastmod`、`changefreq`、`priority` 字段
- ❌ 包含不应索引的模板文件（如 `_layouts/home.html`）

---

## 二、SEO 问题诊断

### 2.1 严重问题（需立即修复）

| 优先级 | 问题 | 影响 |
|--------|------|------|
| 🔴 P0 | 全站缺少 Meta Description | 搜索结果摘要质量极低，CTR 严重受损 |
| 🔴 P0 | 首页 Title 重复 "Souls - Souls" | 浪费最重要的 SEO 位置 |
| 🟡 P1 | sitemap 包含模板文件 | 浪费爬虫配额，可能导致索引问题 |

### 2.2 中等问题（建议1周内修复）

| 优先级 | 问题 | 影响 |
|--------|------|------|
| 🟡 P1 | 缺少 Open Graph 标签 | 社交分享展示效果差 |
| 🟡 P1 | 缺少 Twitter Card | 社交媒体流量受损 |
| 🟡 P1 | 无 Schema.org 结构化数据 | 无法获得富媒体搜索结果 |
| 🟢 P2 | URL 路径不友好 | `/real_world/` 对 SEO 价值低 |
| 🟢 P2 | 缺少 canonical 标签 | 潜在的重复内容问题 |

### 2.3 优化机会（建议1月内实施）

| 优先级 | 机会 | 预期收益 |
|--------|------|----------|
| 🟢 P2 | 长尾关键词布局 | 获取精准搜索流量 |
| 🟢 P2 | 内链网络优化 | 提升页面权重分配 |
| 🔵 P3 | FAQ 页面（Featured Snippet）| 获取零位置排名 |
| 🔵 P3 | 专题聚合页 | 捕获高搜索量关键词 |

---

## 三、关键词分析

### 3.1 当前关键词覆盖

**已有的自然关键词**（从内容中提取）:
- 历史人物：诸葛亮、孔子、曹操、李白、杜甫
- 领域标签：哲学、历史、文学、军事、科学
- 时代标签：三国、唐代、宋朝、古希腊

**缺失的核心关键词**:
- AI 相关：AI prompt、AI角色、AI人格、AI对话
- 产品相关：soul模板、角色扮演、system prompt
- 场景相关：历史人物AI、 philosophers AI、角色扮演提示词

### 3.2 长尾关键词机会

| 关键词类型 | 示例 | 搜索意图 |
|-----------|------|---------|
| 人物+AI | "诸葛亮 AI prompt" | 寻找特定角色的AI设定 |
| 场景+prompt | "历史人物角色扮演提示词" | 寻找玩法指南 |
| 产品+用途 | "AI人格设定下载" | 寻找可下载资源 |
| 问题型 | "如何让AI扮演历史人物" | 寻找教程 |

---

## 四、优化建议

### 4.1 立即执行（本周内）

#### 建议 1: 修复首页 Title
```html
<!-- 当前 -->
<title>Souls - Souls</title>

<!-- 建议 -->
<title>Agent Souls - 让AI拥有历史人物的灵魂 | AI角色Prompt库</title>
```

#### 建议 2: 添加全站 Meta Description
```html
<!-- 首页 -->
<meta name="description" content="收录200+历史人物的AI灵魂设定。与诸葛亮对话战略、向苏格拉底学习提问、让孔子解读论语。免费下载SOUL.md，打造个性化AI助手。">

<!-- 分类页 -->
<meta name="description" content="200+历史人物AI角色设定：诸葛亮、苏格拉底、孔子、曹操等。下载SOUL.md，让AI以历史伟人的思维方式与你对话。">

<!-- 详情页 -->
<meta name="description" content="与{{人物名}}对话的完整AI灵魂设定。包含核心信念、对话风格、典型回应模式。免费下载SOUL.md。">
```

#### 建议 3: 清理 sitemap.xml
- 移除 `_layouts/`、`_includes/` 路径
- 为有效页面添加 `lastmod`、`changefreq`、`priority`

### 4.2 短期优化（2周内）

#### 建议 4: 添加 Open Graph 标签
```html
<meta property="og:title" content="诸葛亮 AI灵魂设定 | Agent Souls">
<meta property="og:description" content="与诸葛亮对话的完整AI人格设定。包含核心信念、对话风格、常用表达。">
<meta property="og:type" content="article">
<meta property="og:url" content="https://agent-souls.com/real_world/zhuge_liang/">
<meta property="og:site_name" content="Agent Souls">
```

#### 建议 5: 添加 Schema.org 结构化数据
```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "诸葛亮 AI Soul",
  "description": "AI人格设定，让AI以诸葛亮的方式思考与对话",
  "author": {"@type": "Organization", "name": "Agent Souls"},
  "about": {"@type": "Person", "name": "诸葛亮"}
}
```

#### 建议 6: 添加使用场景内容
在每个 soul 页面底部添加：
```markdown
## 使用场景

### 适合的问题类型
- 战略决策咨询
- 团队管理困境

### 对话示例
**用户**：如何带领团队度过难关？
**诸葛亮**：先主创业未半而中道崩殂...

### 适用人群
- 历史爱好者
- 战略管理者
```

### 4.3 中期优化（1月内）

#### 建议 7: 创建专题聚合页
- `/prompts/historical-figures/` - 历史人物AI Prompts大全
- `/guides/` - AI人格设定使用指南
- `/faq/` - 常见问题（针对 Featured Snippet 优化）

#### 建议 8: 构建内链网络
- 同分类 soul 自动关联
- 共享 tags 的 soul 优先推荐
- 添加 "相关灵魂" 板块

#### 建议 9: 优化 robots.txt
```
User-agent: *
Allow: /
Disallow: /_layouts/
Disallow: /_includes/
Disallow: /assets/js/
Disallow: /assets/css/

Sitemap: https://agent-souls.com/sitemap.xml
```

---

## 五、预期效果

### 5.1 短期效果（1个月）
- 首页品牌词排名进入第1页
- 收录页面数稳定在 200+
- 搜索结果 CTR 提升 20%+

### 5.2 中期效果（3个月）
- 20+ 长尾词进入前3页
- 有机流量增长 50%+
- 热门人物页面（诸葛亮、孔子）进入前5页

### 5.3 长期效果（6个月）
- 成为 "历史人物AI prompt" 领域权威站点
- 获得 Google 富媒体展示
- 建立稳定自然流量渠道

---

## 六、监控指标

建议设置以下 KPI 进行跟踪：

| 指标 | 当前 | 1月目标 | 3月目标 |
|------|------|---------|---------|
| 收录页面数 | ~200 | 210+ | 220+ |
| 首页品牌词排名 | ? | 前5 | 前3 |
| 长尾词前10页数量 | ? | 10+ | 30+ |
| 有机流量（月） | ? | +20% | +50% |
| 平均 CTR | ? | 3%+ | 5%+ |

---

## 七、执行检查清单

- [ ] 修复首页 Title
- [ ] 添加所有页面 Meta Description
- [ ] 清理 sitemap.xml 中的模板文件
- [ ] 添加 Open Graph 标签
- [ ] 添加 Schema.org 结构化数据
- [ ] 优化 robots.txt
- [ ] 创建专题聚合页
- [ ] 添加 FAQ 页面
- [ ] 设置 Google Search Console
- [ ] 提交更新后的 sitemap

---

*报告生成时间: 2026-03-09*  
*分析工具: acpx codex + web_fetch*
