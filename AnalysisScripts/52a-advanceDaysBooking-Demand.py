from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

print(len(catDict.keys()))




dictKeys = list(catDict.keys())
dictKeys.sort()

for key in dictKeys:
    if len(catDict[key]['type']) == 0:
        del catDict[key]
studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
# cities = {'Barcelona', 'Berlin', 'Hamburg', 'Liverpool', 'London', 'Lyon', 'Madrid', 'Paris', 'Las Vegas', 'Los Angeles', 'Miami','New York City', 'Ottawa', 'Toronto','Washington D.C.' }
targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/APPNAME/'


catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
notFound = {}
totalTypes = {}

citiesAndServices = {}
for city in cities:
    citiesAndServices[city] = {}
    for service in studiedApps.keys():
        citiesAndServices[city][service] = {}
        for cat in catCats:
            citiesAndServices[city][service][cat] = {}



totalModels = {}

moreThanOne = {}
totalVehicles = {}


ownerVehicles = {}
for city in cities:
    ownerVehicles[city] = {}
    for service in studiedApps.keys():
        ownerVehicles[city][service] = {}

studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/vehicleCat-output/'
fx = open(loadPath + 'vehicleCategories.txt','r')
carIdToCat = json.loads(fx.read())
fx.close()

possibleCats = ['sedan', 'SUV', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
priceDict = {}
currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21
vehiclePrices = {}

totalMeta = {'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}, 'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}}

pricesDict = {}

weekdays= ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
 
carDatesDict = {}    


studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1


platformService = {}
for platform in studiedApps:
    platformService[platform] = {}
    # vehiclePrices[platform] = {}
    listData = {}
    carDatesDict[platform] = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0
    carCount = 0
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        if cityName != 'New York':
            platformService[platform][cityName] = 1
            print(platform, cityName)
            carDatesDict[platform][cityName] = {}
            if 1:
            # try:
                fx = open(tempFolder+fileName,'r')
                content = json.loads(fx.read())
                fx.close()
                carCount = 0
                totalDates = list(content.keys())
                totalDates.sort()
                keyCount = 0
                vehiclePrices = {}

                for i in range(0, len(totalDates)):
                    keyDate = totalDates[i]
                    recordDate = totalDates[i]
                    recordDate = recordDate.split(')')[0]
                    startDate = recordDate.split(' (')[0]

                    d0 = startDate#datetime.strptime(startDate, '%Y-%m-%d')
                    d1 = ''
                    aheadDates = recordDate.split(' (')[1]
                    aheadDates = aheadDates.split(' - - ')
                    aheadDates[0] = aheadDates[0].split(' ')[0]
                    # aheadDates[1] = aheadDates[1].split(' ')[0]

                    if platform == 'Turo':
                        aheadDates[0] = aheadDates[0].split('-')
                        aheadDates[0] = aheadDates[0][2]+'-'+aheadDates[0][0]+'-'+aheadDates[0][1]
                    d1 = aheadDates[0]

                    for vehicleId in content[keyDate]:
                        vid = str(vehicleId)
                        try:
                            v10 = carDatesDict[platform][cityName][vid]
                        except:
                            carDatesDict[platform][cityName][vid] = {}
                        
                        try:
                            v10 = carDatesDict[platform][cityName][vid][d0]
                        except:
                            carDatesDict[platform][cityName][vid][d0] = []
                        vehicleTrips = content[keyDate][vehicleId]['trips']
                        
                        carDatesDict[platform][cityName][vid][d0].append([d1, vehicleTrips])
                        # print(vid, d0, d1, vehicleTrips)
                        # time.sleep(10000)
            fx = open('carDatesDict-'+platform+'-'+cityName+'.txt','w')
            fx.write(json.dumps(carDatesDict))
            fx.close()
            carDatesDict[platform] = {}
    carDatesDict = {}    

print(platformService)