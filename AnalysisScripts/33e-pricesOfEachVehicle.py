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

totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

# print(len(catDict.keys()))




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
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1
possibleCats = ['sedan', 'SUV', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
priceDict = {}
currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21

maxTuple = [0,'','']
minTuple = [100000000,'','']

fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()

carPriceDict = {}

for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0

    for fileName in filenames:
        cityName = fileName.split('-')[0]
        carPriceDict = {}
        if cityName != 'New York':
            averageList = []
            totalIDsPics = {}
            cityVehiclePricesDict = {}
            if 1:
            # try:
                print(platform,cityName)
                fx = open(tempFolder+fileName,'r')
                content = json.loads(fx.read())
                fx.close()
                carCount = 0
                totalDates = list(content.keys())
                totalDates.sort()
                keyCount = 0
                for i in range(0, len(totalDates)):
                    keyDate = totalDates[i]
                    # if i%50000 == 1:
                    #     print('\t\t', i, keyDate)
                    recordDate = totalDates[i]
                    recordDate = recordDate.split(')')[0]
                    startDate = recordDate.split(' (')[0]
                    d0 = datetime.strptime(startDate, '%Y-%m-%d')
                    aheadDates = recordDate.split(' (')[1]
                    aheadDates = aheadDates.split(' - - ')
                    aheadDates[0] = aheadDates[0].split(' ')[0]
                    aheadDates[1] = aheadDates[1].split(' ')[0]

                    if platform == 'Turo':
                        d1 = datetime.strptime(aheadDates[0], '%m-%d-%Y')
                    else:
                        d1 = datetime.strptime(aheadDates[0], '%Y-%m-%d')

                    dayDifference = d1-d0
                    dayDifference = str(dayDifference)
                    dayDifference = dayDifference.split(' ')[0]
                    # print(startDate,aheadDates, dayDifference)
                    # time.sleep(0.1)

                    for vehicleId in content[keyDate]:
                        car = content[keyDate][vehicleId]
                        vehicleId = vehicleId
                        bookingPrice = car['bookingPrice']
                        if platform == 'Turo' or platform == 'GetAround':
                            bookingPrice = bookingPrice.split(' ')
                            bookingPrice = round(float(bookingPrice[0]) * currencyConversion[bookingPrice[1]],2)
                        else:
                            bookingPrice = [bookingPrice[0:1], bookingPrice[1:]]
                            bookingPrice = round(float(bookingPrice[1]) * currencyConversion[bookingPrice[0]],2)

                        mulFactor = .63

                        if platform == 'Turo':
                            if cityName == 'London':
                                mulFactor = 0.65
                            bookingPrice = round(bookingPrice*mulFactor,2)
                        if platform == 'GerAroundEurope':
                            if cityName == 'Liverpool' or cityName == 'London':
                                mulFactor = 0.75
                            bookingPrice = round(bookingPrice*mulFactor,2)
                        try:
                            val = carPriceDict[vehicleId]
                        except:
                            carPriceDict[vehicleId] = []
                        carPriceDict[vehicleId].append([bookingPrice, dayDifference, aheadDates[0]])
                        # print(aheadDates, bookingPrice, vehicleId)
                        # time.sleep(1000)
            savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/33e-output/'
            fx = open(savePath + platform+'-'+cityName+'.txt','w')
            fx.write(json.dumps(carPriceDict))
            fx.close()
            # print('done with pricingDict')
