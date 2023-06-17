import requests
import json

# Define your location coordinates

latitude= 28.237118# Latitude of first coordinate
longitude = 83.982767
distance = 1000  # Distance in meters

# Send the request
url = f'https://overpass-api.de/api/interpreter?data=[out:json];node(around:{distance},{latitude},{longitude})["building"];out;'
response = requests.get(url)

# Check the response status
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
  

    # Process the data
    for result in data['elements']:
        building = result.get('tags', {}).get('building', 'N/A')
        name = result.get('tags', {}).get('name', 'N/A')
        print(f"Building Type: {building}\nName: {name}\n")

else:
    print(f"Request failed with status code: {response.status_code}")
