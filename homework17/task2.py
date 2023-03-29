import requests
import json
while True:
    city = input('Enter the name of the city: ')
    url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
    try:
        response = requests.get(url).json()
        lat = float(response['results'][0]['latitude'])
        long = float(response['results'][0]['longitude'])
        url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=1'
        response = requests.get(url).json()
        print(f"The current temperature in {city} is {response['current_weather']['temperature']} degrees Celsius")
    except KeyError:
        print("Coordinates for this city could not be found. Try another city.")
