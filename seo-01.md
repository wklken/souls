# Souls 项目 SEO 优化报告 v1.0

**日期**: 2026-03-09  
**站点**: https://agent-souls.com/  
**项目**: Souls - AI 人格模板库

---

## 一、站点现状诊断

### 1.1 基本概况

| 指标 | 数值 |
|------|------|
| 收录规模 | 212 个独立页面（200 历史人物 + 4 虚构角色 + 8 专家角色） |
| 技术栈 | Jekyll 静态站点，GitHub Pages 部署 |
| 语言支持 | 中英双语（国际化已实现） |
| 基础配置 | 已配置 sitemap.xml、robots.txt、search.json |

### 1.2 主要问题清单

| 问题 | 影响程度 | 优先级 |
|------|----------|--------|
| 首页标题冗余 "Souls - Souls" | 品牌词重复，浪费标题权重 | 高 |
| 缺少 Meta Description | 搜索结果摘要质量低，CTR 下降 | 高 |
| 无 Open Graph / Twitter Card | 社交分享展示效果差 | 中 |
| 无结构化数据 (Schema.org) | 搜索引擎理解不足，难获富媒体展示 | 高 |
| URL 路径未优化关键词 | `/real_world/` 对用户无意义 | 中 |
| 内链网络薄弱 | 页面间权重传递不足 | 中 |
| 长尾词布局空白 | 错失大量精准流量机会 | 高 |
| sitemap 包含非页面文件 | 如 `_layouts/home.html` 不应被索引 | 中 |
| 部分 soul 缺少 tags | 影响搜索和推荐效果 | 中 |

---

## 二、SEO 优化方案

### 2.1 技术基础优化（阶段一：1-2 天）

#### 2.1.1 标题与 Meta 描述优化

**首页 (index.html)**

```html
<title>Agent Souls - 让AI拥有历史人物的灵魂 | AI Soul Prompts Library</title>
<meta name="description" content="收录200+历史人物与虚拟角色的AI灵魂设定。与诸葛亮对话战略、向苏格拉底学习提问、让孔子解读论语。免费下载SOUL.md，打造个性化AI助手。">
```

**分类页 (real_world.md)**

```html
<title>历史人物AI灵魂库 - Agent Souls | 孔子、苏格拉底、诸葛亮Prompt</title>
<meta name="description" content="收录200+历史人物的AI灵魂设定：诸葛亮、苏格拉底、孔子、曹操等。下载SOUL.md，让AI以历史伟人的思维方式与你对话。">
```

**专家角色页 (personas.md)**

```html
<title>专家角色AI Prompt - Agent Souls | 产品总监、CTO、投资人</title>
<meta name="description" content="8大专家角色AI人格：产品总监、硅谷CTO、投资人、管理顾问等。获取专业领域的AI对话设定，提升决策质量。">
```

**虚拟世界页 (virtual_world.md)**

```html
<title>虚拟角色AI设定 - Agent Souls | 孙悟空、福尔摩斯、哈姆雷特</title>
<meta name="description" content="经典虚拟角色AI人格设定：孙悟空、福尔摩斯、哈姆雷特、堂吉诃德。让AI以文学角色的方式与你互动。">
```

**详情页模板 (_layouts/soul.html)**

```html
<title>{{ page_title_zh }} AI灵魂设定 - {{ tags[0] }} | Agent Souls</title>
<meta name="description" content="与{{ page_title_zh }}对话的完整AI灵魂设定。包含核心信念、对话风格、典型回应模式。免费下载SOUL.md，打造{{ tags[0] }}类型的AI助手。">
```

#### 2.1.2 Open Graph 标签

在每个页面 `<head>` 中添加：

```html
<!-- Open Graph -->
<meta property="og:title" content="{{ page_title_zh }} AI灵魂设定 | Agent Souls">
<meta property="og:description" content="与{{ page_title_zh }}对话的完整AI人格设定。包含核心信念、对话风格、常用表达。">
<meta property="og:url" content="https://agent-souls.com{{ page.url }}">
<meta property="og:type" content="article">
<meta property="og:locale" content="zh_CN">
<meta property="og:locale:alternate" content="en_US">
<meta property="og:site_name" content="Agent Souls">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{{ page_title_zh }} AI灵魂设定">
<meta name="twitter:description" content="与{{ page_title_zh }}对话的完整AI人格设定">
```

#### 2.1.3 Schema.org 结构化数据

在详情页添加 JSON-LD：

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "{{ page_title_zh }} AI Soul",
  "description": "AI人格设定，让AI以{{ page_title_zh }}的方式思考与对话",
  "author": {
    "@type": "Organization",
    "name": "Agent Souls",
    "url": "https://agent-souls.com"
  },
  "about": {
    "@type": "Person",
    "name": "{{ page_title_zh }}"
  },
  "inLanguage": ["zh", "en"],
  "isAccessibleForFree": true,
  "license": "https://github.com/wklken/souls/blob/main/LICENSE"
}
</script>
```

#### 2.1.4 Canonical 标签与多语言支持

```html
<!-- Canonical URL -->
<link rel="canonical" href="https://agent-souls.com{{ page.url }}">

<!-- Hreflang 标签（多语言 SEO） -->
<link rel="alternate" hreflang="zh" href="https://agent-souls.com{{ page.url }}">
<link rel="alternate" hreflang="en" href="https://agent-souls.com/en{{ page.url }}">
<link rel="alternate" hreflang="x-default" href="https://agent-souls.com{{ page.url }}">
```

---

### 2.2 内容优化（阶段二：3-5 天）

#### 2.2.1 长尾关键词矩阵

基于 212 个 soul 页面，布局以下长尾词：

**类型一：人物 + AI/Prompt**

| 中文关键词 | 英文关键词 | 目标页面示例 |
|------------|------------|--------------|
| 诸葛亮 AI 对话设定 | Zhuge Liang AI persona | /real_world/zhuge_liang/ |
| 苏格拉底式提问 prompt | Socratic questioning prompt | /real_world/socrates/ |
| 孔子论语 AI 解读 | Confucius AI character | /real_world/confucius/ |
| 曹操性格分析 prompt | Cao Cao personality prompt | /real_world/cao_cao/ |
| 福尔摩斯角色扮演 | Sherlock Holmes roleplay | /virtual_world/sherlock_holmes/ |
| 孙悟空 AI 设定 | Sun Wukong AI soul | /virtual_world/sun_wukong/ |

**类型二：场景 + 用途**

| 关键词 | 搜索意图 | 建议行动 |
|--------|----------|----------|
| 历史老师 AI 提示词 | 教育场景 | 创建专题页 /guides/education/ |
| 哲学对话 AI 人格 | 学习场景 | 优化哲学家详情页 |
| 战略顾问 AI 设定 | 商业场景 | 创建专题页 /guides/business/ |
| 文学创作 AI 助手 | 创作场景 | 创建作家专题页 |

**类型三：专家角色关键词**

| 中文 | 英文 | 目标页 |
|------|------|--------|
| 产品总监 AI Prompt | Product Director AI prompt | /personas/product_director/ |
| 投资人 AI 设定 | Venture Capitalist AI persona | /personas/venture_capitalist/ |
| 硅谷 CTO 对话风格 | Silicon Valley CTO AI | /personas/silicon_valley_cto/ |

#### 2.2.2 内容增强模板

在每个 soul 详情页添加 **"使用场景"** 章节：

```markdown
## 使用场景

### 适合的问题类型
- 战略决策咨询
- 团队管理困境
- 危机处理建议
- 历史事件分析

### 对话示例

**用户**：如何带领团队度过难关？

**诸葛亮**：先主创业未半而中道崩殂，今天下三分，益州疲弊...
（以下为该角色的典型回答风格示例，约 100-150 字）

### 适用人群
- 历史爱好者
- 战略管理者
- 写作者/编剧
- AI 角色扮演玩家

### 相关推荐
- [曹操](/real_world/cao_cao/) - 了解对手视角
- [司马懿](/real_world/sima_yi/) - 另一位战略家
- [刘备](/real_world/liu_bei/) - 仁德之君的视角
```

#### 2.2.3 内链网络构建

**自动内链规则**：

1. **同分类关联**：相同 category 的 soul 自动关联
2. **标签关联**：共享 tags 的 soul 优先推荐
3. **时代关联**：相同时代的人物互相链接
4. **领域关联**：相同领域（哲学/军事/文学）互相链接

在详情页底部添加 **"相似灵魂"** 板块：

```html
<section class="related-souls">
  <h3>相似的灵魂</h3>
  <div class="related-grid">
    <!-- 自动展示同分类/同标签的其他 6 个 soul -->
  </div>
</section>
```

---

### 2.3 流量获取优化（阶段三：持续）

#### 2.3.1 专题聚合页（Landing Pages）

创建以下高价值 landing pages，针对高搜索量关键词：

**页面一：历史人物 AI Prompts 大全**

```yaml
url: /prompts/historical-figures/
title: 历史人物 AI Prompts 大全 - 200+人物免费使用
description: 最全的历史人物AI对话提示词库。孔子、苏格拉底、诸葛亮、曹操...一键下载，让AI拥有历史伟人的智慧。
```

内容结构：
- 热门人物推荐（TOP 12）
- 按时代分类（先秦/秦汉/三国/唐宋/明清/西方古代/西方近代）
- 按领域分类（哲学/军事/政治/文学/科学）
- 使用指南

**页面二：AI 人格设定指南**

```yaml
url: /guides/
title: AI人格设定完全指南 - 打造专属AI角色
```

内容：
- 什么是 AI Soul？
- 如何使用 SOUL.md
- 热门使用场景
- 常见问题 FAQ

**页面三：专家角色 Prompts**

```yaml
url: /prompts/expert-personas/
title: 专家角色 AI Prompts - 产品、投资、咨询、医疗
```

#### 2.3.2 FAQ 页面（针对 Featured Snippet）

创建 `/faq/` 页面，回答结构化问题：

**Q1: 什么是 AI Soul？**
- AI Soul 是让 AI 扮演特定角色的完整人格设定
- 包含核心信念、说话风格、知识边界等

**Q2: 如何在 ChatGPT/Claude 中使用这些设定？**
- 下载 SOUL.md 文件
- 将内容作为 system prompt 使用
- 或使用 "扮演 XX 角色" 的简化指令

**Q3: 这些 AI 人格是怎么生成的？**
- 基于历史人物的公开资料
- 由 AI 辅助生成，人工审核
- 所有内容标注"AI生成，仅供参考"

**Q4: 可以商用吗？**
- 项目采用 MIT 协议
- 可自由使用、修改、商用

**Q5: 如何贡献新的 soul？**
- 在 GitHub 提交 Issue
- 使用 soul-creator skill 创建并提交 PR

---

### 2.4 技术细节优化（阶段四：1 天）

#### 2.4.1 sitemap.xml 清理

当前问题：sitemap 包含不应索引的文件

**移除项**：
- `_layouts/home.html`
- `_layouts/soul.html`
- `_layouts/default.html`
- `_includes/` 下的所有文件
- `.html` 后缀的重复项

**保留项**：
- 首页 `/`
- 分类页 `/real_world/`, `/personas/`, `/virtual_world/`
- 所有 soul 详情页

#### 2.4.2 缺失数据补全

需要补全 tags 的 soul 列表：
- /real_world/bai_qi/
- /real_world/han_xin/
- /real_world/desiderius_erasmus/
- /real_world/boccaccio/
- /real_world/yan_fu/
- /real_world/george_berkeley/

#### 2.4.3 robots.txt 优化

```
User-agent: *
Allow: /

# 禁止爬虫索引模板和包含文件
Disallow: /_layouts/
Disallow: /_includes/
Disallow: /assets/js/
Disallow: /assets/css/

Sitemap: https://agent-souls.com/sitemap.xml
```

#### 2.4.4 性能优化

- 确保图片懒加载
- 压缩 CSS/JS
- 启用 Gzip 压缩（GitHub Pages 自动支持）
- 移动端响应式检查

---

## 三、执行计划与时间表

### 第一周：基础修复（高优先级）

| 天数 | 任务 | 文件 |
|------|------|------|
| Day 1 | 修复首页 title/description | `index.md`, `_config.yml` |
| Day 1 | 修复分类页 meta | `real_world.md`, `personas.md`, `virtual_world.md` |
| Day 2 | 详情页动态 meta | `_layouts/soul.html` |
| Day 2 | 添加 Open Graph 标签 | `_layouts/default.html` |
| Day 3 | 清理 sitemap | `sitemap.xml` 或生成脚本 |
| Day 3 | 修复 robots.txt | `robots.txt` |
| Day 4 | 补全缺失 tags | 对应 soul 的 markdown 文件 |
| Day 5 | 测试与验证 | 使用 Google Search Console |

### 第二周：内容增强

| 天数 | 任务 | 说明 |
|------|------|------|
| Day 6-7 | 添加使用场景模板 | 更新 `_layouts/soul.html` |
| Day 8-9 | 实施内链推荐系统 | 修改 soul.html 模板 |
| Day 10 | 添加 Schema 结构化数据 | 添加到 soul.html |

### 第三周：专题页与 FAQ

| 天数 | 任务 | 说明 |
|------|------|------|
| Day 11-12 | 创建 /prompts/historical-figures/ | 新页面 |
| Day 13 | 创建 /guides/ 指南页 | 新页面 |
| Day 14 | 创建 /faq/ 页面 | 新页面 |

### 第四周：持续优化

- 提交 sitemap 到 Google Search Console
- 监控收录情况
- 根据搜索表现迭代关键词策略

---

## 四、预期效果与 KPI

### 4.1 短期目标（1个月）

| 指标 | 当前 | 目标 |
|------|------|------|
| 首页品牌词排名 | 不确定 | 第1页前3 |
| 收录页面数 | ~200 | 200+ |
| 平均 CTR | 未知 | 提升 20% |

### 4.2 中期目标（3个月）

| 指标 | 目标 |
|------|------|
| 长尾词排名 | 20+ 长尾词进入前3页 |
| 有机流量 | 月访问增长 50%+ |
| 热门人物页面 | 诸葛亮、孔子进入前5页 |

### 4.3 长期目标（6个月）

- 成为 "历史人物AI prompt" 相关搜索的权威站点
- 获得 Google 富媒体展示（Rich Snippets）
- 建立稳定的自然流量获取渠道

---

## 五、监控与工具

### 5.1 必备工具

- **Google Search Console**: 监控收录、排名、点击率
- **Google Analytics**: 流量分析
- **PageSpeed Insights**: 性能检测
- **Schema Markup Validator**: 结构化数据验证

### 5.2 关键检查清单

- [ ] 所有页面都有唯一的 title
- [ ] 所有页面都有 description（155字符以内）
- [ ] Open Graph 标签验证通过
- [ ] Schema 结构化数据无错误
- [ ] sitemap 只包含有效页面
- [ ] 移动端体验良好
- [ ] 页面加载时间 < 3秒

---

## 六、附录

### 6.1 关键代码片段

**动态生成 Meta Description（Jekyll）**

```liquid
{% if page.description %}
  <meta name="description" content="{{ page.description }}">
{% else %}
  <meta name="description" content="与{{ page.title }}对话的完整AI灵魂设定。包含核心信念、对话风格、典型回应模式。免费下载SOUL.md，打造个性化AI助手。">
{% endif %}
```

**生成相似推荐（基于 tags）**

```liquid
{% assign current_tags = page.tags %}
{% assign related_souls = site.pages | where: 'layout', 'soul' %}
{% for soul in related_souls %}
  {% if soul.url != page.url %}
    {% assign soul_tags = soul.tags %}
    {% for tag in current_tags %}
      {% if soul_tags contains tag %}
        <!-- 显示推荐 -->
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

### 6.2 参考资料

- [Google SEO 入门指南](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Schema.org 文档](https://schema.org/)
- [Open Graph 协议](https://ogp.me/)
- [Jekyll SEO 最佳实践](https://jekyllrb.com/docs/step-by-step/10-deployment/)

---

**文档版本**: v1.0  
**下次更新**: 根据实施进度更新
