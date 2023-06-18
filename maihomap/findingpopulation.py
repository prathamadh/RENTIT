import requests

url = 'https://overpass-api.de/api/interpreter?data=[out:json];area(around:1000, latitude, longitude)["amenity"="dentist"];out;'
# Replace latitude and longitude with the coordinates of the location you want to search around

response = requests.get(url)

# Access the response data, which will be in JSON format
data = response.json()
print(data)
         