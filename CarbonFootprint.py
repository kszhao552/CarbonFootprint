import json
import requests
import Conversion
from UserInterface import UserInterface
from APIFunctions import Path
import PySimpleGUI as sg


totalCarbon = 0
tripCarbon = 0
path = Path()
path.GUI.SecondInterface()
kwh = path.GUI.kwh * 12
gallonsPropane = path.GUI.gallonsPropane * 12
cubicFeetNatGas = path.GUI.cubicFeetNatGas * 12
gallonsHeatOil = path.GUI.gallonsHeatOil * 12
distance = path.distance
distance = Conversion.MetersToMiles(distance)
time = path.time
fuelEconomy = path.GUI.fuelEconomy
diesel = path.GUI.diesel
airDistance = path.GUI.airDistance
gallonsDriven = Conversion.GallonsUsed(fuelEconomy,distance)

totalCarbon += Conversion.ElecToCO2(kwh)
totalCarbon += Conversion.HeatingOilToCO2(gallonsHeatOil)
totalCarbon += Conversion.NatGasToCO2(cubicFeetNatGas)
totalCarbon += Conversion.PropaneToCO2(gallonsPropane)
if diesel:
    tripCarbon += Conversion.DieseltoCO2(gallonsDriven)
else:
    tripCarbon += Conversion.UnleadedToCO2(gallonsDriven)
totalCarbon += Conversion.AirTravelToCO2(airDistance)
totalCarbon = round(totalCarbon)

sg.popup("Your annual carbon footprint is", totalCarbon, "Ibs CO₂/year", "With this trip, your carbon footprint will increase by", tripCarbon, "Ibs CO₂")
