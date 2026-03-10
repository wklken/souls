---
layout: default
title: "AI 灵魂团队 | 哲学家团队、创业产品团队"
title_en: "Teams"
title_zh: "灵魂团队"
seo_title_zh: "AI 灵魂团队 | 哲学家团队、创业产品团队"
seo_title_en: "AI Soul Teams | Philosopher Team, Startup Product Team"
description: "AI 灵魂团队配置，一键组建哲学家团队、创业产品团队。下载团队配置 JSON，快速在本地拉起一个 AI 团队进行协作。"
description_zh: "AI 灵魂团队配置，一键组建哲学家团队、创业产品团队。下载团队配置 JSON，快速在本地拉起一个 AI 团队进行协作。"
description_en: "AI soul team configurations. Build your Philosopher Team or Startup Product Team with one click. Download team config JSON to quickly deploy an AI team locally for collaboration."
image: "https://robohash.org/agent-souls-teams.png?size=1200x630&set=set4&bgset=bg1"
category: teams
permalink: /teams/
---

<div class="soul-list">
  <h1 data-i18n="nav.teams">灵魂团队</h1>
  <p class="category-description" data-i18n="teams.description">组建 AI 灵魂团队，让多个 AI 角色协作完成任务</p>
  
  <div class="team-grid" id="team-grid">
    {% if site.data.teams.size > 0 %}
    {% for team in site.data.teams %}
      {% assign team_name_zh = team.name_zh %}
      {% assign team_name_en = team.name_en %}
      {% assign team_desc_zh = team.description_zh %}
      {% assign team_desc_en = team.description_en %}
      {% assign team_tags_zh = team.tags %}
      {% assign team_tags_en = team.tags_en %}
      <a href="/teams/{{ team.id }}/" class="team-card">
        <div class="team-card-header">
          <div
            class="team-name"
            data-localized-zh="{{ team_name_zh | escape }}"
            data-localized-en="{{ team_name_en | escape }}"
          >{{ team_name_zh }}</div>
          {% if team_name_en and team_name_en != team_name_zh %}
          <div
            class="team-english"
            data-localized-zh="{{ team_name_en | escape }}"
            data-localized-en="{{ team_name_zh | escape }}"
          >{{ team_name_en }}</div>
          {% endif %}
        </div>
        <div
          class="team-description"
          data-localized-zh="{{ team_desc_zh | escape }}"
          data-localized-en="{{ team_desc_en | escape }}"
        >{{ team_desc_zh }}</div>
        <div class="team-meta">
          <span class="team-member-count">
            <span class="member-icon">👥</span>
            <span data-i18n="teams.members" data-count="{{ team.members.size }}">{{ team.members.size }} 位成员</span>
          </span>
          {% if team_tags_zh %}
          <div
            class="team-tags"
            data-localized-zh="{{ team_tags_zh | slice: 0, 3 | join: ', ' | escape }}"
            data-localized-en="{{ team_tags_en | slice: 0, 3 | join: ', ' | escape }}"
          >{{ team_tags_zh | slice: 0, 3 | join: ', ' }}</div>
          {% endif %}
        </div>
      </a>
    {% endfor %}
    {% else %}
    <p class="list-empty">暂无团队数据</p>
    {% endif %}
  </div>
</div>
