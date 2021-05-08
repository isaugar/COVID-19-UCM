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

#leemos todso los csv con los datos csse_covid_19_daily_reports
df =spark.read.option("header","true").option("inferSchema","true").csv("./Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*.csv")

ret  = df.withColumn('Lat', regexp_replace('Lat', 'Unknown', '')).filter((df['Country_Region'] != "US")).sort(df.Last_Update.asc())
ret = ret.fillna({'Province_State':" "})

#1 tranformamos en fecha 
#2 seleccionamos las columnas que nos interesan

pandasRet = ret.select(col('Country_Region').cast(StringType()),ret['Province_State'],ret['Lat'].cast(FloatType()),ret['Long_'].cast(FloatType()),when(to_date(col("Last_Update"),"M/d/yy").isNotNull(),to_date(col("Last_Update"),"M/d/yy")).otherwise(to_date(col("Last_Update"),"yyyy-MM-dd")).alias("Last_Update1"),ret['Confirmed'].cast(IntegerType()),ret['Deaths'].cast(IntegerType()),ret['Recovered'].cast(IntegerType()),ret['Active'].cast(IntegerType())).orderBy(col("Country_Region").asc(),col("Province_State").asc(),col("Last_Update1").asc()).toPandas()

#Calculo confirmados diarios 
#pandasRet.loc[((pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1))) & (pandasRet['Confirmed'] <= pandasRet['Confirmed'].shift(1)) ) , 'Confirmed'] = np.NaN
#pandasRet['Confirmed'] = pandasRet['Confirmed'].pad()
#pandasRet['Confirmed'] = pandasRet['Confirmed'].interpolate().round(0)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | ((pandasRet['Province_State'] != pandasRet['Province_State'].shift(1))), 'Daily_Confirmed'] = pandasRet['Confirmed']
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) ) , 'Daily_Confirmed'] = pandasRet['Confirmed'] - pandasRet['Confirmed'].shift(1)


#Calculo muertes diarias
#pandasRet.loc[((pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1))) & (pandasRet['Deaths'] <= pandasRet['Deaths'].shift(1)) ) , 'Deaths'] = np.NaN
#pandasRet['Deaths'] = pandasRet['Deaths'].pad()
#pandasRet['Deaths'] = pandasRet['Deaths'].interpolate().round(0)
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) ) , 'Daily_Deaths'] = pandasRet['Deaths'] - pandasRet['Deaths'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Deaths'] = pandasRet['Deaths']

#Calculo recuperados diarios
#pandasRet.loc[((pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1))) & (pandasRet['Recovered'] <= pandasRet['Recovered'].shift(1)) ) , 'Recovered'] = np.NaN
#pandasRet['Recovered'] = pandasRet['Recovered'].pad()
#pandasRet['Recovered'] = pandasRet['Recovered'].interpolate().round(0)
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) ) , 'Daily_Recovered'] = pandasRet['Recovered'] - pandasRet['Recovered'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Recovered'] = pandasRet['Recovered']

#Calculo activos diarios
pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1))) , 'Daily_Active'] = pandasRet['Active'] - pandasRet['Active'].shift(1)
pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Active'] = pandasRet['Active']

#Calculo Tasa incidencia
pandasRet["IP"] = (pandasRet["Daily_Confirmed"] + pandasRet["Daily_Deaths"]) - pandasRet["Daily_Recovered"]

#Eliminamos fechas repetidas de los csv cuando no se daban datos diarios
pandasRes = pandasRet.loc[(pandasRet['Last_Update1'] != pandasRet['Last_Update1'].shift(1)) & (pandasRet['Province_State'] != "") ]

pandasRes.loc[((pandasRet['Recovered']) < pandasRet['Recovered'].shift(1)) & ((pandasRet['Province_State']) == pandasRet['Province_State'].shift(1)), 'Recovered' ] = np.NaN
pandasRes.loc[(pandasRet['Daily_Recovered']) < 0, 'Daily_Recovered' ] = np.NaN
#pandasRes['Recovered'] = pandasRes['Recovered'].pad()
pandasRes['Daily_Recovered'] = pandasRes['Daily_Recovered'].pad()

pandasRes.loc[((pandasRet['Deaths']) < pandasRet['Deaths'].shift(1)) & ((pandasRet['Province_State']) == pandasRet['Province_State'].shift(1)), 'Deaths' ] = np.NaN
pandasRes.loc[(pandasRet['Daily_Deaths']) < 0, 'Daily_Deaths' ] = np.NaN
#pandasRes['Deaths'] = pandasRes['Deaths'].pad()
pandasRes['Daily_Deaths'] = pandasRes['Daily_Deaths'].pad()

pandasRes.loc[((pandasRet['Confirmed']) < pandasRet['Confirmed'].shift(1)) & ((pandasRet['Province_State']) == pandasRet['Province_State'].shift(1)), 'Confirmed' ] = np.NaN
pandasRes.loc[(pandasRet['Daily_Confirmed']) < 0, 'Daily_Confirmed' ] = np.NaN
#pandasRes['Confirmed'] = pandasRes['Confirmed'].pad()
pandasRes['Daily_Confirmed'] = pandasRes['Daily_Confirmed'].pad()

#pandasRes['Active'] = pandasRes['Active'].pad()
pandasRes['Daily_Active'] = pandasRes['Daily_Active'].pad()

#Comprobamos tipos y si se han devuelto datos
pandasRes.info()

#Guardamos en csv
pandasRes.to_csv("WorldWitoutUSA-Pad-" + time.strftime("%c") + "-semicolon"  + ".csv", sep = ';')
pandasRes.to_csv("WorldWitoutUSA-Pad-" + time.strftime("%c") +"-comma" + ".csv", sep = ',')




