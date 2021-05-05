#!/bin/sh
echo **************INIT ENVIROMENT******************


echo ***********UPDATING CSV****************
ls -la
DIR="/home/ubuntu/Covid/COVID-19/"

if [ -d $DIR ];
then
cd /home/ubuntu/Covid/COVID-19/
pwd
git init
git remote remove origin
git remote add origin https://github.com/CSSEGISandData/COVID-19.git 
git fetch origin
git reset --hard origin/master
else
mkdir -p ~/Covid/
cd ~/Covid/ 
git clone https://github.com/CSSEGISandData/COVID-19.git
fi


echo *************PROCESSING DATA****************


#rm -rf  ~/aux 
cd /home/ubuntu/Covid/COVID-19 
mkdir -p ./tmp/

mv  /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-22-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-23-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-24-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-25-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-26-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-27-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-28-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-29-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-30-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/01-31-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-01-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-02-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-03-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-04-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-05-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-06-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-07-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-08-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-09-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-10-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-11-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-12-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-13-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-14-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-15-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-16-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-17-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-18-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-19-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-20-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-21-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-22-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-23-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-24-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-25-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-26-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-27-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-28-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/02-29-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-01-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-02-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-03-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-04-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-05-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-06-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-07-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-08-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-09-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-10-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-11-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-12-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-13-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-14-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-15-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-16-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-18-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-19-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-20-2020.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-21-2020.csv /home/ubuntu/Covid/COVID-19/tmp/

DIR="/home/ubuntu/Covid/COVID-19/aux/"
if [ -d $DIR ];
then
echo 
else
spark-submit ~/ChangeFormat.py
mv /home/ubuntu/Covid/COVID-19/aux/*.csv /home/ubuntu/Covid/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/
fi



rm -fr /home/ubuntu/Covid/COVID-19/tmp/ 





