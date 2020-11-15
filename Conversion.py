#conversion values
ELECTRICTYKWH = .953
HEATINGOILGALLON = 22.3989
NATURALGASS100CUBICFT = 11.7065
PROPANEGALLON = 12.6986

UNLEADEDGALLON = 19.3565
DIESELGALLON = 22.5092
AIRTRAVELPERMILE = .4409

METERSTOMILESDIVISOR = 1609

ROUND = 2

def ElecToCO2(kwh):
   return round(kwh * ELECTRICTYKWH, ROUND)

def HeatingOilToCO2(gallons):
    return round(gallons * HEATINGOILGALLON, ROUND)

def NatGasToCO2(cubicft):
    return round(cubicft * NATURALGASS100CUBICFT, ROUND)

def PropaneToCO2(gallons):
    return round(gallons * PROPANEGALLON, ROUND)

def UnleadedToCO2(gallons):
    return round(gallons * UNLEADEDGALLON, ROUND)

def DieseltoCO2(gallons):
    return round(gallons * DIESELGALLON, ROUND)

def AirTravelToCO2(miles):
    return round(miles * AIRTRAVELPERMILE, ROUND)

def GallonsUsed(fuelEconomy, distance):
    return round(float(distance/fuelEconomy), ROUND)

def MetersToMiles(meters):
    return round(float(distance/METERSTOMILESDIVISOR = 1609), ROUND)