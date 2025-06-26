import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file 
load_dotenv()  # Loads API key from .env
API_KEY = os.getenv('WEATHER_API_KEY')

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """Fetch weather data for a given city name using OpenWeatherMap API."""
    if not API_KEY:
        raise ValueError("API key is not set. Please set the WEATHER_API_KEY environment variable.")
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error fetching weather data: {response.status_code} - {response.text}")


if __name__ == "__main__":
    print("🌤️ Welcome to the Weather CLI App!")
    city = input(" Please enter a city name to get weather info: ")
    try:
        weather_data = get_weather(city)
        print(json.dumps(weather_data, indent=4))  # Print the weather data in a pretty format
    except Exception as e:
        print(f"An error occurred: {e}")