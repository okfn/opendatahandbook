---
redirect_from: /pt_BR/appendices/index.html
section: guide
lang: pt_BR
title: Formatos de Arquivo
---

## Uma Visão Geral sobre os Formatos de Arquivos

### JSON

JSON é um formato de arquivos simples que é muito fácil de ler em qualquer linguagem de programação. Sua simplicidade significa que é geralmente mais fácil de ler para computadores que outros formatos, tais como XML.

### XML

XML é um formato amplamente utilizado para intercâmbio de dados porque proporciona boas oportunidades para guardar a estrutura nos dados e na maneira pela qual os arquivos são construídos, além de permitir que desenvolvedores escrevam parte da documentação juntamente com os dados sem interferir na sua leitura.

### RDF

Um formato chamado RDF, recomendado pelo W3C, torna possível representar dados numa forma mais fácil para combinar informações de múltiplas fontes. Dados RDF podem ser armazenados em XML e JSON, além de outras serializações. RDF encoraja o uso de URLs como identificadores, o que fornece uma maneira conveniente de interconectar diretamente iniciativas de {term:dados abertos} na Web. O RDF ainda não é muito difundido, mas tem sido uma tendência entre iniciativas de Governo Aberto, incluindo os projetos de Dados Abertos Governamentais Ligados britânicos e espanhóis. O inventor da Web, Tim Berners-Lee, recentemente propôs um esquema de cinco estrelas\_ que inclui dados em RDF como uma meta a ser visada por iniciativas de dados abertos.

### Planilhas

Muitos órgãos públicos têm informações armazenadas em planilhas, por exemplo Microsoft Excel. Esses dados podem ser usados imediatamente com as descrições corretas do que as diferentes colunas significam.

Entretanto, em alguns casos podem haver macros e fórmulas em planilhas, que podem ser algo complicado de se lidar. É, portanto, aconselhável documentar tais cálculos próximo à planilha, já que ela é geralmente mais acessível à leitura por quem vai usá-la.

### Arquivos Separados por Vírgula(CSV)

O formato de arquivo CSV pode ser muito útil . É compacto e, portanto, adequado para transferir grandes conjuntos de dados com a mesma estrutura. Entretanto, o formato é tão espartano que os dados são, muitas vezes, inúteis sem uma documentação, já que pode ser quase impossível adivinhar o significado das diferentes colunas. É, portanto, particularmente importante para os arquivos CSV que a documentação de cada campo seja precisa.

Ademais, é essencial que a estrutura do arquivo seja respeitada, já que a simples omissão de um campo pode perturbar a leitura de todos os dados remanescentes no arquivo, sem que haja uma real oportunidade de retificá-los, pois não se pode determinar como o restante dos dados podem ser interpretados.

### Documento de Texto

Documentos clássicos em formatos tais como Word, ODF, OOXML ou PDF podem ser suficientes para mostrar certos tipos de dados - por exemplo, listas de e-mail relativamente simples ou algo equivalente. Pode ser barato exibi-los assim, pois é frequentemente o formato em que os dados nasceram. O formato não dá suporte a manter a estrutura consistente, o que muitas vezes significa que é difícil entrar com os dados por meios automatizados. Certifique-se de usar modelos como a base de documentos que mostrarão dados para o reúso, para que pelo menos seja possível tirar a informação dos documentos.

Ele também pode suportar o uso adicional de dados para usar marcações tipográficas tanto quanto possível, para que se torne mais fácil para uma máquina distinguir títulos (de qualquer tipo especificado) do conteúdo, e daí em diante. Geralmente, recomenda-se não exibir no formato de processadores de texto, se os dados existirem em um formato diferente.

### Texto Puro

Documentos de texto puro (.txt) são muito fáceis de ler para computadores. Eles geralmente excluem metadados estruturais dentro do documento. Mas isso significa que os desenvolvedores precisarão criar um interpretador (em inglês, "parser") para interpretar cada documento na medida em que ele aparece.

Alguns problemas podem ser causados na troca de arquivos de texto puro entre sistemas operacionais. MS Windows, Mac OS X e outras variações de Unix têm as suas próprias maneiras de dizer ao computador que determinado ponto é o final de uma linha.

### Imagem digitalizada

Provavelmente a forma menos adequada para a maioria dos dados, mas ambos TIFF e JPEG-2000 podem, pelo menos, marcá-los com documentação do que está na foto - até mesmo marcar uma imagem de um documento com seu conteúdo de texto completo. Isto pode ser relevante para exibir imagens de dados que não nasceram eletronicamente - um exemplo óbvio são registros antigos de igrejas e outros materiais de arquivo - e uma imagem é melhor que nada.

### Formatos proprietários

Alguns sistemas dedicados, etc., têm seus próprios formatos de dados nos quais podem salvar ou exportar dados. Algumas vezes pode ser suficiente publicar os dados em um formato como esse - especialmente se se esperar que o uso posterior seja feito em um sistema similar àquele de onde vieram. O local onde mais informações sobre esses formatos proprietários podem ser encontradas deve sempre ser indicado, por exemplo fornecendo um link para o website do fornecedor. Geralmente, recomenda-se exibir dados em formatos não-proprietários, onde for possível.

### HTML

Hoje em dia muitos dados estão disponíveis em formato HTML em vários sítios. Isto pode muito bem ser suficiente, se os dados forem muito estáveis e de escopo limitado. Em alguns casos, pode ser preferível ter os dados de uma forma mais fácil para descarregar e manipular, mas como é barato e fácil fazer referência a uma página em um website, esse pode ser um bom ponto de partida para a exibição dos dados.

Normalmente, seria mais apropriado usar tabelas em documentos HTML para guardar os dados, sendo que é importante que os vários campos de dados sejam mostrados e recebam IDs que tornem fácil encontrar e manipular os dados. O Yahoo desenvolveu uma ferramenta (<http://developer.yahoo.com/yql/>) que pode extrair informações estruturadas de um website, e tais ferramentas podem fazer muito mais com os dados se eles estiverem cuidadosamente etiquetados.

## Formatos Abertos de Arquivo

Mesmo se a informação for fornecida em formato eletrônico, legível por máquina, e em detalhes, podem haver problemas relacionados ao formato do arquivo.

Os formatos em que a informação é publicada - em outras palavras, a base digital em que a informação é armazenada - podem ser "abertos" ou "fechados". Em um formato aberto as especificações do software estão disponíveis para qualquer pessoa, livre de cobrança. Isso permite-as usar estas especificações em seus próprios softwares, sem qualquer limitação de reúso imposta por direitos de propriedade intelectual.

Se o formato de um arquivo é "fechado", pode ser porque o formato é proprietário e sua especificação ou não está disponível publicamente, ou até se encontra disponível mas seu reúso é limitado. Se a informação for disponibilizada em um formato de arquivo fechado, pode gerar significativos obstáculos ao reúso, obrigando aqueles que desejam usar esta informação a comprar o software necessário.

O benefício dos formatos abertos de arquivo é que eles permitem aos desenvolvedores produzir múltiplos softwares e serviços que utilizem estes formatos. Isto então minimiza os obstáculos ao reúso da informação que eles contêm.

Usar formatos proprietários de arquivos, para os quais a especificação não está publicamente disponível, pode criar uma dependência em software de terceiros ou em detentores de licença de formatos de arquivo. Nos piores casos, isto pode significar que a informação só pode ser lida usando certos pacotes de software, que podem ser proibitivamente caros, ou que podem se tornar obsoletos.

É preferível, sob a perspectiva dos {term:dados abertos governamentais} que a informação seja disponibilizada em **formatos de arquivo abertos que sejam legíveis por máquinas.**

### Exemplo: dados de tráfego do Reino Unido

Andrew Nicolson é um desenvolvedor de software que esteve envolvido em uma campanha (em última análise, bem-sucedida) contra a construção de uma nova estrada, a passagem Westbury Leste, no Reino Unido. Andrew estava interessado em acessar e usar os dados de tráfego das estradas, usados para justificar as propostas de construção. Ele conseguiu obter alguns dos dados relevantes por meio de pedidos de acesso à informação. Mas o governo local forneceu os dados em um formato proprietário que só pode ser lido usando software produzido por uma empresa chamada Saturn, que se especializa em modelagem e previsão de tráfego. Não é fornecida uma versão do software "somente para leitura", portanto o grupo d Andrew não teve escolha senão comprar uma licença do software, pagando £500 libras (R\$ 1.400) após fazer uso de um desconto educacional. Os pacotes principais de software na lista de preços da Saturn em abril de 2010 começavam com £13.000 libras (mais de R\$ 35.000), um valor que está muito além do alcance da maioria dos cidadãos comuns.

Embora nenhuma lei de acesso à informação dê direito ao acesso à informação em formatos abertos, as iniciativas de dados abertos governamentais estão começando a ser acompanhadas de documentos que estipulam que as informações oficiais devem ser disponibilizadas em formatos de arquivo abertos. O padrão-ouro tem sido definido pela Administração Obama, com a Diretiva de Governo Aberto promulgada em dezembro de 2009, que diz:

> *Até o limite praticável e sujeito a restrições válidas, os órgãos devem publicar as informações online em um formato aberto que possa ser recuperado, descarregado, indexado e pesquisado por ferramentas comumente utilizadas de aplicações de buscas na web. Um formato aberto é independente de plataforma, legível por máquinas e publicado sem restrições que impeçam o reúso da informação.*

## Como posso usar um determinado formato?

Quando um órgão público for publicar novos dados – dados que nunca foram publicados – você deve escolher o formato que oferecer o melhor equilíbrio entre custo e adequação ao propósito. Para cada formato há algumas coisas das quais você deve estar ciente, e esta seção procura explicá-las.

Esta seção se foca somente em como as superfícies cortadas podem ser melhor arranjadas para que máquinas possam acessá-las diretamente. Conselhos e orientações sobre como sítios e soluções na web devem ser projetados podem ser encontrados em outros lugares.

### Serviços web

Para dados que mudam frequentemente, e onde cada recuperação é de tamanho limitado, é muito relevante publicá-los por webservices. Há muitas maneiras de se criar um webservice, mas alguns dos mais usados são SOAP e REST. Geralmente, mais SOAP que REST, mas serviços REST são muito fáceis de se desenvolver e usar, e por isso são um padrão amplamente utilizado.

### Banco de Dados

Assim como webservices, bancos de dados podem fornecer acesso aos dados dinamicamente. Bancos de dados têm a vantagem de permitir a usuários somente a extração na qual eles estejam interessados.

Há algumas preocupações de segurança quando se permite a extração remota de bancos de dados. E o acesso a banco de dados só é útil se a estrutura do banco e a importância de cada tabela e campo estiverem bem documentadas. Frequentemente, é relativamente simples e barato criar webservices que expõem os dados de um banco de dados, o que pode ser uma maneira fácil de tratar as preocupações de segurança.
