
library(dplyr)
library(ggplot2)
library(tidyverse)
library(quantreg)

###################################################################################################################################

#SI - TODAS REGIONES#

ggplot(data = Spain) + geom_point(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Blue") + 
  geom_smooth(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Red") + facet_wrap( ~ Province_State, nrow = 5)

#SI - ANALISIS INDIVIDUAL#

ggplot(data = candalusia) + geom_point(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Blue") + 
  geom_smooth(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Red")


###################################################################################################################################

#NO#

ggplot(data = candalusia) + geom_quantile(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Blue") + 
  geom_smooth(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Red")

###################################################################################################################################

#????#

ggplot(data = candalusia) + geom_area(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Blue") + 
  geom_smooth(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Red") + facet_wrap( ~ Province_State, nrow = 5)

#IND - PARA VER EL ACUMULADO DE CASOS CONFIRMADOS ETC#

ggplot(data = candalusia) + geom_area(mapping = aes(x=Last_Update1, y=Confirmed), color="Blue")

#DIARIOS#

ggplot(data = candalusia) + geom_area(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Blue")


#TODOS - PARA VER EL ACUMULADO DE CASOS CONFIRMADOS ETC#

#CONFIRMADOS#

ggplot(data = Spain) + geom_area(mapping = aes(x=Last_Update1, y=Confirmed), color="Blue") + facet_wrap( ~ Province_State, nrow = 5)

#MUERTES#

ggplot(data = Spain) + geom_area(mapping = aes(x=Last_Update1, y=Deaths), color="Blue") + facet_wrap( ~ Province_State, nrow = 5)

#RECUPERADOS#

ggplot(data = Spain) + geom_area(mapping = aes(x=Last_Update1, y=Recovered), color="Blue") + facet_wrap( ~ Province_State, nrow = 5)


###################################################################################################################################

#???? MIRAR CON DATOS BIEN - COMO LA DE ARRIBA PERO SIN RELLENO#

ggplot(data = candalusia) + geom_line(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Blue") + 
  geom_smooth(mapping = aes(x=Last_Update1, y=Daily_Confirmed), color="Red")

#PARA VER EL ACUMULADO DE CASOS CONFIRMADOS ETC - COMO LA DE ARRIBA PERO SIN RELLENO#

#CONFIRMADOS#

ggplot(data = candalusia) + geom_line(mapping = aes(x=Last_Update1, y=Confirmed), color="Blue")


#MUERTES#

ggplot(data = candalusia) + geom_line(mapping = aes(x=Last_Update1, y=Deaths), color="Blue")


#RECUPERADOS#

ggplot(data = candalusia) + geom_line(mapping = aes(x=Last_Update1, y=Recovered), color="Blue")

###################################################################################################################################

#TODOS - PARA VER EL ACUMULADO DE CASOS CONFIRMADOS ETC#

#CONFIRMADOS#

lp1 <- ggplot(data = Spain) + geom_line(mapping = aes(x=Last_Update1, y=Confirmed), color="Blue") + geom_line(mapping = aes(x=Last_Update1, y=Deaths), color="Red") + facet_wrap( ~ Province_State, nrow = 5)
lp1 + scale_fill_discrete(name ="Title", labels =c("A","B"))

#MUERTES#

ggplot(data = Spain) + geom_line(mapping = aes(x=Last_Update1, y=Deaths), color="Blue") + facet_wrap( ~ Province_State, nrow = 5)

ggplot(data = Spain) + geom_line(aes(Last_Update1,Deaths, colour = "Muertes")) + facet_wrap( ~ Province_State, nrow = 5)

ggplot(Spain,aes(Last_Update1,Deaths, colour = "Red")) + geom_point() + facet_wrap( ~ Province_State, nrow = 5)


ggplot(data = Spain) + geom_line(aes(Last_Update1,Daily_Deaths, colour = "Muertes")) + geom_line(aes(Last_Update1,Daily_Confirmed, colour = "Confirmados")) + geom_line(aes(Last_Update1,Daily_Recovered, colour = "Recuperados")) + facet_wrap( ~ Province_State, nrow = 5) + labs(x = "Fecha", y ="", title = "España", colour = "Leyenda")



ggplot(data = Spain) + geom_line(mapping = aes(x=Last_Update1, y=Confirmed, col = Confirmed), color="Blue") + facet_wrap( ~ Province_State, nrow = 5)

ggplot(data = Spain) + geom_point(aes(x=Last_Update1, y=Confirmed), color="Blue") + geom_point(aes(x=Last_Update1, y=Deaths), color="Red") + facet_wrap( ~ Province_State, nrow = 5)
  
geom_line(mapping = aes(x=Last_Update1, y=Deaths), color="Blue") + facet_wrap( ~ Province_State, nrow = 5)

ggplot(data = Spain,aes(x=Last_Update1, y=Deaths), color="Blue") + geom_line() + facet_wrap( ~ Province_State, nrow = 5)


#RECUPERADOS#

ggplot(data = Spain) + geom_line(mapping = aes(x=Last_Update1, y=Recovered), color="Blue") + facet_wrap( ~ Province_State, nrow = 5)


###################################################################################################################################


ggplot(data = candalusia) + geom_step(mapping = aes(x=Last_Update1, y=Confirmed), color="Blue") + 
  geom_smooth(mapping = aes(x=Last_Update1, y=Confirmed), color="Red") + facet_wrap( ~ Province_State, nrow = 5)


###################################################################################################################################
