
import json
import requests

class Path:
    def __init__(self, origin,destination):
        self.origin = get_address_id(origin)
        self.destination = get_address_id(destination)
        self.distance = get_distance(self.origin,self.destination)


    



def get_address_id(address):
    clean_add = address.replace(" ","%20")
    loc_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+clean_add + "&key="+"AIzaSyAYZcB1L-QlsdsJSP-gYx7pkPreirPET1Q")
    return loc_response.json()['results'][0]['place_id']


def get_distance(start,end):
    response = requests.get(f"https://maps.googleapis.com/maps/api/distancematrix/json?origins=place_id:{start}&destination=place_id:{end}&key=AIzaSyAYZcB1L-QlsdsJSP-gYx7pkPreirPET1Q")
    return response.json()#     ['rows'][0]["elements"][0]["distance"]["value"]

x = Path("Boston University","Boston Common")
print(x.distance)