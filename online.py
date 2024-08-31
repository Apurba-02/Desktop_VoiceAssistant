import sys
import requests
import pywhatkit as kit

# Set the default encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def find_my_ip():
    ip_response = requests.get('http://api.ipapi.com/api/check?access_key=').json()
    city = ip_response["city"]
    return city

def weather_forecast(city):
    api_key = ''  
    weather_response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}").json()
    weather = weather_response["weather"][0]["main"]
    temp = weather_response["main"]["temp"]
    feels_like = weather_response["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

