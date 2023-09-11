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
# studiedApps['Turo'] = 1
# studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
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

bookingDict = {}
for platform in studiedApps:
    # vehiclePrices[platform] = {}
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0
    bookingDict = {}

    bookingDict[platform] = {}


    for fileName in filenames:
        cityName = fileName.split('-')[0]
        if cityName != 'New York':
            bookingDict[platform] = {}
            bookingDict[platform][cityName] = {}
            print(platform, cityName)
            totalIDsPics = {}
            cityVehiclePricesDict = {}
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
                    if i%50000 == 1:
                        print('\t\t', i, keyDate)
                        # if i > 10:
                        #     break
                    recordDate = totalDates[i]

                    recordDate = recordDate.split(')')[0]
                    startDate = recordDate.split(' (')[0]
                    # startDate = startDate.split('-')
                    # startDate = startDate[1]+'-'+startDate[2]+'-'+startDate[0]
                    # d0 = datetime.strptime(startDate, '%Y-%m-%d')
                    aheadDates = recordDate.split(' (')[1]
                    aheadDates = aheadDates.split(' - - ')
                    aheadDates[0] = aheadDates[0].split(' ')[0]
                    aheadDates[1] = aheadDates[1].split(' ')[0]

                    
                    if 'Turo' in platform:
                        aheadDates[0] = aheadDates[0].split('-')
                        aheadDates[0] = aheadDates[0][2]+'-'+aheadDates[0][0]+'-'+aheadDates[0][1]

                    # print(aheadDates[0], startDate)
                    # time.sleep(10000)

                    for vehicleId in content[keyDate]:
                        try:
                            val = bookingDict[platform][cityName][vehicleId]
                        except:
                            bookingDict[platform][cityName][vehicleId] = {}

                        # try:
                        #     val = bookingDict[platform][cityName][vehicleId][aheadDates[0]+'~'+aheadDates[1]]
                        # except:
                        #     bookingDict[platform][cityName][vehicleId][aheadDates[0]+'~'+aheadDates[1]] = []
                        # bookingDict[platform][cityName][vehicleId][aheadDates[0]+'~'+aheadDates[1]].append((startDate, content[keyDate][vehicleId]['trips']))
                        # print(aheadDates[0], startDate)
                        # time.sleep(10000)
                        try:
                            val = bookingDict[platform][cityName][vehicleId][aheadDates[0]]
                        except:
                            bookingDict[platform][cityName][vehicleId][aheadDates[0]] = []
                        if aheadDates[0] >= startDate:
                            bookingDict[platform][cityName][vehicleId][aheadDates[0]].append((startDate, content[keyDate][vehicleId]['trips']))
                            # break
            savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/18-output/'+platform+'/'         
            fx = open(savePath +cityName+'-bookingDict.txt','w')
            fx.write(json.dumps(bookingDict[platform][cityName]))
            fx.close()
            print('\t saving cooking dict for', platform, cityName)