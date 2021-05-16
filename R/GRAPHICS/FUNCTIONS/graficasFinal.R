
library(dplyr)
library(ggplot2)
library(tidyverse)
library(quantreg)

Netherlands<-filter(MundoSInUSA, Country_Region=="Netherlands")

Netherlands2<-filter(Netherlands,!is.na(Province_State), Province_State != "Unknown")


ggplot(data = Netherlands2) + geom_line(aes(Last_Update1,Daily_MuertosMM, colour = "Muertes")) + geom_line(aes(Last_Update1,Daily_ConfirmedMM, colour = "Confirmados")) + geom_line(aes(Last_Update1,Daily_RecuperadosMM, colour = "Recuperados")) + facet_wrap( ~ Province_State, nrow = 6) + labs(x = "Fecha", y ="", title = "Holanda", colour = "Leyenda")

ggplot(data = Netherlands2) + geom_line(aes(Last_Update1,IPMM, colour = "IP"))  + facet_wrap( ~ Province_State, nrow = 5) + labs(x = "Fecha", y ="", title = "Holanda", colour = "Leyenda")

ggplot(data = Netherlands2) + geom_line(aes(Last_Update1,R0MM, colour = "R0"))  + facet_wrap( ~ Province_State, nrow = 5) + labs(x = "Fecha", y ="", title = "Holanda", colour = "Leyenda")
