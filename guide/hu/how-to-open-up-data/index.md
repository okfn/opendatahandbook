---
section: guide
lang: hu
title: Hogyan tegyük nyílttá az adatokat?
---

Ez a szakasz alkotja a kézikönyv magját. Konkrét, részletes tanácsokkal szolgál arról, hogy az adattulajdonosok miként tehetik nyílttá az adataikat. Végigvesszük az alapokat, de kitérünk a buktatókra is. Végül, beszélünk az esetlegesen fellépő érdekesebb problémákról.

Az adatok nyílttá tevéséhez három alapszabályt javaslunk:

-   **Egyszerűség**. Kezdjük kicsi, egyszerű és gyors projektekkel. Nincs előírva, hogy az összes adathalmazt azonnal nyílttá kell tennünk. Tökéletes az is, ha egyetlen adathalmazzal, vagy egy nagyobb adathalmaz egyetlen részével kezdünk – természetesen, minél több adathalmazt tudunk nyílttá tenni, annál jobb.

    Tartsuk észben, hogy ez az innovációról szól. A lehető leggyorsabban haladni jó, mert így lendületet kaphatunk és gyakorlati tapasztalatokat szerzünk – az innováció azonos mértékben szól a kudarcról és a sikerről: nem minden adathalmaz fog hasznossá válni.

-   **Kapcsolat a felhasználókkal**. Lépjünk kapcsolatba az adataink potenciális felhasználóival és újrafelhasználóival, amilyen hamar és amilyen sűrűn csak lehet, legyenek akár civilek, üzletemberek vagy fejlesztők. Ezzel biztosíthatjuk, hogy a szolgáltatásunk következő iterációja a lehető legrelevánsabbá váljon.

    Fontos észben tartani, hogy az adatok nagy része nem közvetlenül, hanem "info-közvetítőkön" keresztül fog a felhasználókhoz jutni. Ők azok, akik átalakítják, vagy más adatokkal vegyítik az adatokat azok prezentálása előtt. Például, a legtöbbünknek nincs szüksége egy nagy, GPS koordinátákat tartalmazó adatbázisra, sokkal inkább a térképeket preferáljuk. Ezért, elsőként az "info-közvetítőkkel" lépjünk kapcsolatba, hiszen ők fogják újrahasznosítani az információkat.

-   **Tisztázzuk a gyakori aggodalmakat és félreértéseket**. . Ez különösen fontos, ha egy olyan nagy szervezettel vagy szervezetnek dolgozunk, mint az állam. Az adatok nyílttá tevésekor számos kérdéssel és aggodalommal fogunk találkozni. Fontos, hogy (a) azonosítsuk a legfontosabbakat és (b) a lehető leghamarabb tisztázzuk őket.

Az adatok nyílttá tevése négy fő lépésből áll, melyek mindegyikével a következő részben fogunk részletesen foglalkozni. Sorrendjük csak megközelítőleges - számos lépés egyszerre is elvégezhető.

1.  **Válasszunk adathalmaz(oka)t.** Válasszuk ki azokat az adathalmaz(oka)t, amelyeket nyílttá szeretnénk tenni. Tartsuk szem előtt, hogy amennyiben a későbbi szakaszokban problémába ütközünk, visszatérhetünk (vagy vissza kell térnünk) ehhez a lépéshez.
2.  **Alkalmazzunk egy nyílt licenszet.**
    1.  Állapítsuk meg, hogy az adatok milyen szellemi tulajdonjogokkal rendelkeznek.
    2.  Alkalmazzunk egy megfelelő "nyílt" licenszet, amely lefedi ezeket a jogokat és támogatja a "Mit jelent az, hogy nyílt adat" részben leírt "nyílt adat" definíciót.
    3.  Amennyiben ezt nem tudjuk megtenni, ugorjunk az első lépésre és próbálkozzunk egy másik adathalmazzal.

3.  **Tegyük elérhetővé az adatokat** - letölthetően, valamilyen hasznos formátumban. Fontolóra vehetjük ezek alternatív módon, például egy API-n keresztül való publikálását is.
4.  **Tegyük felfedezhetővé** - tegyük ki az adatainkat a webre, esetleg rendezzük katalógusba a nyílt adathalmazainkat.

## Válasszunk adathalmaz(oka)t!

Első lépésként válasszuk ki azokat az adathalmaz(oka)t, amelyeket nyílttá szeretnénk tenni – tartsuk azonban észben, hogy az adatok nyílttá tevésének teljes folyamata iteratív, ezért ha a későbbiekben problémába ütközünk, visszatérhetünk ehhez a lépéshez. 

Ha már pontosan tudjuk, hogy mely adathalmaz(oka)t kívánjuk nyílttá tenni, ugorjunk a következő szakaszra. Számos esetben azonban, különösen nagy intézménynél, kihívást jelenthet annak kiválasztása, hogy mely adathalmazokra fókuszáljunk. Hogyan lépjünk ekkor tovább?

Gyors megoldásként készíthetünk egy listát, hogy áttekintsük, első ránézésre mely adathalmazok tűnnek alkalmasnak. A későbbi szakaszokban lesz időnk részletesen ellenőrizni az egyes elemek megfelelőségét.

**Nem követelmény**, hogy átfogó listát készítsünk az adathalmazainkról. Az elsődleges szempont, hogy egyáltalán megvalósítható-e az adatok publikálása (akár nyíltan, akár másként) - lásd az [előző szakaszt](../what-is-open-data/).

### A közösség igényei alapján

Elsőként célszerű a közösséget megkérdezni. Azok, akik hozzá fognak férni az adatokhoz és fel fogják azokat használni, nagy valószínűséggel jó rálátással rendelkeznek arról, hogy mely adatok lehetnek értékesek.

1.  Készítsünk egy rövid listát a potenciális adathalmazokról, amelyekről visszajelzést szeretnénk kapni. A listának nem szükségszerűen kell megegyeznie az elvárásainkkal, a fő cél az, hogy megismerjük az adatokra vonatkozó igényeket. Ez alapulhat például más országok [nyílt adat](/glossary/hu/terms/open-data/) katalógusain.
2.  Hozzunk létre egy RFC-t (Request For Comment).
3.  Publikáljuk az RFC-t egy weblapon. Gondoskodjunk arról, hogy az RFC saját URL-lel rendelkezzen, hogy az a közösségi oldalakon is könnyen megosztható legyen.
4.  Biztosítsuk, hogy a válaszok beküldése egyszerű legyen. Kerüljük a kötelező regisztrációt, mert az csökkenti a válaszadók számát.
5.  Küldjük el az RFC-t a releváns levelezőlistáknak, fórumoknak és személyeknek, hivatkozva a fő weblapunkra.
6.  6.	Rendezzünk egy konzultációs eseményt. Találjunk olyan alkalmas időpontot, amikor az átlagos üzletemberek, [adatszekértők](/glossary/hu/terms/data-wrangler/) és tisztviselők is részt tudnak ezen venni.
7.  7.	Keressünk meg egy politikust, hogy beszéljen a szervezetünk érdekében. A nyílt adatok nagy valószínűséggel egy olyan nagyobb szabályozás részei, amelynek célja az állami információkhoz való hozzáférés növelése.

### Pénzügyi költségek alapján

Mennyi pénzt költenek a hivatalok az általuk kezelt adatok gyűjtésére és karbantartására? Ha egy adott adathalmazra sok pénzt fordítanak, ahhoz nagy valószínűséggel mások is hozzá szeretnének férni.

Ez az érvelés magával hordozhatja az "ingyenélés" aggályát.   Felmerülhet a kérdés, hogy "Miért kapják meg mások ingyen azokat az információkat, amelyek ilyen sokba kerülnek?". A válasz az, hogy a költségeket elnyeli a közigazgatás egy adott funkció ellátása érdekében. Ha az adatok már rendelkezésre állnak, azok harmadik fél számára történő továbbításának költsége közelít a nullához. Ezért, ezeknek célszerű ingyenesnek lenniük.

### A publikálás egyszerűsége alapján

Némely esetben, ahelyett, hogy eldöntenénk, mely adatok a legértékesebbek, célszerű lehet áttekinteni, hogy melyeket a legkönnyebb eljuttatni a nyilvánossághoz. A kisméretű, könnyű kiadások katalizátorként viselkedhetnek a szervezetekben bekövetkező nagyobb viselkedésbeli változásokhoz.

Legyünk azonban óvatosak ezzel a megközelítéssel. Előfordulhat, hogy ezek a kis kiadások olyan csekély értékkel rendelkeznek, hogy semmit sem hoznak létre belőlük. Amennyiben ez bekövetkezik, a projekt égészébe vetett hit meginoghat.

### Mások tevékenysége alapján

A nyílt adatok egy növekvő mozgalom. Valószínűleg számos olyan ember dolgozik a területünkön, aki átlátja, hogy más területek mivel foglalkoznak. Készítsünk egy listát más hivatalok tevékenységei alapján.

## Használjunk nyílt licenszet (jogi nyíltság)!

A legtöbb jogrendszerben az adatok szellemi tulajdonjogai megtiltják, hogy azokat a tulajdonos explicit engedélye nélkül egy harmadik fél újrahasznosítsa és továbbterjessze. Azokban az országokban, ahol e jogok megléte bizonytalan is fontos az, hogy az adatainkat licensszel lássuk el, pusztán az egyértelműség kedvéért. Ezáltal, **amennyiben az adatainkat elérhetővé akarjuk tenni, célszerű azokat valamilyen licensszel ellátnunk** – és ha [nyílttá](http://opendefinition.org/) kívánjuk tenni őket, ez még inkább fontos.

Milyen licenszeket használhatunk? Mi azt javasoljuk, hogy "nyílt" adatok esetén az [Open Definition](open_)-ben előírtaknak megfelelő licenszek egyikét alkalmazzuk, amely az "adatokhoz megfelelő" jelöléssel rendelkezik. Ezek listája (a felhasználásukra vonatkozó utasításokkal) a következő címen érhető el:

-   <http://opendefinition.org/licenses/>

A licenszek alkalmazására vonatkozó rövid, 1 oldalas útmutató az Open Data Commons oldalán a következő címen érhető el:

-   <http://opendatacommons.org/guide/>

## Tegyük elérhetővé az adatokat (technikai nyíltság)!

A [nyílt adatoknak](/glossary/hu/terms/open-data/) jogilag és technikailag is nyíltnak kell lenniük. Specifikusan, az adatoknak valamilyen [gép által olvasható](/glossary/en/terms/machine-readable/) formátumban kell szabadon letölthetőnek lenniük.

**Elérhető**

Az adatok ára nem lehet több, mint azok reális reprodukciós költsége, lehetőleg ingyenes internetes letöltésként elérhetően. Ez az árazási modell azért engedhető meg, hogy ne kelljen költségekbe bocsátkoznunk az adatok szolgáltatása miatt.

**Egyben**

Az adatokat egészükben kell publikálni. Például ha valamilyen állami nyilvántartással rendelkezünk, az egész regisztert letölthetővé kell tennünk. Egy webes API vagy hasonló szolgáltatás is rendkívül hasznos lehet, de ezek nem helyettesítik a letöltési lehetőséget.

**Nyílt, gép által olvasható formátum**

Az állami szféra által publikált adatoknak nem célszerű szabadalmi korlátozásokkal rendelkeznie. Ennél is fontosabb, hogy olyan gépi formátumot használjunk, amely leginkább támogatja az újrafelhasználást. Vegyünk például olyan PDF dokumentumokként (Portable Document Format) publikált statisztikákat, amelyeket gyakran használnak a jó minőségű nyomtatásban. Habár ezek az emberek számára jól olvashatóak, a számítógépeknek igen nehézkes a feldolgozásuk, ami nagyban korlátozza az adatok újrahasznosításának lehetőségét.

A következő szabályok betartásából jelentős előnyünk származhat:

-   törekedjünk az egyszerűségre
-   cselekedjünk gyorsan
-   legyünk pragmatikusak

Jobb most nyers adatokat kiadni, mint hat hónap múlva tökéleteseket.

Az adatok közzétételének számos különböző módja van. Az internet korában a legkézenfekvőbb az online publikálás. Ennek a modellnek számos változata létezik. A legegyszerűbb az, ha a hivatalok az adatokat a saját weblapjukon teszik elérhetővé, és egy központi katalógus a látogatót a megfelelő forrásra irányítja. Léteznek azonban alternatívák.

Amennyiben a [konnektivitás](/glossary/hu/terms/connectivity/) korlátozott, vagy az adatok mennyisége extrém nagy, indokolt lehet ezek más formátumban történő disztribúciója. A következő szakaszban olyan alternatívákról is szót fogunk ejteni, amelyek rendkívül alacsony költségekkel járnak.

### Online módszerek

#### Saját weblapon

A webes tartalomért felelős csapatok leggyakrabban használt módszere a fájlok publikálására a saját weblapokra történő közzététel és letöltési lehetőség. Miképp ezek hozzáférést nyújtanak például a különböző vitaanyagokhoz, a módszer az adatfájlok közzétételére is tökéletesen megfelel.

Ennek a megközelítésnek az egyik nehézsége, hogy a külső érdeklődők számára nehéz felkutatni, hogy hol találhatnak naprakész információkat. Ez teher lehet azoknak, akik eszközöket készítenek az adataink felhasználásával.

#### Harmadik féltől származó weblapon keresztül

Az idők során számos repozitórium vált egy adott terület adatainak központi gyűjtőhelyévé. A xively.com  például összeköti a szenzorok birtokosait azokkal, akik ezek adataihoz szeretnének hozzáférni.

A harmadik féltől származó weblapok rendkívül praktikusak lehetnek. Ezek már rendelkeznek a téma iránt érdeklődő közösséggel, valamint tartalmaznak további adathalmazokat. Amennyiben az adatunk része egy ilyen platformnak, úgy halmozott pozitív érdeklődés jöhet létre.

A nagybani adatplatformok olyan infrastruktúrával rendelkeznek, amelyek ki tudják szolgálni az igényeket. Továbbá, gyakran kínálnak analitikai és használati információkat. Használatuk az állami ügynökségek számára ingyenes is lehet.

Az ilyen platformok használatának két ára lehet. Az első a függetlenség. A hivatalunknak képesnek kell lennie átadni az adatok kezelését másoknak. Ez gyakran politikai, jogi, vagy szervezeti működés szempontjából nehéz lehet. A második pedig a nyíltság. Bizonyosodjunk meg róla, hogy az adatplatformunk agnosztikus arra, hogy ki férhet hozzá. A szoftverfejlesztők és tudósok számos operációs rendszert használnak, az okostelefonra írtaktól kezdve a szuperszámítógépes rendszerekig. Az adatoknak mindannyiuk számára elérhetőnek kell lennie.

#### FTP szerveren

Egy kevésbé divatos módja a fájljaink közzétételének a File Transfer Protocol (FTP). Ez akkor bizonyulhat jó választásnak, ha a közönségünk műszaki háttérrel rendelkezik, például azok szoftverfejlesztők vagy tudósok. Az FTP rendszert a HTTP helyett használják, de specifikusan fájlátvitelekhez hozták létre.

Az FTP manapság már nem túl népszerű. Szemben a weblapokkal, az FTP szerveren történő böngészés hasonlít a számítógépünk könyvtáraiban való böngészésre. Ezáltal, habár a feladatát ellátja, a webes fejlesztőcégeknek sokkal kevesebb lehetőségük lesz pénzt kérniük a testreszabásért.

#### Torrentként

A [BitTorrent](/glossary/hu/terms/bittorrent/) a törvénykezés számára a szerzői jogok megsértése kapcsán vált ismertté. A BitTorrent ún. torrent fájlokat használ, amelyek elosztják a fájlok terjesztési költségét a fájlokhoz hozzáférő felhasználók között. A szerverek túlterhelése helyett a kereslet növekedésével nő a kínálat is. A rendszer épp ezért olyan sikeres a filmek megosztásában. A BitTorrent rendkívül hatékony módja a nagy mennyiségű adatok továbbításának.

#### API-ként

Az adatokat publikálhatjuk egy [Application Programming Interface](/glossary/hu/terms/application-programming-interface/) (API-n) keresztül is. Ezek az interfészek rendkívül népszerűek, mert lehetővé teszik a programozóknak, hogy az adatok csak egyes részeit válasszák ki, ahelyett, hogy azok egészével, egyetlen nagy fájlként kellene dolgozniuk. Az API-k általában egy valós időben frissülő adatbázishoz kapcsolódnak. Vagyis, ha egy API-n keresztül tesszük elérhetővé az információkat, azzal biztosíthatjuk, hogy azok mindig naprakészek legyenek.

Minden nyílt adatokkal foglalkozó kezdeményezés elsődleges céljának a nyers adatok egyben történő publikálása kell lennie. Egy API fenntartása több költséggel jár:

1.  Az ár. Sokkal több fejlesztést és karbantartást igényelnek, mint az egyszerű fájlok.
2.  Az elvárások. Hogy a rendszer mögött kialakulhasson egy felhasználói bázis, fontos megbízhatóságot sugallnunk. Ha valami elromlik, tőlünk várják, hogy vállaljuk a javítás költségeit.

Az API-k előnyei, hogy a felhasználók: 
1.	másodpercre aktuális adatokat, például közlekedési információkat érhetnek el
2.	az adatoknak csak az aktuálisan használt részei kerülnek továbbításra, csökkentve az ezzel járó költségeket. 

Az egyben történő letöltés lehetősége bizosítja, hogy:

-   nincs függés az adatok eredeti szolgáltatójától, vagyis ha újrastrukturálás vagy költségvetési ciklusváltás miatt a körülmények megváltoznak, az adatok továbbra is elérhetőek maradnak.
-   bárki beszerezheti és továbbterjesztheti az adatok másolatait. Ez csökkenti a forrást kiadó szervezet terjesztési költségeit és kiküszöböli a szűk keresztmetszeteket.
-   az adatok felhasználásával mások új szolgáltatásokat fejleszthetnek, mert biztos, hogy azokat nem vonják meg tőlük.

Az adatok egészben történő publikálása lehetővé teszi, hogy azokat az eredetitől eltérő célra használják. Például, más formátumba konvertálhatják őket, összevethetik őket más forrásokkal, verziókövetést alkalmazhatnak rajtuk vagy több helyen archiválhatják őket. Habár az adatok legfrissebb verzióját nyugodtan publikálhatjuk egy API-n keresztül, a nyers adatokat is célszerű egyben, szabályos időközönként publikálni.

Például, az [az Eurostat statisztikai szolgáltatás](http://epp.eurostat.ec.europa.eu/) esetén az élő adatok mellett lehetőség van az adatok egyben történő letöltésére, az oldal közel 4 000 adatfájllal rendelkezik. Az oldal naponta kétszer frissül és  [Tab-separated values] (/glossary/en/terms/tab-separated-values/) (TSV) formátumban kínál letöltéseket. Továbbá, dokumentációt is tartalmaz a letöltés módjáról valamint az adatfájlokról.

Egy másik példa a [District of Columbia Data Catalog](http://opendata.dc.gov/), amely az aktuális élő adatok mellett lehetővé teszi adatok CSV és XLS formátumú letöltését.

## Tegyük felfedezhetővé az adatokat!

A [nyílt adatok](/glossary/en/terms/open-data/) mit sem érnek felhasználók nélkül. Fontos biztosítanunk, hogy mások is képesek legyenek megtalálni a forrásanyagokat. Ez a szakasz az erre irányuló különböző megközelítésekkel foglalkozik.

A legfontosabb feladatunk, hogy olyan semleges teret kínáljunk, amely képes ellenállni a hivatalok közti politikának és a későbbi költségvetési ciklusoknak. A jogi korlátok, legyenek akár szektoriálisak akár földrajziak, nehézzé tehetik az együttműködést. Azonban, a közös munka jelentős előnyökkel jár. Minél egyszerűbb az adatok felfedezése, annál gyorsabban jönnek létre hasznos, új eszközök a segítségükkel.

### Elérhető eszközök

A weben számos olyan eszköz található, amelyek kifejezetten az adatok jobb felfedezhetőségét segítik.

Közülük az egyik legkiemelkedőbb a [DataHub](http://thedatahub.org/), amely katalógusként és adattárként szolgál adathalmazok számára szerte a világon. Az oldal megkönnyíti az anyagok publikálását a magánszemélyek és szervezetek számára, a felhasználóknak pedig segít a keresett adatok megtalálásában.

Ezen felül, az oldal tucatnyi, specializált katalógust kínál a különböző szektorok és helyek számára. Számos tudományos közösség hozott létre katalógusrendszert saját területén, mert a publikációkhoz gyakran van szükség adatokra.

### Az állam számára

Az eddigi tapasztalatok szerint általában egy vezető minisztériumot bíznak meg azzal, hogy katalógust készítsen az állami adatokról. A katalógusok létrehozásakor törekedjünk olyan struktúra létrehozására, amely más minisztériumok és részlegek számára is lehetővé teszi az információik naprakészen tartását.

Álljunk ellen a késztetésnek, hogy saját magunk készítsük el a katalógust kezelő szoftvert. Léteznek olyan ingyenes, nyílt forráskódú szoftvermegoldások (például a [CKAN](http://ckan.org/)), amelyet már számos kormány adaptált. Így többnyire nincs szükség egy saját platformba külön forrásokat fektetni.

Létezik néhány dolog, amely a legtöbb nyílt adat katalógusból hiányzik, így a programunknak célszerű figyelembe venni a következőket:

-   Adjunk lehetőséget arra, hogy a magán és közösségi szektorok kiegészíthessék az adatokat. Érdemes lehet a katalógusra regionális katalógusként, nem regionális állami katalógusként tekinteni.
-   Könnyítsük meg az adatminőség javítását azzal, hogy engedélyezzük a leszármazott adathalmazok katalógusba vételét. Például, ha valaki címeket geokódolt, és megosztaná a munkáját másokkal, de az adatahalmazoknak csak egy verziója engedélyezett, az efféle fejlesztések rejtve maradnak.
-   Legyünk toleránsak azzal, ha az adataink máshol is megjelennek.  A tartalmat az érintett közösségek valószínűleg duplikálni fogják. Ha van egy folyók vízszintjeit monitorozó adatbázisunk, az adataink megjelenhetnek a hidrológusok katalógusában.
-   Biztosítsuk, hogy a hozzáférés igazságos legyen. Próbáljuk elkerülni a privilegizált hozzáférési szinteket az állami tisztségviselők vagy a hivatásos kutatók számára, mert ez aláaknázza a közösség részvételét és elkötelezettségét.

### A civil társadalom számára

Legyünk nyitottak egy kiegészítő katalógus létrehozására a nem-hivatalos adatok számára.

Nagyon ritka, hogy az állam nem hivatalos vagy nem mérvadó forrásokkal foglalkozzon. A tisztviselők gyakran hatalmas erőfeszítéseket tesznek annak érdekében, hogy ne okozzon kínos politikai visszhangot vagy egyéb problémát az adatok rossz felhasználása, vagy az azoktól való túlzott függés.

Továbbá, az állam valószínűleg nem kíván olyan kezdeményezéseket támogatni, amelyek üzleti információkkal vegyítik a saját információjukat. Az államigazgatás joggal szkeptikus a profitirányultság miatt. Ezért indokolt lehet egy független katalógus létrehozása a közösségek, cégek és más felhasználók számára.
