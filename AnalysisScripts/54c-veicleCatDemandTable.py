from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()


fx = open('finalCarColors.txt', 'r')
carColors = json.loads(fx.read())
fx.close()




loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'  


carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'suv']

studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1



analyzedData = {}

vc = 0
totalTrips = 0


currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


cityCurrencyMap = {}
cityCurrencyMap['Las Vegas'] = 1
cityCurrencyMap['Los Angeles'] =1 
cityCurrencyMap['Miami'] = 1
cityCurrencyMap['New York City'] =1 
cityCurrencyMap['Washington D.C.'] =1 
cityCurrencyMap['Toronto'] = 0.73
cityCurrencyMap['Ottawa'] = 0.73
cityCurrencyMap['Barcelona'] = 1.06
cityCurrencyMap['Berlin'] = 1.06
cityCurrencyMap['Hamburg'] = 1.06
cityCurrencyMap['Liverpool'] = 1.21
cityCurrencyMap['London'] = 1.21
cityCurrencyMap['Lyon'] = 1.06
cityCurrencyMap['Madrid'] = 1.06
cityCurrencyMap['Paris'] = 1.06




studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1


lengthMulMap = {}
lengthMulMap['GerAroundEurope'] = {}
lengthMulMap['GerAroundEurope']['sedan']= 7.17
lengthMulMap['GerAroundEurope']['suv']= 6.98
lengthMulMap['GerAroundEurope']['hatchback']= 6.78
lengthMulMap['GerAroundEurope']['wagon']= 4.8
lengthMulMap['GerAroundEurope']['van/minivan']= 5.5
lengthMulMap['GerAroundEurope']['coupe']= 3
lengthMulMap['GerAroundEurope']['truck']= 1

lengthMulMap['GetAround'] = {}
lengthMulMap['GetAround']['sedan']= 2.891
lengthMulMap['GetAround']['suv']= 2.72
lengthMulMap['GetAround']['hatchback']= 2.72
lengthMulMap['GetAround']['wagon']= 2.14
lengthMulMap['GetAround']['van/minivan']= 2.491
lengthMulMap['GetAround']['coupe']= 1.92
lengthMulMap['GetAround']['truck']= 3.3


lengthMulMap['Turo'] = {}
lengthMulMap['Turo']['sedan']= 7.973
lengthMulMap['Turo']['suv']= 7.22
lengthMulMap['Turo']['hatchback']= 8.21
lengthMulMap['Turo']['wagon']= 8.05
lengthMulMap['Turo']['van/minivan']= 6.87
lengthMulMap['Turo']['coupe']= 5.121
lengthMulMap['Turo']['truck']= 6.661



priceMulMap = {}

priceMulMap = {}
priceMulMap['GetAround'] = {}
priceMulMap['GetAround']['sedan']= 1.546
priceMulMap['GetAround']['suv']= 1.376
priceMulMap['GetAround']['hatchback']= 1.42
priceMulMap['GetAround']['wagon']= 1.41
priceMulMap['GetAround']['van/minivan']= 1.194
priceMulMap['GetAround']['coupe']= 1.76
priceMulMap['GetAround']['truck']= 1.17

priceMulMap['GerAroundEurope'] = {}
priceMulMap['GerAroundEurope']['sedan']= 3
priceMulMap['GerAroundEurope']['suv']= 2.76555
priceMulMap['GerAroundEurope']['hatchback']= 2.52
priceMulMap['GerAroundEurope']['wagon']= 1.45
priceMulMap['GerAroundEurope']['van/minivan']= 1.846
priceMulMap['GerAroundEurope']['coupe']= 1
priceMulMap['GerAroundEurope']['truck']= 1


priceMulMap['Turo'] = {}
priceMulMap['Turo']['sedan']= 2.36
priceMulMap['Turo']['suv']= 2.13
priceMulMap['Turo']['hatchback']= 2.511
priceMulMap['Turo']['wagon']= 2.516
priceMulMap['Turo']['van/minivan']= 1
priceMulMap['Turo']['coupe']= 1.944
priceMulMap['Turo']['truck']= 1.97
for platform in priceMulMap:
    for cat in priceMulMap[platform]:
        priceMulMap[platform][cat] *= 1.2


platFormCatTrip = {}


cityDict = {}
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']




colorVehicleTripsDict = {}
possibleColors = {}

for platform in carColors:
    for city in carColors[platform]:
        for carId in carColors[platform][city]:
            possibleColors[carColors[platform][city][carId]] = 1
# possibleColors = list(possibleColors.keys())
# print(possibleColors)

possibleColors = carCats
# # for color in possibleColors:
# #     possibleColors[color] = {}
# time.sleep(100000)


studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1


vehiclesDict = {}
for cat in carCats:
    vehiclesDict[cat] = {}
    for platform in studiedApps:
        
        vehiclesDict[cat][platform] = {}
        vehiclesDict[cat][platform]['pre']= [0]
        vehiclesDict[cat][platform]['during']= {}
        vehiclesDict[cat][platform]['during']['price'] = [60]
        vehiclesDict[cat][platform]['during']['distance'] = [57]
        vehiclesDict[cat][platform]['during']['util'] = [1.2]

for platform in studiedApps:
    colorVehicleTripsDict[platform] = {}
    # print(platform)
    platFormCatTrip[platform] = {}
    fx = open(loadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()
    catVehicleDict = {}
    v1 = []
    v2 = []
    for cityName in analyzedData[platform]:
        if cityName != 'New York':
            city = cityName
            colorVehicleTripsDict[platform][cityName] = {}
            for color in possibleColors:
                colorVehicleTripsDict[platform][cityName][color] = {}
                # colorVehicleTripsDict[platform][cityName][color]['vehicleIDs'] = []
                colorVehicleTripsDict[platform][cityName][color]['trips'] = []
            # print('\t',cityName)
            fx = open(loadPath +platform+'-'+cityName+'-tripDetails.txt','r')
            tripDetailsDict = json.loads(fx.read())
            fx.close()
            for carId in analyzedData[platform][cityName]:
                vc += 1
                cat = 'sedan'
                
                try:
                    cat = cityServiceCat[platform][cityName][carId][0]
                except:
                    pass

                carDays = analyzedData[platform][cityName][carId]['dates'][2]
                experimentTripsVehicle = abs(analyzedData[platform][cityName][carId]['trips'][1]-analyzedData[platform][cityName][carId]['trips'][0])

                vehiclesDict[cat][platform]['pre'].append(analyzedData[platform][cityName][carId]['trips'][0])

                experimentTripsVehicle = (experimentTripsVehicle/carDays)*30

                vehiclesDict[cat][platform]['during']['util'].append(experimentTripsVehicle)


                for tripObj in tripDetailsDict[platform][cityName][carId]:
                    
                    tripObj['length'] = tripObj['length'] * lengthMulMap[platform][cat]
                    tripObj['price'] = tripObj['price'] *  tripObj['length']# * priceMulMap[platform][cat]
                    tripObj['carId'] = carId
                    tripObj['carCat'] = cat
                    tripObj['platform'] = platform
                    
                    vehiclesDict[cat][platform]['during']['price'].append(tripObj['price'])
                    vehiclesDict[cat][platform]['during']['distance'].append(tripObj['length'])


cityShort = {}
cityShort['Barcelona'] = 'BAR'
cityShort['Berlin'] = 'BER'
cityShort['Hamburg'] = 'HAM'
cityShort['Los Angeles'] = 'LAX'
cityShort['London'] = 'LDN'
cityShort['Liverpool'] = 'LPL'
cityShort['Las Vegas'] = 'LVX'
cityShort['Lyon'] = 'LYN'
cityShort['Madrid'] = 'MAD'
cityShort['Miami'] = 'MIA'
cityShort['New York City'] = 'NYC'
cityShort['Ottawa'] = 'OTW'
cityShort['Paris'] = 'PAR'
cityShort['Toronto'] = 'TRT'
cityShort['Washington D.C.'] = 'WDC'
newHeatMapData = []

carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'suv']

beforeTrips = []
duringTrips = []
distAverage = []
priceAverage= []

pshort = {}
pshort['Turo'] = '\\tr'
pshort['GetAround'] = '\\ga'
pshort['GerAroundEurope'] = '\\gre'

cvar = 0
for cat in carCats:
    tp = []
    th = []
    for platform in studiedApps:
        beforeTrips += vehiclesDict[cat][platform]['pre']
        duringTrips += vehiclesDict[cat][platform]['during']['price']
        distAverage +=vehiclesDict[cat][platform]['during']['distance']
        priceAverage +=vehiclesDict[cat][platform]['during']['price']
        va1 = sum(vehiclesDict[cat][platform]['pre'])
        if va1 > 1000:
            va1 = str(int(va1/1000))+'K'
        va2 =  len(vehiclesDict[cat][platform]['during']['price'])
        if 'sedan' in cat or 'suv' in cat:
            cvar += va2
        if va2 > 1000:
            va2 = str(int(va2/1000))+'K'

        v01= ''
        tp += vehiclesDict[cat][platform]['during']['price']
        th+= vehiclesDict[cat][platform]['during']['distance']

        if 'Turo' in [platform]:
            v01 = '\multirow{3}{*}{'+cat+'}'
        print(
            v01,'&',
            pshort[platform],
            # cat, platform,
            '&', va1,
            '&',va2,
            '&', round(np.average((vehiclesDict[cat][platform]['during']['util'])),1),
            '&', round(np.average((vehiclesDict[cat][platform]['during']['distance'])),1),
            '&', round(np.average((vehiclesDict[cat][platform]['during']['price'])),1),
            '\\\\')
        print('\\cline{2-7}')
    
    print('\\hline\n\n')

    print('%',sum(tp)/sum(th))


print(sum(beforeTrips))
print(len(duringTrips))
print(np.average(distAverage))
print(np.average(priceAverage))

print(cvar/len(duringTrips))