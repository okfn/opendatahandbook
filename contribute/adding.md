---
section: contribute
lang: en
title: Adding a page
authors:
 - Sam Smith
---

<p class="lead">Most of what you need to know to add a new page is covered under '<a href="{{ "/contribute/editing/" | prepend: site.baseurl }}" rel="external">Editing a page</a>', so make sure you have first read through that section.</p>

Adding a page follows a similar process to editing. Instead of locating your page, your first step is to locate your new page's parent directory.

## 1. Create the page

First locate the parent directory, or folder, in which your file will live. If you are adding a page to the English language Handbook, for example, you should be in the '**en**' directory, where you'll see a list of all the Handbook pages.

Above the list of pages is a breadcrumb trail `{{ site.github_repo }} / guide / en /`, to the right of which is a plus symbol <code class="icon-plus"><span>[plus icon]</span></code>. Click the plus symbol to create your new page.

## 2. Name your file

You should now have a new file editor page open. The first editable section you are presented with is the '*Name your file*' field. As we touched upon when looking at [editing files]({{ "/contribute/editing/" | prepend: site.baseurl }}), the file name corresponds to the URL of the page on the site. There are a few of rules to follow here:

* The file name should reflect the title of the new page
* Must be unique
* Should be all lowercase
* Words should be separated by hyphens (-)
* File name should end with the extension '*.md*' (the .md extension indicates a markdown file)

As an example, if you were creating a page titled '*My Cool Page*', you would use a file name of:

    my-cool-page.md

Assuming you are creating this in the '*en*' directory, this would result in a URL of *{{ site.url }}/en/my-cool-page*

<div class="note">
  <h6>Note</h6>
  <p>The actual words used in your file name are not crucial. It’s fine to use a more succinct version of your page title, for example.</p>
</div>

## 3. Formatting your content

This step is the same as when editing a page. You need to start your file with the Front Matter, then add your content, formatting it using Markdown. Here is a template to get you started:

    ---
    title: My Cool Page
    authors:
     - Fred Bloggs
    ---

    ##A large introductory paragraph.

    Regular paragraphs, separated by empty lines.

    ###A heading

    Another paragraph.

     * Maybe
     * a
     * list

When you’re done, click '*Propose new file*'.

## 4. Make a pull request

Once you have created your page(s) and updated the contents document, you're ready to make your pull request. Click the pull request icon to the right of the screen <code class="icon-git-pull-request"><span>[git pull-request icon]</span></code>, then click '*New pull request*'.

At the top of the resulting comparison screen, you’ll see a row of select boxes. You want to make sure these are configured like so:

<div class="github panel">
  <div class="range-editor">
    <span class="icon-git-compare range-editor-icon"></span>
    <div class="range">

      <div class="range-cross-repo-pair">
        <div class="select-menu js-menu-container js-select-menu fork-suggester">
          <span class="minibutton select-menu-button js-menu-target" role="button" aria-label="Choose a Base Repository" aria-haspopup="true">
            <i>base fork:</i>
            <span class="js-select-button css-truncate css-truncate-target" title="base: ckan/ckan">{{ site.github_username }}/{{ site.github_repo }}</span>
          </span>
        </div>

        <div class="select-menu js-menu-container js-select-menu commitish-suggester">
          <span class="minibutton select-menu-button js-menu-target branch" role="button" aria-label="Choose a base branch" aria-haspopup="true">
            <i>base:</i>
            <span class="js-select-button css-truncate css-truncate-target" title="base: master">gh-pages</span>
          </span>
        </div>
      </div>

      <span class="dots">...</span>

      <div class="range-cross-repo-pair">
        <div class="select-menu js-menu-container js-select-menu fork-suggester">
          <span class="minibutton select-menu-button js-menu-target" role="button" aria-label="Choose a Head Repository" aria-haspopup="true">
            <i>head fork:</i>
            <span class="js-select-button css-truncate css-truncate-target" title="head: mintcanary/ckan"><em>username</em>/{{ site.github_repo }}</span>
          </span>
        </div>

        <div class="select-menu js-menu-container js-select-menu commitish-suggester">
          <span class="minibutton select-menu-button js-menu-target branch" role="button" aria-label="Choose a head branch" aria-haspopup="true">
            <i>compare:</i>
            <span class="js-select-button css-truncate css-truncate-target" title="compare: master"><em>branch</em></span>
          </span>
        </div>

      </div>
    </div>
  </div>
</div>

_**username** being your github username, **branch** being the branch you have been working on._

You should now be able to see listed below, all the changes that you wish to contribute. If everything looks as it should, click '*Create pull request*'.

Give your pull request a title and description, then click '*Create pul request*'. You have now contributed your pages to the Handbook :)
