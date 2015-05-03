---
layout: default
wide: true
title: Value Stories
---

<div class="stories">
  <span class="pre-header">{{ page.title }}</span>
  <ul class="post-list">
  {% for page in site.pages %}
  {% if page.section == 'value-stories' %}
    <li>
      <h2>
        <a class="post-link" href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a>
      </h2>
      <span class="post-excerpt">{{ page.content | truncatewords: 100 | strip_html }} </span>
      <a class="post-link" href="{{ page.url | prepend: site.baseurl }}">More</a>
      </li>
      {% endif %}
    {% endfor %}
  </ul>
</div>
