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


for city in cities:
    priceDict[city] = []
    # for cat in carCats:
    #     priceDict[city][cat] = []

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
            print(platform, cityName)
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            # print(content.keys())
            # content= content[cityName]
            fx.close()
            city = cityName
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
                    for j in range(0, len(totalAheadDates)):
                        curentAheadDate = totalAheadDates[j]
                        price = content[vehicleId][currentDate][curentAheadDate]
                        # vehiclePrices.append(price)
                        d1 = datetime.strptime(currentDate, '%Y-%m-%d')
                        try:
                            d2 = d1 + timedelta(days=int(curentAheadDate))
                            dayOfWeek = d2.strftime("%A")
                            # print(d1,d2,dayOfWeek, curentAheadDate)
                            # time.sleep(100000)
                            vehiclePrices.append((price,dayOfWeek))
                            # vehiclePriceDays.append(dayOfWeek)
                        except:
                            pass
                            # print(d1, curentAheadDate)
                # print(vehiclePrices[:10])
                vehiclePrices = list(set(vehiclePrices))
                vehiclePrices.sort(key=lambda x:x[0])
                for item in vehiclePrices[:10]:
                    # print(item)
                    priceDict[city].append(item[1])
                
from collections import Counter
for city in priceDict:
    mlist = priceDict[city]
    print(city, Counter(mlist))
# fx = open('priceDict.txt','w')
# fx.write(json.dumps(priceDict))
# fx.close()
# print('saved price cats dictionary too')

# print(len(exceptionCount.keys()), len(totalVehicles.keys()))
