---
redirect_from: /fr/appendices/index.html
section: guide
lang: fr
title: Formats de fichier.
---

## Une vue d'ensemble des formats de fichiers

### JSON

JSON est un format de fichier trés simple qui est vraiment facilemement lisible par tous les langages de programmation. Cette simplicité signifie qu'il est généralement plus facile pour un oridnateur de traiter ces fichiers comparé a d'autres, telles que XML.

### XML

XML est un format largement utilisé pour l'échange de données, car il conserve la structure des données et la façon dont les fichiers sont construits, et permet aux développeurs d'écrire des parties de la documentation avec les données sans interférer avec leur lecture.

### RDF

Un format recommandé par le W3C est le RDF, car il permet de représenter les données sous une forme qui rend la combinaison de données de différentes sources plus facile. Les données RDF peuvent être stockées, parmi d'autres formats, en XML et JSON. Le format RDF encourage l'utilisation d'URL en tant qu'identifiant, facilitant ainsi l'interconnexion des initiatives d'open data à travers le web. Le format RDF, bien que pas encore alrgement répandu, a été utilisé par certaines initiatives d'open governement, comme les projets espagnols et britanniques d'open data lié ?. L'inventeur du web, Tim Berners-Lee, a récemment proposé un programme de notation des initiatives d'open data en cinq étoiles, qui place les données liées au format RDF comme le but à atteindre.

### Feuilles de calcul

De nombreuses autorités ont laissé des informations dans des feuilles de calcul, par exemple Microsoft Excel. Ces données peuvent souvent être utilisées immédiatement avec des descriptions correctes des différentes colonnes.

Cependant, dans certains cas, des macros et des formules subsistent dans les feuilles de calcul, ce qui peut s'avérer assez compliqué à manipuler. Il est toutefois conseillé de documenter ces calculs dans les feuilles de calcul, pour que cela soit plus facilement compréhensible par les utilisateurs.

### Séparer les fichiers par une virgule

Les fichiers CSV sont un format très utile, car ils sont compacts et permetttent ainsi de transférer de larges ensembles de données en conservant la même structure. Cependant, ce format est tellement fruste que, sans métadonnées, certaines données peuvent être inutiles car il est impossible de deviner le sens des différentes colonnes. C'est pourquoi il est important, lors du recours à des formats séparés par des virgules, que les métadonnées des champs individuels soient renseignées.

Par ailleurs, il est essentiel que la structure du fichier soit conservée, car une seule omission d'un champ peut perturber la lecture de tout le document et des données qui suivent, sans pouvoir corriger l'erreur pusiqu'il ne préjuge aucunement de la façon dont les données suivantes doivent être interprétées.

### Document texte

Les documents classiques dans des formats comme Word, ODF, OOXML, ou PDF peuvent être suffisants pour montrer certains types de données - par exemple, des listes de diffusion relativement stables ou équivalent. Il peut être simple et plus sage de présenter les données sous ces formats, puisque c'est souvent le format natif des données. Cependant, le format texte ne permet pas de conserver une structure de données cohérente et compréhensible, ce qui signifie souvent qu'il est difficile de saisir des données par des moyens automatisés. Veillez à utiliser des modèles comme base des documents pour permettre d'afficher des données de réutilisation, de sorte qu'il soit au moins possible d'extraire des informations de ces documents.

Il peut également soutenir l'utilisation des données ultérieure en utilisant des balises typographiques autant que possible de sorte qu'il devienne plus facile pour une machine de distinguer les rubriques (tout type spécifié) à partir du contenu et ainsi de suite. Généralement, il est recommandé de ne pas exposer les données au format texte, ci celles-ci existent dans un format différent.

### Texte

Les documents texte (.txt) sont très faciles à lire par les ordinateurs. Ils excluent généralement les métadonnées structurelles de l'intérieur du document, ce qui signifie que les développeurs devront créer un analyseur qui peut interpréter chaque document tel qu'il apparaît.

Certains problèmes peuvent être liés à la conversion des fichiers texte entre les systèmes d'exploitation. MS Windows, Mac OS X et d'autres variantes d'Unix ont leur propre façon de dire à l'ordinateur qu'ils ont atteint la fin de la ligne.

### Image numérisée

Probablement la forme la moins appropriée pour la plupart des données, mais TIFF et JPEG-2000 peuvent au moins les marquer avec la documentation de ce qui est dans l'image - jusque pour marquer l'image via le texte intégral du document. Il peut être pertinent d'affichage des données en tant qu'images lorsque les données ne sont pas au format d'origine électronique - un exemple évident est les anciens enregistrements d'église et d'autres documents d'archives - et une image est meilleure que rien.

### Formats propriétaires

Some dedicated systems, etc. have their own data formats that they can save or export data in. It can sometimes be enough to expose data in such a format - especially if it is expected that further use would be in a similar system as that which they come from. Where further information on these proprietary formats can be found should always be indicated, for example by providing a link to the supplier's website. Generally it is recommended to display data in non-proprietary formats where feasible.

### HTML

Nowadays much data is available in HTML format on various sites. This may well be sufficient if the data is very stable and limited in scope. In some cases, it could be preferable to have data in a form easier to download and manipulate, but as it is cheap and easy to refer to a page on a website, it might be a good starting point in the display of data.

Typically, it would be most appropriate to use tables in HTML documents to hold data, and then it is important that the various data fields are displayed and are given IDs which make it easy to find and manipulate data. Yahoo has developed a tool (<http://developer.yahoo.com/yql/>) that can extract structured information from a website, and such tools can do much more with the data if it is carefully tagged.

## Formats de Fichier Ouvert

Même si l'information est fournie sous forme électronique, directement lisible par les machines, et détaillée, il peut y avoir des problèmes en relation avec le format de fichier en lui même.

The formats in which information is published – in other words, the digital base in which the information is stored - can either be "open" or "closed". An open format is one where the specifications for the software are available to anyone, free of charge, so that anyone can use these specifications in their own software without any limitations on re-use imposed by intellectual property rights.

If a file format is "closed", this may be either because the file format is proprietary and the specification is not publicly available, or because the file format is proprietary and even though the specification has been made public, re-use is limited. If information is released in a closed file format, this can cause significant obstacles to reusing the information encoded in it, forcing those who wish to use the information to buy the necessary software.

Le bénéfice des formats de fichier ouverts est qu'ils permettent aux développeurs de produire une multitude de briques logicielles et de services utilisant ces formats. Cela diminue ainsi les obstacles à la réutilisation des informations qu'ils contiennent.

L'utilisation de formats de fichiers propriétaires pour lesquels la spécification n'est pas accessible au public pourrait créer une dépendance vis-à-vis des titulaires de licence de logiciel tiers ou de format de fichier tiers. Dans les scénarios les plus défavorables, cela peut signifier que l'information ne peut être lue qu'en utilisant certains progiciels, qui peuvent être prohibitifs ou qui peuvent devenir obsolètes.

La préférence de la perspective {term: open government data} est donc que les informations soient publiées dans des ** formats de fichiers ouverts qui sont lisibles par machine. **

### Par exemple: les données anglaises relatives au trafic.

Andrew Nicolson est un développeur de logiciels impliqué dans une campagne (en fin de compte réussie) contre la construction d'une nouvelle route, le Westbury Eastern bypass, au Royaume-Uni. Andrew était intéressé par l'accès et l'utilisation des données sur le trafic routier qui servaient à justifier les propositions. Il a réussi à obtenir certaines des données pertinentes via des demandes d'information sur la liberté d'information, mais le gouvernement local a fourni les données dans un format exclusif qui ne peut être lu qu'en utilisant un logiciel produit par une entreprise appelée Saturn, spécialisée dans la modélisation et la prévision du trafic. Il n'y a aucune disposition pour une version "en lecture seule" du logiciel, donc le groupe d'Andrew n'a eu d'autre choix que d'acheter une licence de logiciel, finissant par payer £ 500 (600 €) lors de l'utilisation d'un rabais éducatif. Les progiciels principaux de la liste de prix d'avril 2010 de Saturne commencent à £ 13,000 (plus de 15 000 €), un prix hors de la portée de la plupart des citoyens ordinaires.

Bien qu'aucune loi sur l'accès à l'information n'accorde un droit d'accès à l'information dans des formats ouverts, les initiatives publiques de données gouvernementales commencent à être accompagnées de documents de politique qui stipulent que les informations officielles doivent être mises à disposition dans les formats de fichiers ouverts. La mise en place de l'étalon-or a été l'administration Obama, avec la Directive du gouvernement ouvert publiée en décembre 2009, qui dit:

> * Dans la mesure du possible et soumis à des restrictions valides, les agences doivent publier des informations en ligne dans un format ouvert qui peut être récupéré, téléchargé, indexé et recherché par des applications de recherche Web couramment utilisées. Un format ouvert est indépendant de la plate-forme, lisible par la machine et mis à la disposition du public sans restrictions qui entraverait la réutilisation de cette information. *

## Comment j'utilise un format spécifique ?

Lorsqu'une autorité doit publier de nouvelles données - des données qui n'ont pas été fournies auparavant - vous devriez choisir le format qui offre le meilleur équilibre entre coût et adéquation à des fins spécifiques. Pour chaque format, il y a certaines choses que vous devriez connaître, et cette section a pour but de les expliquer.

Cette section se concentre uniquement sur la meilleure façon de répartir les surfaces coupées afin que les machines puissent y accéder directement. Des conseils et bonnes pratiques sur la façon dont les sites Web et les solutions Web devraient être conçus peuvent être trouvés ailleurs.

### Services web

Pour les données qui changent fréquemment, et où chaque tirage est limité en taille, il est préférable de publier les données via des Web-services. Il existe plusieurs façons de créer un service Web, mais certains des plus utilisés sont SOAP et REST. En général, SOAP sur le service REST et REST sont très faciles à développer et à utiliser, et sont donc des normes largement utilisés.

### Base de données

Comme les services Web, les bases de données fournissent un accès direct aux données de manière dynamique. Les bases de données ont l'avantage de permettre aux utilisateurs d'extraire uniquement ce qui les intéressent.

Certaines préoccupations de sécurité concernant l'extraction de base de données à distance et l'accès à la base de données ne sont utiles que si la structure de la base de données et l'importance des tables et des champs sont bien documentés. Souvent, il est relativement simple et peu coûteux de créer des services Web qui exposent des données à partir d'une base de données, ce qui peut être un moyen facile d'aborder les problèmes de sécurité.
