
En esta carpeta se pueden encontrar diferentes funciones para ampliar la cantidad de variables de un dataset, requerirá tener activado el paquete 'dplyr' y el dataset de entrada debera contener los siguientes campos:

- Country_Region
- Province_State
- Last_Update1
- Daily_Confirmed
- Daily_Deaths
- Daily_Recovered
- Daily_Active

Las funciones se ejecutan de la siguiente manera:

1- Se compila el codigo de la funcion, dicha funcion aparecera en el apartado de variables a la derecha.
2- Se ejecuta el siguiente codigo: Nombre_Dataset_Salida <- NombreFuncion(NombreDatasetEntrada).


-> FuncionR0: Esta funcion recibe como entrada un dataset con los campos mencionados anteriormente, y devuelve el mismo dataset pero esta vez con la variable R0 calculada en una columna adicional.

-> FuncionSuavizar:  Esta funcion recibe como entrada un dataset con los campos mencionados anteriormente, y devuelve un dataset con los campos: Daily_ConfirmedMM, Daily_DeathsMM, Daily_RecoveredMM y Daily_ActiveMM, las cuales son las variables Daily anteriormente mencionadas pero con una media movil a 7 dias.

-> Funcion IPMM: Esta funcion recibe como entrada un dataset con los campos mencionados anteriormente, y devuelve un dataset con el campo IPMM el cual es el Índice de Peligrosidad calculado con la media móvil.

-> Funcion R0MM: Esta funcion recibe como entrada un dataset con los campos mencionados anteriormente, y devuelve el mismo dataset pero esta vez con la variable R0MM calculada con la media móvil.

-> Funcion RepartoPonderado: Esta funcion recibe como entrada un dataset con los campos mencionados anteriormente, y devuelve otro dataset idéntico, pero realizando un reparto ponderado en la columna Daily_Confirmed en caso de encontrar ceros.

