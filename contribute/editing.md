---
section: contribute
lang: en
title: Editing a page
authors:
 - Sam Smith
---

<p class="lead">If you haven't done so already, the first thing you need to do is head over to <a href="https://github.com/" rel="external">Github</a> and create your free account.</p>

There are three steps to editing a page. First you need to locate the page you wish to edit. There are a couple of ways to do this. **Method A** is probably the simplest, and most likely way you'll do it. **Method B** will serve as a primer for the next section: *Adding a page*.

## 1. Locate the page

#### Method A: Browse the website

While reading any section of the Handbook you'll see a button with the paper icon <code class="icon-paper"><span>[paper icon]</span> Improve this page</code> in the right side or bottom of the page, depending on the size of the screen. Hovering over it then clicking an '*Edit on Github*' button will take you directly to an editable version of that page. Easy huh?

<div class="note">
  <h6>Note</h6>
  <p>When the editable page opens it will (most likely) contain a message saying <em>"You need to fork this repository to propose changes."</em>. If this is your first edit to The Open Data Handbook there will be a '<em>Fork this repository and propose changes</em>' button. This is normal and part of the workflow. Click the button to start editing.</p>
</div>

#### Method B: Browse the Github repository

The entire file structure of this site can be browsed on Github. For example, the root of the site is [here](https://github.com/{{ site.github_username }}/{{ site.github_repo }}), and the English language guide section of the Handbook is [here](https://github.com/{{ site.github_username }}/{{ site.github_repo }}/tree/gh-pages/guide/en). It's helpful to understand that the page URLs correspond to the file structure you see here. So, if you wanted to edit the Open Data Guide introduction page, given that it's URL is <code>{{ site.url }}/<strong>guide</strong>/<strong>en</strong>/<strong>introduction</strong>/</code> we know this file can be found in the <code><strong>guide</strong>/<strong>en</strong>/<strong>introduction</strong></code> directory with the filename <code><strong>index</strong>.md</code> Following these links you should see a preview of the page you wish to edit. From here click the edit icon <code class="icon-pencil"><span>[pencil icon]</span></code> to start editing.

<div class="note">
  <h6>Pro Tip!</h6>
  <p>Press <code>t</code> on any tree or blob page to launch the file finder.</p>
</div>

## 2. Make your changes

With the editable content in front of you, you're probably either thinking "great, let's get editing", or "hang on, this looks a bit weird". In case it's the latter, let's have a closer look. The first thing to recognise is the 'Front Matter', which will look like this:

    ---
    title: Introduction
    ---

The front matter must be the first thing in the file, must adhere to the above syntax, and must be set between triple-dashed lines. Numerous variables can be set here, but you'll usually just need `title`. The title set here will be used as the main heading for the page, as well as in the browser tab.

The other important thing to recognise is the Markdown syntax. For example, where you see a line commencing with two hash marks:

    ## Do you know exactly how much of your tax money is spent on street lights?

This is the Markdown way of creating a level two heading. On the site it will be outputted like so:

## Do you know exactly how much of your tax money is spent on street lights?

Another common formatting requirement is bullet points, or lists. These are achieved in Markdown by using asterisks, like so:

    * civil servants
    * journalists
    * politicians

giving you:

* civil servants
* journalists
* politicians

Links are created like so:

    Give your data a home at the [Datahub](http://datahub.io/).

result:

Give your data a home at the [Datahub](http://datahub.io/).

<div class="note">
  <h6>Pro Tip!</h6>
  <p>To get a link to a specific heading on this site, hover over it then click the section icon <code class="icon-section"><span>[section icon]</span></code>. This will show you the URL.</p>
</div>

More Markdown examples can be found [here]({{ "/contribute/markdown-examples/" | prepend: site.baseurl }}), and a more detailed overview [here](http://daringfireball.net/projects/markdown/syntax).

If you are unsure of your markup while editing, you can switch to the preview tab <code class="icon-eye"><span>[eye icon]</span> Preview changes</code> to see how it will be rendered.

<div class="note">
  <h6>Note</h6>
  <p>The Github previews will look stylistically different from the live site. A different font will be used for example.</p>
</div>

Once you are happy with your changes, add a summary of what you've changed in the field below the editable text. Then click '*Propose file change*'.

## 3. Make a pull request

You will now be presented with a 'pull request' form. So far, the changes you have made are to your own copy, or fork of the handbook. A pull request simply sends a request to the authors/maintainers of the live handbook, asking them to include your changes - and put them live! Add any comments you have for the handbook team, then press '*Create pull request*'.

Your work here is done :) If you need to make related changes though, any new commits pushed to your branch will automatically be added to the pull request.
