Ejecución de Scripts:

spark-submit [direccion/nombre:script.py] [argumentos]

Ejemplos:

spark-submit ./CountryFilter-NA.py Spain Madrid [Esto ejecutará el comando que filtra por pais (Spain) y permite filtar por comunidad también (Madrid)]

CASO ESPECIAL

spark-submit ./CountryFilter.py Spain Catalonia [Esto ejecutará el comando que filtra por pais (Spain) y permite filtar por comunidad también (Catalunya) y realizara el interpolado se guradara como "Spain Catalonia.csv"]
spark-submit ./CountryFilter.py Spain Catalonia [Esto ejecutará el comando que filtra por pais (Spain) y rellenando los datos NaN con el primer dato no null de los días anteriores, es decir, utilizara la funcion .pad(), se guardaria como "Spain-Pad"]

<b> Comprobar que el script tiene permiso de ejecución.
