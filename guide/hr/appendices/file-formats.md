---
redirect_from: /hr/appendices/index.html
section: guide
lang: hr
title: Formati datoteka
---

## Pregled formata datoteka

### JSON

JSON je jednostavan format koji je lako čitljiv bilo kojem programskom jeziku. Njegova jednostavnost omogućava računalima lakšu obradu nego recimo XML format.

### XML

XML je široko rasprostranjeni format za izmjenu podataka jer čuva strukturu podataka i način na koji su podaci uneseni te omogućava programerima da upišu dijelove dokumentacije unutar podataka bez miješanja, odnosno čitanja istih.

### RDF

Preporučeni W3C format, RDF, omogućava prestavljanje podataka u formi koja olakšava kombinaciju podataka iz više izvora. RDF podaci mogu biti pohranjeni u XML-u i JSON-u, između ostalih. RDF potiče uporabu URL-ova kao identifikatora, što predstavlja jednostavan način povezivanja postojećih inicijativa vezanih uz otvorene podatke na Webu. RDF još nije široko rasprostranjen, no rastući je trend u inicijativama "Otvorenih" vlada, uključujući britanske i španjolske vladine projekte vezane uz otvorene podatke. Izumitelj Weba, Tim Berners-Lee, je nedavno predložio shemu od pet zvjezdica koja uključuje povezane RDF podatke kao cilj kojemu trebaju težiti inicijative otvorenih podataka.

### Proračunske tablice

Mnoge institucije svoje podatke drže u proračunskim tablicama, kao što je Microsoft Excel. Ti podaci često mogu smjesta biti korišteni s točnim opisima stupaca.

No, u nekim slučajevima, proračunske tablice mogu sadržavati makronaredbe i formule, što može otežati rad s njima. Stoga se predlaže da te kalkulacije budu odvojene od proračunskih tablica, što će korisnicima konkretno olakšati čitanje.

### Podaci odvojeni zarezima

CSV ili Comma Separated Files (podaci odvojeni zarezima) mogu biti vrlo koristan format zbog svoje kompaktnosti te mogućnosti prenošenja velikih količina podataka s nepromijenjenom strukturom. Međutim, ovaj format je toliko spartanski da su podaci često beskorisni bez dokumentacije pošto je skoro pa nemoguće prepoznati što koji stupac znači. Stoga je posebno značajno za formate koji koriste zareze da sadrže precizne upute o značenju pojedinih polja.

Osim toga, nužno je očuvati strukturu datoteke, jer samo jedno pogrešno polje može izobličiti značenja svih preostalih podataka bez mogućnosti ispravka, jer se ne može utvrditi kako interpretirati ostale podatke.

### Tekstualni Dokument

Klasični dokumenti u formatima poput Word-a, ODF-a, OOXML-a, ili PDF-a mogu biti dostatni za pokazivanje određenih vrsta podataka, na primjer, relativno stabilnih mailing lista ili nečega ekvivalentno tome. Možda je ovaj način prikazivanja podataka jeftin, budući da se radi o formatima u kojima su podaci često puta i nastali. Format ne podržava održavanje strukture konzistentnom, što često znači probleme prilikom automatiziranog unosa podataka. Pobrinite se koristiti predloške kao baze dokumenata koje će prikazati podatke za upotrebu, kako bi barem bilo moguće izvući informacije iz dokumenata.

Također se može poduprijeti daljnje korištenje podataka za korištenje tipografskih oznaka što je više moguće tako da stroj lakše raspoznaje zaglavlja (bilo kojeg tipa) od sadržaja i slično. Generalno se ne predlaže izlaganje u formatu koji koristi riječi za obradu, ako su podaci zapisani u nekom drugom formatu.

### Čisti tekst

Čisti tekstualni dokumenti (.txt) su jako razumljivi računalima. Oni obično ne sadržavaju strukturalne metapodatke unutar dokumenta, što znači da će razvojni programeri morati napraviti analizator koji će interpretirati svaki dokument koji se pojavi.

Određeni problemi mogu nastati prebacivanjem čistog teksta između različitih operativnih sustava. MS Windows, Mac OS X i ostale Unix varijante imaju svoje zasebne načine kojima govore računalu da su dosegli kraj retka.

### Skenirana slika

Vjerojatno najmanje pogodni oblik za većinu podataka, no i TIFF i JPEG-2000 ih mogu barem označiti interpretacijom što je na slici - pa sve do toga da mogu kreirati sliku s interpretacijama cijelog tekstualnog sadržaja dokumenta. Ovaj pristup može biti koristan u prikazivanju podataka koji nisu stvoreni elektronski. Očiti primjer su zapisi starih crkvi te ostali arhivski materijal - bolje je imati sliku nego ništa.

### Zakonom zaštićeni formati

Neki posebni sustavi, primjerice, imaju vlastite podatkovne formate u koje mogu spremiti ili eksportirati podatke. Nekada može biti dovoljno samo izložiti podatke u takvom formatu, posebice ako ih se misli koristiti u sličnom sustavu kao iz kojeg su i došli. Uvijek treba postojati poveznica preko koje se može naći više informacija o zaštićenim formatima, primjerice poveznica na web stranicu onoga tko je dostavio taj format. U praksi se preporučuje prikazivati podatke u zakonom nezaštićenim formatima kad god je moguće.

### HTML

Danas je sve više podataka dostupno u HTML formatu na raznim stranicama. Ovo može biti sasvim dostatno ako su podaci stabilni i ograničeni u svojoj količini. U nekim slučajevima, podatke se preferira držati u obliku jednostavnijem za preuzimanje i izmjene, no kako je ovo jeftin i jednostavan način za upućivanje na druge stranice, može biti dobra početna točka u prikazivanju podataka.

U pravilu, u HTML dokumentima bi bilo najpogodnije koristiti tablice za unos podataka, a zatim je bitno da razna polja podataka budu prikazana i označena kako bi se podaci mogli s lakoćom naći i uređivati. Yahoo je razvio alat (<http://developer.yahoo.com/yql/>) koji može izvlačiti strukturirane informacije s određene stranice, a takvi alati mogu i puno više ako su podaci precizno označeni.

## Datoteke otvorenih formata

Čak i ako su informacije pružene u elektroničkom formatu čitljive stroju, i to u detalje, mogu se pojaviti problemi vezani uz sam format datoteke.

Formati u kojima su objavljene informacije, drugim riječima, digitalna baza u kojoj su informacije pohranjene, može biti ili "otvorena" ili "zatvorena". Otvoreni formati su oni gdje su specifikacije softvera besplatne i dostupne svima, kako bi svi mogli te specifikacije koristiti u vlastistim softverima bez ograničenja koja se nameću zakonom o intelektualnom pravu vlasništva.

Ako je format datoteke "zatvoren", to može biti zato što je format ili zaštićen sa specifikacijama nedostupnim javnosti ili zato što je format zakonom zaštićen, a iako je dokumentacija javna, upotreba je ograničena. Ako su informacije objavljene unutar zatvorenog formata, to može uzrokovati značajne prepreke u korištenju tih informacija, te natjerati pojedince koji žele koristiti te podatke da kupe potrebni softver.

Dobrobit datoteka otvorenog formata je da dopuštaju programerima izradu većeg broja softverskih paketa i usluga korištenjem tih formata. To za posljedicu ima smanjenje prepreka u korištenju informacija koje sadrže.

Korištenje zaštićenih podatkovnih formata za koje specifikacije nisu javno dostupne može stvoriti ovisnost o vlasnicima licence formata ili softverima trećih strana. U najgorim slučajevima, to može značiti da se informacije mogu vidjeti samo u slučaju kada se koriste određeni softverski paketi, koji mogu biti iznimno skupi ili koji mogu zastarjeti.

Stoga je sklonost otvorenih državnih podataka da se podaci objave u datotekama otvorenih formata koji su čitljivi strojevima.

### Primjer: Podaci o prometu u Ujedinjenom Kraljevstvu

Andrew Nicolson je razvojni programer koji je bio dio (uspješne) kampanje protiv izgradnje Westbury Eastern zaobilaznice, nove ceste u Ujedinjenom Kraljevstvu. Andrewa je zanimalo kako doći do podataka o prometu koji su opravdavali prijedloge te kako ih iskoristiti. Iako je uspio nabaviti nekolicinu relevantnih podataka putem zahtjeva za slobodu informacija, lokalna vlada mu je dala podatke u zaštićenom formatu koji je bio čitljiv jedino korištenjem softvera proizvođača Saturn, specijaliziranog za prometne modele i prognoze. Kako ne postoji "read only" verzija tog softvera, Andrew i njegova grupa nisu imali drugog izbora nego kupiti softverske licence, što ih je nakon primjene popusta u svrhu obrazovanja koštalo 500£ (600€). Osnovne softverske pakete, u travnju 2010., Saturn je naplaćivao 13 000£ (preko 15 000€), što je cijena koju malo koji građanin može platiti.

Iako ne postoji zakon o pristupu informacijama koji daje pravo pristupa informacijama otvorenih formata, inicijative otvorenih državnih podataka sve češće sadrže dokumentaciju koja propisuje da službene informacije moraju biti dane u otvorenim formatima. Određivanje zlatnog standarda je bilo za vrijeme Obamine administracije, s Direktivom Otvorene Vlade izdanom u prosincu 2009., koja kaže:

> *Do određene mjere i podložne valjanim restrikcijama, organizacije bi trebale objaviti informacije online u otvorenom formatu koji se može pronaći, preuzeti, indeksirati i pretražiti obično korištenim aplikacijama za pretraživanje. Otvoreni format je onaj koji je neovisan o platformi, čitljiv strojevima te dostupan javnosti bez restrikcija koje bi sprječavale korištenje tih informacija van originalnog područja.*

## Kako koristim dani format?

Kada vlast mora predstaviti nove podatke koji još nisu bili predstavljeni, treba odabrati format koji pruža najbolji omjer troškova i namjene. Za svaki format treba imati na umu nekoliko stvari, što ćemo objasniti u ovome dijelu.

Ovaj je dio usmjeren na to kako najbolje urediti površine da im strojevi mogu direktno pristupiti. Savjeti i upute o dizajniranju web stranica i izradi web rješenja mogu se naći negdje drugdje.

### Web servisi

Za podatke koji se često mijenjaju te su preuzimanja ograničena u veličini, vrlo je bitno prikazati podatke putem web servisa. Nekoliko je načina kako izraditi web servis, no neki od najčešće korištenih su SOAP i REST. U pravilu, SOAP se češće koristi od REST-a, no oba su vrlo jednostavna za izradu i korištenje, stoga su u širokoj primjeni.

### Baza podataka

Kao i web servisi, baze podataka dinamički pružaju direktan pristup podacima. Prednost baza podataka je ta što korisnicima omogućavaju izvadak konkretno onoga što ih zanima.

Postoje određena sigurnosna pitanja u vezi dopuštanja izvatka baze podataka na daljinu, a pristup bazi podataka je koristan samo onda kada su struktura baze te važnost pojedinih tablica i polja dobro dokumentirane. Odgovor na ova sigurnosna pitanja je često puta izrada jeftinih i jednostavnih web servisa za prikaz podataka iz baza podataka.