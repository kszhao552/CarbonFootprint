import json
import requests
import Conversion
import Comparisons
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
totalDistance = path.GUI.carDistance
time = path.time
fuelEconomy = path.GUI.fuelEconomy
diesel = path.GUI.diesel
airDistance = path.GUI.airDistance
gallonsDriven = Conversion.GallonsUsed(fuelEconomy,distance)
totalGallonsDriven = Conversion.GallonsUsed(fuelEconomy,totalDistance)
totalCarbon += Conversion.ElecToCO2(kwh)
totalCarbon += Conversion.HeatingOilToCO2(gallonsHeatOil)
totalCarbon += Conversion.NatGasToCO2(cubicFeetNatGas)
totalCarbon += Conversion.PropaneToCO2(gallonsPropane)
if diesel:
    tripCarbon += Conversion.DieseltoCO2(gallonsDriven)
    totalCarbon += Conversion.DieseltoCO2(totalGallonsDriven)
else:
    tripCarbon += Conversion.UnleadedToCO2(gallonsDriven)
    totalCarbon += Conversion.UnleadedToCO2(totalGallonsDriven)

totalCarbon += Conversion.AirTravelToCO2(airDistance)
totalCarbon = round(totalCarbon)

sg.popup(f"Your annual carbon footprint is {totalCarbon} Ibs CO₂/year.\nWith this trip, your carbon footprint will increase by {tripCarbon} Ibs CO₂")

totalCarbon += tripCarbon

while True:
    var = path.GUI.ThirdInterface()
    if var == -1:
        break

    sg.popup(f"Your annual carbon footprint is {totalCarbon} Ibs CO₂/year.\nWith this trip, your carbon footprint will increase by {tripCarbon} Ibs CO₂")
    totalCarbon += tripCarbon
totalCarbon = round(totalCarbon)
totalResult = Comparisons.totalFootprintComp(totalCarbon)
if (totalResult[1] == 1):
    totalComparison = 'less'
else:
    totalComparison = 'more'

sg.popup(f"Your annual carbon footprint is\n{totalCarbon} Ibs CO₂/year.\n Your usage is {totalResult[0]} % {totalComparison} compared to the national average")