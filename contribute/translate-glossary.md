---
section: contribute
lang: en
title: Translating the glossary
authors:
 - Mor Rubinstein
---

## What's new in the glossary

In the old version of the handbook, the glossary was one page with all of the terms in it. In the new version, we gave each glossary a webpage for better referencing and linking.

Glossaries that were translated in the old version of the handbook have been transfered to the new site. Please check if your language has an old version of the glossary. You can find them [here](https://github.com/{{ site.github_username }}/{{ site.github_repo }}/tree/gh-pages/glossary).

## If you do have an old version translated, follow these steps:

The old glossary format does not allow linking from the new version of the guide, and you will need to transfer the term to the new format.

### 1. Create a new folder for the term

Under your language folder, follow the breadcrumb trail `{{ site.github_repo }} / glossary / es /`, to the right of which is a plus symbol <code class="icon-plus"><span>[plus icon]</span></code>. Create a folder for each term by pressing on the plus symbol <code class="icon-plus"><span>[plus icon]</span></code> and type the term name in English. The folder name should be in lower-case letters with dashes ('-') instead of white spaces. Add a slash ('/') in the end of the name to create a new folder.

### 2. Translate the term

Open a new 'index.md' file by clicking on the plus symbol <code class="icon-plus"><span>[plus icon]</span></code>.

In the text editor below add the front matter:

    ---
    section: terms
    lang: en
    title: The term name
    ---

Change the 'lang' field to your language code. Change the title to the term title in YOUR language.

Below the front matter copy the term from the old glossary.

### 3. Make a pull request.

All done! Keep doing this until all terms got their own folder and page.

## If you have never translated the glossary before, follow the these steps:

### 1. Copy the English glossary

Copy the English terms directory into your target language directory in the glossary folder. This step can not be done through the Github website and you will have to fork the handbook for your machine. Information about forking and cloning can be find [here](https://help.github.com/articles/fork-a-repo/). Notice, some languages have already been moved and translated. Check the folder to make sure you are not overwriting someone's work.

### 2. Edit the term

Choose a term and open the 'index.md' file.

The front matter looks as follows:

    ---
    section: terms
    lang: en
    title: The term name
    ---

Change the lang field to your language code. Change the title to the term title in YOUR language.

In the text editor, below the front matter, enter your translation to the term.

### 3. Submit changes through a pull request.

All done! Thank you for your help!
