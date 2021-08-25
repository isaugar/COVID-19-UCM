from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.functions import udf,substring, length, col, expr
from pyspark.sql.types import *
import pandas as pd
import string
import sys

#leemos el pais por consola
#country = sys.argv[1]

#creamos la sesion de spark
spark=SparkSession.builder.master("local[*]").appName("rating").getOrCreate()

#leemos todso los csv con los datos
df =spark.read.option("header","true").option("inferSchema","true").csv("./tmp/*.csv")
df.printSchema()

ret = df.withColumn('FIPS', lit("")).withColumn('Admin2',lit("")).withColumn('Province_State',df['Province/State']).withColumn('Country_Region',df['Country/Region']).withColumn('Last_Update', df['Last Update']).withColumn('Lat', df['Latitude']).withColumn('Long_', df['Longitude']).withColumn('Confirmed', df['Confirmed']).withColumn('Deaths', df['Deaths']).withColumn('Recovered', df['Recovered']).withColumn('Active', lit(0)).withColumn('Combined_Key', lit("")).withColumn('Incident_Rate', lit(0.0)).withColumn('Case_Fatality_Ratio', lit(0.0)).na.fill("0.0", ["Lat"]).na.fill("0.0",["Long_"]).select('FIPS','Admin2','Province_State','Country_Region','Last_Update','Lat','Long_','Confirmed','Deaths','Recovered','Active','Combined_Key','Incident_Rate','Case_Fatality_Ratio')

ret  = ret.withColumn('Country_Region', regexp_replace('Country_Region', 'South Korea', 'Korea, South')).withColumn('Country_Region', regexp_replace('Country_Region', 'Viet Nam', 'Vietnam')).withColumn('Province_State', regexp_replace('Province_State', 'None', '')).withColumn('Country_Region', regexp_replace('Country_Region', 'Viet Nam', 'Vietnam')).withColumn('Country_Region', regexp_replace('Country_Region', 'Bahamas, the', 'Bahamas')).withColumn('Country_Region', regexp_replace('Country_Region', 'Czech Republic', 'Czechia')).withColumn('Country_Region', regexp_replace('Country_Region', 'Gambia, the', 'Gambia')).withColumn('Country_Region', regexp_replace('Country_Region', 'Taiwan*', 'Taiwan')).withColumn('Country_Region', regexp_replace('Country_Region', 'Honk Kong SAR', 'Honk Kong')).withColumn('Country_Region', regexp_replace('Country_Region', 'Iran (Islamic Republic of)', 'Iran')).withColumn('Country_Region', regexp_replace('Country_Region', 'Macao SAR', 'Macau')).write.format("csv").mode('overwrite').option("header","true").save("/home/ubuntu/Covid/COVID-19/aux")









