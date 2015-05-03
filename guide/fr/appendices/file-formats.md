---
title: Formats de fichier.
---

## Une vue d'ensemble des formats de fichiers

### JSON

JSON est un format de fichier trés simple qui est vraiment facile de lire pour tous les langages de programmation. Cette simplicité signifie qu'il est généralement facile pour un ordinateur de traiter comparé a d'autres, telles que XML.

### XML

XML is a widely used format for data exchange because it gives good opportunities to keep the structure in the data and the way files are built on, and allows developers to write parts of the documentation in with the data without interfering with the reading of them.

### RDF

Un format recommandé par le W3C est le RDF, car il permet de représenter les données sous une forme qui rend la combinaison de données de différentes sources plus facile. Les données RDF peuvent être stockées, parmi d'autres formats, en XML et JSON. Le format RDF encourage l'utilisation d'URL en tant qu'identifiant, facilitant ainsi l'interconnexion des initiatives d'open data à travers le web. Le format RDF, bien que pas encore alrgement répandu, a été utilisé par certaines initiatives d'open governement, comme les projets espagnols et britanniques d'open data lié ?. L'inventeur du web, Tim Berners-Lee, a récemment proposé un programme de notation des initiatives d'open data en cinq étoiles, qui place les données liées au format RDF comme le but à atteindre.

### Feuilles de calcul

De nombreuses autorités ont laissé des informations dans la feuille de calcul, par exemple Microsoft Excel. Ces données peuvent souvent être utilisé immédiatement avec des descriptions correctes des différentes colonnes.

However, in some cases there can be macros and formulas in spreadsheets, which may be somewhat more cumbersome to handle. It is therefore advisable to document such calculations next to the spreadsheet, since it is generally more accessible for users to read.

### Séparer les fichiers par une virgule

Les fichiers CSV sont un format très utile, car ils sont compacts et permetttent ainsi de transférer de large ensembles de données en conservant la même structure. Cependant, ce format est tellement fruste que, sans métadonnées, certaines données peuvent être inutiles car il est impossible de deviner le sens des différentes colonnes. C'est pourquoi il est important, lors du recours à des formats séparés par des virgules, que les métadonnées des champs individuels soit renseigné.

Furthermore it is essential that the structure of the file is respected, as a single omission of a field may disturb the reading of all remaining data in the file without any real opportunity to rectify it, because it cannot be determined how the remaining data should be interpreted.

### Document texte

Classic documents in formats like Word, ODF, OOXML, or PDF may be sufficient to show certain kinds of data - for example, relatively stable mailing lists or equivalent. It may be cheap to exhibit in, as often it is the format the data is born in. The format gives no support to keep the structure consistent, which often means that it is difficult to enter data by automated means. Be sure to use templates as the basis of documents that will display data for re-use, so it is at least possible to pull information out of documents.

Il peut également soutenir l'utilisation des données ultérieure en utilisant des balises typographiques autant que possible de sorte qu'il devient plus facile pour une machines de distinguer les rubriques (tout type spécifié) à partir du contenu et ainsi de suite. Généralement, il est recommandé de ne pas exposer les données au format texte, ci celle-ci existent dans une format différent.

### Texte

Plain text documents (.txt) are very easy for computers to read. They generally exclude structural metadata from inside the document however, meaning that developers will need to create a parser that can interpret each document as it appears.

Certains problèmes peuvent être liés à la commutation des fichiers texte entre les systèmes d'exploitation. MS Windows, Mac OS X et d'autres variantes d'Unix ont leur propre façon de dire à l'ordinateur qu'ils ont atteint la fin de la ligne.

### Image numérisée

Probably the least suitable form for most data, but both TIFF and JPEG-2000 can at least mark them with documentation of what is in the picture - right up to mark up an image of a document with full text content of the document. It may be relevant to their displaying data as images whose data are not born electronically - an obvious example is the old church records and other archival material - and a picture is better than nothing.

### Formats propriétaires

Some dedicated systems, etc. have their own data formats that they can save or export data in. It can sometimes be enough to expose data in such a format - especially if it is expected that further use would be in a similar system as that which they come from. Where further information on these proprietary formats can be found should always be indicated, for example by providing a link to the supplier's website. Generally it is recommended to display data in non-proprietary formats where feasible.

### HTML

Nowadays much data is available in HTML format on various sites. This may well be sufficient if the data is very stable and limited in scope. In some cases, it could be preferable to have data in a form easier to download and manipulate, but as it is cheap and easy to refer to a page on a website, it might be a good starting point in the display of data.

Typically, it would be most appropriate to use tables in HTML documents to hold data, and then it is important that the various data fields are displayed and are given IDs which make it easy to find and manipulate data. Yahoo has developed a tool (<http://developer.yahoo.com/yql/>) that can extract structured information from a website, and such tools can do much more with the data if it is carefully tagged.

## Formats de Fichier Ouvert

Même si l'information est fournie sous forme électronique, directement lisible par les machines, et détaillée, il peut y avoir des problèmes en relation avec le format de fichier en lui même.

The formats in which information is published – in other words, the digital base in which the information is stored - can either be “open” or “closed”. An open format is one where the specifications for the software are available to anyone, free of charge, so that anyone can use these specifications in their own software without any limitations on re-use imposed by intellectual property rights.

If a file format is “closed”, this may be either because the file format is proprietary and the specification is not publicly available, or because the file format is proprietary and even though the specification has been made public, re-use is limited. If information is released in a closed file format, this can cause significant obstacles to reusing the information encoded in it, forcing those who wish to use the information to buy the necessary software.

Le bénéfice des formats de fichier ouverts est qu'ils permettent aux développeurs de produire une multitude de briques logicielles et de services utilisant ces formats. Cela diminue ainsi les obstacles à la réutilisation des informations qu'ils contiennent.

Using proprietary file formats for which the specification is not publicly available can create dependence on third-party software or file format license holders. In worst-case scenarios, this can mean that information can only be read using certain software packages, which can be prohibitively expensive, or which may become obsolete.

The preference from the {term:open government data} perspective therefore is that information be released in **open file formats which are machine-readable.**

### Par exemple: les données anglaises relatives au trafic.

Andrew Nicolson is a software developer who was involved in an (ultimately successful) campaign against the construction of a new road, the Westbury Eastern bypass, in the UK. Andrew was interested in accessing and using the road traffic data that was being used to justify the proposals. He managed to obtain some of the relevant data via freedom of information requests, but the local government provided the data in a proprietary format which can only be read using software produced by a company called Saturn, who specialise in traffic modelling and forecasting. There is no provision for a “read only” version of the software, so Andrew's group had no choice but to purchase a software license, eventually paying £500 (€600) when making use of an educational discount. The main software packages on the April 2010 price list from Saturn start at £13,000 (over €15,000), a price which is beyond the reach of most ordinary citizens.

Although no access to information law gives a right of access to information in open formats, open government data initiatives are starting to be accompanied by policy documents which stipulate that official information must be made available in open file formats. Setting the gold standard has been the Obama Administration, with the Open Government Directive issued in December 2009, which says:

> *To the extent practicable and subject to valid restrictions, agencies should publish information online in an open format that can be retrieved, downloaded, indexed, and searched by commonly used web search applications. An open format is one that is platform independent, machine readable, and made available to the public without restrictions that would impede the re-use of that information.*

## Comment j'utilise un format spécifique ?

When an authority must exhibit new data – data that has not been exhibited before – you should choose the format that provides the best balance between cost and suitability for purpose. For each format there are some things you should be aware of, and this section aims to explain them.

This section focuses only on how the cut surfaces are best arranged so that machines can access them directly. Advice and guidance about how web sites and web solutions should be designed can be found elsewhere.

### Services web

For data that changes frequently, and where each pull is limited in size, it is very relevant to expose data through web services. There are several ways to create a web service, but some of the most used is SOAP and REST. Generally, SOAP over REST, REST services, but are very easy to develop and use, so it is a widely used standard.

### Base de données

Like web services, databases provide direct access to data dynamically. Base de donnéess have the advantage that they can allow users to put together just the extraction that they are interested in.

There are some security concerns about allowing remote database extraction and database access is only useful if the structure of the database and the importance of individual tables and fields are well documented. Often, it is relatively simple and inexpensive to create web services that expose data from a database, which can be an easy way to address safety concerns.