---
redirect_from: /lt_LT/appendices/index.html
section: guide
lang: lt_LT
title: Failų formatai
---

## Failų formatų apžvalga

### JSON

JSON yra paprastas failų formatas, kurį labai lengva skaityti bet kuriai programavimo kalbai. Jo paprastumas reiškia, kad kompiuteriams jį apdoroti lengviau nei kitus formatus, pavyzdžiui, XML.

### XML

XML yra plačiai naudojamas formatas dalijantis duomenimis, nes jis suteikia galimybę išlaikyti duomenų struktūrą ir įrašyti dokumentaciją kartu su duomenimis neatliekant pačių duomenų nuskaitymo.

### RDF

W3C rekomenduoja formatą trumpiniu RDF, kuris įgalina saugoti duomenis taip, kad būtų galima apjungti duomenis gautus iš skirtingų šaltinių. RDF duomenys gali būti išsaugoti XML arba JSON formatu, bei kitais formatais. RDF skatina internetinių nuorodų naudojimą kaip unikalų raktą, kuris įgalina sujungti įvairias :term:'open data' iniaciatyvas internete. RDF vis dar nėra labai stipriai išpopuliarėjęs, tačiau tai dažniausiai naudojmas formatas tarp Atviros Vyriausybės iniciatyvų, įskaitant Didžiosios Britanijos ir Ispanijos Vyriausybių sujungtus Open Data projektus. Interneto kūrėjęs, Tim Berners-Lee neseniai paskelbė penkių žvaigždučių schemą į kurią įeina sujungti RDF duomenys kaip prioritetas atvirų duomenų srityje.

### Skaičialentės (spreadsheets)

Daugelis valstybės institucijų saugo informaciją skaičialentėse, pavyzdžiui, Microsoft Excel. Tokie duomenys dažnai gali būti naudojami tuoj pat, jei tik teisingai aprašytos stulpelių reikšmės.

Tačiau, kai kuriais atvejais skaičiuoklių dokumentuose gali atsirasti papildomos informacijos arba formulių, su kuriomis gali būti sunku dirbti. Tokiu atveju patartina skaičiavimus dokumentuoti šalia duomenį, nes taip patogiau vartotojams perskaityti.

### Kableliu atskirto turinio failai

CSV gali būti labai naudingas formatas, nes yra kompaktiškas, taigi tinkamas keistis dideliems duomenų rinkiniams, turintiems vienodą struktūrą. Tačiau šis formatas toks "spartietiškas", kad duomenys dažnai būna beverčiai be dokumentacijos, kadangi gali būti beveik neįmanoma atspėti, ką reiškia kurie stulpeliai. Todėl labai svarbu, kad kablelių atskirto turinio failuose būtų tiksliai dokumentuotos laukų reikšmės.

Dar daugiau, failo struktūros būtina griežtai laikytis, nes praleista viena reikšmė gali neleisti nuskaityti viso likusio failo informacijos. Taip pat būtų sunku atitaisyti informaciją, nes nežinia kaip turėtų atrodyti duomenys.

### Tekstinis dokumentas

Klasikinių dokumentų tokiais formatais, kaip Word, ODF, OOXML arba PDF gali pakakti kai kurioms duomenų rūšims. Jais skelbti duomenis gali būti pigu, kadangi dažnai tai yra pradinis duomenų formatas. Tačiau tokie formatai nepalaiko vienodos duomenų struktūros, o tai reiškia, kad gali būti sunku automatizuoti duomenų apdorojimą. Pasistenkite naudoti dokumentų šablonus, leisiančius suprasti, kokia duomenų struktūra, kad vėliau būtų įmanoma iš tų dokumentų ištraukti ir struktūrizuoti duomenis.

Jis taip pat gali palaikyti įvairias tipografines žymas, taigi skaitant mašininiu būdu galima būtų atskirti pavadinimus nuo turinio, ir taip toliau. Bet paprastai rekomenduojama nesinaudoti teksto redagavimo formatais, jei galima rinktis kitus formatus.

### Grynasis tekstas

Tekstiniai failai(.txt) yra lengvai kompiuterių perskaitomi. Dažniausiai į juos neįeina meta duomenys apie dokumentą, taigi kūrėjai turėtų nusiskaityti duomenis taip, kad būtų galima interpretuoti informaciją tokią kokia ji yra, be papildomo žinojimo apie dokumento struktūrą(meta duomenų).

Gali būti problemų, naudojant grynojo teksto failus skirtingose operacinėse sistemose. MS Windows, Mac OS X ir Unix kiekviena savaip pasako kompiuteriui, kad jau pasiekė failo pabaigą.

### Skanuotas paveikslėlis

Greičiausiai labiausiai netinkantis duomenų formatas, tačiau tiek TIFF, tiek JPEG-2000 gali būti susieti su komentaru kas yra paveikle arba pateikti pilną paveiklo turinio aprašymą. Tai gali būti svarbu duomenims, kurių prigimtis nėra elektroninė - geriausias pavyzdys būtų seni bažnytiniai archyvo įrašai, tada nuotrauka geriau nei nieko.

### Nuosavybiniai formatai

Kai kurios dedikuotos sistemos turi nuosavus duomenų formatus, kuriais išsaugo duomenis. Kartais gali ir pakakti atverti duomenis tokiu formatu - ypač jei tikimasi, kad duomenys bus toliau naudojami panašioje sistemoje kaip ta, kurioje tie duomenys dabar yra. Visada turi būti nurodyta, kur rasti daugiau informacijos apie šiuos nuosavybinius formatus, pavyzdžiui, gali būti nuoroda į tiekėjo svetainę. Vis tik, rekomenduojama duomenis pateikti ne nuosavybiniu formatu, kur tik tai įmanoma.

### HTML

Šiandien daug duomenų skelbiami įvairiose svetainėse HTML formatu. To gali pakakti, jei duomenys stabilūs ir nedidelės apimties. Kartais geriau duomenis pateikti taip, kad būtų lengva juos atsisiųsti ir su jais dirbti, tačiau kadangi į svetainę pigu ir paprasta nukreipti, tai gali būti visai gera pradžia skelbiant duomenis.

Dažniausiai patogiausia naudoti lenteles HTML dokumentuose laikyti duomenims. Taip pat svarbu, kad duomenų laukai turėtų unikalius kodus, kad būtų lengva atlikti duomenų paiešką ir darbą. Yahoo sukūrė įrankį (<http://developer.yahoo.com/yql/>), kuris skirtas nuskaityti informaciją iš svetainės ir tokie įrankiai su duomenimis gali atlikti ivairias sudėtingesnes manipuliacijas.

## Atviri failų formatai

Net jei duomenys pateikiami elektroniniu, mašininiam skaitymui pritaikytu formatu, ir labai smulkiai, vis tiek gali būti problemų, susijusių su pačiu formatu.

Formatai, kuriais informacija skelbiama - kitaip tariant, ta skaitmeninė bazė, kurioje saugoma informacija - gali būti "atvira" arba "uždara". Atviro formato specifikacija yra prieinama bet kam ir nemokamai, taigi visi gali be intelektinės nuosavybės teisių apribojimų naudoti tas specifikacijas kurdami savo programinę įrangą.

Jei formatas "uždaras", taip gali būti arba dėl to, kad failo formatas nuosavybinis ir specifikacija nėra prieinama visuomenei, arba dėl to, kad failo formatas yra nuosavybinis ir net jei specifikacija vieša, jos naudojimas ribotas. Jei informacija paskelbiama naudojantis uždaru formatu, gali kilti rimtų kliūčių tai informacijai panaudoti, ir norintiems ja naudotis gali tekti pirkti tam reikalingą programinę įrangą.

Atvirų failų formatų privalumas tas, kad jie leidžia programinės įrangos kūrėjams sukurti įvairius įrankius, galinčius naudotis tais formatais. Tai minimizuoja kliūtis pernaudoti failuose esančią informaciją.

Naudojant failų formatus, kurių specifikacija nėra viešai prieinama, galima sukelti priklausomumą nuo kitos programinės įrangos arba failo formato licenzijos problemas. Blogiausiu atveju informacija galės būt nuskaityta tik su specifine programine įranga, kas gali būti labai brangu.

term:'Atvirų valdžios duomenių' reikšmė yra ta, jog duomenys yra pateikiami **atviru failų formatu, kuris yra lengvai nuskaitomas.**

### Pavyzdys: Didžiosios Britanijos transporto duomenys

Andrew Nicolson yra programinės įrangos kūrėjas, kuris buvo įsitraukęs į (galiausiai sėkmingą) kampaniją prieš naujo kelio, Westbury Eastern aplinkkelio Didžiojoje Britanijoje, statybas. Andrew domino prieiga prie kelių transporto judėjimo duomenų, kurie buvo naudojami vertinant pasiūlymus. Jam pavyko kai kuriuos duomenis gauti pasinaudojus prašymais suteikti informaciją, tačiau vietos valdžia teikdavo informaciją nuosavybiniu formatu, ir juos buvo galima perskaityti tik naudojant kompanijos "Saturn", kuri specializavosi transporto judėjimo modeliavime ir prognozavime, programinę įrangą. Ši programinė įranga neturi versijos, skirtos vien tik informacijos perskaitymui, taigi Andrew neturėjo kitos išeities, kaip tik nusipirkti programinės įrangos licenciją, kuri jam kainavo 500 svarų (600 eurų) su nuolaida akademinėms reikmėms. Pagrindinių programinės įrangos modulių kainos kompanijos "Saturn" kainoraštyje 2010 metų balandžio mėnesį prasidėjo nuo 13 000. svarų (virš 15 000. eurų) - tai kainos, neįkandamos daugumai paprastų piliečių.

Nors nėra teisiškai būtina duomenis pateikti atviru formatu, tačiau atviros valdžios iniciatyvos teikia pirmenybę būtent atviriems duomenų formatams, taip pat leidžia reglamentuojančius įstatymus, jog duomenys turi būti pateikti atviru formatu. Bene reikšmingiausias pavyzdys yra Obama'os administracija su Atviros valdžios direktyva, patvirtinta 2009 m., kuri teigia:

> *Institucijos, kiek tai įmanoma ir nėra ribojama dėl kitų priežasčių, turi teikti informaciją internete ir atviru formatu, atsisiunčiamą, indeksuojamą ir randamą įprastų žiniatinklio paieškos aplikacijų. Atviru formatu laikomas formatas, kurio platforma yra nepriklausoma, skaitoma mašininiu būdu ir prieinamas visuomenei be apribojimų, kurie galėtų apriboti informacijos pakartotinį panaudojimą.*

## Kaip naudoti duotuosius formatus?

Kai valdininkai turi paviešinti naujus duomenis, kurie paviešinami pirmą kartą, turi būti parinktas formatas, subalansuojantis kainą su tinkamumu naudoti. Kiekvienam formatui yra savi niuansai, su kuriais reikia susipažinti. Šis skyrius bandys tuos niuansus paaiškinti.

Šis skyrius akcentuoja tik tai, kaip sukarpyti paviršiai yra geriausiai surikiuojami, kad kompiuteriai galėtų pasiekt juos tiesiogiai. Patarimai, kaip interneto svetainės turi būti sukurtos gali būti rasti kituose informacijos šaltiniuose.

### Žiniatinklio paslaugos (Web services)

Kai duomenys kinta dažnai ir kiekvienas parsiuntimas yra limituojamas, labai svarbu duomenis pateikti per internetinę paslaugą (web services). Yra keletas būdų sukurti internetinę paslaugą (web services), bet populiariausi yra SOAP ir REST. Bendru atveju, SOAP geriau nei REST, tačiau pastarąjį labai lengva naudoti, taigi jis tapo standartu.

### Duomenų bazė

Kaip ir internetinės paslaugos (web services), duomenų bazės suteikia tiesioginę prieigą prie duomenų. Duomenų bazių privalumas - tik dalies duomenų peržiūra ar redagavimas, visiškai atsiribojant nuo likusių.

Yra keletas saugumo rūpesčių dėl leidimo nuotoliniam duomenų naudojimui. Duomenų bazės prieinamumas naudingas tik tuomet, jei duomenų bazė labai gerai dokumentuota. Dažnai ganėtinai paprasta ir nebrangu sukurti internetinę paslaugą (web services), kuri pateikia duomenis iš duomenų bazės, o tai patogus būdas išvengti saugumo problemų.