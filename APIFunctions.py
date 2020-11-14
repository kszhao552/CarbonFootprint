
import json
import requests
from UserInterface import UserInterface
import config 

class Path:
    def __init__(self):
        GUI = UserInterface()
        
        
        while( True ) :
            GUI.Interface()
            self.origin= get_address_code(GUI.origin)
            self.destination = get_address_code(GUI.destination)
            if  self.origin != "No Address Found" and self.destination != "No Address Found":
                break

            
        self.distance, self.time = get_distance_info(self.origin,self.destination)
        

    



def get_address_code(address):
    clean_add = address.replace(" ","%20")
    loc_response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={clean_add}&key={config.api_key}")

    if loc_response.json()["status"] != "OK":
        return "No Address Found"
    
    return loc_response.json()['results'][0]['plus_code']["global_code"]


def get_distance_info(start,end):
    clean_start = start.replace('+','%2B')
    clean_end = end.replace('+','%2B')

    response = requests.get(f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={clean_start}&destinations={clean_end}&key=AIzaSyAYZcB1L-QlsdsJSP-gYx7pkPreirPET1Q")
    distance = response.json()#['rows'][0]["elements"][0]["distance"]["value"]
    time = response.json()#['rows'][0]["elements"][0]["duration"]["value"]
    return distance, round(time/60.0)

