import requests
import json
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert decimal degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radius of the Earth in kilometers
    radius = 6371

    # Calculate the distance
    distance = radius * c

    return distance



# Send the request
url = 'https://overpass-api.de/api/interpreter?data=[out:json];area[name="Pokhara"];node(area)["amenity"="dentist"];out;'
response = requests.get(url)
lat1 = 28.237118# Latitude of first coordinate
lon1 = 83.982767

# Check the response status
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Process the data
    for result in data['elements']:
        name = result.get('tags', {}).get('name', 'N/A')
        latitude = result.get('lat', 'N/A')
        longitude = result.get('lon', 'N/A')
        distance=calculate_distance(lat1, lon1, latitude, longitude)
        print(f"Name: {name}\nLatitude: {latitude}\nLongitude: {longitude}\n {distance}")

else:
    print(f"Request failed with status code: {response.status_code}")




