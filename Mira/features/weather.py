import requests
from Mira.config import config



weather_api_key = "b2a5261e84b941c1bc7e6ef0abfd1966"



def get_current_weather(city):
    try:
        current_weather_url = "https://api.weatherbit.io/v2.0/current?&city=" + city + "&key=" + weather_api_key
        current_weather = requests.get(current_weather_url).json()
        temperature = current_weather["data"][0]["temp"]
        description = current_weather["data"][0]["weather"]["description"]
        current_weather_result = "The temperature in " + city.capitalize() + " is " + str(temperature) + " degrees celcius and you can see " + description

        return current_weather_result
    except Exception as e:
        print(e)
        return "Sorry, I couldn't find the city in my database. Please try again"
    
def get_weather_forecast(city):
    try:
        weather_forecast_url = "https://api.weatherbit.io/v2.0/forecast/daily?city=" + city + "&key=" + weather_api_key
        weather_forecast = requests.get(weather_forecast_url).json()

        return weather_forecast
    except Exception as e:
        print(e)
        return "Sorry, I couldn't find the city in my database. Please try again"