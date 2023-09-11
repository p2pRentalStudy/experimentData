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


citiesAndServicesMeta = {}
citiesAndServicesMeta['Turo'] = ['Las Vegas', 'Liverpool', 'London', 'Los Angeles','New York City', 'Miami', 'Ottowa', 'Toronto', 'Washinton D.C']
citiesAndServicesMeta['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
citiesAndServicesMeta['GerAroundEurope'] = ['London','Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris']

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

colorMap = {}
colorMap['green'] = 'white'
colorMap['white'] = 'black'
colorMap['yellow'] = 'gray'
colorMap['red'] = 'blue'
colorMap['cyan'] = 'red'
colorMap['blue'] = 'green'
colorMap['gray'] = 'cyan'
colorMap['black'] = 'yellow'




vehicleColorDict = {}


colorsSupply = {}
colorCatSupply = {}

for cat in catCats:
    colorCatSupply[cat] = []

for city in cities:
    colorsSupply[city] = []
# cities = c1cities
totalCatsDict = {}
for cat in catCats:
    totalCatsDict[cat] = 0
for service in citiesAndServicesMeta:
    vehicleColorDict[service] = {}
    for city in citiesAndServicesMeta[service]:
        vehicleColorDict[service][city] = {}
        cityCars = 0
        catsCount = {}
        for cat in catCats:
            catsCount[cat] = 0
        
        #load color file 
        if city == 'Ottowa':
            city = 'Ottawa'
        if city == 'Washinton D.C':
            city = 'Washington D.C.'
        fx = open('/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/4x3-output/'+service+'~'+city+'~carColorsDict.txt')
        colorDict = json.loads(fx.read())
        fx.close()
        # print(service,city, len(colorDict.keys()))
        # time.sleep(10000)

        # print('\t', service)
        for cat in citiesAndServices[city][service]:
            # cityCars += len(citiesAndServices[city][service][cat])
            # catsCount[cat] += len(citiesAndServices[city][service][cat])
            for id in citiesAndServices[city][service][cat].keys():
                try:
                    carColor = colorDict[id]
                    carColor = colorMap[carColor]
                    colorsSupply[city].append(carColor)
                    colorCatSupply[cat].append(carColor)
                    vehicleColorDict[service][city][id] = carColor

                except:
                    pass
                
totalSupplyColors = []

from collections import Counter

from collections import Counter

for city in colorsSupply:
    for item in colorsSupply[city]:
        # print(item)
        totalSupplyColors.append(item)


totalLength = len(totalSupplyColors)
totalSupplyColors = Counter(totalSupplyColors) 
tempList = []
for key in totalSupplyColors:
    tempList.append([key,totalSupplyColors[key]])
for i in range(0, len(tempList)):
    tempList[i] = [tempList[i][0], round(tempList[i][1]/totalLength,5)]
    
tempList.sort(key=lambda x:x[1], reverse=True)
title = 'total'
print(title, tempList)
print()   
print()   

for city in colorsSupply:
    totalSupplyColors = colorsSupply[city]
    totalLength = len(totalSupplyColors)
    totalSupplyColors = Counter(totalSupplyColors) 
    tempList = []
    for key in totalSupplyColors:
        tempList.append([key,totalSupplyColors[key]])
    for i in range(0, len(tempList)):
        tempList[i] = [tempList[i][0], round(tempList[i][1]/totalLength,2)]
        
    tempList.sort(key=lambda x:x[1], reverse=True)
    title = city
    print(title, tempList)

print()   
print()   

for cat in catCats:
    totalSupplyColors = colorCatSupply[cat]
    totalLength = len(totalSupplyColors)
    totalSupplyColors = Counter(totalSupplyColors) 
    tempList = []
    for key in totalSupplyColors:
        tempList.append([key,totalSupplyColors[key]])
    for i in range(0, len(tempList)):
        tempList[i] = [tempList[i][0], round(tempList[i][1]/totalLength,2)]
        
    tempList.sort(key=lambda x:x[1], reverse=True)
    title = cat
    print(title, tempList)



fx = open('finalCarColors.txt','w')
fx.write(json.dumps(vehicleColorDict))
fx.close()
