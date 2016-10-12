---
redirect_from: /rs/appendices/index.html
section: guide
lang: rs
title: Formati fajlova
---

## Pregled formata fajlova

### JSON

JSON je jednostavan format koji je lako čitljiv za bilo koji programski jezik. Njegova jednostavnost omogućava kompjuterima lakšu obradu nego recimo u slučaju XML formata.

### XML

XML je široko korišćen format za razmenu podataka, jer ima mogućnost čuvanja strukture podataka i način na koji su podaci uneti, a programerima omogućava da unose delove dokumentacije unutar podataka bez mešanja, odnosno čitanja istih.

### RDF

Preporučeni W3C format, RDF, omogućava prestavljanje podataka u formi koja olakšava kombinaciju podataka iz više izvora. RDF podaci mogu biti sačuvani u XML-u i JSON-u, između ostalih. RDF podstiče upotrebu URL-ova kao identifikatora, što predstavlja jednostavan način povezivanja inicijativa u vezi sa [otvorenim podacima](/glossary/en/terms/open-data/) , koje već postoje na vebu. RDF još nije široko rasprostranjen, ali predstavlja trend u inicijativama otvorenih vlada, uključujući projekte britanske i španske vlade u vezi sa otvorenim podacima. Pronalazač veba, Tim Berners-Li, nedavno je predložio šemu od [pet zvezdica](http://lab.linkeddata.deri.ie/2010/star-scheme-by-example/) koja uključuje povezane RDF podatke kao cilj kome treba da teže inicijative otvorenih podataka.

### Spreadsheets

Mnoge institucije svoje podatke drže u spreadsheets (podaci organizovani u formi tabele), kao što je Microsoft Excel. Ti podaci često se mogu odmah koristiti uz tačan opis šta različite kolone znače.

Međutim, u nekim slučajevima, oni mogu sadržati šablone i formule, što može biti teško za rukovanje. Stoga se predlaže da ti proračuni budu odvojeni od samih tabela (spreadsheets), jer je korisnicima generalno lakše za čitanje.

### Podaci odvojeni zarezima

CSV ili Comma Separated Files (podaci odvojeni zarezima) mogu biti veoma koristan format zbog svoje kompaktnosti, a to znači i mogućnosti prenosa velikih količina podataka iste sturkture. Međutim, ovaj format je toliko “spartanski” da su podaci često beskorisni bez dokumentacije, pošto je skoro pa nemoguće prepoznati što koji stupac znači. Stoga je za formate koji koriste zareze posebno značajno da sadrže precizna uputstva o značenju pojedinih polja.

Osim toga, nužno je očuvati strukturu datoteke, jer samo jedno pogrešno polje može da poremeti značenja svih preostalih podataka bez stvarne mogućnosti ispravke, jer se ne može utvrditi kako treba interpretirati preostale podatke.

### Tekstualni dokument

Klasični dokumenti u formatima poput Word-a, ODF-a, OOXML-a ili PDF-a mogu biti dovoljni za pokazivanje određenih vrsta podataka - na primer, relativno stabilnih mailing lista ili nečega sličnog tome. Možda je ovaj način prikazivanja podataka jeftin, budući da je reč o formatu u kome su podaci najčešće i nastali. Format ne podržava očuvanje konzistente strukture, što često znači probleme prilikom automatizovanog unosa podataka. Pobrinite se da koristite utvrđene obrasce kao osnovu za dokumenta, koji će prikazati podatke za ponovnu upotrebu, kako bi barem bilo moguće izvući informacije iz dokumenata.

Može podržati i daju upotrebu podataka za korišćenje tipografskih oznaka što je više moguće, tako da mašina lakše raspoznaje zaglavlja (bilo kog tipa) od sadržaja i tako dalje. Generalno se ne predlaže izlaganje u ovom formatu, ukoliko podaci postoje i u nekom drugom formatu.

### Čist tekst

Čisti tekstualni dokumenti (.txt) lako su čitljivi za komjutere. Oni obično ne sadrže strukturalne metapodatke unutar dokumenta, što znači da programeri moraju naprave analizator koji će interpretirati svaki dokument kako se pojavi.

Određeni problemi mogu nastati prebacivanjem čistog teksta između različitih operativnih sistema. MS Windows, Mac OS X i druge Unix varijante imaju svoje posebne načine kojima govore kompjuteru da su stigli do kraja reda.

### Skenirana slika

Verovatno najmanje pogodan oblik za većinu podataka, ali i TIFF i JPEG-2000 mogu barem da dokumentuju šta je na slici - pa sve do toga da mogu kreirati sliku dokumenta sa celim tekstualnim sadržajem dokumenta. To može biti korisno za prikazivanje podataka koji nisu nastali u elektornskoj formi  - očigledan primer su stari crkveni zapisi i drugi arhivski materijal - a bolje je imati sliku nego ništa.

### Zakonom zaštićeni formati

Neki posebni sistemi, na primer, imaju svoje formate u kojima mogu čuvati ili eksportovati podatke. Nekada je dovoljno samo izložiti podatke u takvom formatu, naročito ako je očekivano da će se i ubuduće koristiti u sličnom sistemu iz koga su potekli. Kada god je moguće utvrditi dodatne informacije o ovim zaštićenim formatima to uvek treba naznačiti, na primer linkovima do sajta proizvođača. Generalno se preporučuje prikazivanje podataka u zakonom nezaštićenim formatima kad god je to moguće.

### HTML

Danas je sve više podataka dostupno u HTML formatu na raznim sajtovima. To može biti sasvim dovoljno ako su podaci dosta stabilni i ograničenog obima. U nekim slučajevima, poželjno je imati podatke u obliku jednostavnijem za preuzimanje i modifikovanje, ali kako je ovo jeftin i jednostavan način za upućivanje na druge stranice na sajtu, može biti dobra početna tačka u prikazivanju podataka.

Po pravilu, najbolje bi bilo koristiti tabele u HTML dokumentima za unos podataka, a zatim je bitno da različita polja podataka budu prikazana i identifikovana radi lakog pronalaženja i menjanja podataka. Yahoo je razvio alat (http://developer.yahoo.com/yql/) koji može izvlačiti strukturirane informacije sa nekog sajta, a takvi alati mogu pružiti dosta više ukoliko su podaci pažljivo označeni.

## Fajlovi otvorenih formata

Čak i ako su informacije date u elektronskom i mašinski čitljivom formatu, i ako su detaljne, mogu se pojaviti problemi u vezi sa samim formatom fajla.

Format u kome su objavljene informacije, drugim rečima, digitalna baza u kojoj su informacije sačuvane, može biti "otvorena" ili "zatvorena". Otvoren format je onaj format gde su specifikacije za softver dostupne svima i besplatne, tako da bilo ko može da koristi ove specifikacije u svom programu bez bilo kakvih ograničenja nametnutih zakonima o intelektualnoj svojini.

Ukoliko je format fajla "zatvoren", razlog tome može biti zato što je format zaštićen i specifikacije nisu objavljene ili zato što je format zakonom zaštićen, a iako su specifikacije objavljene, upotreba je ograničena. Ako su informacije objavljene unutar zatvorenog formata, to može izazvati značajne prepreke kod upotrebe tih informacija i primorati one koji žele da koriste te podatke da kupe potrebni softver.

Korist od fajlova otvorenog formata jeste to što programerima dozvoljavaju izradu većeg broja paketa programa i usluga korišćenjem ovih formata. To zatim umanjuje prepreke za ponovno korišćenje informacija koje sadrže.

Korišćenje zaštićenih formata, gde specifikacije nisu javno dostupne može da dovede do zavisnosti od sfotvera trećih lica ili vlasnika licence za format fajla. U najgorem slučaju, to znači da se informacije čitaju samo uz pomoć određenih programskih paketa, koji mogu biti naročito skupi ili koji mogu da zastare.

Stoga je iz perspektive [otvorenih podataka državnih institucija](/glossary/en/terms/open-government/)  poželjno objavljivanje podataka u **otvorenom formatu, koji je mašinski čitljiv.**

### Primer: Podaci o saobraćaju u Ujedinjenom Kraljevstvu

Endrju Nikolson je programer koji je bio deo (uspešne) kampanje protiv izgradnje novog puta u Ujedinjenom Kraljevstvu, Vestburi Istern zaobilaznice. Njega je zanimalo kako da pristupi i koristi podatke o saobraćaju, koji su korišćeni kao artument u prilog predlogu za izgradnju puta. On je uspeo da nabavi deo relevantnih podataka uz pomoeć zahteva za slobodan pristup informacijama, ali su mu lokalne vlasti dale podatke u zaštićenom formatu, čitljivom samo uz pomoć softvera kompanije Saturn, koja je specijalizovana za modele i prognoze u saobraćaju. Kako nije postojala “read only” (samo čitanje) verzija tog softvera, Endrju i njegova grupa nisu imali izbora sem da kupe licencu za softver i plate 500 funti (600 evra) i to sa popustom za obrazovne svrhe. Početna cena osnovnih programskih paketa Saturna u aprilu 2010. godine bila je 13.000 funti (više od 15.000 evra), što je cena koju retko koji običan građanin može da plati.

Iako ne postoji zakon o slobodnom pristupu informacijama od javnog značaja, koji garantuje pravo pristupa informacijama u otvorenom formatu, inicijative otvorenih državnih podataka sve češće sadrže i dokumentaciju koja propisuje da zvanične informacije moraju biti dostupne u otvorenom formatu. Uspostavljanje zlatnog standarda desilo se u vreme Obamine administracije, sa Direktivom otvorene vlade, koja je objavljena u decembru 2009. i koja kaže:

> *Do određene mere i podložne određenim restrikcijama, organizacije bi trebalo da  informacije objavljuju onlajn u otvorenom formatu koji se može pronaći, preuzeti, indeksirati i pretraživati uz pomoć uobičajenih aplikacija za pretragu. Otvoreni format je onaj format koij ne zavisi od platforme, mašinski čitljiv i dostupan javnosti bez ograničenja koja bi sprečavala ponovnu upotrebu tih informacija.*

## Kako koristiti dati format?

Kada vlast treba da predstavi nove podatke, koji još nisu predstavljeni, treba odabrati format koji pruža najbolji odnos troškova i namene. Za svaki format treba imati na umu nekoliko stvari, što će biti objašnjeno u nastavku.

Ovaj deo se pre svega bavi time kako najbolje urediti stranice tako da mašine mogu direktno da im pristupe. Saveti i uputstva o dizajniranju web stranica i izradi web rešenja mogu se naći na drugom mestu.

### Web servisi

Za podatke koji se često menjaju, a preuzimanja su ograničena u veličini, veoma je važno prikazati podatke putem web servisa. Postoji nekoliko načina za izradu web servisa, a među onima koji se najčešće koriste jesu SOAP i REST. Po pravilu, SOAP se češće koristi od REST-a, ali su oba vrlo jednostavna za izradu i korišćenje, pa je to dosta raširen standard.

### Baza podataka

Kao i web servisi, baze podataka dinamički pružaju direktan pristup podacima. Baze podataka imaju tu prednost što korisnicima omogućavaju da izdvoje samo ono što ih zanima.

Postoje određena bezbednosna pitanja u vezi sa izdvajanjem podataka iz baze na daljinu, a pristup bazi podataka koristan je samo onda kada su struktura baze i važnost pojedinih tablica i polja dobro dokumentovane. Često je relativno jednostavno i jeftino napraviti web servis za prikaz podataka iz baze, što može biti dobar odgovor na sigurnosna pitanja.
