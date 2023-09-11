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

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13-output/APPNAME/'
carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']


priceDict = {}

months = ['09', '10', '11', '12', '01', '02', '03', '04']
for city in cities:
    priceDict[city] = {}
    for month in months:
        priceDict[city][month] = []

exceptionCount = {}
totalVehicles = {}
for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    # print(tempFolder, filenames)

    for fileName in filenames:
        cityName = fileName.split('-')[1]
        cityName = cityName.replace('.txt','')
        if cityName != 'New York':
            city = cityName
            print(platform, cityName)
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            # print(content.keys())
            # content= content[cityName]
            fx.close()
            for vehicleId in content:
                vehiclePrices = []
                vehiclePriceDays = []
                totalVehicles[vehicleId] = 1
                totalDates = list(content[vehicleId].keys())
                totalDates.sort()
                
                for i in range(0, len(totalDates)):
                    currentDate = totalDates[i]
                    totalAheadDates =  list(content[vehicleId][currentDate].keys())
                    totalAheadDates.sort()
                    iet = 0
                    for j in range(0, len(totalAheadDates)):
                        curentAheadDate = totalAheadDates[j]
                        price = content[vehicleId][currentDate][curentAheadDate]
                        if platform == 'GetAround':
                            price = price*2.1
                        d1 = datetime.strptime(currentDate, '%Y-%m-%d')
                        iet += 1
                        try:
                            d2 = str(d1 + timedelta(days=int(curentAheadDate)))
                            # print(d2)
                            d2 = d2.split('-')
                            priceDict[cityName][d2[1]].append(price)
                            # time.sleep(1000)
                        except Exception as e:
                            # print(iet, e)
                            pass
                        if iet > 10:
                            break
                            
                        
                
from collections import Counter
for city in priceDict:
    print(city)
    prevAverage = 0
    overallAverage = []
    for platform in priceDict[city]:
        if len(priceDict[city][platform]) > 0:
            overallAverage+= priceDict[city][platform]

    overallAverage = np.average(overallAverage)
    for platform in priceDict[city]:
        if len(priceDict[city][platform]) > 0:
            print('\t', platform, np.average(priceDict[city][platform]) , np.average(priceDict[city][platform])/overallAverage)
            # if prevAverage != 0:
            #     print('\t\t', prevAverage/np.average(priceDict[city][platform]))
            # prevAverage = np.average(priceDict[city][platform])
