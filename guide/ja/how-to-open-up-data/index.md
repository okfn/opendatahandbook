---
redirect_from: /ja/how-to-open-up-data/index.html
section: guide
lang: ja
title: データをオープンにするには
---

このセクションがこのハンドブックの肝となるところだ。データを持っている人はそれをどうやってオープンにすればいいのか、具体的な方法を詳しく説明する。基本的なところを解説していくが、陥りがちな罠についても紹介する。最後に、考えうるもっと細かい問題について取り上げる。

データをオープンにするにあたっては、これらのルールに従うことをおすすめする。

-   **シンプルに保つ。** ちいさいところからシンプルに始め、素早く進める。すべてのデータセットを今この場ですぐにオープンにする必要はない。とりあえずまずはひとつのデータセットだけとか、あるいは大きなデータセットの一部だけをオープンにするというところから始めるのでもかまわない。 -- もちろん、より多くのデータセットをオープンにできたほうがよいのだが。

> これはイノベーションなんだ。動き出すのが早ければ早いほどいい。そのほうが勢いをつけやすいし、実際にやってみて初めて気づくことだってある。 -- イノベーションが成功するか失敗するかは五分五分だし、すべてのデータセットが有用だとは限らない。

-   **早めに巻き込み、頻繁にかかわらせる。** 実際にデータを使ったり使う可能性があったりする人たちを早めに巻き込んでいこう。一般市民だったり企業だったり、開発者だったりするだろう。そうすれば、あなたのサービスはあるべき姿により近づいていく。

> 心しておきたいのは、データの大半は最終的なユーザーに直接届くわけではないということだ。たいていは「情報メディア」を経由して届くことになる。データを受け取り、それを変換したりリミックスしたりして見せ方を変える人たちがいるのだ。たとえば、GPSの座標の大規模なデータベースを直接読みたいという人はほとんどいない。私たちが欲しいのは、そんなものではなく地図だ。というわけで、まずは情報メディアを巻き込もう。彼らがデータを活用し、目的にあわせて形を変えてくれる。

-   **ありがちな不安や誤解に対応する。** これが特に重要になるのは、たとえば政府のような大規模な機関で働いている場合だ。データをオープンにするや否や、大量の問い合わせや不安がる声を受けることになる。このとき大切なことは、鍵を握る人物がだれかを見極めて、できるだけ早い段階から彼らに対応するということだ。

データをオープンにする手順は、大きく分けると四段階になる。それぞれについて、以下で詳しく説明する。並び順はあくまでも大まかなものであり、これらの手順の多くは同時進行で進めることもできる。

1.  **データセットを選ぶ。** - オープンにしようとしているデータセットを選ぶ。今後もし何か問題が起こったら、いつでもこの段階まで戻れる(というか、戻らざるを得なくなる)ことを覚えておこう。
2.  **オープンなライセンスを適用する。**
    1.  そのデータにどんな知的財産権が存在するかを確かめる。

> 2.  適切な「オープン」ライセンスを選んですべての知財をライセンスし、先ほど「オープンデータとは何か」で議論したオープン性の定義に対応する。
> 3.  注意: もしこれが不可能なら、ステップ1に戻って別のデータセットを試してみよう。

3.  **データを公開する。** - 有用なフォーマットで、まとめて公開する。別の方法での公開、たとえばAPI経由で使えるようにするなどの方法を検討してもかまわない。
4.  **データを発見してもらう。** - ウェブに投稿したり中央カタログをまとめたりして、オープンデータセットを発見してもらえるようにする。

## データセットを選ぶ

オープンにしたいデータセットを選ぶのが第一段階だ。とはいえ、データをオープンにする手順はイテレーティブなものであり、後の段階で問題が発生したらいつでもここまで戻ってこられることを覚えておこう。

もしオープンにしたいデータセットが既にはっきりしているのなら、そのまま次のセクションまで進もう。しかしたいていの場合は、特に大規模な組織内においては、どのデータセットに注目するかを決めるのは難しい。そんな場合はどうすればいいのだろうか?

このリストが、どのデータセットをオープンにできるかを特定するための最初の一歩となるだろう。この後の段階で、個々のデータセットが適切かどうかをより詳しくチェックするときがくる。

There is **no requirement** to create a comprehensive list of your datasets. The main point to bear in mind is whether it is feasible to publish this data at all (whether openly or otherwise) - see [this previous section](../what-is-open-data/).

### コミュニティに尋ねる

まずはじめに、コミュニティに聞いてみることをおすすめする。コミュニティとは、実際にそのデータにアクセスしたりデータを使ったりしている人のことである。彼らはきっと、どのデータに価値があるかをよく知っているだろう。

1.  Prepare a short list of potential datasets that you would like feedback on. It is not essential that this list concurs with your expectations, the main intention is to get a feel for the demand. This could be based on other countries' [open data](/glossary/ja/terms/open-data/) catalogs.
2.  提案文書を作成する。
3.  提案文書をウェブページに公開する。その提案を指す一意なURLを用意し、直接アクセスできるようにしておこう。そうすればソーシャルメディアでの共有がしやすくなり、提案が発見されやすくなる。
4.  簡単に意見を表明できる方法を提供する。登録をしないと意見を投稿できないなどということはやめよう。そんなことをすれば、反応が少なくなってしまう。
5.  関連するメーリングリストやフォーラムなどに提案文書の情報を拡散させ、文書のあるウェブページの場所を広める。
6.  打ち合わせの場を設ける。平均的な会社員、データを扱う人、そして役人などが参加しやすいような日時で開催すること。
7.  あなたの所属機関の立場を代弁してもらうよう、政治家に依頼する。オープンデータは、政府の情報にアクセスしやすくする政策の一部となるだろう。

### コストについて

政府機関が自ら保持するデータの収集や保守にかける費用は、どの程度になるだろう?もし特定のデータセットに対して多くの費用をつぎ込んでいるのなら、それはきっと他の人たちも利用したくなるものだろう。

この主張は、ただ乗りしようとする人たちを考慮せずには行えない。きっと「こんなに金をかけて集めた情報を、どうして無料で開放してやる必要があるんだ?」という問いが出てくるはずで、それに答えられなければならない。その答えは、特定の役割を果たす公営企業にコストを吸収させるということだ。いったん収集したデータを第三者に送信するためのコストは、事実上ゼロに等しい。したがって、それに対して課金すべきではない。

### 公開の容易性

どのデータに価値があるのかを判断するよりも、むしろ一般公開しやすいのはどのデータなのかという基準で考えたほうがよいこともある。公開しやすい小さなデータを公開することで、その組織の行動を変えさせるきっかけにすることができる。

しかし、この方式を使うときは注意を要する。そういった小さなデータを公開してもその効果がほとんど目に見えず、結局何も変わらないままということもあり得る。もしそうなったら、組織内での信頼も落ちてしまう。

### 周りを見渡す

オープンデータは今も成長段階のムーブメントだ。あなたのまわりには、他の分野での動きに詳しい人もきっと多いだろう。他の機関がやっていることを元にしてデータをリストアップするといい。

## オープンなライセンスを適用する(法的にオープンにする)

多くの司法機関ではデータに対する知的財産権が存在し、第三者によるデータの利用や再利用そして再配布などには明示的な許可を要する。知的財産権が存在するかどうかが不確かな場合でも、何らかのライセンスを適用して明確にしておくことが大切だ。したがって、 **データを公開するつもりなら、それに何らかのライセンスを適用しなければならない。** データを [open](http://opendefinition.org/) にするつもりなら、さらにそれが重要となる。

では、いったいどんなライセンスが使えるのだろう? 'オープン' データに適用するライセンスとしておすすめするのは、 [Open Definition](open_) に準拠したライセンスの中でデータに適しているとされているものだ。その一覧(および利用方法)は、ここで見ることができる。

-   <http://opendefinition.org/licenses/>

オープンデータにライセンスを適用する際の簡単な手引きがOpen Data Commonsのサイトで公開されている。

-   <http://opendatacommons.org/guide/>

## データを公開する(技術的にオープンにする)

{term:オープンデータ} というからには、法的にオープンにするだけではなく技術的にもオープンにしなければならない。特に大切なのは、データをまとめて公開する際に {term:機械可読} 形式にしておくことだ。

**Available**

データを公開するにあたって、複製するための実費を超える値段をつけてはいけない。インターネットから無料でダウンロードできるようにするのがおすすめだ。この価格体系を実現できる理由は、データを提供するにあたってその組織がよけいなコストをかけるべきではないからだ。

**In bulk**

データは完全なセットとして公開しなければならない。法の下で収集された記録を持っているのなら、その一部ではなく全体をダウンロードできるようにする必要がある。Web APIなどのサービスも便利ではあるが、一括アクセスの代替にはならない。

**In an open, machine-readable format**

Re-use of data held by the public sector should not be subject to patent restrictions. More importantly, making sure that you are providing machine-readable formats allows for greatest re-use. To illustrate this, consider statistics published as PDF (Portable Document 
Format) documents, often used for high quality printing. While these statistics can be read by humans, they are very hard for a computer to use. This greatly limits the ability for others to re-use that data.

次の原則に従えば、多大な恩恵を受けられる。

-   シンプルに保つ
-   すばやく動く
-   実利的であることを心がける

具体的には、生のデータを今この時点で公開するほうが、きちんとまとめたものを半年後に公開するよりもよいということだ。

データを他の人たちに公開するには、さまざまな方法がある。インターネット世代の人たちにとっていちばん自然なのは、オンラインで公開することだ。この方式にも様々なバリエーションがある。最も基本的なやり方は、その組織自身のウェブサイトからデータを取得できるようにし、中央カタログから直接その場所を指すようにするという方法だ。しかし、それ以外にも方法はある。

{term:接続性} に制限があったりデータのサイズがあまりにも大きかったりする場合には、他のフォーマットでの配布もあり得る。このセクションではそういった代替手段についても扱う。これらは価格を低く抑えるために使える。

### オンラインでの公開

#### 既存のウェブサイト経由で

ウェブコンテンツチームにとって一番なじみのある方式は、ファイルをウェブページからダウンロードできるようにすることだろう。いつも会議の議事録を公開しているのと同じように、データファイルもまったく同じ方式で公開すればよい。

この方式の問題のひとつは、情報がどこにアップロードされたのかを外部の人が探しにくいということだ。また、公開されたデータを利用するツールを作る人たちにかかる負担も多くなる。

#### 第三者のサイト経由で

さまざまな分野で、データのハブとなるリポジトリが多数存在する。たとえばpachube.comは、測定機器とその測定値にアクセスしたい人たちとをつなげるために作られている。また、Infochimps.comやTalis.comといったサイトは、公共機関が大量のデータを保管して自由に使えるようにしている。

第三者のサイトは非常に有用に使える。その主な理由は、特定の分野に興味のある人たちや同じ分野の他のデータセットが既にそこに集まっているからである。こういったプラットフォームにデータを追加すれば、相乗効果によってよりよい結果を得られる。

大規模データプラットフォームは、既に要件を満たす基盤を提供している。多くの場合、統計情報や利用状況なども得られる。公的機関の場合は、無料で使えることが一般的だ。

これらのプラットフォームには二種類のコストがかかる。まずは独立性。自分の組織のデータを他社に委ねてしまうことになる。たいていの場合、政治的・法的・あるいは運営上の理由でそれは難しい。もうひとつのコストはオープン性だ。データを預けたプラットフォームに対して誰がアクセスできるかは把握できないということを認識する必要がある。ソフトウェア開発者や科学者たちが使うOSは幅広く、スマートフォンの場合もあればスーパーコンピューターの場合もある。どんな環境からでもデータにアクセスできなければならない。

#### FTPサーバーから

最近ではあまりはやらなくなったが、File Transfer Protocol (FTP)を使ってファイルにアクセスさせる方式もある。この方式が適しているのは、ソフトウェア開発者や科学者などの技術分野を相手にする場合だ。FTPはHTTPのかわりに使うことができ、ファイルの転送に特化して設計されている。

FTPにはかつてほどの人気はなくなった。ウェブサイトを提供するのに比べると、FTPサーバーを扱うというのはコンピューター上のフォルダを扱うのに似ている。したがって、たとえそれが目的にかなっていたとしても、そのカスタマイズを請け負えるウェブ開発会社はあまりいないだろう。

#### torrentで

[BitTorrent](/glossary/ja/terms/bittorrent/) は、政府の人間にはおなじみになりつつあるシステムだろう。というのも、著作権違反に関連して語られることが多くなったからである。BitTorrentは、torrentsというファイルを利用するシステムであり、ファイルにアクセスしようとする人たちにコストを分散させる仕組みがある。サーバーにだけ負荷をかけるのではなく、需要が増加するのにあわせて供給も増やすようにしている。だからこそ、このシステムは動画の共有の世界で成功したのだ。大規模なデータを配布するためのシステムとして、これは非常に効率的なものだ。

#### APIとして

データの公開を [Application Programming Interface](/glossary/ja/terms/application-programming-interface/) (API)で行うこともできる。この方式は、近年はやりつつある。すべてのデータを巨大なファイルで一括提供するのではなく、プログラマー側で特定の箇所を選んで取得できるようにする仕組みだ。APIは一般的にデータベースにつながっており、データはリアルタイムに更新される。つまり、情報をAPI経由で公開しておけばそれが常に最新であることを保証できるというわけだ。

すべてのデータに対する主導権を握るには、一括で公開することをまず考えなければならない。APIとして提供すれば、次のようなコストが発生する。

1.  金額。ファイルで提供することに比べて、その仕組みを開発したり保守したりするための資金を要する。
2.  期待。そのシステムの利用者のコミュニティを育てるには、APIを確実に提供することが重要だ。何か問題が発生すれば、それは自分たちが修正しなければならない。

データへの一括アクセスを提供すれば、次のようなことを保証できる。

-   データの提供者の事情に依存しない。つまり、仮に組織の編成や予算などの状況が変わったとしても、データはそのまま使える。
-   誰でも複製して再配布できる。これによって元の所有者が各所に配布するコストを削減でき、単一障害点がなくなる。
-   そのデータを使って第三者が自分でサービスを開発できる。データが手元から離れないことを確信できるからだ。

データを一括で提供すれば、他の人たちが本来の目的を超えてデータを活用できるようになる。たとえば別のフォーマットに変換したり他のリソースとリンクさせたり、バージョン管理して複数の場所でアーカイブしたりといった具合だ。最新版のデータがAPI経由で取得できるようにしたとしても、生のデータも定期的に一括公開しておくべきだ。

For example, the [Eurostat statistical service](http://epp.eurostat.ec.europa.eu/) has a bulk download facility offering over 4000 data files. It is updated twice a day, offers data in [Tab-separated values](/glossary/ja/terms/tab-separated-values/) (TSV) format, and includes documentation about the download facility as well as about the data files.

Another example is the [District of Columbia Data Catalog](http://octo.dc.gov/DC/OCTO/), which allows data to be downloaded in CSV and XLS format in addition to live feeds of the data.

## データを発見してもらう

{term:オープンデータ} は、ユーザーなしでは存在し得ない。他の人たちがそのデータを発見できるようにする必要がある。このセクションでは、そのための様々な手法を取り上げる。

最も大切なことは、中立な場所で公開することだ。そうすれば、組織内の勢力争いや予算の都合などに振り回されずに済む。司法の管轄をまたがった協力は難しいことだろう。しかし、うまく協力すればかなりの恩恵を受けられる。他の人たちがデータを発見しやすくなればなるほど、新しい便利なツールが早く作られるようになる。

### 既存のツール

さまざまなツールがウェブ上に存在する。データを発見されやすくすることに特化したものである。

One of the most prominent is the [DataHub](https://datahub.ckan.io/) and is a catalog and data store for datasets from around the world. The site makes it easy for individuals and organizations to publish material and for data users to find material they need.

さらに、さまざまな機関や場所に特化したカタログも数多く存在する。科学者のコミュニティの多くは個々の分野のカタログシステムを構築しており、公開用のデータを求めている。

### 政府の皆さんへ

ここまでで明らかになったとおり、正統な方法はその機関自身に政府のデータを扱うカタログを作らせることだ。カタログを構築する際には、各部署が自分の情報を最新に保ちやすいような仕組みを作るようにしよう。

Resist the urge to build the software to support the catalog from scratch. There are free and open source software solutions (such as [CKAN](http://ckan.org/)) which have been adopted by many governments already. As such, investing in another platform may not be needed.

多くのオープンデータカタログが見落としている点をいくつか取り上げる。プログラムを作る場合にはこれらを検討しよう。

-   Providing an avenue to allow the private and community sectors to add their data. It may be worthwhile to think of the catalog as the region's catalog, rather than the regional government's.
-   Facilitating improvement of the data by allowing derivatives of datasets to be cataloged. For example, someone may geocode addresses and may wish to share those results with everybody. If you only allow single versions of datasets, these improvements remain hidden.
-   Be tolerant of your data appearing elsewhere. That is, content is likely to be duplicated to communities of interest. If you have river level monitoring data available, then your data may appear in a catalog for hydrologists.
-   Ensure that access is equitable. Try to avoid creating a privileged level of access for officials or tenured researchers as this will undermine community participation and engagement.

### 市民の皆さんへ

Be willing to create a supplementary catalog for non-official data.

It is very rare for governments to associate with unofficial or non-authoritative sources. Officials have often gone to great expense to ensure that there will not be political embarrassment or other harm caused from misuse or overreliance on data.

Moreover, governments are unlikely to be willing to support activities that mesh their information with information from businesses. Governments are rightfully skeptical of profit motives. Therefore, an independent catalog for community groups, businesses and others may be warranted.
