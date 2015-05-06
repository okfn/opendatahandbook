---
section: guide
lang: zh_TW
title: 檔案格式
---

## 檔案格式綜覽

### JSON

JSON 是一種簡單的檔案格式，任何程式語言都可輕鬆讀取。其簡易的特性代表它和其他格式 - 例如 XML 相較，可更容易地透過電腦來處理。

### XML

XML廣泛地使用於資料交換，因為其可以完好地保存資料中的結構，還有檔案建立的方式，並且能讓程式員將部份說明文件寫進同檔案中，而不會干擾資料的可讀性

### RDF

RDF，一種W3C所建議的格式， 他呈現資料的方式讓其與其他格式相比，叫能結合多種不同的資料來源。RDF資料可以XML和JSON儲存。RDF建議使用URLs當作識別方式，提供一種方便的方式可直接相互連結於網頁上現存的[open data](/glossary/zh_TW/terms/open-data/) 草案。RDF目前使用還不廣泛，但已逐漸開始隨著開放政府草案有變多的趨勢，像是英國和西班牙政府的「連結開放資料計劃」。還有全球資訊網的發明者，Tim Berners-Lee，最近也提出了一個五星等級方案，內容包含將連結的RDF資料成為開放資料草案追求的目標。

### 試算表

許多政府機關都會使用試算表來記錄他們的資訊，例如 Microsoft 的 Excel。只要將各欄位所代表的內容做個說明，這些資料常常就能馬上開放和使用。

然而，許多請況下會有巨集和方程式存在試算表中，造成處理上的困難。因此我們建議把算式紀錄在試算表旁，這樣對使用者來說也較好讀。

### CSV 逗點分隔檔案

CSV 是一種非常有用的檔案格式，因為它非常的輕巧，所以很適合用來傳送大量相同結構的資料。但是由於這樣的格式太專一性，要去推測不同欄位之間的特性是非常困難。所以假使沒有標明使用規範，很難去使用這些資料。因此對於這類逗號分隔的檔案格式來說，個別使用規範的正確性是相當的重要。

遵循檔案的結構非常重要，因為省略一個欄位會干擾讀取其他檔案中的資料，並且無從修正，因為它並不能判別剩下的資料要怎麼詮釋。

### 文書文件

Classic documents in formats like Word, ODF, OOXML, or PDF may be sufficient to show certain kinds of data - for example, relatively stable mailing lists or equivalent. It may be cheap to exhibit in, as often it is the format the data is born in. The format gives no support to keep the structure consistent, which often means that it is difficult to enter data by automated means. Be sure to use templates as the basis of documents that will display data for re-use, so it is at least possible to pull information out of documents.

It can also support the further use of data to use typography markup as much as possible so that it becomes easier for a machine to distinguish headings (any type specified) from the content and so on. Generally it is recommended not to exhibit in word processing format, if data exists in a different format.

### 純文字檔

純文字檔(.txt)也是一種電腦可以輕易讀取的檔案類型，然而它常常排除了結構後設資料，也就是說，程式撰寫者必須自己建立語法分析器，以便解譯不同的檔案。

在不同的作業系統上轉換純文字檔時，可能會遇到一些問題。MS Windows、Mac OS X和其他的Unix介面都有自己的一套方式告訴電腦他們的限制在哪。

### 掃描圖檔

Probably the least suitable form for most data, but both TIFF and JPEG-2000 can at least mark them with documentation of what is in the picture - right up to mark up an image of a document with full text content of the document. It may be relevant to their displaying data as images whose data are not born electronically - an obvious example is the old church records and other archival material - and a picture is better than nothing.

### 轉有格式

一些比較專業的系統，會有它們自己的檔案格式提供儲存或是匯出。有時以這種格式公開還算可行，特別當我們預期這些檔案之後會用類似的系統處理。這時應該要提供關於該專屬格式的詳細資訊，像是提供軟體商的網頁連結。但一般來說，我們還是建議以非專有格式來顯示資料比較恰當。

### HTML

現今許多資料都以HTML格式儲存與不同的網站。如果資料本身穩定且有限定的規模，這種方式是足夠的。雖然在許多狀況下，將資料以容易下載與操作的型態儲存可能比較好，但因為放在網頁上的作法既便宜又容易查詢，所以還算是展示資料時的一個好出發點。

一般來說如果要保存資料，於HTML中使用表格是最合適的方法，然後以不同的資料欄位來呈現並給予識別碼，這樣對於資料的查詢與處理將更為便利。雅虎發展一套工具([http://developer.yahoo.com/yql/)可以擷取網站的結構資訊，而這種工具對那些標示詳細的資料可做的事更多。](http://developer.yahoo.com/yql/)可以擷取網站的結構資訊，而這種工具對那些標示詳細的資料可做的事更多。)

## 開放檔案格式

就算資訊是詳細的透過電子、機器可讀的格式提供出來，但是在檔案本身的格式上面可能還是會遇到一些問題。

The formats in which information is published – in other words, the digital base in which the information is stored - can either be “open” or “closed”. An open format is one where the specifications for the software are available to anyone, free of charge, so that anyone can use these specifications in their own software without any limitations on re-use imposed by intellectual property rights.

If a file format is “closed”, this may be either because the file format is proprietary and the specification is not publicly available, or because the file format is proprietary and even though the specification has been made public, re-use is limited. If information is released in a closed file format, this can cause significant obstacles to reusing the information encoded in it, forcing those who wish to use the information to buy the necessary software.

開放文件格式的好處在於他們讓開發者能夠利用這些格式開發多類型的套裝軟體與服務。如此一來，就能夠減少資料重複使用上的困難。

使用封閉規格的私有檔案格式，可能會造成對第三方軟體或檔案格式授權持有者的依賴。最糟糕的情形下，這可能代表著我們的資訊需要特定的軟體才能讀取，這些軟體不是過份地昂貴，就是可能會過期，不再支援。

因此從{term:open government data}的觀點來看，我們比較偏好使用\**機器可讀的開放檔案格式*\*來釋出資訊。

### 例如英國的交通運輸數據

Andrew Nicolson 是一個軟體工程師，他參與了 (並且成功) 一個抵制新路拓建工程的活動，該工程位於英國 Westbury 鎮東方。Andrew 想要存取並使用當地交通資料作為抵擋該工程提案的依據。他試圖透過資訊自由法取得相關的資料，但當地政府所提供的資料是專屬私有格式，只能透過一家軟體公司所販賣的軟體讀取。該公司名稱為「土星」，主要提供模擬交通模型與預測服務。他們並沒有供應「純讀取」版軟體，所以 Andrew 的團隊只能花錢購買教育版授權，約 500 英鎊 (600 歐元)。而這套軟體的主體部份於 2010 年 4 月的價格從一萬 3 千英鎊起跳(超過一萬 5 千歐元)，這個價格遠超過一般市民的負擔能力。

雖然沒有一個資訊自由法給予人民以開放格式存取的權力，但開放政府資料草案開始規定資訊釋出時必須提供開放檔案格式。 歐巴馬政府建立了一個黃金準則，在2009年十月時他的開放政府指令提到：

> *為了擴展實用性與合理的限制，政府機關應以開放格式將資訊公開於網路上，透過使用網路搜尋程式，這些資訊可以被擷取、下載、索引和搜尋。開放格式具有跨平台、機器可讀的特性，並且不會限制大眾對於該資訊的再使用權利。*

## 我要如何使用既有的格式？

當政府必須公開新資料，而這些資料之前又沒有公開過。這時我們選擇格式要試著在花費和達到目的之間取得平衡。每種格式都有需注意的地方，而本節會將針對這些解釋。

本部份只針對如何適當地將資料表層去除，讓機器可直接存取。至於如何設計網站和網路解決方案的建議與引導，這些可以在其他地方找到。

### 網路服務

對於更改頻繁，而且每次處理都有一定容量限制的資料，非常適合使用Web服務公開資料。有許多方式可以提供Web服務，其中比較常用到的是SOAP和REST。一般來說，SOAP over REST或REST服務非常容易開發與使用，因此成為廣泛使用的標準。

### 資料庫

如同Web服務，資料庫提供對資料的動態直接存取，並且可以讓使用者將其感興趣的資料擷取並集中在一起。

There are some security concerns about allowing remote database extraction and database access is only useful if the structure of the database and the importance of individual tables and fields are well documented. Often, it is relatively simple and inexpensive to create web services that expose data from a database, which can be an easy way to address safety concerns.