---
section: contribute
title: Adding a resource to the library
authors:
 - Mor Rubinstein
lang: en
---

<p class="lead">Our resource library is a curated collection of open data reosurces across the community. Everyone can add a resource to the library. This is how to do so.</p>

## 1. Add a folder

Log in to GitHub and head to this [link](https://github.com/{{ site.github_username }}/{{ site.github_repo }}/tree/gh-pages/resources).

Every resource has a slug number. To add your resource, you need to give it a number. Look at the list and give your resource the number that follows the current last number in the list (e.g. if the number is 056, your resource should be named 057).

Click on the plus symbol <code class="icon-plus"><span>[plus icon]</span></code> in the directory line and add the number and a slash ('/'). For example: `060/`.

## 2. Add an index file

Click on the plus symbol <code class="icon-plus"><span>[plus icon]</span></code> again. Add a file named 'index.md' to your new folder.

## 3. Add the resource

In the text editor, add the front matter fields in this pattern:

    ---
    section: resources
    lang: Two first letters of the language, according to language code in this table
    Author: The name(s) of the person(s) who wrote the text
    Country: One or more countries by full name, separated with a comma: ",". If there is no specific country, write 'global'
    Description: 1-5 lines that summarizes the text
    Keywords: Important descriptors of the text, separated with a comma, ","
    Link: The link to the resource online
    MediaType: List one out of these four types: Presentation, Article, Publication, Video
    Notes: Any notes or comments
    Publishing_date: The year the resource was published, e.g. 2015
    Publishing_entity: The organisation(s) which publish the resource
    Region: North America, Latin America, Asia, Europe, Africa, Mena, Global
    Title: The name of the resource
    Topic: Choose one out of these nine: The Basics, Advocacy, Privacy, Civic Engagement, Right for Information, Data Training, Policy Standards
    ---

## 4. Make a pull request

Click on "Create a new branch for this commit and start a pull request." This will allow us to review your changes.

Thank you! All done!
