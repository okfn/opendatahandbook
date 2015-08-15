---
section: contribute
lang: en
title: Translating the guide
authors:
 - Mor Rubinstein
---

<p class="lead">Translating the guide is easy, no need to any other software, all you need is a github account!</p>

Some languages already have translated versions of the guide. If you don't have a version in your language, here is how to do it.

## 1. Create a new language folder

In github, under the breadcrumb - `{{ site.github_repo }} / guide /` there will be a plus symbol <code class="icon-plus"><span>[plus icon]</span></code>. Click on it and enter your [two letter languages code](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). Add a slash ('/') after the two letter to create a folder.

## 2. Create a page folder

Now you will see your language code and a plus symbol <code class="icon-plus"><span>[plus icon]</span></code> on the breadcrumb. Add a page name that you want to translate in **English** and add a slash at the end.

## 3. Translate the content

You will now see a new plus symbol <code class="icon-plus"><span>[plus icon]</span></code>. Add the file name 'index.md'.

In the text editor add the following front matter:

    ---
    section: guide
    lang: The two letter code for your language
    title: The title in your language
    ---

Translate as usual.

## 4. Create a pull request

If all good, we will add it to the site.

Repeat for other parts of the guide if needed. That's it, you are all done!<br />
Thank you for helping us to make the guide accessiable to others!
