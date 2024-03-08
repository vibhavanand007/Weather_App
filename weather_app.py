#weather_API(https://www.weatherapi.com/)

import requests
import json
import time

def greeting():
    timestamp = time.strftime("%H:%M:%S")
    # print(timestamp)
    timestamp_H = int(time.strftime("%H"))
    # timestamp_H = int(input("Time_ "))
    if (20< timestamp_H or timestamp_H <=4):
        print("Hola,./!#,.")
    elif (16< timestamp_H <=20):
        print("Hola, Good Evening")
    elif (11< timestamp_H <=16):
        print("Hola, Good Afternoon")
    elif (4< timestamp_H <=11):
        print("Hola,Good Morning")

greeting()


city = input("Enter the name of city\n::")
url = f"https://api.weatherapi.com/v1/current.json?key=667c519607424ec993384321240803&q={city}"

r = requests.get(url)
weather_dic =  json.loads(r.text)
# print(weather_dic)
country = weather_dic["location"]["country"]
state = weather_dic["location"]["region"]
latitude = weather_dic["location"]["lat"]
longitude = weather_dic["location"]["lon"]
localtime = weather_dic["location"]["localtime"]
temp_c = weather_dic["current"]["temp_c"]
feelslike_c = weather_dic["current"]["feelslike_c"]
temp_f = weather_dic["current"]["temp_f"]
feelslike_f = weather_dic["current"]["feelslike_f"]
wind_dir = weather_dic["current"]["wind_dir"]
humidity = weather_dic["current"]["humidity"]

print(f"LOCAL TIME : {localtime}")
print(f"COUNTRY_{country}")
print(f"STATE_{state}")
print(f"LATITUDE-{latitude}     LONGITUDE-{longitude}")
print(f"TEMP {temp_c} C     FEELS LIKE {feelslike_c} C")
print(f"TEMP {temp_f} F     FEELS LIKE {feelslike_f} F")
print(f"HUMIDITY {humidity}")
print(f"WIND DIR '{wind_dir}'")