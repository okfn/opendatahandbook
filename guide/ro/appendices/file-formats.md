---
section: guide
lang: ro
title: Formate de fișier
---

## O privire de ansamblu asupra formatelor fișierelor

### JSON

JSON este un format de fișier simplu care este foarte ușor de interpretat prin orice limbaj de programare. Simplitatea sa constă în ușurința cu care computerele procesează acest format spre deosebire de altele, cum ar fi XML.

### XML

XML este un format pentru schimbul de date folosit pe scară largă, deoarece oferă oportunități de a păstra structura în date și în modul în care fișierele sunt construite. De asemenea îngăduie dezvoltatorilor să scrie părți din documentație fără a interveni asupra modului de citire.

### RDF

Un format recomandat de W3C ce face posibilă reprezentarea datelor într-o formă ce face ușoară combinarea din mai multe surse. Datele RDF pot fi stocate în XML și JSON, printre altele. RDF încurajează folosirea URL ca identificatori, care oferă un mod convenabil de a interconecta inițiativele de [open data](/glossary/ro/terms/open-data/) de pe web. RDF nu este încă foarte răspândit, dar a devenit o tendință printre inițiativele de guvernare deschisă, inclusiv proiectele de date deschise conectate ale guvernelor Marii Britanii și Spaniei (British and Spanish Government Linked Open Data). Inventatorul Web, Tim Berners-Lee, a propus o schemă cinci-stele ([fivesstar](http://lab.linkeddata.deri.ie/2010/star-scheme-by-example/)) care include date RDF conectate ca scop al căutării de inițiative pentru date deschise.

### Foi de Calcul

Multe autorități au informații rămase în foi de calcul, spre exemplu Microsoft Excel. Aceste date pot fi adeseori utilizate imediat cu descrierea corectă a ceea ce înseamnă fiecare coloană.

Cu toate acestea, în unele cazuri pot exista formule în foile de calcul, care pot fi mai dificile în manevrare. Este recomandată documentarea acestor formule alături de foile de calcul, pentru a fi în general mai accesibile utilizatorilor.

### Fișiere separate prin virgulă

CSV poate fi un format foarte folositor pentru că este compact și deci potrivit pentru transferul de seturi mari de date cu aceeași structură. Totuși, formatul este așa de spartan încât datele sunt deseori nefolosibile fără documentație pentur că este aproape imposibil de ghicit semnificația diferitelor coloane. Este deci important pentru fișierele separate prin virgulă ca documentația pentru câmpurile individuale să fie precise.

Mai mult este esențial ca structura fișierului să fie respectată, pentru că o singură omisiune a unui câmp poate îngreuna citirea datelor rămase în fișier fără vreo posibilitate de a rectifica eroarea, pentru că nu se paote determina cum trebuies interpretate datele rămase.

### Documente text

Documentele în formate clasice precum Word, ODF, OOXML sau PDF pot fi suficiente pentru a expune anumite tipuri de date - spre exemplu, în liste de mesaje sau altele. Ar putea fi mai ușor să fie prezentate în aceste formate, pentru că sunt formatele în care datele au fost introduse ințial. Formatele nu oferă niciun suport pentru a păstra o structură consistentă, ceea ce de multe ori înseamnă că este dificilă introducerea de date în mod automat. Folosirea șabloanelor ca bază pentru documentele care vor expune date pentru refolosire, face posibilă cel puțin extragerea informației din documente.

De asemenea poate sprijini folosirea ulterioară a formatelor tipografice pe cât posibil pentru ca astfel să fie mai ușor distingerea antetelor (de orice tip) de către o mașină din orice conținut. În general este nu recomandată folosirea formatulelor Word, dacă datele există și în alte formate.

### Text simplu

Documentele în format text simplu (.txt) sunt foarte ușor de citit de către calculatoarele. În general acestea exclud metadatele din interiorul documentuli, ceea ce înseamnă că dezvoltatorii vor fi nevoiți să creeze un program pentru analiză sintactică care poate interpreta fiecare document așa cum apare.

Unele probleme pot fi cauzate de schimbul de fișiere text între sistemele de operare. MS Windows, Mac OS X și alte variante Unix au fiecare propriul mod de a spune calculatoarelor că au ajuns la sfârșit de linie.

### Imagini scanate

Probabil cel mai puțin potrivit format pentru cele mai multe date, dar ambele formate TIFF și JPEG-2000 pot cel puțin marca cu documentație ce anume este în imagine - până acolo încât să marcheze imaginea unui document cu tot textul acelui document. Poate fi relevantă expunerea datelor ca imagini pentru acele date care nu au fost create în format electronic, cum ar fi materialele din arhive, iar o imagine este mai bună decât nimic.

### Formatele proprietărești

Unele sisteme dedicate au propriile formate de date în care pot salva sau exporta date. Uneori poate fi suficientă expunerea datelor în astfel de formate - în special dacă se așteaptă ca utilizările ulterioare să aibă loc în sisteme similare celor din care provin. Ar trebui întotdeauna indicat unde anume se pot găsi informații ulterioare despre aceste formate, spre exemplu o legătură către situl web al distribuitorului. In general se recomandă expunerea datelor în formate neproprietărești acolo unde este posibil.

### HTML

În zile noastre majoritatea datelor sunt disponibile în HTML pe diverse situri. Aceasta poate fi suficient dacă datele sunt stabile și limitate în scop. În unele cazuri, este de preferat obținerea într-o formă simplă de descărcat și manevrat, dar este simplu să se ofere o legătură către o pagină web, ar putea fi un bun punct de plecare în expunerea datelor.

În mod normal, ar fi mai potrivită folosirea tabelelor în documente HTML pentru a păstra datele, și apoi este important ca diversele câmpuri de date să fie afișate și să li se dea identificatori care fac ușoară manevrarea datelor. Yahoo a dezvoltat o unealtă (<http://developer.yahoo.com/yql/>) care poate extrage informații structurate dintr-un sit web și astfel de unelte pot face mai multe cu datele care sunt etichetate cu atenție.

## Formate de fișier deshise

Chiar dacă informația este oferită în format electronic, în formate ce pot fi citite automat și în detaliu, pot exista probleme legate de formatul fișierului.

Formatele în care informația este publicată - cu alte cuvinte formatul digital în care informația este stocată - pot fi „deschise” sau „închise”. Un format deschis este unul în care specificațiile pentru programe sunt standardizate, disponibile oricui, astfel încât oricine poate folosi aceste specificații în propriile programe fără alte limitări in refolosire impuse de drepturile de proprietate intelectuală.

Dacă un format de fișier este „închis”, aceasta poate fi pentru că formatul este proprietăresc și specificațiile nu sunt public accesibile sau pentru că formatul este proprietăresc și deși specificațiile au fost făcute publice, reutilizarea este limitată. Dacă informația este eliberată într-un fișier în format închis, aceasta poate produce obstacole semnificative în reutilizarea informației codificată în fișier, forțându-i pe cei care doresc să folosească informația să cumpere programele necesare.

Beneficiul formatelor de fișiere deschise este că ele permit dezvoltatorilor să producă pachete de programe și servicii folosind aceste formate. Aceasta minimizează obstacolele refolosirii informației pe care o conțin.

Folosirea formatelor de fișier proprietăresc pentru care specificațiile nu sunt accesibile pot crea dependențe de terțe programe sau terți deținători de drepturi asupra formatelor de fișiere. În cel mai rau caz, aceasta înseamnă că informația poate fi citită doar folosind anumite pachete de programe, la prețuri neaccesibile, sau care pot deveni depășite.

Din perspectiva {term:open government data} este preferată publicarea informației în **formate de fișier deschise care pot fi citite automat.**

### Exemplu: date despre trafic în Regatul Unit

Andrew Nicolson este un dezvoltator de programe care a fost implicat într-o campanie (în cele din urmă de succes) împotriva construirii unei noi străzi, Westbury Eastern, în Regatul unit. Andrew a fost interesat de accesarea și folosirea datelor despre trafic ce erau folosite pentru a justifica propunerile. A reușit să obțină câteva dintre cele mai relevante date prin cereri bazate pe legislația privind liberul acces la informație, dar autoritățile locale au oferit datele într-un format proprietăresc ce poate fi citit doar folosind programe produse de o companie numită Saturn, specializată în modelarea și anticiparea traficului. Nu era oferită o versiune „” a programului, așa că grupul lui Andrew nu avut nicio alternativă, decât să cumpere o licență pentru programe, plătind în final £500 (€600) utilizând o reducere educatională. Pachete principale de programe de pe lista de prețuri ale comaniei Saturn, din aprilie 2010, pornesc de la £13,000 (peste €15,000), un preț care nu este accesibil cetățenilor obișnuiți.

Deși nicio lege pentru accesul la informație nu dă dreptul la accesul în formate deschise, inițiativele guvernamentale de deschidere a datelor încep să fie însoțite de documente de politici care stipulează că informațiile oficiale trebuie să fie disponibile în formate deschise. Standardul înalt a fost stabilit de administrația Obama, prin Directiva pentru o duvernare deschisă, din decembrie 2009, care spune:

> *Pe cât posibil și în concordanță cu restricțiile valabile, agențiile ar trebui să publice informația pe internet într-un format deschis care poate fi găsit, descărcat, indexat și în care se poate căuta folosind aplicații de căutare web. Un format deschis este unul care este independent de platformă, se poate citi automat și poate fi disponibil publicului fără restricții care ar împiedica refolosirea acelei informații.*

## Cum folosesc un anumit format?

Când o autoritate trebuie să expună noi date - date care nu au fost expuse înainte - ar trebui să alegi formatul care oferă cel mai bun balans între cost și potrivirea cu scopul. Pentru fiecare format există anumite lucruri de care trebuie să fii conștient și această secțiune încearcă să le explice.

Această secțiune se focalizează doar pe modul în care elementele sunt îmbinate astfel încât să poată fi accesate automat. Sfaturi și ghiduri despre cum ar trebui proiectate siturile și serviciile web pot fi găsite în altă parte.

### Servicii Web

Pentru date care se schimbă frecvent și acolo unde fiecare cerere este limitată în dimensiune, este relevantă expunerea datelor prin servicii web. Există mai multe moduri de a crea servicii web, dar unele dintre cele mai folosite sunt SOAP și REST. În general, SOAP mai mult decât REST sau servicii REST, dar sunt foarte ușor de dezvoltat și folosit, așa că sunt standarde folosite pe scară largă.

### Baze de date

La fel ca serviciile web, bazele de date oferă acces direct la date în mod dinamic. Bazele de date au avantajul ca pot îngădui utilizatorilor să pună la un loc doar extragerile care îi interesează.

Există unele îngrijorări cu privire la securitate atunci când se îngăduie acces de la distanță pentru extragerea din bazele de date și accesul la bazele de date este folositor doar dacă structura bazei de date și importanța tabelelor individuale și a câmpurilor sunt bine documentate. Adesea, este relativ simplu și ieftin să se creeze servicii web care expun date dintr-o bază de date, care poate fi o metodă ușoară de a aborda îngrijorările cu privire la securitate.