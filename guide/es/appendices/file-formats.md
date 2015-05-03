---
title: Formato de Archivos
---

## Un Repaso de los Formatos de Archivos

### JSON

JSON es un formato de archivo que es muy fácil de leer por cualquier lenguaje de programación. Su simplicidad significa que es generalmente fácil de procesar para las computadoras a comparación de otros, como lo es XML.

### XML

XML es un formato ampliamente utilizado para el intercambio de datos debido a que ofrece buenas oportunidades de mantener la estructura de los datos y la forma en que los archivos son construidos, y permite a los desarrolladores escribir partes de la documentación con los datos sin interferir con la lectura de ellos.

### RDF

Un formato recomendado por W3C llamado RDF permite representar datos en unEsa forma que facilita la combinación de información de diferentes fuentes. Los datos RDF pueden ser almacenados en XML y JSON, entre otras serializaciones. RDF promueve el uso de URLs como identificadores, lo que brinda una manera conveniente de interconectar iniciativas de "Datos Abiertos" existentes. RDF todavía no se ha generalizado, pero es una tendencia entre iniciativas de Gobierno Abierto, incluso las iniciativas de Linked Data de los gobiernos británico y español. El inventor de la Web, Tim Berners-Lee, propuso recientemente un esquema de puntuación de cinco estrellas que incluye Linked Data en formato RDF como una meta a alzanzar en las iniciativas de Datos Abiertos.

### Hojas de Cálculo

Muchas autoridades tienen información que queda en la hoja de cálculo, por ejemplo Microsoft Excel. Estos datos a menudo pueden ser utilizados inmediatamente con las descripciones correctas de lo que las distintas columnas significan.

Sin embargo, en algunos casos puede ser macros y fórmulas en hojas de cálculo, las cuales pueden ser más incómodas para manipular. Por tanto, es recomendable documentar este tipo de cálculos junto a la hoja de cálculo, ya que generalmente es más accesible para los usuarios al leer.

### Archivos separado por comas

Los archivos CSV pueden ser un formato útil debido a que son compactos y por lo tanto adecuado para transferir grandes conjuntos de datos con la misma estructura. Sin embargo, el formato es tan espartano que los datos son frecuentemente inservibles sin documentación, ya que puede ser casi imposible adivinar el significado de las diferentes columnas. Por tanto, es particularmente importante para los formatos separados por comas que la documentación de los campos individuales sea precisa.

Además, es esencial que la estructura del archivo sea respetada, como una omisión única de un campo puede perturbar la lectura de todos los datos restantes en el archivo sin ninguna posibilidad real de rectificarla, porque no se puede determinar cómo los datos restantes deben ser interpretados.

### Documento de Texto

Documentos clásicos en formatos como Word, ODF, OOXML, o PDF, puede ser suficiente para mostrar ciertos tipos de datos, por ejemplo, listas de correo o equivalente. Puede que sea barato para exponerlos, siempre que ese sea el formato en que la data se haya creado. El formato no da soporte para mantener la estructura coherente, lo cual significa que a veces es difícil para introducir datos por medios automatizados. Asegúrese de utilizar las plantillas como base de documentos en las que se mostrarán los datos para su reutilización, por lo que es al menos posible extraer información de los documentos.

También se puede apoyar el uso posterior de los datos que utilice el marcador de la tipografía tanto como sea posible para que sea más fácil para una máquina para distinguir las partidas (de cualquier tipo) a partir del contenido y así sucesivamente. En general se recomienda no exhibir en formato de procesamiento de texto, si hay datos en un formato diferente.

### Texto

Documentos de texto (. Txt) son muy fáciles para leer en los ordenadores. Por lo general, no incluyen metadatos estructurales, lo que significa que los desarrolladores necesitan para crear un programa de análisis que pueda interpretar cada documento tal y como aparece.

Algunos problemas pueden ser causados al cambiar archivos de texto plano entre sistemas operativos. MS Windows, Mac OSX y otras variantes de Unix tienen su propia forma de decirle a la computadora que se ha llegado al final de la línea.

### Imagen escaneada

Probablemente la forma menos adecuada para la mayoría de los datos, pero ambos TIFF y JPEG 2000-al menos puede marcarlos con la documentación de lo que está en la imagen - adecuada para marcar la imagen de un documento con contenido de texto completo del documento. Puede ser relevante a los datos que muestran como imágenes aquellos datos que no nacen por la vía electrónica -un ejemplo obvio es la antigua escuela de registros y el material de archivo- y una imagen es mejor que nada.

### Formatos propietarios

Algunos sistemas tienen sus propios formatos de datos que pueden guardar o exportar datos. A veces puede ser suficiente para exponer los datos en un formato - sobre todo si se espera que el uso de más estaría en un sistema similar del que vienen. Sobre donde obtener más información sobre estos formatos, debe estar siempre indicado, por ejemplo, al proporcionar un enlace a la página web del proveedor. En general se recomienda para mostrar los datos en formato libre, cuando sea factible.

### HTML

Hoy en día, muchos datos se encuentran disponibles en formato HTML en varios sitios. Esto sería suficiente, si se trata de datos estables y de alcance limitado. En algunos casos, sería preferible tener los datos de una forma fácil para descargar y manipular, pero como es barato y fácil de hacer referencia a una página en un sitio web, podría ser un buen punto de partida en la pantalla de datos.

Generalmente, sería más apropiado el uso de tablas en documentos HTML para almacenar datos y, es importante que los distintos campos de datos se muestren y sean dadas identificaciones, que hacen más fácil encontrar y manipular los datos. Yahoo ha desarrollado una herramienta (<http://developer.yahoo.com/yql/>) que puede extraer información estructurada de un sitio web, y ciertas herramientas que pueden hacer mucho más con los datos siempre que se encuentren cuidadosamente etiquetados.

## Archivos de formatos abiertos

Incluso si la información se proporciona en formato electrónico, formato legible por máquina, y en detalle, puede haber problemas relacionados con el formato del archivo en sí.

Los formatos en los cuales la información es publicada - en otras palabras, la base digital en la cual la información es almacenada - puede ser "abierto" o "cerrado". Un formato abierto es aquel donde las especificaciones del software están disponibles para cualquier persona, de forma gratuita, así cualquiera puede usar dichas especificaciones en su propio software sin ninguna limitación en su reutilización que fuere impuesta por derechos de propiedad intelectual.

Si el formato del archivo es "cerrado", esto puede ser debido a que el formato es propietario y sus especificaciones no están disponibles públicamente, o porque el formato es propietario y aunque las especificaciones se han hecho públicas, su reutilización es limitada. Si la información es liberada en un formato de archivo cerrados, esto puede causar grandes obstáculos para reutilizar la información codificada en él, forzando a aquellos que deseen usar la información a comprar software innecesario.

La ventaja de los archivos de formatos abiertos, es que permiten a los desarrolladores producir varios paquetes de software y servicios utilizando esos formatos. Esto entonces reduce al mínimo los obstáculos para la reutilización de la información que contienen.

El uso de formatos de archivo con propiedad, para el que la especificación no está disponible públicamente, puede crear dependencia de software de terceros o de los titulares de licencias de los formatos de archivos. En el peor de los casos, esto puede significar que la información sólo se pueden leer con ciertos softwares especiales, que pueden ser muy caros, o que pueden quedar obsoletos.

La preferencia del término Gobierno de Datos Abiertos, es que la información se publicará en formatos de archivo abiertos, los cuales son de lectura mecánica.

### Ejemplo: datos del tráfico en Reino Unido

Andrew Nicholson es un desarrollador de software que estuvo involucrado en una campaña (la cual es un éxito) contra la construcción de una nueva carretera, la carretera de circunvalación al este de Westbury, en el Reino Unido. Andrew estaba interesado en acceder y utilizar los datos de tráfico que se estaban utilizando para justificar las propuestas. Se las arregló para obtener algunos de los datos relevantes a través de la libertad de las solicitudes de información, pero el gobierno local proporcionó los datos en un formato propietario que sólo se pueden leer con el software producido por una empresa llamada Saturno, que se especializa en el modelado de tráfico y las previsiones.

Aunque el no acceso a leyes de información da un derecho a acceder a información de formatos abiertos, la iniciativa de un gobierno de datos abiertos están comenzando a ir acompañadas de una política que estipula que la información oficial debe estar disponible en formatos abiertos. Establecer el estándar de oro ha sido el Gobierno de Obama, cuando lanzó la Directiva de Gobierno Abierto, emitida en diciembre de 2009, la cual estableció:

> *Para la extensión factible y sujeta a restricciones, las agencias deberían publicar información en línea en formatos abiertos que puedan ser recuperados, descargados, indexados y buscados a través de buscadores usualmente utilizados. Un formato abierto debe ser independiente de la plataforma, procesable por computadoras y estar disponible al público sin restricciones que impidan la reutilización de la información.*

## ¿Cómo uso un formato determinado?

Cuando una autoridad debe mostrar nuevos datos - datos que no han sido expuestos antes - se debe elegir el formato que proporciona el mejor equilibrio entre el costo y la idoneidad para el propósito. Para cada formato, hay algunas cosas que usted debe tener en cuenta, y esta sección tiene como objetivo explicarlas.

Esta sección se centra sólo en cómo las superficies de corte son los más dispuestos de modo que las máquinas puedan acceder a ellos directamente. Asesoramiento y orientación acerca de cómo las soluciones de sitios web y la web debe ser diseñado se puede encontrar en otros lugares.

### Servicios Web

Cuando los datos cambian frecuentemente, y el tamaño de cada descargas es limitado, es muy importante exponer la información a través de web services. Hay muchas maneras de crear web services, pero algunos de más usados son SOAP y REST. Generalmente SOAP antes que REST. Los servicios REST son fáciles de desarrollar y entender, por eso es un standard muy usado.

### Base de datos

Como los servicios webs, las bases de datos permiten el acceso directo a los datos dinámicamente. Las bases de datos tienen la ventaja de extraer aquella información en la cual estén interesados.

Hay algunas preocupaciones de seguridad en cuanto a permitir extracciones remotas a bases de datos, y el acceso a las bases de datos es útil si su estructura y la importancia de las tablas y campos individuales están bien documentados. Generalmente es relativamente simple y no tiene costo crear web services que expongan datos de una base de datos, esta puede ser una manera fácil de lidiar con las problemáticas de seguridad.