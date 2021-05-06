#COUNTRY FILTER

Este directorio contiene varios tipos de scripts para generar los ".csv". filtrando por el país o provincia/estado de un país.

Este directorio contiene: 

- BBDD de un pais o provincia/estado de un pais.

- Para facilitar la ayuda al usuario, se ha decidido dividir los scripts en directorios, para evitar confusiones.

- Se añade una carpeta <b>EXAMPLES</b>, dentro de la carpeta hay un example de cada script.

- Se recomienda comprobar los ejemplos para encontrar el script que mejor encaje en su estudio.

- <b>Los script generan dos tipos de .csv, el separado por (,) y separado (;)</b>.

- <b>El script INTERPOLATE solo se puede realizar en la provincia/estado de un pais, sino se usara la función .pad()</b>.

Ejecución de Scripts: 

<b> spark-submit [direccion/nombre:script.py] [argumentos]</b>

- Si el nombre es compuesto, por ejemplo New York, hay que ponerlo entre comillas "New York"

Ejemplos:
- spark-submit ./CountryFilter-NA.py Spain Madrid  [Esto ejecutará el comando que filtra por pais (Spain) y permite filtar por comunidad también (Madrid)]

- CASO ESPECIAL
  - spark-submit ./CountryFilter.py Spain Catalonia  [Esto ejecutará el comando que filtra por pais (Spain) y permite filtar por comunidad también (Catalunya) y realizara el interpolado se guradara como "Spain Catalonia.csv"]
  - spark-submit ./CountryFilter.py Spain Catalonia  [Esto ejecutará el comando que filtra por pais (Spain) y rellenando los datos NaN con el primer dato no null de los días anteriores, es decir, utilizara la funcion .pad(), se guardaria como "Spain-Pad"]
