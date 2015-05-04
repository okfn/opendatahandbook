---
layout: default
wide: true
title: Value Stories
---

<div class="stories">
  <span class="pre-header">{{ page.title }}</span>
  <ul class="post-list">
  {% for story in site.value-stories %}
    <li>
      <h2>
        <a class="post-link" href="{{ story.url | prepend: site.baseurl }}">{{ story.title }}</a>
      </h2>
      <span class="post-excerpt">{{ story.content | truncatewords: 100 | strip_html }} </span>
      <a class="post-link" href="{{ story.url | prepend: site.baseurl }}">More</a>
      </li>
    {% endfor %}
  </ul>
</div>
