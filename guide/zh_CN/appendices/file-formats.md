---
title: 文件格式
---

## 文件格式概览

### JSON

JSON is a simple file format that is very easy for any programming language to read. Its simplicity means that it is generally easier for computers to process than others, such as XML.

### XML

XML is a widely used format for data exchange because it gives good opportunities to keep the structure in the data and the way files are built on, and allows developers to write parts of the documentation in with the data without interfering with the reading of them.

### RDF

A W3C-recommended format called RDF makes it possible to represent data in a form that makes it easier to combine data from multiple sources. RDF data can be stored in XML and JSON, among other serializations. RDF encourages the use of URLs as identifiers, which provides a convenient way to directly interconnect existing {term:open data} initiatives on the Web. RDF is still not widespread, but it has been a trend among Open Government initiatives, including the British and Spanish Government Linked Open Data projects. The inventor of the Web, Tim Berners-Lee, has recently proposed a [fivesstar](http://lab.linkeddata.deri.ie/2010/star-scheme-by-example/) scheme that includes linked RDF data as a goal to be sought for open data initiatives.

### 表单 (Spreadsheets)

很多官方信息都被留存在了电子表单软件比如 Microsoft Excel。这些数据可以立刻被使用只要每一列的数据都有清楚的描述。

However, in some cases there can be macros and formulas in spreadsheets, which may be somewhat more cumbersome to handle. It is therefore advisable to document such calculations next to the spreadsheet, since it is generally more accessible for users to read.

### 逗号分割的文件

CSV文件是很有用的因为它是精简的文件因此很适合用于传输大量相同结构的数据。然而，当缺乏说明文档时这种文件格式常常很难使用因为你很难猜出每一列到底代表这什么意思。因此逗号分号的文件需要清楚正确地记录下每一个数据域的意义。

Furthermore it is essential that the structure of the file is respected, as a single omission of a field may disturb the reading of all remaining data in the file without any real opportunity to rectify it, because it cannot be determined how the remaining data should be interpreted.

### 文本文件

常用的文件格式比如Word，ODF，OOXML，或是PDF，对于用来显示诸如邮件列别之类的数据来说足以胜任了。但这些格式无法保持数据结构的一致性，也就意味着自动从中获取数据是很艰难的。因此建议如果要使用这些文件格式，那么就应该使用模板来创建数据，从而使得自动从文件中抓取数据成为可能。

It can also support the further use of data to use typography markup as much as possible so that it becomes easier for a machine to distinguish headings (any type specified) from the content and so on. Generally it is recommended not to exhibit in word processing format, if data exists in a different format.

### 纯文本

Plain text documents (.txt) are very easy for computers to read. They generally exclude structural metadata from inside the document however, meaning that developers will need to create a parser that can interpret each document as it appears.

在不同操作系统间传输纯文本文件会造成一些问题。MS Windows，Mac OS X 和其他类 UNIX 系统都有自己不同的换行符。

### 扫描的图片

Probably the least suitable form for most data, but both TIFF and JPEG-2000 can at least mark them with documentation of what is in the picture - right up to mark up an image of a document with full text content of the document. It may be relevant to their displaying data as images whose data are not born electronically - an obvious example is the old church records and other archival material - and a picture is better than nothing.

### 私有文件格式

Some dedicated systems, etc. have their own data formats that they can save or export data in. It can sometimes be enough to expose data in such a format - especially if it is expected that further use would be in a similar system as that which they come from. Where further information on these proprietary formats can be found should always be indicated, for example by providing a link to the supplier's website. Generally it is recommended to display data in non-proprietary formats where feasible.

### HTML

Nowadays much data is available in HTML format on various sites. This may well be sufficient if the data is very stable and limited in scope. In some cases, it could be preferable to have data in a form easier to download and manipulate, but as it is cheap and easy to refer to a page on a website, it might be a good starting point in the display of data.

Typically, it would be most appropriate to use tables in HTML documents to hold data, and then it is important that the various data fields are displayed and are given IDs which make it easy to find and manipulate data. Yahoo has developed a tool (<http://developer.yahoo.com/yql/>) that can extract structured information from a website, and such tools can do much more with the data if it is carefully tagged.

## 开放数据格式

即使信息被提供在电子的，可机器阅读的格式并且内容详尽，文件格式本身仍可能造成一定的问题。

信息公开的格式，或者说信息存储的方式，可以是「开放」或者「封闭」的。开放的格式指的是其标准可被任何人免费获取，因此任何人可以创建自己的软件来实现这个格式而不需要受到知识产权的限制。

如果一个文件的格式被认为是「封闭」的，那么要么是因为这个文件格式是私有的并且其标准无法公开访问，或者是因为这个文件格式的标准虽然可公开访问但是它本身仍旧私有而且使用受限。如果信息被公开在这种封闭的格式下，那么重利用这些信息将会被大大限制并且破事人们不得不去够买相应的软件来得以使用这些信息。

开放性的文件格式的好处在于它允许开发者基于它开发不同的软件和服务。进而这可以降低重用数据的壁垒。

Using proprietary file formats for which the specification is not publicly available can create dependence on third-party software or file format license holders. In worst-case scenarios, this can mean that information can only be read using certain software packages, which can be prohibitively expensive, or which may become obsolete.

The preference from the {term:open government data} perspective therefore is that information be released in **open file formats which are machine-readable.**

### 例子：英国交通数据

Andrew Nicolson is a software developer who was involved in an (ultimately successful) campaign against the construction of a new road, the Westbury Eastern bypass, in the UK. Andrew was interested in accessing and using the road traffic data that was being used to justify the proposals. He managed to obtain some of the relevant data via freedom of information requests, but the local government provided the data in a proprietary format which can only be read using software produced by a company called Saturn, who specialise in traffic modelling and forecasting. There is no provision for a “read only” version of the software, so Andrew's group had no choice but to purchase a software license, eventually paying £500 (€600) when making use of an educational discount. The main software packages on the April 2010 price list from Saturn start at £13,000 (over €15,000), a price which is beyond the reach of most ordinary citizens.

Although no access to information law gives a right of access to information in open formats, open government data initiatives are starting to be accompanied by policy documents which stipulate that official information must be made available in open file formats. Setting the gold standard has been the Obama Administration, with the Open Government Directive issued in December 2009, which says:

> *To the extent practicable and subject to valid restrictions, agencies should publish information online in an open format that can be retrieved, downloaded, indexed, and searched by commonly used web search applications. An open format is one that is platform independent, machine readable, and made available to the public without restrictions that would impede the re-use of that information.*

## 我如何使用一个给定的文件格式？

当官方必须要展示新数据的时候，你应当选取一种文件格式来平衡成本需求和可持续使用的需求。对于每一种你应该知道的文件格式，我们这一节中都会给出详细的解释。

这一节将侧重在如何安排cut surfaces来使机器直接访问。关于网站和网络服务的建议和指导可以到其他地方获得。

### 网络服务

对于经常有大规模变动的数据，通过网络服务提供数据是较好的方式。网络服务可以通过很多方式创建，但最常用的是 REST 和 SOAP。一般来说，相比 SOAP，REST 服务更容易开发和使用因此它是较常用的网络服务标准。

### 数据库

和网络服务一样，数据库也提供数据的动态访问。数据库的优势在于它们能允许用户只关注它们感兴趣的数据和数据关系。

允许远程数据抓取有这一定的安全隐患。数据访问仅在其结构和重要的数据表格和数据域都已经配备了完好的说明文档才会有用。通常而言，建设网络服务来提供数据库数据是较为安全，简单且成本低廉的方式。