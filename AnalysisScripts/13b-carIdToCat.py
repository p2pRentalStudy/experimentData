from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

print(len(catDict.keys()))
dictKeys = list(catDict.keys())
dictKeys.sort()
studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'


catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
totalTypes = []
vehicleCats = {}
for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0

    
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        if cityName != 'New York':
            print(platform, cityName)
            if 1:
                fx = open(tempFolder+fileName,'r')
                content = json.loads(fx.read())
                fx.close()
                for id in content:
                    vehicleid = platform+'~'+id
                    for date in content[id]:
                        car = content[id][date]
                        toBeSearchedKey = car['model'].lower()+'~'+car['make'].lower()
                        types = catDict[toBeSearchedKey]['type']
                        newTypes = []
                        for i in range(0,len(types)):
                            cat = types[i]
                            cat = cat.lower()
                            if cat == 'truck':
                                cat  = 'pickup'
                            elif cat == 'suv':
                                cat  = 'SUV'
                            elif cat == 'car':
                                cat  = 'sedan'
                            elif cat == 'convertible_':
                                cat  = 'convertible'

                            if cat == 'minivan':
                                cat = 'van/minivan'
                            elif cat == 'pickup':
                                cat = 'truck'
                            elif cat == 'convertible':
                                cat = 'coupe'
                            elif cat == 'van':
                                cat = 'van/minivan'
                            newTypes.append(cat)

                        vehicleCats[vehicleid] = newTypes
                        catDict[toBeSearchedKey]['type'] = newTypes

                        totalTypes += newTypes
                        totalTypes = list(set(totalTypes))
                        break
totalTypes = list(set(totalTypes))
print(totalTypes)
savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/vehicleCat-output/'         
fx = open(savePath + 'vehicleCategories.txt','w')
fx.write(json.dumps(vehicleCats))
fx.close()
print('\t saving the categories dictionary')

fx = open('carCatCleaned.txt','w')
fx.write(json.dumps(catDict))
fx.close()
print('saved updated cats dictionary too')