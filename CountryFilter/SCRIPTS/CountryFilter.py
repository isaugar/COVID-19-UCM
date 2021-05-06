from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.functions import udf,substring, length, col, expr
from pyspark.sql.types import *
import pandas as pd
import numpy as np
import string
import sys

#leemos el pais por consola
country = sys.argv[1]
state = None
if len(sys.argv) == 3 :
	state = sys.argv[2]

#creamos la sesion de spark
spark=SparkSession.builder.master("local[*]").appName("rating").getOrCreate()
spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")

#leemos todso los csv con los datos
if country == "US":
	df=spark.read.option("header","true").option("inferSchema","true").csv("./Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports_us/*.csv")
else:
	df=spark.read.option("header","true").option("inferSchema","true").csv("./Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/*.csv")

#filtramos por el pais que nos interesa
if state is None:
	ret  = df.withColumn('Lat', regexp_replace('Lat', 'Unknown', '')).filter((df['Country_Region'] == country) & (df['Lat'] != '')).sort(df.Last_Update.asc())
else:
	ret  = df.withColumn('Lat', regexp_replace('Lat', 'Unknown', '')).filter((df['Country_Region'] == country) & (df['Province_State'] == state) & (df['Lat'] != '')).sort(df.Last_Update.asc())

#1 cogemos substring y tranformamos en fecha 
#2 seleccionamos las columnas que nos interesan
if country == "US":
	pandasRet = 	ret.select(col('Country_Region').cast(StringType()),col('Province_State').cast(StringType()),ret['Lat'].cast(FloatType()),ret['Long_'].cast(FloatType()),when(to_date(col("Last_Update"),"M/d/yy").isNotNull(),to_date(col("Last_Update"),"M/d/yy")).otherwise(to_date(col("Last_Update"),"yyyy-MM-dd")).alias("Last_Update1"),ret['Confirmed'].cast(IntegerType()),ret['Deaths'].cast(IntegerType()),ret['Recovered'].cast(IntegerType()),ret['Active'].cast(IntegerType()),ret['People_Tested'].cast(IntegerType()),ret['People_Hospitalized'].cast(IntegerType())).orderBy(col("Country_Region").asc(),col("Province_State").asc(),col("Last_Update1").asc()).na.fill("").toPandas()

else:
	pandasRet = ret.select(col('Country_Region').cast(StringType()),col('Province_State').cast(StringType()),ret['Lat'].cast(FloatType()),ret['Long_'].cast(FloatType()),when(to_date(col("Last_Update"),"M/d/yy").isNotNull(),to_date(col("Last_Update"),"M/d/yy")).otherwise(to_date(col("Last_Update"),"yyyy-MM-dd")).alias("Last_Update1"),ret['Confirmed'].cast(IntegerType()),ret['Deaths'].cast(IntegerType()),ret['Recovered'].cast(IntegerType()),ret['Active'].cast(IntegerType())).orderBy(col("Country_Region").asc(),col("Province_State").asc(),col("Last_Update1").asc()).na.fill("").toPandas()




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
if country == "US": 
	pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) | (pandasRet['Province_State'] == "")  ) , 'Daily_Tested'] = pandasRet['People_Tested'] - pandasRet['People_Tested'].shift(1)
	pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Tested'] = pandasRet['People_Tested']

	pandasRet.loc[(pandasRet['Country_Region'] == pandasRet['Country_Region'].shift(1)) & ((pandasRet['Province_State'] == pandasRet['Province_State'].shift(1)) | (pandasRet['Province_State'] == "")  ) , 'Daily_Hospitalized'] = pandasRet['People_Hospitalized'] - pandasRet['People_Hospitalized'].shift(1)
	pandasRet.loc[(pandasRet['Country_Region'] != pandasRet['Country_Region'].shift(1)) | (pandasRet['Province_State'] != pandasRet['Province_State'].shift(1)), 'Daily_Hospitalized'] = pandasRet['People_Hospitalized']



#Eliminamos fechas repetidas de los csv cuando no se daban datos diarios
pandasRes = pandasRet.loc[(pandasRet['Last_Update1'] != pandasRet['Last_Update1'].shift(1)) ]

#con esto ponemos a Null los valores incoherente (que son menores que los anteriores siendo acumulados)

pandasRes.loc[(pandasRet['Daily_Recovered']) < 0, 'Daily_Recovered' ] = np.NaN

pandasRes.loc[(pandasRet['Daily_Deaths']) < 0, 'Daily_Deaths' ] = np.NaN

pandasRes.loc[(pandasRet['Daily_Confirmed']) < 0, 'Daily_Confirmed' ] = np.NaN

if country == "US":

	pandasRes.loc[(pandasRet['Daily_Tested']) < 0, 'Daily_Tested' ] = np.NaN

	pandasRes.loc[(pandasRet['Daily_Hospitalized']) < 0, 'Daily_Hospitalized' ] = np.NaN



#con la funcion pad() usamos el primer valor no nulo anterior


if state is None:

	pandasRes['Daily_Recovered'] = pandasRes['Daily_Recovered'].pad()

	pandasRes['Daily_Deaths'] = pandasRes['Daily_Deaths'].pad()

	pandasRes['Daily_Confirmed'] = pandasRes['Daily_Confirmed'].pad()

	if country == "US":
		pandasRes['Daily_Tested'] = pandasRes['Daily_Tested'].pad()
		pandasRes['Daily_Hospitalized'] = pandasRes['Daily_Hospitalized'].pad()
else:
	pandasRes['Daily_Recovered'] = pandasRes['Daily_Recovered'].interpolate().round(0)

	pandasRes['Daily_Deaths'] = pandasRes['Daily_Deaths'].interpolate().round(0)

	pandasRes['Daily_Confirmed'] = pandasRes['Daily_Confirmed'].interpolate().round(0)

	if country == "US":
		pandasRes['Daily_Tested'] = pandasRes['Daily_Tested'].interpolate().round(0)
		pandasRes['Daily_Hospitalized'] = pandasRes['Daily_Hospitalized'].interpolate().round(0)

#Calculo Tasa incidencia
pandasRes["IP"] = (pandasRes["Daily_Confirmed"] + pandasRes["Daily_Deaths"]) - pandasRes["Daily_Recovered"]


#Comprobamos tipos y si se han devuelto datos
pandasRet.info()
pandasRes.info()

#Guardamos en csv
if state is None:
	pandasRes.to_csv(country + "-Pad-"  + ".csv")
else:
	pandasRes.to_csv(country  + "-Interpolate-" + state + ".csv")




