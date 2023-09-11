from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


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
targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'


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


for key in catDict.keys():
    # print(catDict[key])
    types = catDict[key]['type']
    for i in range(0,len(types)):
        ctype = types[i]
        if ctype != 'SUV':
            ctype = ctype.lower()
        if ctype == 'car':
            ctype = 'sedan'
        if '_' in ctype:
            ctype = ctype[:-1]
        catDict[key]['type'][i] = ctype

# for key in tempDict.keys():
#     # print(catDict[key])
#     types = tempDict[key]
#     for i in range(0,len(types)):
#         ctype = types[i]
#         if ctype != 'SUV':
#             ctype = ctype.lower()
#         if ctype == 'car':
#             ctype = 'sedan'
#         if '_' in ctype:
#             ctype = ctype[:-1]
#         tempDict[key][i] = ctype

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

cityVehiclesAndDailyVehicles = {}
for platform in studiedApps:
    
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0

    for fileName in filenames:
        cityName = fileName.split('-')[0]
        if cityName != 'New York':
            try:
                val = cityVehiclesAndDailyVehicles[cityName]
            except:
                cityVehiclesAndDailyVehicles[cityName] = {}
                cityVehiclesAndDailyVehicles[cityName]['totalVehicles'] = {}
            # try:
            #     var = ownerVehicles[cityName][platform]
            # except:
            #     ownerVehicles[cityName][platform] = {}
            print(platform, cityName)
            # 
            totalIDsPics = {}
            if 1:
            # try:
                fx = open(tempFolder+fileName,'r')
                content = json.loads(fx.read())
                fx.close()
                carCount = 0
                for id in content:
                    
                    for date in content[id]:
                        car = content[id][date]
                        ownerID = content[id][date]['ownerID']
                        # print(car['make'], car['model'])
                        totalVehicles[platform+id] = 1
                        toBeSearchedKey = car['model'].lower()+'~'+car['make'].lower()
                        totalModels[toBeSearchedKey] = 1
                        cityVehiclesAndDailyVehicles[cityName]['totalVehicles'][platform+'~'+id] = toBeSearchedKey

                        try:
                            val = cityVehiclesAndDailyVehicles[cityName][date]
                        except:
                            cityVehiclesAndDailyVehicles[cityName][date] = {}
                        cityVehiclesAndDailyVehicles[cityName][date][platform+'~'+id] = toBeSearchedKey

                        
                        # print(cat)
                        # time.sleep(1000)
                        # 
            # except Exception as e:
            #     print(e)

print(len(catDict.keys()),len(totalVehicles.keys()), len(moreThanOne.keys()))
print(len(totalTypes), totalTypes.keys())
# time.sleep(1000)
f = 0

catsCount = {}
for cat in catCats:
    catsCount[cat] = 0

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

cities = [
    'Barcelona', 
    'Berlin', 
    'Hamburg', 
    'Los Angeles',
    'London', 
    'Liverpool', 
    'Las Vegas', 
    'Lyon', 
    'Madrid',
    'Miami', 
    'New York City', 
    'Ottawa',  
    'Paris',  
    'Toronto',
    'Washington D.C.' ]

totalAverage = []
for i in range(0, len(cities)):
    city = cities[i]
    datesAverage = []
    maxCars = 0
    for date in cityVehiclesAndDailyVehicles[city]:
        if date!='totalVehicles':
            datesAverage.append(len(cityVehiclesAndDailyVehicles[city][date].keys()))
            maxCars = max(maxCars,len(cityVehiclesAndDailyVehicles[city][date].keys()))
    totalCars = len(cityVehiclesAndDailyVehicles[city]['totalVehicles'].keys())
    datesAverage = [maxCars]
    print(cityShort[city], totalCars,maxCars, np.average(datesAverage), round(np.average(datesAverage)/totalCars*100,2))

    if 1:
    # if round(np.average(datesAverage)/totalCars*100,2) < 30:
    #     totalAverage.append(round(np.average(datesAverage)/totalCars*100,2)*2)
    # else:
        totalAverage.append(round(np.average(datesAverage)/totalCars*100,2))

print(np.average(totalAverage))