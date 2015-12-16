# Handbook Theme

This is essentially a stripped down version of http://opendatahandbook.org/. The intention is for it to be reused, as a base for other websites. Please note, relatively little time has been spent so far, converting this from a bespoke site to something generic. You will probably find Open Data Handbook specific stuff in the code. Please raise any issues [here](https://github.com/okfn/handbook-theme/issues).

## Dependancies

* [Jekyll](http://jekyllrb.com/)

## Suggested workflow

### Quick Start

 - Clone this repository
 - Create a new branch for your code, e.g `gh-pages`
 - Start editing your new branch

### Theme updates

In order to include updates in the future, we suggest that you add this repository as a remote to your project. You can then cherry pick any updates into your customised branch. Equally, if you make a change to your custom branch that you feel should be part of the theme, feel free to make a pull request.

## Config options

Aside from standard Jekyll options, we have:

 - `devs`, `contributors` & `supporters` - used to generate the [Credits](http://opendatahandbook.org/credits/) page.
 - `googleanalytics` - assign a Google Analytics tracking ID to add the analytics code to the footer. If you do not wish to include the Google Analytics code, remove this.
 - `related_projects` - populates the list in the footer

 Note: the correct use of `baseurl` is as described [here](https://byparker.com/blog/2014/clearing-up-confusion-around-baseurl/)

## Front matter

Set per page, layout or as a default (see http://jekyllrb.com/docs/configuration/#front-matter-defaults)

 - `lead` - if defined, first paragraph in the page will be larger
 - `edit` -  if defined, a link to edit the page will be present in the page tools.
 - `wide` - if defined, the menu will automatically expand on wide (enough) screens.
 - `authors` - allows single or multiple authors
 - `section` - defines the section headings at the top of each page.

## Layouts

 - `default` - includes header and footer
 - `page` - adds page structure to `default`. **If unsure, use this layout**.
 - `post`, `docs` - similar to `page`, with subtle differences. You can probably ignore these.
 - `apps` - originally used for http://opendatahandbook.org/solutions/en/ still quite bespoke at this time.
