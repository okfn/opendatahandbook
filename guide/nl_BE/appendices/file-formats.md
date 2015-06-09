---
redirect_from: /nl_BE/appendices/index.html
section: guide
lang: nl_BE
title: Bestandsformaten
---

## Een overzicht van bestandsformaten

### JSON

JSON is een eenvoudig bestandsformat dat gemakkelijk is voor elke programmeertaal om te lezen. Deze eenvoud betekent dat het normaal gesproken makkelijker is te verwerken voor computers dan andere formats, zoals XML.

### XML

XML is een veelgebruikt format voor datauitwisseling omdat het goede mogelijkheden biedt om de structuur in de data te behouden, en de manier waarop bestanden worden geconstrueerd, en het staat gebruikers toe om delen van de documentatie te voorzien van nieuwe stukken zonder hierbij te beïnvloeden hoe de data wordt gelezen.

### RDF

Een W3C-aanbevolen format genaamd RDF maakt het mogelijk om data weer te geven op een manier die het makkelijker maakt om data van meerdere bronnen te combineren. RDF data kan worden opgeslagen in XML en JSON, naast andere serialisaties. RDF moedigt het gebruik van URLs als indentificatoren aan, wat een handige manier biedt om direct ineen te grijpen met bestaande :term: \` open data \` initiatieven op het web. RDF is nog steeds niet veelgebruikt, maar het is een trend geweest onder Open Overheid-initiatieven, waaronder het Britse en Spaanse Government Linked Open Data projecten. De uitvinden van het web, Tim Berners-Lee, heeft recentelijk een vijf-sterren\_ plan opgezet waarin gelinkte RDF data als een doel wordt gezocht voor open data initiatieven.

### Spreadsheets

Veel autoriteiten hebben informatie over in spreadsheets, bijvoorbeeld Microsoft Excel. Deze gegevens kunnen vaak direct worden gebruikt als er op een juiste manier wordt beschreven wat de verschillende kolommen betekenen.

Echter, in sommige gevallen kunnen er macro's en formules in spreadsheets staan, die wat lastig te hanteren kunnen zijn. Het is daarom aan te raden zulke berekeningen naast de spreadsheet te documenteren, omdat dit normaal gesproken toegankelijker is voor gebruikers om te lezen.

### Comma Separated Files

CSV-bestanden kunnen een zeer nuttig format zijn omdat het compact is, en dus geschikt is om grote datasets met eenzelfde structuur over te dragen. Het format is echter zo ruw dat gegevens vaak waardeloos zijn zonder de juiste documentatie, omdat het bijna onmogelijk kan zijn om het belang van de verschillende kolommen te raden. Het is daarom met name voor de comma-separated formats van belang dat de documentatie van de individuele velden correct is.

Tevens is het essentieel dat de structuur van het bestand wordt gerespecteerd, omdat een enkele weglating van een veld het lezen van alle overige data kan verstoren zonder een echte mogelijkheid dit te herstellen, omdat er niet bepaald kan worden hoe de overige data moet worden geïnterpreteerd.

### Tekstdocument

Klassieke documenten in formats als Word, ODF, OOXML of PDF kunnen genoeg zijn om bepaalde vormen van data weer te geven - bijvoorbeeld, relatief stabiele maillijsten of iets dergelijks. Het kan goedkoop zijn om in te publiceren, omdat het vaak het format is waar de data in is ontstaan. Het format geeft geen ondersteuning om de structuur consistent te houden, wat vaak betekent dat het moeilijk is om data geautomatiseerd in te voeren. Zorg er voor dat u templates gebruikt als basis voor documenten die data weergeven voor hergebruik, zodat het in elk geval mogelijk is om informatie ui de documenten te halen.

Het kan ook het verdere gebruik van data ondersteunen om typografie-informatie zo veel mogelijk te gebruiken zodat het makkelijker is voor machines om onderscheid te maken tussen titelkoppen (van elk soort) en tekst et cetera. Het wordt over het algemeen aangeraden om geen gebruik te maken van een tekstverwerkingsformat als data in een ander format beschikbaar is.

### Plain Text

Plain text documenten (.txt) zijn erg makkelijk voor computers om te lezen. Ze hebben echter vaak geen structurele metadata van binnenin het document, wat betekent dat ontwikkelaars een zgh. 'parser'-programma moeten maken die elk document kan interpreteren zoals het eruit ziet.

Er kunnen problemen ontstaan bij het uitwisselen van niet-versleutelde tekstbestanden tussen bestuursystemen. MS Windows, Mac OS X en andere Unix varianten hebben hun eigen manier om de computer te laten weten dat het einde van een regel bereikt is.

### Gescande afbeelding

Waarschijnlijk de minst geschikte vorm voor de meeste data, maar zowel TIFF als JPEG-2000 kunnen tenminste aangeven met documentatie wat er in de afbeelding staat - ze kunnen zelfs een afbeelding uit een document opslaan met de gehele inhoud van het document. Het kan nuttig zijn om hun informatie weer te geven op deze manier, als gegevens niet oorspronkelijk elektronisch zijn - een voor de hand liggend voorbeeld is oude administratie van de kerk en andere archiefmaterialen - en een afbeelding is beter dan niets.

### Proprietaire formaten

Sommige toegewijde systemen, etc. hebben hun eigen dataformats die zij op kunnen slaan of waarin zij data kunnen exporteren. Het kan soms genoeg zijn om data beschikbaar te maken in zo'n format - vooral als men verwacht dat verder gebruik in een soortgelijk systeem als waar het vandaan komt plaats zal vinden. Waar meer informatie over deze bedrijfseigen formats te vinden is moet altijd worden gegeven, bijvoorbeeld door een link te verschaffen naar de website van de leverancier. Het wordt over het algemeen aangeraden om data in niet-bedrijfseigen formats weer te geven, waar mogelijk.

### HTML

Tegenwoordig is veel data beschikbaar in HTML format op verschillende websites. Dit kan zeker genoeg zijn als de data erg stabiel is en een klein bereik heeft. In sommige gevallen kan het gunstiger zijn om data in een vorm te hebben die makkelijk te downloaden en te manipuleren is, maar omdat het goedkoop en makkelijk is om te refereren naar een pagina op een website, kan het een goed beginpunt zijn voor het weergeven van data.

Het zou het meest geschikt zijn om tabellen te gebruiken in HTML documenten om data vast te houden, en dan is het erg belangrijk dat de verscheidene datavelden weer worden gegeven en IDs meekrijgen om het makkelijk te maken de data te vinden en te manipuleren. Yahoo heeft een tool ontwikkeld (<http://developer.yahoo.com/yql/>) die gestructureerde informatie van een website kan halen, en zulke tools kunnen veel meer met data doen als deze goed is gelabeld.

## Open Bestandsformaten

Zelfs als informatie voor handen is in een elektronisch, machine-leesbaar format, en gedetailleerd, kunnen er problemen zijn met het relateren aan het format van het bestand zelf.

De formats waarin informatie is gepubliceerd - in andere woorden, het digitale fundament waar de informatie in opgeslagen is - kan ofwel "open" ofwel "gesloten" zijn. Een open format is een format waarvoor de specificaties voor de software voor iedereen toegankelijk zijn en gratis is, zodat iedereen deze specificaties in hun eigen software kan gebruiken zonder enige beperkingen met betrekking tot het hergebruiken opgelegd door intellectuele eigendomsrechten.

Als een bestandsformat "gesloten" is, kan dit of zijn omdat het bestandsformat een bedrijfsmerk is en de specificaties niet openbaar beschikbaar zijn, of omdat het bestandsformat een bedrijfsmerk is en, ook al zijn de specificaties openbaar gemaakt, hergebruik beperkt is. Als informatie wordt uitgegeven in een gesloten bestandsformat kan dit serieuze obstakels veroorzaken bij het hergebruiken van de informatie die daarin gecodeerd staat, wat degene die de informatie wil gebruiken dwingt om de noodzakelijke software aan te schaffen.

Het voordeel van open file formats is dat deze ontwikkelaars toestaan om meerdere softwarepakketten en services te produceren bij het werken met deze formats. Dit minimaliseert het aantal obstakels bij het willen hergebruiken van de informatie in deze bestanden.

Het gebruik van bedrijfseigen bestandsformaten waarvan de specificaties niet openbaar verkrijgbaar zijn kan een afhankelijkheid creëren van software van derden, of licentiehouders van een bestandsformaat. In het ergste geval kan dit betekenen dat informatie alleen kan worden gelezen met behulp van bepaalde softwarepakketten, die onbetaalbaar duur kunnen zijn, of die kunnen verouderen.

De voorkeur van het :term: \` open overheidsdata \` -perspectief is daarom dat informatie uitgegeven moet worden in **open file formats die machine-leesbaar zijn.**

### Voorbeeld: Verenigd Koninkrijk verkeersgegevens

Andrew Nicolson is een softwareontwikkelaar die betrokken was bij een (uiteindelijk succesvolle) campagne tegen de verwezenlijking van een nieuwe weg, de Westbury Eastern bypass, in Groot-Brittanië. Andrew was geïnteresseerd in toegang krijgen tot en het gebruiken van de wegverkeersdata die werd gebruikt om de voorstellen te verantwoorden. Hij kon een deel van de relevante data bemachtigen via de vrijheid van het vragen om informatie, maar de locale overheid leverde deze data aan in een bedrijfseigen format die alleen gelezen kan worden door de software te gebruiken die wordt gemaakt door een bedrijf genaamd Saturn, dat zich specialiseert in verkeersmodellering en -voorspelling. Er is geen voorziening van een 'read only' versie van de software, dus had Andrew's team geen andere keuze dan de softwarelicentie te kopen, waar uiteindelijk £500 (€600) voor moest worden betaald, waarbij van een onderwijskorting gebruik werd gemaakt. De voornaamste softwarepakketten op de prijslijst van Saturn, in april 2010, beginnen bij £13,000 (meer dan €15,000); een prijs die ver buiten het bereik van de meeste gewone burgers ligt.

Hoewel geen enkele informatietoegankelijkheidswet het recht geeft om informatie te raadplegen in open formats, beginnen initiatieven van open overheidsdata begeleid te worden met beleidsdocumenten die stipuleren dat officiële informatie beschikbaar moet worden gemaakt in open file formats. De Obama Administration heeft hierbij de gouden standaard gezet, met het Open Government Directive, uitgegeven in december 2009, wat zegt:

> *Tot op een hoogte die praktisch haalbaar is en onderworpen is aan gegronde beperkingen, moeten instanties informatie die online wordt gepubliceerd in een open format aanbieden dat kan worden verkegen, gedownload en geindexeerd, en gezocht kan worden door het raadplegen van gangbare manieren van zoeken op het web. Een open format is een format dat platformonafhankelijk en machine-leesbaar is, en dat beschikbaar is voor het publiek zonder restricties die het hergebruiken van die informatie hinderen.*

## Hoe gebruik ik een bepaald format?

Wanneer een autoriteit nieuwe data moet vertonen - data die nog nooit eerder vertoond is - moet het formaat worden gekozen dat de beste balans tussen kosten en beschikbaarheid voor het doel biedt. Voor elk format zijn er enkele dingen waarvan u op de hoogte moet zijn, en deze sectie heeft als doel deze uit te leggen.

Deze sectie focust alleen op hoe de aparte onderdelen het best gesorteerd kunnen worden zodat machines direct toegang kunnen krijgen. Advies en counseling over hoe websites en websolutions ontwikkeld moeten worden kan elders worden gevonden.

### Web services

Voor data die vaak verandert, en waar elke download beperkt is in grootte, is het erg relevant om deze data ten toon te stellen via webservices. Er zijn een aantal manieren om een webservice te creëren, maar twee van de meest gebruikte services zijn SOAP en REST. Over het algemeen, SOAP meer dan REST, REST services, maar zijn erg makkelijk te ontwikkelen en te gebruiken, dus het is een veelgebruikte standaard.

### Database

Net als webservices voorzien databases directe toegang tot data op een dynamische manier. Databases hebben het voordeel dat ze gebruikers kunnen toestaan om alleen de delen samen te voegen en te downloaden waarin zij geïnteresseerd zijn.

Er zijn enkele bezorgdheden met betrekking tot de veiligheid over het toestaan van extractie van databases op afstand, en toegang tot een database is alleen nuttig als de structuur van de database en het belang van individuele tabellen en velden goed gedocumenteerd is. Vaak is het relatief eenvoudig en goedkoop om webservices te creëren die data uit een database beschikbaar maken, wat een simpele manier kan zijn om om te gaan met de zorgen over de veiligheid.