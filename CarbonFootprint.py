import json
import requests
import Conversion

data = requests.get(" https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyB8mwGnOAP0eqxFlLXyOsO2BJC6ubBXqQI")
print(data.json())

