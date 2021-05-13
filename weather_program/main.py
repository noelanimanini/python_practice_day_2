# asks the user to input the city town, etc and returns the weather in the city. 
import requests
from pprint import pprint 

API_Key = "8858bd401a652b4fbff4bfe16d054ae5"

city = input("Enter your city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_Key 

weather_data = requests.get(base_url).json()

pprint(weather_data)