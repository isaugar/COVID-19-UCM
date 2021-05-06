from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.functions import udf,substring, length, col, expr
from pyspark.sql.types import *
import pandas as pd
import numpy as np
import string
import sys
import time

#creamos la sesion de spark
spark=SparkSession.builder.master("local[*]").appName("rating").getOrCreate()
spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")

#leemos todos los csv con los datos de US y reemplaza las latitudes desconocidas y las descarta.
df =spark.read.option("header","true").option("inferSchema","true").csv("./Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports_us/*.csv")

ret  = df.withColumn('Lat', regexp_replace('Lat', 'Unknown', '')).filter(df['Lat'] != '').sort(df.Last_Update.asc())

#Seleccionamos las columnas que nos interesan, tambien corrige la columna fecha, ya que, hay fechas con otro formato.
pandasRet = 	ret.select(col('Country_Region').cast(StringType()),col('Province_State').cast(StringType()),ret['Lat'].cast(FloatType()),ret['Long_'].cast(FloatType()),when(to_date(col("Last_Update"),"M/d/yy").isNotNull(),to_date(col("Last_Update"),"M/d/yy")).otherwise(to_date(col("Last_Update"),"yyyy-MM-dd")).alias("Last_Update1"),ret['Confirmed'].cast(IntegerType()),ret['Deaths'].cast(IntegerType()),ret['Recovered'].cast(IntegerType()),ret['Active'].cast(IntegerType()),ret['People_Tested'].cast(IntegerType()),ret['People_Hospitalized'].cast(IntegerType())).orderBy(col("Country_Region").asc(),col("Province_State").asc(),col("Last_Update1").asc()).na.fill("").toPandas()


#Calculo confirmados diarios 
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) | (pandasRet['Province_State'] == "")  ) , 'Daily_Confirmed'] = pandasRet['Confirmed'] - pandasRet['Confirmed'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Confirmed'] = pandasRet['Confirmed']

#Calculo muertes diarias
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) | (pandasRet['Province_State'] == "")  ) , 'Daily_Deaths'] = pandasRet['Deaths'] - pandasRet['Deaths'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Deaths'] = pandasRet['Deaths']

#Calculo recuperados diarios
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) | (pandasRet['Province_State'] == "")  ) , 'Daily_Recovered'] = pandasRet['Recovered'] - pandasRet['Recovered'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Recovered'] = pandasRet['Recovered']

#Calculo activos diarios
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) | (pandasRet['Province_State'] == "")  ) , 'Daily_Active'] = pandasRet['Active'] - pandasRet['Active'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Active'] = pandasRet['Active']

#Calculo columnas extra de las tablas de USA (People_Tested,People_Hospitalized)
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) | (pandasRet['Province_State'] == "")  ) , 'Daily_Tested'] = pandasRet['People_Tested'] - pandasRet['People_Tested'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Tested'] = pandasRet['People_Tested']

pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) | (pandasRet['Province_State'] == "")  ) , 'Daily_Hospitalized'] = pandasRet['People_Hospitalized'] - pandasRet['People_Hospitalized'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Hospitalized'] = pandasRet['People_Hospitalized']

#Calculo Tasa incidencia
pandasRet["IP"] = (pandasRet["Daily_Confirmed"] + pandasRet["Daily_Deaths"]) - pandasRet["Daily_Recovered"]

#Eliminamos fechas repetidas de los csv cuando no se daban datos diarios
pandasRes = pandasRet.loc[(pandasRet['Last_Update1'] != pandasRet['Last_Update1'].shift(1)) & (pandasRet['Province_State'] != "") ]

#Guardamos en csv
pandasRet.to_csv("US-Negative-NoRep-" + time.strftime("%c") + "-semicolon"  + ".csv", sep = ';')
pandasRet.to_csv("US-Negative-NoRep-" + time.strftime("%c") +"-comma" + ".csv", sep = ',')




