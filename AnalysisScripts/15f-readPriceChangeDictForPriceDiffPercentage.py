from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/vehicleCat-output/'
fx = open(loadPath + 'vehicleCategories.txt','r')
carIdToCat = json.loads(fx.read())
fx.close()

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/15-output/APPNAME/'
carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']


priceDict = {}


for city in cities:
    priceDict[city] = {}
    for cat in carCats:
        priceDict[city][cat] = []

exceptionCount = {}
totalVehiclesPrice = {}
totalMeta = {}
totalVehicles = 0
for platform in studiedApps:
    totalVehiclesPrice[platform] = []
    totalMeta[platform] = {}
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    # print(tempFolder, filenames)

    for fileName in filenames:
        cityName = fileName.split('-')[1]
        cityName = cityName.replace('.txt','')
        if cityName != 'New York':
            totalMeta[platform][cityName] = 1
            print(platform, cityName)
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            totalVehicles += len(content.keys())
            print('\t', totalVehicles, len(content.keys()))
            # content= content[cityName]
            fx.close()
            for vehicleId in content:
                prevVal = 0
                changes = []
                # myList = content[vehicleId]
                myList = content[vehicleId]['data']
                myList.sort(key=lambda x:x[1])

                for i in range(len(myList)):
                    # currentVal = content[vehicleId][i]
                    currentVal = myList[i][0]
                    # print(currentVal)
                    # time.sleep(10000)
                    if prevVal != 0 and prevVal != currentVal:
                        changes.append(round((currentVal-prevVal)/prevVal*100,2))
                    prevVal = currentVal
                # changes = min(changes, 10000)
                totalVehiclesPrice[platform].append((changes, cityName, vehicleId, myList[i]))

print(totalMeta)
savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/15-output/'         
fx = open(savePath+'15f-priceChangeDict.txt','w')
fx.write(json.dumps(totalVehiclesPrice))
fx.close()
print('\t saving dict')
