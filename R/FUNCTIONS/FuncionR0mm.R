 dataSet <- generarR0MM(dataSet)
  
generarR0MM <- function(dataSet){
    
    #Limpiar nulls -> ""
    dataSet$Province_State[is.na(dataSet$Province_State)] <- ""
    
    #bucle que calcula los R0
    
    columna <- rep(0,length(dataSet$Confirmed))
    for(i in (15:(length(dataSet$Confirmed)-15))){
      
      columna[i] = dataSet$Daily_ConfirmedMM[i] / dataSet$Daily_ConfirmedMM[i-14]
      
    }
    
    
    
    #bucle que limpia los R0
    for(i in (15:(length(dataSet$Confirmed)-15))){
      
      if(dataSet$Province_State[i]!=dataSet$Province_State[i-1] || dataSet$Country_Region[i]!=dataSet$Country_Region[i-1]){
        for(j in 0:13){
          
          columna[i+j] = 0
          
        }
        
      }
      
    }
  
  #Meter array prueba en columna
  dataSet$R0MM <- columna
  
  return(dataSet)
  }
