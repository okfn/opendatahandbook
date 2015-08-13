---
section: contribute
title: Contributing to the handbook
authors:
 - Sam Smith
lang: en
---

<p class="lead">Thank you for your interest in helping to build The Open Data Handbook. We warmly welcome comments, corrections and additions, as well as suggestions for additional sections and areas to examine. For general discussion about the Handbook, please <a href="{{ site.contact }}" rel="external">get in touch</a>. To jump in with improvements and additions, read on.</p>

## How this site works

In order to contribute, you need a little insight of how things work under the hood. We're not going to go into too much detail here, but there are three components you need some understanding of.

<div class="contributing">
  <ul class="tools">
    <li class="github"><a href="#Github">Github</a></li>
    <li class="jekyll"><a href="#Jekyll">Jekyll</a></li>
    <li class="markdown"><a href="#Markdown">Markdown</a></li>
  </ul>
</div>

<h3 id="Github">Github</h3>

#### What is it?

GitHub is a web-based repository hosting service, which amongst other things offers revision control and source code management via a web-based graphical interface.

#### Why should I care?

Any changes you wish to make, whether they be edits to an existing page, or creating a new one, will most likely be done via the Github website (it is also possible to download and edit the files on your local machine, instructions for this method will be added in the future). All the files for this site can be browsed and edited the Github website. You will need to [sign up](https://github.com/) for a (free) Github account. For full instructions, see [Editing a page](editing/).

<h3 id="Jekyll">Jekyll</h3>

#### What is it?

Jekyll is a static site generator, which allows us to host websites based on our GitHub repositories. Jekyll takes the content, renders Markdown, and produces a complete, static website ready to be viewed on the web.

#### Why should I care?

All you really need to know about Jekyll is the method it uses to include metadata (ie. page title). Each page needs to start with a section it calls Front Matter, containing the page title. An example is provided in the [Adding a page](adding/) section.

<h3 id="Markdown">Markdown</h3>

#### What is it?

Markdown is a markup language with plain text formatting, designed so that it can be converted to HTML. Markdown can be used to create rich text using a plain text editor.

#### Why should I care?

Markdown is your key to formatting the text you provide for this site. By learning a few intuitive rules you'll be able to ensure your text is formatted with headings, list, quotes etc, without writing any HTML. For examples, head to the [Markdown]({{ "/contribute/markdown-examples/" | prepend: site.baseurl }}) section.
