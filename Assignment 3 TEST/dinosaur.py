import cowsay
import sys
from weatherQuery import get_weather

api_key = 'f3d6d1f6c418203d3d2c727199918c83'

def trex_weather(city):
    weather_data = get_weather(city, api_key)
    
    if weather_data:
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
            
        message = (
            f"The weather in {city} is {description} "
            f"with a temperature of {temperature}°C."
        )
        cowsay.trex(message)
    else:
        print(f"Could not retrieve weather data for {city}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dinosaur.py <city>")
        sys.exit(1)
        
    city = sys.argv[1]
    trex_weather(city)
