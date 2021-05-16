dataSet <- suavizar(dataSet)

suavizar function(dataSet){
  
  #Limpiar nulls -> ""
  dataSet$Province_State[is.na(dataSet$Province_State)] <- ""
  
  Confirmados <- rep(0,length(dataSet$Last_Update1))
  Muertos <- rep(0,length(dataSet$Last_Update1))
  Recuperados <- rep(0,length(dataSet$Last_Update1))
  Activos <- rep(0,length(dataSet$Last_Update1))
  #bucle que suaviza los datos 7 dias
  for(i in (4:(length(dataSet$Last_Update1)-3))){
    
    Confirmados[i] = mean((dataSet$Daily_Confirmed[(i-3):(i+3)]), na.rm = TRUE)
    Muertos[i] = mean((dataSet$Daily_Deaths[(i-3):(i+3)]),na.rm = TRUE)
    Recuperados[i] = mean((dataSet$Daily_Recovered[(i-3):(i+3)]),na.rm = TRUE)
    Activos[i] = mean((dataSet$Daily_Active[(i-3):(i+3)]),na.rm = TRUE)
    
  }
  
  #bucle que limpia los Suavizados
  for(i in (4:(length(dataSet$Last_Update1)-3))){
    
    if(dataSet$Province_State[i]!=dataSet$Province_State[i-1] || dataSet$Country_Region[i]!=dataSet$Country_Region[i-1]){
      for(j in -3:3){
        
        Confirmados[i+j] = 0
        Muertos[i+j] = 0
        Recuperados[i+j] = 0
        Activos[i+j] = 0
        
      }
      
    }
    
  }
  
  #Meter array prueba en columna
  dataSet$Daily_ConfirmedMM = Confirmados
  dataSet$Daily_MuertosMM = Muertos
  dataSet$Daily_RecuperadosMM = Recuperados
  dataSet$Daily_ActivosMM = Activos
  
  return(dataSet)
}
