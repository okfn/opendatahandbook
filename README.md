# opendatahandbook-v2

Repository of http://opendatahandbook.org/

This is a [Jekyll](http://jekyllrb.com/) based site, with pages written in HTML and [Markdown](http://daringfireball.net/projects/markdown/syntax) (specifically [Kramdown](http://kramdown.gettalong.org/syntax.html)), with Markdown being used where possible for ease of editing.

## Editors

Please see the [Contribute](http://opendatahandbook.org/contribute/) section of the site for further instructions.

## Developers

### Dependancies

* [Jekyll](http://jekyllrb.com/)

### Information architecture

There are four sections of content, implemented as simple Jekyll pages: `guide`, `value-stories`, `glossary`, and `resources`.

Some sections have translations. These are implemented by adjacent directories, where the name of the directory is the locale of the translation.

#### Guide

The narrative content of the Open Data Handbook.

#### Value Stories

A collection of stories demonstrating examples of open data wins.

#### Glossary

A glossary explaining terms used in the Open Data Handbook.

#### Resources

Additional resources for the Open Data Handbook.

### Working with the glossary

Each glossary (meaning, each glossary *translation*), is made of three components:

* A 'glossary.html' layout template
* A 'glossary/{lang}/index.md' page, which uses the glossary layout to render a list of glossary terms in the correct language
* A 'glossary/{lang}/terms/' directory, which contains an entry for each glossary term. Each entry is the slugified name of the English version of the term.

Currently, the English glossary has been organized. To expand this pattern to other languages:

* Copy the English terms directory into your target language directory
* If your current index.md has translated glossary terms, then add them to the appropriate page under 'terms', replacing the English text that was copied over from 'en'.
* Then, replace your target language's index.md file with the 'en' one, changing the `lang` value to that of your target language.

### Branches

 - **gh-pages** - live site
 - **master** - minimal content, to speed up building (for development)
 - **theme** - no site specific content, used to create new sites
 