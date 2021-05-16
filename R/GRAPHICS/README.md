
GRAFICAS COVID-19 UCM

FUNCTIONS:

-graficas.R
-graficasFinal.R

========================================================================================================

Hacemos uso de las graficas que nos proporciona la libreria de R ggplot2 cuyas graficas tienen un forma predeterminada de generarse que esta dividida por secciones que se van sumando (+) una a una a la linea de codigo final para poder ir añadiendo los componentes necesarios a la grafica y de esta forma conseguir el grafico desado.

Ejemplo:

	ggplot(data = Netherlands2) + geom_line(aes(Last_Update1,Daily_MuertosMM, colour = "Muertes")) + geom_line(aes(Last_Update1,Daily_ConfirmedMM, colour = "Confirmados")) + geom_line(aes(Last_Update1,Daily_RecuperadosMM, colour = "Recuperados")) + facet_wrap( ~ Province_State, nrow = 6) + labs(x = "Fecha", y ="", title = "Holanda", colour = "Leyenda")

- La seccion de data se utiliza para indicar a ggplot el dataset del cual se van a extraer los datos que vamos a utilizar para generar la grafica.

- geom_line es una función de la cual se crean las graficas basadas en una linea geometrica y se encarga de dibujar la grafica en si misma, geom_line es tan solo uno de los muchos tipos de graficos que se pueden realizar y veremos a continuacion. Este tipo de funciones requieren de unos parametros para poder dibujar la grafica, en el parametro aes se indican cuales van a ser los ejes x e y del grafico, además de esto se añade el color de la linea dentro de la grafica y el nombre que va a tener esta en la leyenda, en el primer caso por ejemplo "Muertes".

- Como se puede observar a este primer geom_line se le añaden otros dos más puesto que el objetivo de la grafica es el de comparar los tres campos dentro de una grafica conjunta.

- facet_wrap lo utlizamos en este caso para que el grafico que se genera este dividido por las regiones del pais y de esta forma nos devuelva n numero de graficas, siendo n igual al numero de regiones que haya dentro del pais seleccionado, en este caso holanda. Los argumentos de esta función son primero la variable por la cual se creará esta división y el número de lineas en las cuales queremos dividir todas las graficas que se generen.

- labs se utiliza para añadir y cambiar las etiquetas del grafico para poder asi adecuarlo al maximo a lo deseado, en este ejemplo se modifican tanto el nombre del eje x como del y, se añade un titulo a la grafica correspondiendo al pais que representa y por último se cambia el nombre de la Leyenda para que quede la grafica de forma unificada y lo más coherente posible.

========================================================================================================

graficas.R

En este script de R hemos realizado una serie de pruebas con todos los tipos de graficos que se pueden realizar con los tipos de datos que tenemos en este caso variables continuas, el objetivo de este script es el de evaluar todos los tipos de graficos que disponemos y ver cual de todos es el más apropiado para la reprenstación final de los datos, en la carpeta EXAMPLES se encuentra ejemplos de todos los tipos de graficos disponibles

graficasFinal.R

Este script de R es el que hemos utlizado para poder realizar todas las graficas de los paises que hemos seleccionado, y de las funciones finales que hemos utlizado para esto:

	Netherlands<-filter(MundoSInUSA, Country_Region=="Netherlands")

Realizando este operación lo que estamos realizado es la creación de un dataset especifico sacado del dataset completo de todos los paises que tenemos (MundoSInUSA), usamos la función filter para esto filtrando por el nombre del pais seleccionado, en este ejemplo Holanda.

	Netherlands2<-filter(Netherlands,!is.na(Province_State), Province_State != "Unknown")

En esta segunda operación realizamos un segundo dataset con un segundo filtrado con el objetivo de eleminar las filas en las que el pais no dividia por regiones los datos (NA en la variable Province_State) y aquellas que por error se generasen bajo el nombre "Unknown". La generación de un segundo dataset no es obligatorio ya que se podria reescribir en el anterior el nuevo pero lo hemos hecho asi para evitar confusiones y aportar claridad.

	ggplot(data = Netherlands2) + geom_line(aes(Last_Update1,Daily_MuertosMM, colour = "Muertes")) + geom_line(aes(Last_Update1,Daily_ConfirmedMM, colour = "Confirmados")) + geom_line(aes(Last_Update1,Daily_RecuperadosMM, colour = "Recuperados")) + facet_wrap( ~ Province_State, nrow = 6) + labs(x = "Fecha", y ="", title = "Holanda", colour = "Leyenda")

	ggplot(data = Netherlands2) + geom_line(aes(Last_Update1,IPMM, colour = "IP"))  + facet_wrap( ~ Province_State, nrow = 5) + labs(x = "Fecha", y ="", title = "Holanda", colour = "Leyenda")

	ggplot(data = Netherlands2) + geom_line(aes(Last_Update1,R0MM, colour = "R0"))  + facet_wrap( ~ Province_State, nrow = 5) + labs(x = "Fecha", y ="", title = "Holanda", colour = "Leyenda")

Por último con el dataset final realizamos las graficas correspondientes, la primera es la misma que la explicada en el ejemplo parte por parte y lo que genera son multiples graficas todas juntas de cada region del pais elegido, dentro de cada cual hay una linea geometrica que representa en diferentes colores a los campos de media movil de muertos diarios, media movil de casos confirmados diarios y media movil de recuperados diarios.

Las siguientes dos funciones generan multiples graficas divididas por regiones de nuevo aunque en este caso solo muestran un dato, la primera función lo hace con el indice de peligrosidad (IP), calculado a partir de la siguiente fórmula: muertos diarios + confirmados diarios - recuperados diarios. La segunda función lo hace con el número de reproducción (R0), caculado a partir de la siguiiente fórmula: confirmados diarios / confirmados diarios-14
