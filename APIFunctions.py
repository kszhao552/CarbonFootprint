import json
import requests
import sys
from UserInterface import UserInterface
import config 

class Path:
    def __init__(self):
        self.GUI = UserInterface()
        self.origin_lat = 0
        self.origin_lng = 0
        self.destination_lat =0
        self.destination_lng = 0
        
        while( True ) :
            bar = self.GUI.Interface()
            if bar == -1:
                sys.exit()
            self.origin_lat,self.origin_lng= get_address_code(self.GUI.origin)

            self.destination_lat,self.destination_lng = get_address_code(self.GUI.destination)
            if self.origin_lng != None and self.destination_lng != None:
                break

            
        self.distance, self.time = get_distance_info(self.origin_lat,self.origin_lng,self.destination_lat,self.destination_lng)

    def destinations(self):
        self.origin_lat = 0
        self.origin_lng = 0
        self.destination_lat =0
        self.destination_lng = 0
        
        while( True ) :
            bar = self.GUI.ThirdInterface()
            if bar == -1:
                return -1
            self.origin_lat,self.origin_lng= get_address_code(self.GUI.origin)

            self.destination_lat,self.destination_lng = get_address_code(self.GUI.destination)
            if self.origin_lng != None and self.destination_lng != None:
                break
        self.distance, self.time = get_distance_info(self.origin_lat,self.origin_lng,self.destination_lat,self.destination_lng)
        return 0


    



def get_address_code(address):
    clean_add = address.replace(" ","%20")
    loc_response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={clean_add}&key={config.api_key}").json()

    if loc_response["status"] != "OK":
        return None,None
    
    return loc_response['results'][0]['geometry']["location"]["lat"],loc_response['results'][0]['geometry']["location"]["lng"]


def get_distance_info(startlat,startlong,endlat,endlong):
    print(startlat,startlong,endlat,endlong)
    response = requests.get(f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={startlat},{startlong}&destinations={endlat},{endlong}&key={config.api_key}").json()
    distance = response['rows'][0]["elements"][0]["distance"]["value"]
    time = response['rows'][0]["elements"][0]["duration"]["value"]
    return distance, round(time/60.0)
