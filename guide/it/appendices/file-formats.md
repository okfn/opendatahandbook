---
title: Formati dei file
---

## Una panoramica sui formati di file

### JSON

JSON è un formato di file semplice e molto facile da leggere per tutti i linguaggi di programmazione. La sua semplicità vuol dire che è in generale più facile da elaborare per i computer rispetto ad altri formati, quale l'XML.

### XML

XML è un formato ampiamente utilizzato per lo scambio dei dati perché fornisce buone opportunità per conservare la struttura dei dati ed il modo in cui i file sono predisposti, e consente agli sviluppatori di includere parte della documentazione insieme ai dati ma senza interferire con la loro lettura.

### RDF

Un formato raccomandato dal W3C è l' RDF, che consente di rappresentare i dati in una forma che rende facilmente integrabili dati provenienti da fonti diverse. I dati RDF possono essere memorizzati in XML e JSON, oltre che in altri formati. L'RDF incoraggia l'uso di URL come identificatori, provvedendo così un sistema utile per collegare direttamente le iniziative Open Data sul web. L'RDF è ancora poco diffuso, ma il suo uso sta diventando comune fra le iniziative di Open Government, compresi i progetti Linked Open Data dei governi britannico e spagnolo. L'inventore del Web, Tim Berners-Lee, ha proposto una classificazione a cinque stelle che indica i dati RDF come un obiettivo da perseguire nelle iniziative Open Data.

### Fogli di calcolo

Molte autorità hanno informazioni archiviate in fogli di calcolo, come ad esempio Microsoft Excel. Questi dati possono spesso essere utilizzati immediatamente assieme alla corretta descrizione di ciò che le varie colonne rappresentano.

Tuttavia, in alcuni casi potrebbero esserci macro e formule nei fogli di calcolo, che possono essere scomodi da gestire. Si consiglia pertanto di documentare tali calcoli accanto al foglio elettronico, facilitando la loro accessibilità per gli utenti.

### Comma Separated File - Dati Separati da Virgola

I file CSV possono essere un formato molto utile perché compatti e quindi adatti per trasferire grandi insiemi di dati con la stessa struttura. Tuttavia, il formato è così spartano che i dati, senza documentazione, sono spesso inutili dal momento che diventa quasi impossibile identificare il significato delle diverse colonne. È pertanto fondamentale che sia fornita un'appropriata documentazione insieme ai file in formato CSV.

É inoltre essenziale che la struttura del file sia rispettata. L'omissione anche di un solo campo può impedire lettura di tutti i restanti dati del file, senza alcuna possibilità di correzione, in quanto non è possibile interpretare il senso dei campi successivi.

### Documento di testo

Documenti in formati classici come Word, ODF, OOXML, o PDF possono essere sufficienti per mostrare alcuni tipi di dati - ad esempio, mailing list relativamente stabili o loro equivalenti. Possono essere condivisi a basso costo, essendo i formati in cui spesso i dati sono nati. Questi formati non aiutano in alcun modo a mantenere coerente la struttura, e quindi è spesso difficile inserire i dati in modo automatico. Assicuratevi di utilizzare come base dei documenti dei modelli che possano evidenziare i dati per un loro potenziale riutilizzo, in modo che almeno sia possibile estrarre le informazioni dai documenti.

Il successivo utilizzo di dati può anche essere favorito da markup tipografici, che rendono più facile per una macchina distinguere le intestazioni (di qualsiasi specifico tipo) dal contenuto e così via. Generalmente si raccomanda di non proporre i dati in formato word processing, se i dati sono disponibili in formato diverso.

### Testo semplice

I documenti di testo (.txt) sono molto facili da leggere per i computer. Tuttavia generalmente non includono meta-dati strutturali dall'interno del documento, con la conseguenza che gli sviluppatori devono creare un parser/analizzatore in grado di interpretare ogni documento così come appare.

Alcuni problemi possono nascere quando i file di testo sono scambiati tra sistemi operativi diversi. MS Windows, Mac OS X e altre varianti di Unix hanno un proprio modo di istruire il computer sul raggiungimento del fine - rigo.

### Immagine acquisita (scanner)

Probabilmente la forma meno adatta per la maggior parte dei dati, ma sia TIFF che JPEG-2000 sono in grado di aggiungere dettagli su ciò che è rappresentato nella foto - fino anche a inserire nell'immagine un contenuto con del testo integrale del documento. Possono essere utili per la visualizzazione come immagini di quei dati che non sono stati originati elettronicamente - un esempio immediato è il materiale di una vecchia chiesa e altri archivi - e una foto è meglio di niente.

### Formati proprietari

Alcuni sistemi specializzati hanno i propri formati di dati in cui possono salvare o esportare dati. A volte può anche essere sufficiente condividere i dati in questi formati - soprattutto se si prevede che l'uso successiva sia fatto in un sistema simile a quello da cui provengono. Dovrebbe sempre essere indicato dove si possono trovare ulteriori informazioni su questi formati proprietari, ad esempio con un link al sito web del fornitore. In generale si consiglia, ove possibile, di condividere dati utilizzando formati non proprietari.

### HTML

Oggi una gran quantità di dati è disponibile nel formato HTML su vari siti. Ciò sarebbe senz'altro sufficiente se i dati fossero molto stabili e i e riguardas un ambito limitato. In qualche caso sarebbe preferibile avere i dati in un formato più semplice da scaricare e manipolare, ma visto che è semplice ed economico fare riferimento ad una pagina di un sito web, quello potrebbe essere un buon punto di partenza per mostrare i dati.

Tipicamente sarebbe più opportuno utilizzare tabelle nei documenti HTML per contenere i dati, e che i vari campi di dati siano visualizzati e identificati in modo che siano facili da trovare e manipolare. Yahoo ha sviluppato uno strumento (<http://developer.yahoo.com/yql/>) in grado di estrarre informazioni strutturate da un sito web: tali strumenti possono raggiungere risultati molto migliori se i dati sono accuratamente etichettati.

## Formati di file aperti

Anche se le informazioni sono fornite in formato elettronico, in formato leggibile dalla macchina e nel dettaglio, ci possono essere questioni relative al formato del file stesso.

I formati in cui le informazioni sono pubblicate - in altre parole, la base digitale in cui sono memorizzate le informazioni - può essere "aperto" o "chiuso". Un formato aperto è quello in cui le specifiche per il software sono a disposizione di chiunque, gratuitamente, in modo che chiunque possa utilizzarle nel proprio software senza alcuna limitazione di riutilizzo imposto attraverso diritti di proprietà intellettuale.

Quando il formato è "chiuso", può significare o che il formato è proprietario e le caratteristiche tecniche non sono pubblicamente disponibili, o che il formato del file è proprietario ed anche se le specifiche tecniche sono pubbliche, il riutilizzo è limitato. La pubblicazione dell'informazione in un formato chiuso può causare notevoli ostacoli per la sua riutilizzazione dei dati in essa codificati, costringendo coloro che desiderano utilizzarle ad acquistare il software necessario.

Il vantaggio dei formati di file aperto è che permettono agli sviluppatori di produrre software e servizi multipli utilizzando tali formati. Questo riduce al minimo gli ostacoli per riutilizzare le informazioni in essi contenute.

Usare per i file formati proprietari, per i quali le specifiche non sono disponibili pubblicamente, può creare dipendenza dal software di terzi o dai detentori della licenza del formato. Nel caso peggiore questo può significare che l'informazione può essere letta soltanto utilizzando un certo pacchetto software - che può avere un costo proibitivo, o potrebbe divenire obsoleto.

La preferenza dal punto di vista degli {term:open government data}è che l'informazione deve essere rilasciata in **formati di file aperti che sono machine-readalbe.**

### Esempio: i dati sul traffico nel Regno Unito

Andrew Nicolson è uno sviluppatore software che è stato coinvolto in una campagna (riuscita con successo) contro la costruzione di una nuova strada, la tangenziale Est Westbury, nel Regno Unito. Andrew era interessato ad accedere e utilizzare i dati sul traffico stradale che veniva utilizzati per giustificare le proposte. Riuscì a ottenere alcuni dati interessante attraverso la libertà di richiesta di informazioni, ma il governo locale forniva i dati in un formato proprietario che potevano essere letti solo con il software prodotto dalla società Saturno. Azienda specializzata nella modellazione del traffico e le previsioni. Non era disponibile una versione in "sola lettura" versione del software, obbligando così il gruppo di Andrew gruppo nell'acquisto di una licenza software, scontanto a 500£ (600€) nella versione per enti educativi. Il pacchetto software principale, nel listi di aprile 2010 di Saturno a partiva da 13.000£ (oltre 15.000€ ), un prezzo fuori dalla portata della maggior parte dei cittadini.

Sebbene non si abbia accesso all'informazione, la legge dà il diritto di accesso in formati aperti, le iniziative open government data stanno iniziando ad essere accompagnate da documenti programmatici che prevedono che le informazioni ufficiali debbano essere rese disponibili in formati aperti. L'impostazione del gold standard è stata fatta dall'amministrazione Obama, con la direttiva Open Government pubblicata nel dicembre 2009, che dice:

> *Per quanto possibile e soggetti a valide restrizioni, gli enti dovrebbero pubblicare online le informazioni in un formato aperto in modo che possano essere recuperate, scaricate, indicizzate e ricercate da comune applicazioni web di ricerca. Un formato aperto deve essere indipendente dalla piattaforma, machine-readable, e resi disponibili al pubblico senza restrizioni che ne impediscona il riuso.*

## Come si fa ad usare un determinato formato?

Quando un ente deve presentare nuovi dati - dati che non sono stati esposti prima - dovrebbe scegliere il formato che offre il miglior equilibrio tra costi e l'idoneità allo scopo. Per ogni formato ci sono alcune cose di cui bisogna essere a conoscenza, e questa sezione mira a spiegarle.

Questa sezione si concentra sui servizi di interoperabilità in modo da favorire l'accesso diretto fra macchine. Consigli e indicazioni su come le soluzioni e siti debbano essere progettati può essere trovato altrove.

### Servizi web - web services

Per i dati soggetti a frequenti modifiche, e dove ogni download è limitato nelle dimensioni, è molto utile esporre i dati attraverso web services. Ci sono diversi modi per creare un web service, ma alcuni dei più utilizzati sono SOAP e REST. Generalmente, SOAP su REST, servizi REST, ma sono molto facili da sviluppare e utilizzare, e si tratta pertanto di uno standard ampiamente utilizzato.

### Database

Al pari dei web service, i database consentono dinamicamente un accesso diretto ai dati. I database hanno il vantaggio di poter consentire agli utenti di mettere insieme ed estrarre soltanto ciò a cui sono interessati.

Ci sono alcuni problemi di sicurezza nel estrazione remota da un database e l'accesso al database è utile solo se la struttura del database e l'importanza delle singole tabelle e campi sono ben documentati. Spesso, è relativamente semplice e poco costoso per creare servizi web che espongono i dati da un database, risolvendo, in maniera molto semplice i problemi di sicurezza.