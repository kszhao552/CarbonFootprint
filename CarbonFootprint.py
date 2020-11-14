import json
import requests


data = requests.get(" https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=KEY")
print(data.json())

#conversion values
ELECTRICTYKWH = .953
HEATINGOILGALLON = 22.3989
NATURALGASS100CUBICFT = 11.7065
PROPANEGALLON = 12.6986

UNLEADEDGALLON = 19.3565
DIESELGALLON = 22.5092
AIRTRAVELPERMILE = .4409
