# Importing cowsay and sys library.
import cowsay # pip install cowsay
import sys
# The 'get_weather' function and the 'api_key' variable is imported from the 'weatherQuery' python file.
from weatherQuery import get_weather, api_key

def trex_weather(city):
    """
    This function retrieves the weather data for a city chosen by the user and displays it in an ascii T-rex's speech bubble. 
    """
    weather_data = get_weather(city, api_key)
    if weather_data:
        # Setting variables equal to the temperature, humidity and weather description from weather_data.
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        message = (
            f"Weather in {city}:\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Description: {description}" )
        
        # Displays the ascii T-rex with the message in the speech bubble.
        cowsay.trex(message)
    else:
        # If the city typed in by the user cannot be fetched, the error message below is displayed.
        print(f"The weather data for {city} could not be found.")

# Checking whether the correct number of arguments have been run on the command line.
# sys.argv[0]:'dinosaur.py'
# sys.argv[1]: city name
if len(sys.argv) != 2:
    print("Please type the name of the city in speech marks after python dinosaur.py")
    print('Example: python dinosaur.py "Canterbury" ')
    # Terminating program with an error.
    sys.exit(1)

# The city from the command line argument is retrieved.       
city = sys.argv[1]
# The 'trex_weather' function is called.
trex_weather(city)


## The arguments below are what I typed into the command prompt.
# cd "C:\Users\risha\Desktop\UNI\ASSIGNMENTS\Y1\Python tasks\Assignment 3 TEST"
# python dinosaur.py "Canterbury"
