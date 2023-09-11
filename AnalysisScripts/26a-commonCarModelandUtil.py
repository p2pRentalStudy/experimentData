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

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/vehicleTrips.txt'
fx = open(loadPath,'r')
tripsDict = json.loads(fx.read())
fx.close()


catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
totalTypes = []
from collections import Counter
maxCars = 5

myvehicles = []
vehicleCats = {}
modelUtil = {}
for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0


    print(platform)
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        if cityName != 'New York':
            print('\t', cityName)
            if 1:
                fx = open(tempFolder+fileName,'r')
                content = json.loads(fx.read())
                fx.close()
                cityList = []
                cityModelUtil = {}
                for id in content:
                    vehicleid = platform+'~'+id
                    dates = list(content[id].keys())
                    dates.sort()
                    # if 1:
                    try:
                        data = tripsDict[platform][cityName][id]
                        # print(data)
                        
                        date = dates[0]
                        
                        car = content[id][date]
                        toBeSearchedKey = car['model'].lower()+'~'+car['make'].lower()
                        try:
                            val = cityModelUtil[toBeSearchedKey]
                        except:
                            cityModelUtil[toBeSearchedKey] = []

                        try:
                            val = modelUtil[toBeSearchedKey]
                        except:
                            modelUtil[toBeSearchedKey] = []
                        
                        cityModelUtil[toBeSearchedKey].append(data[1]/(data[0]/7))
                        modelUtil[toBeSearchedKey].append(data[1]/(data[0]/7))
                        
                        myvehicles.append(toBeSearchedKey)
                        cityList.append(toBeSearchedKey)
                    except:
                        pass
                counter = Counter(cityList)
                counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)

                # counter = cityList[:10]
                keyCount = 0
                
                # counter = cityList[-10:]
                
                
                for i in range (0, len(counter)):
                    print('\t\t', counter[i], np.average(cityModelUtil[counter[i][0]]))
                    keyCount += 1
                    if keyCount == maxCars:
                        break
                print()
                keyCount = 0

                firstVar = len(counter)-100
                if firstVar < 0:
                    firstVar = len(counter)-10
                for i in range (max(firstVar, 0), len(counter)):
                    print('\t\t', counter[i], np.average(cityModelUtil[counter[i][0]]))
                    keyCount += 1
                    if keyCount == maxCars:
                        break

counter = Counter(myvehicles)

counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)

# counter = cityList[:10]
keyCount = 0
print('OVERALL')
for i in range (0, len(counter)):
    print('\t', counter[i], np.average(modelUtil[counter[i][0]]))
    keyCount += 1
    if keyCount == maxCars:
        break

# counter = cityList[-10:]
keyCount = 0
print()
for i in range (len(counter)-1000, len(counter)):
    print('\t', counter[i], np.average(modelUtil[counter[i][0]]))
    keyCount += 1
    if keyCount == maxCars:
        break

# print(counter)
