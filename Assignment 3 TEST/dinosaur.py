import cowsay
import sys
from weatherQuery import get_weather

api_key = 'f3d6d1f6c418203d3d2c727199918c83'

def trex_weather(city):
    weather_data = get_weather(city, api_key)
    
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
            
        message = (
            f"Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Description: {description}"
        )
        cowsay.trex(message)
    else:
        print(f"The weather data for {city} could not be found.")

if len(sys.argv) != 2:
    print("Usage: python dinosaur.py <city>")
    sys.exit(1)
        
city = sys.argv[1]
trex_weather(city)

# /home/codespace/.python/current/bin/python3 "/workspaces/Mercury/Assignment 3 TEST/dinosaur.py" "Kent"