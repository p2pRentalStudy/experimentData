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


# fx = open('carCatCleaned.txt', 'r')
# catDict = json.loads(fx.read())
# fx.close()

# print(len(catDict.keys()))


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


fx = open('carCatCleaned.txt','r')
catDict = json.loads(fx.read())
fx.close()


fx = open('citiesAndServicesCats.txt','r')
citiesAndServices = citiesAndServicesCats = json.loads(fx.read())
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

catCats = ['sedan', 'suv', 'hatchback', 'van/minivan',  'truck',  'coupe', 'wagon']

print('City', '&', end = ' ')
for j in range(0, len(catCats)):
    print(catCats[j], end = '& ')

print('Total \\\\')
# time.sleep(1000)

totalCars3 = 0

c1cities = [
    'Los Angeles',
    'Las Vegas', 
    'Miami', 
    'New York City', 
    'Washington D.C.' ]


# cities = c1cities
totalCatsDict = {}
for cat in catCats:
    totalCatsDict[cat] = 0

totalCars = []
from collections import Counter
for i in range(0,len(cities)):
    city = cities[i]
    # print(city)
    # totalCars
    cityCars = []
    catsCount = {}
    for cat in catCats:
        catsCount[cat] = 0
    for service in citiesAndServices[city]:
        # print('\t', service)
        for cat in citiesAndServices[city][service]:
            # cityCars += len(citiesAndServices[city][service][cat])
            for id in citiesAndServices[city][service][cat]:
                car = citiesAndServices[city][service][cat][id]
                # print(car[0])
                carI = 0
                cityCars.append(car[carI])
                totalCars.append(car[carI])
        # cityCars = Counter(cityCars)
    carCount = len(cityCars)
    cityCars = [[x,cityCars.count(x)] for x in set(cityCars)]
    cityCars.sort(key=lambda a: a[1], reverse=True)
    cityCars = cityCars[:3]
    newList = []
    for x in cityCars:
        newList.append([x[0], x[1]/carCount])
    print('\t', city, newList)
cityCars = totalCars
carCount = len(cityCars)

totalMakers = {}
for x in cityCars:
    totalMakers[x] = 1
cityCars = [[x,cityCars.count(x)] for x in set(cityCars)]
cityCars.sort(key=lambda a: a[1], reverse=True)
cityCars = cityCars[:8]
newList = []
added = 0
for x in cityCars:

    newList.append([x[0], round(x[1]/carCount*100,2)])
    added +=  round(x[1]/carCount*100,2)
print( len(totalMakers.keys()), newList, added)
        