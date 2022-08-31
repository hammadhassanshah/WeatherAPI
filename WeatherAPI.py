import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "41e48edf7333fc47a9cac41eddebfec6"

CITY = input("Please enter the name of your city:",)


def kelvin_to_celsius_farenheit(kelvin):
    celsius = kelvin - 273.15
    farenheit = celsius * (9/5) + 32
    return celsius, farenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)


temp_kelvin = response['main']['temp']
temp_celsius, temp_farenheit = kelvin_to_celsius_farenheit(temp_kelvin)
feels_like_kelvin = response['main']['temp']
feels_like_celsius, feels_like_farenheit = kelvin_to_celsius_farenheit(
    feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(
    response['sys']['sunrise']+response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(
    response['sys']['sunset']+response['timezone'])


print(f"Temperature in {CITY}: {temp_celsius: .2f}°C or {temp_farenheit}°F")
print(
    f"Temperature in {CITY} feels like: {feels_like_celsius: .2f}°C or {feels_like_farenheit}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print("General Weather in {CITY}: {description}")
print(f"Sunrises in {CITY} at {sunrise_time} local time.")
print(f"Sun sets in {CITY} at {sunset_time} local time.")
