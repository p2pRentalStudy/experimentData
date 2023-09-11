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
# targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData//13-output/'+platform+'/'


catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
notFound = {}
totalTypes = {}


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


citiesPriceAverage = {}

for city in cities:
    citiesPriceAverage[city] = []

for platform in studiedApps:
    listData = {}
    tempFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData//13-output/'+platform+'/'

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0

    for fileName in filenames:
        cityName = fileName.split('-')[1].replace('.txt', '')
        print(platform, cityName)
        # time.sleep(100000)

        fx = open(tempFolder+fileName,'r')
        content = json.loads(fx.read())
        fx.close()
        
        for vehicleId in content:
            for recocrdDate in content[vehicleId]:
                for dayDifference in content[vehicleId][recocrdDate]:
                    bookingPrice = content[vehicleId][recocrdDate][dayDifference]
                    print(cityName, platform, vehicleId, bookingPrice)

                    time.sleep(200000)
