# Project: Fetching current weather data using OpenWeatherMap API.
# This program:
# 1. Reads the location from command line arguments.
# 2. Downloads weather JSON data from OpenWeatherMap.
# 3. Converts JSON string into Python dictionary.
# 4. Prints weather information for today and the next two days.

import json
import requests
import sys

# Check if location is provided
if len(sys.argv) < 2:
    print('Usage: python weather.py city_name')
    sys.exit()

# Get location from command line
location = ' '.join(sys.argv[1:])

# Your API key from OpenWeatherMap
# you can generate your API key from this: https://home.openweathermap.org/api_keys
# apiKey = 'YOUR_API_KEY'

# Build API URL
url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={apiKey}&units=metric'

# Download weather data
print('Fetching weather data...')

response = requests.get(url)

# Check if request was successful
response.raise_for_status()

# Convert JSON response into Python dictionary
weatherData = json.loads(response.text)

# Print city name
print('\nWeather Report for:', weatherData['city']['name'])

# Print weather for today and next two days
for i in range(3):

    # Get forecast data
    weather = weatherData['list'][i * 8]

    # Get weather description
    description = weather['weather'][0]['description']

    # Get temperature
    temperature = weather['main']['temp']

    print('\nDay', i + 1)
    print('Weather:', description)
    print('Temperature:', str(temperature) + '°C')