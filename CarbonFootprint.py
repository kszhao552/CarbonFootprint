import json
import requests


data = requests.get(" https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyCUwwh5NUdfGua-7zBV2-CJSDAadu1FJz0")
print(data.json())


ELECTRICTYKWH = .953
HEATINGOIL = 10.

GASOLINE = 19.592481

