---
section: contribute
lang: en
title: Adding a term to the glossary
authors:
 - Mor Rubinstein
---

<p class="lead">Each glossary (meaning, each translated instance of the glossary), has three components:</p>

* A layout template for the glossary homepage: 'glossary.html'
* A layout template for the glossary in each language: 'glossary/{lang}/index.md'
* A directory of the glossary terms. Each term in the directory is listed as the url slug (In English, all lower case letters, and hyphens instead of white spaces).

Currently, the English glossary has been updated and organized. Other languages please follow these [instructions](http://opendatahandbook.org/contribute/translate-glossary/).

To add a new term, all you need is to have a GitHub account.

## 1. Create a folder for the term

Log in to GitHub and go to this [link](https://github.com/{{ site.github_username }}/{{ site.github_repo }}/tree/gh-pages/glossary/en/terms)

You will see the branch name ('gh-pages') and a directory. You will also see the breadcrumb `{{ site.github_repo }} / glossary / en / terms / +`. Click on the plus symbol <code class="icon-plus"><span>[plus icon]</span></code> to create a new folder.

Write the name of the term that you want to add in a new slug (In English, all lower case letters, and hyphens instead of white spaces) and add a slash ('/') at the end of the terms name. This will create a new folder name.

## 2. Create a file for your term

Now you will see the breadcrumb - `{{ site.github_repo }} / glossary / en / terms / your-new-term / + ` Click on the plus symbol <code class="icon-plus"><span>[plus icon]</span></code> again. Now write in the path 'index.md'. This will save the whole file as a markdown file.

## 3. Write the term definition

In the text editor below, add the front matter (Jekyll way to mark the page):

    ---
    section: terms
    lang: en
    title: The term name
    ---

Write the term definition after the front matter as usual.

## 4. Make a pull request

Click on “Create a new branch for this commit and start a pull request.” This will allow us to review your changes.

Thank you! All done! If the handbook editors are happy with your term, it will be added to the glossary.
