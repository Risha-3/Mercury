# Importing cowsay and sys library
import cowsay
import sys
# The 'get_weather' function and the 'api_key' variable is imported from the 'weatherQuery' python file.
from weatherQuery import get_weather, api_key

def trex_weather(city):
    """
    This function retrieves data from the API which holds weather data in dictionary format. 
    """
    weather_data = get_weather(city, api_key)
    if weather_data:
        # Setting variables equal to the temperature, humidity and weather description from the ---.
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        message = (
            f"Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Description: {description}"
        )
        # Displays the message in the t-rex's speech bubble.
        cowsay.trex(message)
    else:
        # If the city typed in by the user cannot be found in the ---, the message below is displayed.
        print(f"The weather data for {city} could not be found.")

if len(sys.argv) != 2:
    print("Usage: python dinosaur.py <city>")
    sys.exit(1)
        
city = sys.argv[1]
trex_weather(city)

# /home/codespace/.python/current/bin/python3 "/workspaces/Mercury/Assignment 3 TEST/dinosaur.py" "Canterbury"
