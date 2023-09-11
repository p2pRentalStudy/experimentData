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
for i in range(0,len(cities)):
    city = cities[i]
    # print(city)
    cityCars = 0
    catsCount = {}
    for cat in catCats:
        catsCount[cat] = 0
    for service in citiesAndServices[city]:
        # print('\t', service)
        for cat in citiesAndServices[city][service]:
            cityCars += len(citiesAndServices[city][service][cat])
            catsCount[cat] += len(citiesAndServices[city][service][cat])
            # if len(citiesAndServices[city][service][cat]) > 0:
            # print('\t\t', cat, len(citiesAndServices[city][service][cat]))
    print(cityShort[city], '&', end = ' ')
    for j in range(0, len(catCats)):
        totalCars = catsCount[catCats[j]]
        totalCatsDict[catCats[j]] += catsCount[catCats[j]]

        if totalCars > 999:
            totalCars = str(round(totalCars/1000,1))+'K'
        print(str(totalCars)+' ('+str(round((catsCount[catCats[j]]/cityCars)*100,1))+'\\%)', end = ' & ')
    
    totalCars2 = cityCars
    if totalCars2 > 999:
        totalCars2 = str(round(totalCars2/1000,1))+'K'
    print(totalCars2,' \\\\ \\hline')
    print('')
    
    # print('\t', catsCount, cityCars) #(round(cityCars/len(totalVehicles)*100,2),'\%'))
    totalCars3 += cityCars

# print('\\textbf{Total} &',end = ' ')
print('Total &',end = ' ')


catsCount = totalCatsDict
for j in range(0, len(catCats)):
        totalCars = catsCount[catCats[j]]
        
        if totalCars > 999:
            totalCars = str(round(totalCars/1000,1))+'K'
        # print('\\textbf{'+str(totalCars)+' ('+str(round((catsCount[catCats[j]]/totalCars3)*100,1))+'\\%)}', end = ' & ')

        print(''+str(totalCars)+' ('+str(round((catsCount[catCats[j]]/totalCars3)*100,1))+'\\%)', end = ' & ')
    

if totalCars3 > 999:
    totalCars3 = str(round(totalCars3/1000,1))+'K'
# print('\\textbf{',totalCars3,'} \\\\ \\hline')
print('',totalCars3,' \\\\ \\hline')

print('')


print('Came here')