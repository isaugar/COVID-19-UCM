dataSet<- generarR0(dataSet)

generarR0 <- function(dataSet){
  
  #Limpiar nulls -> ""
  dataSet$Province_State[is.na(dataSet$Province_State)] <- ""
  
  #bucle que calcula los R0

  columna <- rep(0,length(dataSet$Confirmed))
  for(i in (15:(length(dataSet$Confirmed)))){
    
    if((!is.na(dataSet$Daily_Confirmed[i])) && (!is.na(dataSet$Daily_Confirmed[i])))
      columna[i] = dataSet$Daily_Confirmed[i] / dataSet$Daily_Confirmed[i-14]
    
  }
  
  
  #bucle que limpia los R0
  for(i in (15:(length(dataSet$Confirmed)))){
    
    if(dataSet$Province_State[i]!=dataSet$Province_State[i-1] || dataSet$Country_Region[i]!=dataSet$Country_Region[i-1]){
      for(j in 0:13){
        
        columna[i+j] = 0
        
      }
      
    }
    
  }
 
  #Meter array prueba en columna
  dataSet$R0 <- columna
  
  return(dataSet)
  
}
