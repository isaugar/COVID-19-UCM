dataSet<- generarIP(dataSet)

generarIP <- function(dataSet){

dataSet$IPMM <- dataSet$Daily_MuertosMM + dataSet$Daily_ConfirmedMM - dataSet$Daily_RecuperadosMM


 return(dataSet)
  
}
