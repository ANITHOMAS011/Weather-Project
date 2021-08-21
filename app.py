import requests
import time
import pandas as pd
from pymongo import MongoClient
from flask import Flask, render_template

app = Flask(__name__)

client = MongoClient("mongodb+srv://Ani:WeatherCan@cluster0.i5fm0.mongodb.net/WeatherDB?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.get_database('WeatherDB')


r1 = requests.get("http://api.weatherapi.com/v1/current.json?key=e8ff6d7f35334f22a7c192339211708&q=New York&aqi=no")
r2 = requests.get("http://api.weatherapi.com/v1/current.json?key=e8ff6d7f35334f22a7c192339211708&q=Sydney&aqi=no")
r3 = requests.get("http://api.weatherapi.com/v1/current.json?key=e8ff6d7f35334f22a7c192339211708&q=Toronto&aqi=no")
r4 = requests.get("http://api.weatherapi.com/v1/current.json?key=e8ff6d7f35334f22a7c192339211708&q=Delhi&aqi=no")
r5 = requests.get("http://api.weatherapi.com/v1/current.json?key=e8ff6d7f35334f22a7c192339211708&q=London&aqi=no")
#while True:
if r1.status_code == 200:
    newyork = r1.json()
    print(newyork)
    db.Toronto.insert_one(newyork)
    #time.sleep(60)
else:
    exit()
if r2.status_code == 200:
    sydney = r2.json()
    print(sydney)
    db.Toronto.insert_one(sydney)
    #time.sleep(60)
else:
    exit()
if r3.status_code == 200:
    toronto = r3.json()
    print(toronto)
    db.Toronto.insert_one(toronto)
    #time.sleep(60)
else:
    exit()
if r4.status_code == 200:
    delhi = r4.json()
    print(delhi)
    db.Toronto.insert_one(delhi)
    #time.sleep(60)
else:
    exit()
if r5.status_code == 200:
    london = r5.json()
    print(london)
    db.Toronto.insert_one(london)
    #time.sleep(60)
else:
    exit()


@app.route('/')
def home():
    newyork = r1.json()
    sydney = r2.json()
    toronto = r3.json()
    delhi = r4.json()
    london = r5.json()
    return render_template('pages/homePage.html', **locals())


# %% Toronto
@app.route('/toronto')
def toronto():
    toronto = r3.json()
    cityName = toronto['location']['name']
    condition = toronto['current']['condition']['text']
    temp_c = toronto['current']['temp_c']
    country= toronto['location']['country']
    localtime = toronto['location']['localtime']
    humidity = toronto['current']['humidity']
    precipitation = toronto['current']['precip_mm']
    wind = toronto['current']['wind_kph']
    pressure = toronto['current']['pressure_in']

    return render_template('pages/Toronto.html', **locals())

# %% Delhi
@app.route('/delhi')
def delhi():
    delhi = r4.json()
    cityName = delhi['location']['name']
    condition = delhi['current']['condition']['text']
    temp_c = delhi['current']['temp_c']
    country= delhi['location']['country']
    localtime = delhi['location']['localtime']
    humidity = delhi['current']['humidity']
    precipitation = delhi['current']['precip_mm']
    wind = delhi['current']['wind_kph']
    pressure = delhi['current']['pressure_in']

    return render_template('pages/Delhi.html', **locals())

# %% New York
@app.route('/newyork')
def newyork():
    newyork = r1.json()
    cityName = newyork['location']['name']
    condition = newyork['current']['condition']['text']
    temp_c = newyork['current']['temp_c']
    country= newyork['location']['country']
    localtime = newyork['location']['localtime']
    humidity = newyork['current']['humidity']
    precipitation = newyork['current']['precip_mm']
    wind = newyork['current']['wind_kph']
    pressure = newyork['current']['pressure_in']

    return render_template('pages/New York.html', **locals())

# %% Sydney
@app.route('/sydney')
def sydney():
    sydney = r2.json()
    cityName = sydney['location']['name']
    condition = sydney['current']['condition']['text']
    temp_c = sydney['current']['temp_c']
    country= sydney['location']['country']
    localtime = sydney['location']['localtime']
    humidity = sydney['current']['humidity']
    precipitation = sydney['current']['precip_mm']
    wind = sydney['current']['wind_kph']
    pressure = sydney['current']['pressure_in']

    return render_template('pages/Sydney.html', **locals())

# %% London
@app.route('/london')
def london():
    london = r5.json()
    cityName = london['location']['name']
    condition = london['current']['condition']['text']
    temp_c = london['current']['temp_c']
    country= london['location']['country']
    localtime = london['location']['localtime']
    humidity = london['current']['humidity']
    precipitation = london['current']['precip_mm']
    wind = london['current']['wind_kph']
    pressure = london['current']['pressure_in']

    return render_template('pages/London.html', **locals())


#time.sleep(60)

if __name__ == "__main__":
    app.run()