avgKwh = 877 * 12 # The average amount of kilowatt hours of electricity consumed per person per year
avgHeatOil = 1.489 * 12 # The average amount of gallons of heating oil consumed per person per year
avgNatGas = 2.14 * 12 # The average amount of gallons of natural gas consumed per person per year
avgPropane = 15.04 * 12 # The average amount of gallons of propane consumed per person per year
avgGasDriven = 48.598 * 12 # The average amount of gallons of gasoline consumed per person per year
avgMilesFlown = 1946.7 # The average amount of miles flown per person per year
avgFootPrint = 53898 # The average amount of pounds of CO2 produced per person per year

def kwhComp(userConsumption):
    ratio = userConsumption / avgKwh
    if (ratio > 1):
        ratio -= 1
        betterThanAverage = 0
    else:
        ratio -= 1
        ratio *= -1
        betterThanAverage = 1
    percentDiff = ratio * 100
    percentDiff = round(percentDiff, 2)   
    return [percentDiff, betterThanAverage]

def heatOilComp(userConsumption):
    ratio = userConsumption / avgHeatOil
    if (ratio > 1):
        ratio -= 1
        betterThanAverage = 0
    else:
        ratio -= 1
        ratio *= -1
        betterThanAverage = 1
    percentDiff = ratio * 100
    percentDiff = round(percentDiff, 2)   
    return [percentDiff, betterThanAverage]

def natGasComp(userConsumption):
    ratio = userConsumption / avgNatGas
    if (ratio > 1):
        ratio -= 1
        betterThanAverage = 0
    else:
        ratio -= 1
        ratio *= -1
        betterThanAverage = 1
    percentDiff = ratio * 100
    percentDiff = round(percentDiff, 2)   
    return [percentDiff, betterThanAverage]

def propaneComp(userConsumption):
    ratio = userConsumption / avgPropane
    if (ratio > 1):
        ratio -= 1
        betterThanAverage = 0
    else:
        ratio -= 1
        ratio *= -1
        betterThanAverage = 1
    percentDiff = ratio * 100
    percentDiff = round(percentDiff, 2)   
    return [percentDiff, betterThanAverage]

def gasComp(userConsumption):
    ratio = userConsumption / avgGasDriven
    if (ratio > 1):
        ratio -= 1
        betterThanAverage = 0
    else:
        ratio -= 1
        ratio *= -1
        betterThanAverage = 1
    percentDiff = ratio * 100
    percentDiff = round(percentDiff, 2)   
    return [percentDiff, betterThanAverage]

def airMilesComp(userConsumption):
    ratio = userConsumption / avgMilesFlown
    if (ratio > 1):
        ratio -= 1
        betterThanAverage = 0
    else:
        ratio -= 1
        ratio *= -1
        betterThanAverage = 1
    percentDiff = ratio * 100
    percentDiff = round(percentDiff, 2)   
    return [percentDiff, betterThanAverage]

def totalFootprintComp(userConsumption):
    ratio = userConsumption / avgFootPrint
    if (ratio > 1):
        ratio -= 1
        betterThanAverage = 0
    else:
        ratio -= 1
        ratio *= -1
        betterThanAverage = 1
    percentDiff = ratio * 100
    percentDiff = round(percentDiff, 2)   
    return [percentDiff, betterThanAverage]