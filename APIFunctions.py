
import json
import requests

class Path:
    def __init__(self, origin,destination):
        self.origin = origin
        self.destination = destination



def get_address_id(address):
    clean_add = address.replace(" ","%20")
    loc_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+clean_add + "&key="+"AIzaSyAYZcB1L-QlsdsJSP-gYx7pkPreirPET1Q")
    return loc_response.json()['results'][0]['place_id']

