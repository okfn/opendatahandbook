---
section: guide
lang: hu
title: Fájlformátumok
---

## Áttekintés a fájlformátumokról

### JSON

A JSON egy egyszerű fájlformátum, amely minden programozási nyelv számára rendkívül könnyen olvasható. Az egyszerűségének köszönhetően a számítógép általi feldolgozásuk általában könnyebb, mint más formátumoké, például az XML-é.

### XML

Az XML egy adatcserére szolgáló, széles körben elterjedt formátum, amely képes megőrizni az adatok struktúráját és felépítését. Lehetővé teszi a fejlesztőnek, hogy a dokumentáció egy részét egybeírják az adatokkal, anélkül, hogy ez zavarná azok olvasását.

### RDF

A W3C által ajánlott RDF formátum lehetővé teszi az adatok olyan formában történő tárolását, hogy az könnyen kombinálható legyen más forrásból származó adatokkal.  Az RDF adatokat például XML-ben, JSON-ban és más szerializált formátumokban is tárolhatjuk. A szabvány bátorítja az URL-ek azonosítóként történő használatát, ami kézenfekvő módja annak, hogy közvetlenül összekössük a weben található nyílt adat kezdeményezéseket. Az RDF egyelőre nem terjedt el széles körben, de egyre gyakrabban feltűnik a Nyílt Állam kezdeményezéseknél, például a Brit és Spanyol állami Linked Open Data projektekben. A Web feltalálója, Tim Berners-Lee 2003-ban javaslatot tett egy [öt csillagos](http://lab.linkeddata.deri.ie/2010/star-scheme-by-example/) sémára, amely az összekötött RDF adatokat is tartalmazza, a nyílt adat kezdeményezések által elérendő célok közé.

### Táblázatok

Számos szervezet továbbra is táblázatkezelő alkalmazásokban, például Microsoft Excelben tárol információkat. Ezek az adatok gyakran azonnal felhasználhatóak, ha az egyes oszlopok jelentése megfelelő jelöléssel rendelkezik.

Azonban néhány esetben a táblázatok olyan makrókat és képleteket tartalmaznak, amelyek feldolgozása némileg problémás lehet. Ezért javasolt, hogy a táblázat mellett dokumentáljuk az efféle számításokat, mert az általában könnyebben hozzáférhető a felhasználók számára.

### Vesszővel tagolt értékek (.CSV)

A CSV rendkívül hasznos formátum, mert kompaktsága révén alkalmas nagy, azonos struktúrával rendelkező adathalmazok továbbítására. Azonban ez a formátum olyan spártai, hogy az adatok dokumentáció nélkül gyakran használhatatlanok, mert szinte lehetetlen kitalálni az egyes oszlopok jelentését. Ezért CSV fájlok esetén különösen fontos, hogy a mezők dokumentációja pontos legyen.

Továbbá kulcsfontosságú, hogy tartsuk tiszteletben a fájl struktúráját, mert akár egyetlen mező elhagyása is meggátolhatja a fájl további adatainak kiolvasását a hibajavítás reális esélye nélkül, így a hátralévő adatok értelmezésének megfelelő módja nem megállapítható.

### Szöveges dokumentumok

A hagyományos dokumentumformátumok, például a Word, ODF, OOXML, vagy PDF elégségesek lehetnek bizonyos adatok tárolására - például, viszonylag stabil levelezőlisták vagy ezek ekvivalensei esetén. Költséghatékony megoldást jelenthetnek, hiszen az adatok gyakran ezekben a formátumokban születnek. Ezen formátumok nem képesek megőrizni az adatok szerkezeti felépítését, ami gyakran azzal jár, hogy körülményes velük az automatizált adatrögzítés. Az újrahasznosítható adatokat tartalmazó dokumentumaink alapjául használjunk sablonokat, hogy legalább ezzel lehetővé tegyük az információk kinyerését.

Tovább javíthatunk az adatok felhasználhatóságán azzal, hogy a lehető legtöbb esetben alkalmazunk tipográfiai leírókat, hogy megkönnyítsük a gépek számára az egyes fejezetcímek elkülönítését a tartalomtól. Általánosságban az javasolt, hogy ha az adatok eredetileg más formátumban szerepelnek, akkor ne egy szövegszerkesztő formátumban közöljük azokat.

### Egyszerű szövegfájlok

Az egyszerű szövegfájlok (.txt) feldolgozása rendkívül könnyű a számítógépek számára. Azonban, ezek többnyire nem tartalmaznak strukturális metaadatokat, vagyis a fejlesztőknek kell létrehozniuk olyan alkalmazásokat, amelyek képesek értelmezni ezeket a dokumentumokat.

Problémák adódhatnak az egyszerű szövegfájlok operációs rendszerek közti cseréjéből is. Az MS Windows, Mac OS X és más Unix variánsok másként jelzik a sorok végét.

### Szkennelt képek

Habár az adatok többségéhez ezek a formátumok felelnek meg a legkevésbé, a TIFF és a JPEG-2000 képesek tárolni, hogy az adott kép mit ábrázol - sőt, akár a dokumentum szövegének egészét is tartalmazhatják. Ez olyan adatok esetén lehet releváns, amelyek eredetileg nem elektronikus formátumban jöttek létre - nyilvánvaló példák erre a régi egyházi iratok és más archív anyagok - ahol egy kép is jobb a semminél.

### Jogvédett formátumok

Egyes dedikált rendszerek saját adatformátumban mentik ki vagy exportálják az adatokat. Néhány esetben elegendő ezekben publikálni az adatokat - különösképp, ha azokat várhatóan egy hasonló rendszerben fogják felhasználni. Ha ezekről a formátumokról elérhető további információ, javasolt, hogy ezt mindig jelezzük, például a gyártó weblapjára mutató hivatkozás formájában. Általánosságban javasolt, hogy amikor csak lehet, az adatokat nyílt formátumokban közöljük.

### HTML

Manapság nagy mennyiségű adat található HTML formátumban különböző oldalakon. Ez elegendő lehet, ha az adatok nagyon stabilak és korlátozott méretűek. Egyes esetekben célszerűbb az adatokat könnyen letölthető és manipulálható formátumban kihelyezni, ám mivel olcsó és egyszerű egy weblapra hivatkozni, ez jó kezdőpontot jelenthet az adatok közzétételéhez.

HTML esetén többféle módon is javíthatjuk a gépi értelmezhetőséget: az RDFa a W3C ajánlása, míg a Microdata a Google által is támogatott kicsit egyszerűbb forma. Mindkét formátumhoz vannak eszközök, melyekkel ellenőrizhetjük adataink formátumhelyességét. Az ilyen módon feljavított oldalakból a keresőmotorok több információt tudnak feldolgozni.

## Nyílt fájlformátumok

Ha az információt részletes, elektronikus, gép által olvasható formátumban tároljuk, a formátum önmaga továbbra is okozhat problémákat.

A publikáláshoz használt formátum - más szóval, a digitális keret, amelyben az információt tároljuk
- "nyílt", vagy "zárt" lehet. Nyílt formátumoknak azokat a formátumokat nevezzük, amelyek szoftverspecifikációja mindenki számára ingyen elérhető, így bárki felhasználhatja azokat a saját szoftverében az újrafelhasználásra vonatkozó korlátozások nélkül.

Ha egy fájlformátum "zárt", akkor a formátum jogvédett, és a specifikációja nem publikus. Hasonlóképp előfordulhat, hogy a formátum jogvédett, és habár a specifikációja publikus, az újrafelhasználása korlátozva van. Ha zárt fájlformátumban adunk ki információt, az jelentős akadályokat gördíthet az újrahasznosítás elé, mert rákényszeríti a felhasználókat a szükséges szoftver megvásárlására.

A nyílt fájlformátumok előnye, hogy megengedik a fejlesztőknek az ezeket használó szoftvercsomagok és szolgáltatások létrehozását. Ez minimalizálja a bennük lévő információk újrahasznosítását akadályozó tényezőket.

Ha olyan jogvédett fájlformátumokat használunk, melyek specifikációja nem érhető el nyilvánosan, függeni fogunk a harmadik féltől származó szoftverektől vagy a fájlformátum licenszbirtokosától. A legrosszabb esetben ez azt jelentheti, hogy az információt csak olyan szoftvercsomagokkal lehet beolvasni, melyek megfizethetetlenül drágák, vagy amelyek elavulttá válhatnak.

Ezért, a [nyílt állami adatok](/glossary/hu/terms/open-government/) esetén az információkat célszerű  **nyílt, gép által olvasható fájlformátumban publikálni.**

### Példa: Nagy-Britannia útforgalmi adatai

Andrew Nicolson nagy-britanniai szoftverfejlesztő részt vett egy (végül sikeres) kampányban, ami a Westbury Eastern elkerülőút megépítése ellen indult. Andrew hozzá szeretett volna férni és fel szerette volna használni azokat a forgalmi adatokat, amellyel megindokolták a beruházást. Közérdekű adatigénylés útján megszerezte a releváns adatok egy részét, de a helyi önkormányzat ezt olyan jogvédett formátumban adta oda, amit csak a Saturn forgalommodellező és forgalom-előrejelző cég szoftverével lehet megnyitni. A szoftvernek nincs "csak megtekintésre" szánt verziója, így Andrew csoportjának nem volt más választása, mint vásárolni egy szoftverlicenszet, melyért az oktatási kedvezmény igénybevétele után végül 500£-ot fizettek. 2010 áprilisában a Saturn fő szoftvercsomagjának listaára 13.000£-tól indult, ami az átlagemberek számára elérhetetlen.

Habár egy adatigénylésről szóló törvény sem rendelkezik a nyílt formátumokban történő adatkiadásról, a nyílt állam kezdeményezéseknél kezdenek megjelenni azok a szabályozások, melyek előírják, hogy az állami információknak nyílt formátumokban kell lenniük. Jó példa erre az Obama kormány által 2009 decemberében kiadott "Nyílt állam irányelv":

> *A praktikusságnak és érvényben lévő korlátozásoknak megfelelően az ügynökségeknek az információkat egy olyan nyílt formátumban kell online publikálniuk, amely olvasható, letölthető, indexelhető és kereshető az elterjedt webes keresőalkalmazások számára. A nyílt formátumok azok, amelyek platformfüggetlenek, gép által olvashatók, és az információ újrahasznosítását meggátoló korlátozások nélkül elérhetőek a nagyközönség számára.*

## Hogyan használjunk egy adott formátumot?

Amikor egy szervezetnek új adatokat kell közzétennie – olyat, amit még nem publikáltak korábban – javasolt egy olyan formátumot választania, amely a legjobb egyensúlyt kínálja a ráfordítás és a célszerűség között. Minden formátum esetén célszerű tisztában lennünk bizonyos dolgokkal. A következő szakasz ezek bemutatására törekszik.

Arra fókuszálunk, hogy miképp tehetjük a lehető leghatékonyabbá a gépek által történő közvetlen adatfeldolgozást. Tanácsokat és iránymutatásokat arról, hogy a weblapok és webes megoldások hogyan nézzenek ki, máshol találhatunk.

### Webszolgáltatások

Ahol az adatok gyakran változnak, és a lekérdezések mérete korlátozott, rendkívül fontos, hogy az adatokat webszolgáltatásokon keresztül fedjük fel. A webszolgáltatások létrehozásának számos módja van, a leggyakrabban használt technológiák a SOAP és a REST.

### Adatbázisok

Akárcsak a webszolgáltatások, az adatbázisok is közvetlen, dinamikus hozzáférést nyújtanak az adatokhoz. Az adatbázisok azzal az előnnyel rendelkeznek, hogy a felhasználók összeállíthatják a kivonatot, amelyre szükségük van.

A távoli adatbázis kinyerés engedélyezése esetén felmerülhet néhány biztonsági kockázat, továbbá ez csak akkor hasznos, ha az adatbázis struktúrája és az egyes táblák és mezők szerepe megfelelően dokumentálva van. Általában viszonylag könnyű és olcsó olyan webes szolgáltatásokat létrehozni, amelyek adatbázisokból fednek fel adatokat, így ezek kézenfekvő eszközei lehetnek a biztonsági kockázatok kiküszöbölésének.

A SPARQL egy SQL-hez hasonló, szabványos keresőnyelv, melyen keresztül távoli lekérdezési lehetőséget tudunk biztosítani adatainkhoz. A SPARQL-hez egyre több eszköz áll rendelkezésünkre, egyesek szerint ez a jövő kulcs adatbányász eszköze.
