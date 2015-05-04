---
section: guide
lang: de
title: Datenformate
---

## Eine Übersicht über Datenformate:

### JSON

JSON ist ein einfaches Dateiformat, das von fast jeder Programmiersprache automatisch ausgelesen werden kann.

### XML

XML ist ein weitverbreitetes Format zum Datenaustausch weil es Daten gut Strukturieren kann. Ausserdem können XML Dateien eine gute Dokumentation der Daten enthalten.

### RDF

RDF etabliert sich zunehmend als neues 'Meta-Format' für Datensätze. Unter RDF können verschiedene Datensätze aus XML, JSON und anderen Formaten zusammengeführt werden. RDF arbeitet mit direkten Verlinkungen (Deeplinks), dies erleichtert das auffinden der Daten.

### Tabellen

Viele Institutionen haben ihre Informationen in Tabellen organisiert. Diese Daten können können bei guter Dokumentation direkt weiterverwendet werden.

Manchmal enthalten Tabellen Markos und andere Formeln. Diese sollten am besten direkt im Dokument erläutert und dokumentiert werden.

### Komma-Separierte Werte (CSV)

CSV Dateien können sehr praktisch sein um große Datensätze mit gleicher Struktur zu übermitteln. Das Format ist allerdings so spartanisch, dass immer eine gute Dokumentation benötigt wird um die Inhalte richtig zuordnen zu können.

Daten sollten unverändert herausgegeben werden - insbesondere die Struktur des Dokuments darf nicht verändert werden, da es ansonsten leicht zu verwechslungen kommen kann bzw. der Inhalt nicht mehr verständlich ist.

### Word - Dokumente

Formate die besonders bei entnutzern beliebt sind - Word (.doc) Open Office Dokumente oder PDF sind zum Anzeigen von Informationen geeignet. Diese Dokumente können jedoch nur sehr schwer oder garnicht automatisch ausgelesen werden. Die lesbarkeit kann verbessert werden, wenn Sie Dokumente aus Vorlagen erstellen. Solche Vorlagen geben auf wertvolle Metadaten aus.

Für die Weiterverwendung von Daten kann es sinnvoll sein typographische Markups zu nutzen um die Inhalte 'Maschinenfreundlicher' zu machen. Genrell sind Word-Dokumente nicht so gut geeignet wie andere Formate.

### Roher Text (.txt.)

Reine Textdokumente sind für Computer sehr einfach zu lesen. Sie enthalten jedoch keinerlei beschreibung für strukturierte Daten und sind somit für große Datenbanken ungeeignet.

Der Austausch von .txt Dateien kann Problem verursachen, da MS Windows, Mac OS X und andere Unix Versionen verschiedene Interpretationen dieses Formats haben.

### Gescannte Bilder

Scans sind generell wohl die schlechteste Form öffentliche Informatione weiterzugeben. TIFF und JPEG-2000 können aber immerhin Meta Informationen über den Inhalt des Bildes aufnehmen. In manchen Fällen sind Scans allerdings die einzige Möglichkeit Dokumente zu teilen - z.B. bei alten Handschriften auf Kirchenarchiven.

### Proprietäre Formate:

Manche spezialisierte Anwendungen (wie z.B. SPSS für Statistiken) geben ihre Daten in eigenen Formaten aus. Wenn anzunehmen ist, dass Entwickler mit diesem Format arbeiten können spricht in der Regel nichts dagegen die Daten in diesem Format zu belassen. Die größte Zielgruppe erreicht man allerdings, wenn offene Formate verwendet werden.

### HTML

Mittlerweile werden viele Datensätze im HTML Format ausgegeben. Dies funktioniert, wenn die Datensammlung relativ klein ist und sich nur wenig verändert. Vorteilhaft sind hier vor allem die geringen Kosten.

Daten in HTML Dokumenten sollten in gut ausgezeichneten Tabellen bereitgestellt werden. Yahoo hat ein Tool entwickelt, mit dem strukturierte Daten von Webseiten extrahiert werden können (<http://developer.yahoo.com/yql/>).

## Open Office Formate

Auch wenn Informationen in elektronischer, maschinenlesbarer Form präsentiert werden gibt es noch einige Unterschiede zwischen den Dateiformaten.

Dateiformate können entweder offen oder geschlossen ('proprietär') sein. Bei offenen Formaten sind die spezifikationen der Software für jeden kostenfrei verfügbar, jeder kann Sie also in seiner eigenen Software ohne einschränkungen nutzen.

Bei geschlossenen, proprietären Formaten sind die spezifikationen nicht öffentlich verfügbar oder die Weiternutznug ist eingeschränkt. Wenn Daten nur in einem propritären Format zur Verfügung gestellt werden kann dies erheblich Einschränkungen in bezug auf die Möglichkeit der Weiternutzung haben.

Werden offen Datenformate verwendet gibt es in der Regel eine größere Anzahl verfügbarer Software. Meitens ist diese auch kostengünstiger.

Werden proprietäre Formate verwendet kann das dazu führen, dass große Personenkreise von der Nutzung der Daten ausgeschlossen werden, da sie keinen Zugang zu der teuren Software haben oder weil solche Formate verwaisen können.

Offene Regierungsdaten sollten demnach in offenen Formaten und maschinenlesbar veröffentlicht werden.

### Beispiel: Transportdaten in Großbritannien

Andrew Nicolson war Initiator einer Bürgerinitiative die sich erfolgreich gegen den Neubau einer Straße (den Westbury Eastern bypass in Großbritannien) aussprach. Andrew war an den Daten interessiert, die dem Bau und der Genehmigung der Straße zugrunde lagen und Fragte diese nach Informationsfreiheitsgesetz an. Als er die Daten bekam musste er feststellen, dass diese nur mit einem hochspezialisierten Verkehrsplanungsprogramm ausgelesen werden konnten. Eine Universitätslizenz des Programms kostet ca. 600€, eine normale Version mehr als 15.000€. Die Informationen sind also für die meisten Privatanwender nicht einsehbar, da die Kosten die finanzielle Leistungsfähigkeit bei weitem übersteigen.

Informationsfreiheitsgesetze haben in der Regel keine Klausel, die die herausgabe von Informationen in einem offenen Format vorschreibt, doch mittlerweile gibt es mehr und mehr Policy-Dokumente die Regierungen offene Formate empfehlen. Die Obama Administration setze 2009 mit ihrer Open Government Direktive einen hohen Standard:

> *To the extent practicable and subject to valid restrictions, agencies should publish information online in an open format that can be retrieved, downloaded, indexed, and searched by commonly used web search applications. An open format is one that is platform independent, machine readable, and made available to the public without restrictions that would impede the re-use of that information.*

## Wie nutze ich ein bestimmtes Format?

Wenn eine Verwaltung neue Daten veröffentlicht sollte sie das Format auswählen, dass die beste Kosten-Nutzen Balance bietet. Dieser Abschnitt erklärt die Vor- und Nachteile der verschiedenen Formate.

Dieser Abschnitt behandelt nur die automatisierte Verwendung von Daten durch Programmierschnittstellen und andere Programme. Suchmaschinen und Suchmaschinenoptimierung sind nicht gegenstand des Kapitels.

### Web-Services

Bei Daten die sich häufig ändern sollten zur Bereitstellung Web-Services verwendet werden. Die bekanntesten Beispiele sind SOAP und REST.

### Datenbank

Genau wie Web-Services bieten Datenbanken Nutzern die Möglichkeit nur die für sie relevanten Informationen herauszuziehen.

Es gibt verschiedene Sicherheitsbedenken, die oft gegen einen fernzugriff auf Datenbanken eingewandt werden. Zugriff auf Datenbanken ist auch nur sinnvoll, wenn die Daten gut dokumentiert vorliegen. Oftmals ist es sehr einfach, Web Services aufzubauen die Informationen aus Datenbanken bereitstellen und so den Sicherheitsbedenken zu begegnen.