# COVID-19-UCM
Este Repositorio es una aportación al estudio analítico sobre la evolución del COVID-19 a nivel mundial, facilitando varias bases de datos a los interesados, usando como referencia los datos facilitados por la <b> Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE) </b> https://github.com/CSSEGISandData/COVID-19.

Este proyecto crea una BBDD partiendo de los datos anteriormente mencionados, este proceso se encarga a su vez de recopilar y calcular los datos diarios de su global, más el indice de propagación (IP). Se incorporan varios scripts permitiendo al usuario seleccionar la BBDD que más le interese, por ejemplo, interpolando los datos diarios de la región de un pais, filtrar por un unico pais, excluyendo los datos negativos en las tasas diarias... 

Este repositorio esta constituido por cuatro directorios:

- World whitout USA: Los datos de todo el mundo, agrupados por pais y región, a excepción de USA.

- USA-State: los datos de USA, agrupados por estados. 

-	CountryFilter/RegionOptional: Filtro para generar los datos de un país o la región de un país en concreto. 

Cada directorio a su vez esta formado por:

- README.md con información de los scripts.

- Scripts.

- EXAMPLES, con un ejemplo de cada script.

Funciones utilizadas:

- IP = "Daily_Confirmed" + "Daily_Deaths" -"Daily_Recovered"*.

- Daily_xxx = Day(t) - Day(t-1).

- Forward filling = Using .pad() forward-fills the NaNs.

- Interpolate = Using .interpolate() all daily rows [Only country region filter].

Adicionalmente: se creadaa

