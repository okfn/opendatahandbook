---
redirect_from: /en/appendices/index.html
section: guide
lang: pt_PT
title: Formatos de ficheiros
---

## Uma visualização geral dos formatos de ficheiros

### JSON

JSON é um formato de ficheiro simples, muito fácil de ler para qualquer linguagem de programação. A sua simplicidade implica que é, geralmente, mais facilmente processado por computadores do que outros, como o formato XML.

### XML

XML é um formato amplamente utilizado para troca de dados, porque permite manter a estrutura e forma dos dados, e permite que os programadores escrevam parte da documentação com os dados sem interferir com a sua leitura.

### RDF

Um formato recomendado pela W3C, denominado RDF, torna possível representar os dados numa forma que torna mais fácil a combinação de dados de múltiplas fontes. Os dados RDF podem ser guardados em XML e JSON, entre outros. O RDF encoraja a utilização de URL como identificadores, o que fornece uma forma conveniente de interligar iniciativas de [dados abertos](/glossary/en/terms/open-data/) existentes na web. O uso de RDF ainda não é muito amplo, mas tem aumentado nas Iniciativas de Governação Aberta, incluindo os projetos de Dados Interligados dos Governos Espanhol e Britânico. O inventor da web, Tim Berners-Lee, propôs recentemente um esquema [cinco estrelas](http://lab.linkeddata.deri.ie/2010/star-scheme-by-example/) que inclui dados interligados em RDF como um objetivo a atingir pelas iniciativas de dados abertos.

### Folhas de cálculo

Muitas autoridades têm informação em folhas de cálculo, por exemplo Microsoft Excel. Estes dados podem, frequentemente, ser utilizados imediatamente, com as descrições apropriadas do significado das diferentes colunas.

No entanto, em alguns casos, podem existir macros e fórmulas nas folhas de cálculo, o que pode tornar a gestão difícil. É, por isso, aconselhável documentar todos os cálculos desse género junto à folha de cálculo, uma vez que torna a leitura mais acessível aos utilizadores.

### Ficheiros separados por vírgula

Os ficheiros CSV podem ser um formato muito útil, porque é um formato compacto e, por isso, adequado para a transferência de grandes conjuntos de dados com a mesma estrutura. Contudo, os dados são, muitas das vezes, inúteis sem documentação, já que pode ser quase impossível adivinhar o significado de cada uma das colunas. Por isso, é particularmente importante que, nos formatos CSV, a documentação dos campos individuais seja precisa.

Além disso, é essencial que a estrutura do ficheiro seja respeitada, uma vez que uma única omissão de um campo pode perturbar a leitura de todos os outros dados no ficheiro, sem oportunidade de correção, já que não é possível determinar como é que os dados restantes devem ser lidos.

### Documento de texto

Os documentos clássicos em formatos como Word, ODF, OOXML ou PDF podem ser suficientes para mostrarem alguns tipos de dados - por exemplo, listas de correio estáveis e relativamente pequenas. Exibir dados nesses formatos é barato, já que são, frequentemente, os formatos de origem dos dados. O formato não garante a manutenção da estrutura, o que significa, com frequência, que é difícil inserir dados automaticamente. Certifique-se de que utiliza modelos como base dos documentos que vão exibir dados para reutilização, para que seja, pelo menos, possível retirar informação dos documentos.

A posterior utilização de dados pode ser favorecida pela utilização de tipos de letra, de tal modo que se torne fácil para uma máquina a distinção entre cabeçalhos do conteúdo (e assim sucessivamente). Geralmente, recomenda-se a não exibição de dados num formato de documento de texto quando os dados existem também num formato diferente.

### Texto simples

Os documentos de texto simples (.txt) são facilmente legíveis pelos computadores. Geralmente, excluem metadados estruturais do documento, o que significa que os programadores deverão criar um analisador que possa interpretar o documento.

Transferir ficheiros de texto entre diferentes sistemas operativos pode causar alguns problemas. O MS Windows, Mac OS X e outras variantes Unix têm as suas formas próprias de dizer ao computador que chegaram ao fim de uma linha.

### Imagem digitalizada

Provavelmente o menos adequado para a maior parte dos dados, mas quer os ficheiros TIFF quer os ficheiros JPEG-2000 pode, pelo menos, ser documentados com informação do que está na imagem. Pode ser relevante exibir como imagem dados que não tenham sido gerados eletronicamente - um exemplo óbvio são os registos de antigas igrejas e outro material de arquivo - e uma imagem é sempre melhor do que nada.

### Formatos proprietários

Alguns sistemas dedicados têm os seus próprios formatos de ficheiros, em que podem gravar ou exportar dados. Por vezes, pode ser suficiente partilhar os dados nesse formato - em especial, se se esperar que os dados sejam lidos num sistema semelhante ao de origem. Deve indicar-se onde se pode encontrar informação sobre o formato proprietário, por exemplo, através de uma hiperligação para o sítio web do fornecedor. Geralmente, recomenda-se a exibição dos dados em formatos não proprietários sempre que possível.

### HTML

Hoje em dia, muitos dados estão disponíveis em HTML em vários sítios web. Isto pode ser suficiente se os dados forem muito estáveis e de âmbito limitado. Em alguns casos, pode ser preferível ter os dados numa forma mais fácil de descarregar e manipular, mas, uma vez que referenciar uma página num sítio web é fácil e barato, pode ser um bom ponto de partida para exibição de dados.

Tipicamente, seria mais apropriado usar tabelas em documentos HTML para manter os dados, e é também importante que os diferentes campos de dados sejam exibidos e tenham ID que facilitem a sua procura e manipulação. A Yahoo desenvolveu uma ferramenta (<http://developer.yahoo.com/yql/>) que consegue extrair informação estruturada de um sítio web, e estas ferramentas podem fazer ainda mais com os dados, quando estes são corretamente identificados.

## Formatos de ficheiros abertos

Mesmo que a informação esteja disponível em detalhe, num formato eletrónico e mecanicamente legível, pode haver problemas relacionados com o próprio formato do ficheiro.

Os formatos em que a informação é publicada - ou seja, a base digital de armazenamento da informação - podem ser "abertos" ou "fechados". Um formato aberto é um formato em que as especificações para o programa estão disponível para qualquer pessoa, gratuitamente, de tal modo que qualquer um pode usar essas especificações no seu próprio programa sem qualquer limitação de reutilização imposta por direitos de propriedade intelectual.

Se um formato de ficheiro for "fechado", isto pode acontecer por o formato do ficheiro ser proprietário e a especificação não estar disponível publicamente, ou por o formato do ficheiro ser proprietário e, embora a especificação tenha sido tornada pública, a reutilização é limitada. Se a informação for publicada num formato de ficheiro fechado, isto pode criar grandes obstáculos à reutilização da informação codificada nele, forçando aqueles que desejam utilizar a informação a comprarem o programa necessário.

O benefício dos ficheiros de formato aberto é que permitem aos programadores a produção de vários pacotes de programas e serviços utilizando esses formatos. Isto minimiza os obstáculos à reutilização da informação aí contida.

A utilização de formatos de ficheiros proprietários para os quais não há especificação publicamente disponível pode criar uma dependência em programas de terceiros. No pior dos casos, isto pode significar que a informação só pode ser lida utilizando certos programas, o que pode ser proibitivo devido ao custo, ou pode tornar-se obsoleto.

A preferência, na perspetiva dos dados de [governação aberta](/glossary/en/terms/open-government/), é pela publicação da informação em **formatos de ficheiro abertos mecanicamente legíveis.**

### Exemplo: dados de tráfego do RU

Andrew Nicolson é um programador de software que esteve envolvido numa campanha (de sucesso) contra a construção de uma nova estrada, a Westbury Eastern bypass, no Reino Unido. O Andrew estava interessado em aceder e utilizar os dados de tráfego da estrada que estavam a ser utilizados para justificar a proposta. Conseguiu obter alguns dos dados relevantes através de requerimentos de liberdade de informação, mas o governo local forneceu os dados num formato que apenas podia ser lido utilizando um programada de uma empresa chamada Saturn, que se especializava em modelação e previsão de tráfego. Não existia nenhuma uma versão de "leitura apenas" do programa, pelo que o grupo de Andrew não teve outra opção senão comprar uma licença para o programa, pagando £500 (€600) ao fazer uso de um desconto para educação. Os preços dos principais pacotes listados na Saturn em abril de 2010 começavam em £13,000 (mais de €15,000), um preço proibitivo para a maior parte dos cidadãos.

Embora nenhuma lei de acesso a informação conferisse o direito de aceder a informação em formatos abertos, os dados das iniciativas de governação aberta começam a ser acompanhados por documentos que estipulam que a informação oficial deve ser disponibilizada em formatos abertos. A administração de Obama definiu o "gold standard", com a Diretiva de Governação Aberta publicada em dezembro de 2009, que diz:

> *Na medida do possível, e sujeito a restrições válidas, as agências devem publicar a informação online num formato aberto que possa ser obtido, descarregado, indexado e pesquisado por aplicações de pesquisa web comuns. Um formato aberto é um formato tal que seja independente de plataformas, mecanicamente legível, e tornado disponível ao público sem restrições que impeçam a reutilização dessa informação.*

## Como utilizo um formato específico?

Quando uma autoridade publicar novos dados - que ainda não estivessem disponíveis - deve procurar escolher um formato que forneça a melhor relação custo-adequação para o propósito. Para cada formato, há algumas coisas que é importante conhecer, e esta secção espera explicá-las.

Esta secção concentra-se apenas em interoperabilidade de modo a facilitar o acesso direto a partir da máquina. Poderá encontrar conselhos e instruções sobre a construção de sítios e soluções web noutros locais.

### Serviços web

Para dados que mudem frequentemente, e em que o descarregamento tem um tamanho limitado, é muito importante publicar os dados através de serviços web. Há várias formas de criar um serviço web, mas alguns dos mais utilizados são o SOAP e o REST. Geralmente, prefere-se o SOAP ao REST, mas os serviços REST são muito fáceis de desenvolver e utilizar, pelo que são um padrão muito utilizado.

### Base de dados

Tal como os serviços web, as bases de dados podem fornecer acesso aos dados dinamicamente. As bases de dados têm a vantagem de permitirem aos utilizadores extraírem apenas aquilo em que estão interessados.

Há algumas preocupações de segurança quando se permite a extração remota de bases de dados. Além disso, o acesso a bases de dados só é útil se a estrutura da base de dados e a importância de cada tabela e campo estiverem bem documentadas. Frequentemente, é relativamente simples e barato criar serviços web que expõem os dados de uma base de dados de dados, o que pode ser uma maneira fácil de tratar as preocupações de segurança.
