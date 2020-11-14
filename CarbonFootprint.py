import json
import requests


data = requests.get(" https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyCUwwh5NUdfGua-7zBV2-CJSDAadu1FJz0")
print(data.json())

#conversion values
ELECTRICTYKWH = .953
HEATINGOIL = 22.3989
NATURALGASS100CUBICFT = 11.7065
PROPANE = 12.6986

UNLEADED = 19.3565
DIESEL = 22.5092

