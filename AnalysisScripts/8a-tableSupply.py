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

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1

cityDict = {}
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
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

for city in cityCurrencyMap.keys():
    cityDict[city] = {}
    for day in daysOfWeek:
        cityDict[city][day] = []
    cityDict[city]['totalTrips'] = 0



dateToDayDict = {}
v3 = []
v4 = []

fx = open('finalCarColors.txt', 'r')
carColors = json.loads(fx.read())
fx.close()
possibleColors = {}
for platform in carColors:
    for city in carColors[platform]:
        for carId in carColors[platform][city]:
            possibleColors[carColors[platform][city][carId]] = 1
possibleColors = list(possibleColors.keys())

print(possibleColors)

countColor ={}
for color in possibleColors:
    countColor[color] = 0
carCats2 = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'suv']
carCats3 =  {}
for cat in carCats2:
    carCats3[cat] = 0
tv3 = 0
totalTripsPerOwnerData = {}
cities = list(cityCurrencyMap.keys())
cities.sort()
for cityName in cities:#[platform]:
    totalVehicles = 1
    catCars = {}
    for type in carCats2:
        catCars[type] = 0
    for platform in priceMulMap:# ['GerAroundEurope']:#priceMulMap.keys():
        try:
            fx = open(loadPath +platform+'-'+cityName+'-tripDetails.txt','r')
            tripDetailsDict = json.loads(fx.read())
            fx.close()
            # print(platform)
            fx = open(loadPath +platform+'-trips.txt', 'r')
            analyzedData = json.loads(fx.read())
            fx.close()
            for carId in analyzedData[platform][cityName]:
                vc += 1
                cat = 'sedan'
                try:
                    cat = cityServiceCat[platform][cityName][carId][0]
                except:
                    ijk = 10
                carColor = 'white'
                try:
                    carColor = carColors[platform][cityName][carId]
                    # print(platform,city, carId, carColor, cat)
                    # time.sleep(1000)
                except:
                    pass
                countColor[carColor] +=1
                catCars[cat] +=1
                carCats3[cat] += 1
                totalVehicles += 1
                tv3 += 1

        except Exception as e:
            # print(e)
            # time.sleep(1000)
            ijk = 10
    # print(catCars)

    carCats2 = ['sedan', 'suv', 'hatchback', 'van/minivan', 'truck', 'coupe', 'wagon']
    
    print(cityShort[cityName], end=' &')
    for i in range(0,len(carCats2)):
        enval = ' &'
        # if i == len(carCats2)-1:
        #     enval = ' '
        print(catCars[carCats2[i]],'('+str(round(catCars[carCats2[i]]/totalVehicles*100))+'\%)', end=' &')
    print(totalVehicles, end=' ')
    print('\\\\')
    print()

print()
print('Total', end=' &')
# tv3 = 63590
for i in range(0,len(carCats2)):
    enval = ' &'
    if i == len(carCats2)-1:
        enval = ' '
    print(carCats3[carCats2[i]],'('+str(round(carCats3[carCats2[i]]/tv3*100))+'\%)', end=' &')
print(tv3, end=' ')
print('\\\\')


for color in possibleColors:
    print(color, round(countColor[color]/63600*100,2))