
import requests # pip install requests
import json

api_key = 'f3d6d1f6c418203d3d2c727199918c83'

def get_weather(city, api_key):
    """
    This function retrieves the weather data for a city using the Open Weather Map API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" 
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None
