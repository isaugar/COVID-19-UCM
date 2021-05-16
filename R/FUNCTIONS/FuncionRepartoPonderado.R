dataSet <- igualar(dataSet)

igualar <- function(dataSet){
  
  cont <- 0;
  
  #Limpiar nulls -> ""
  dataSet$Province_State[is.na(dataSet$Province_State)] <- ""
  
  for(i in (2:length(dataSet$Province_State))){
    print(dataSet$Province_State[i])
    
    if(dataSet$Province_State[i] != dataSet$Province_State[i-1] || dataSet$Country_Region[i] != dataSet$Country_Region[i-1]){
      cont <- 0
    }
    
    if(!is.na(dataSet$Daily_Confirmed[i]))
    
    if(dataSet$Daily_Confirmed[i] == 0){
    
      cont <- cont+1
      
    }else if(cont != 0){
    
      if(cont+1 <= dataSet$Daily_Confirmed[i]){
        
        for(j in ((i-cont) : (i-1))){
          print(dataSet$Daily_Confirmed[i]%/%(cont+1))
         dataSet$Daily_Confirmed[j] <- (dataSet$Daily_Confirmed[i]%/%(cont+1))
          
        }
        dataSet$Daily_Confirmed[i] <- ((dataSet$Daily_Confirmed[i]%%cont+1)) + ((dataSet$Daily_Confirmed[i]%/%(cont+1)))
        print((dataSet$Daily_Confirmed[i+1]%%cont))
      }
      
      cont <- 0;
      
    }else{
    
      cont <- 0;
    
    }
    
  }
  
  return(dataSet)
}

