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
                prevRank = 0
                currentDate = ''
                prevDate = ''
                changes = []
                changes2 = []
                # myList = content[vehicleId]
                myList = content[vehicleId]['data']
                myList.sort(key=lambda x:x[1])
                totalAvrg = []

                for i in range(len(myList)):
                    # currentVal = content[vehicleId][i]
                    currentVal = myList[i][0]
                    recordDate = myList[i][1]

                    aheadDates = recordDate.split(' (')[1]
                    aheadDates = aheadDates.split(' - - ')
                    aheadDates[0] = aheadDates[0].split(' ')[0]
                    if platform == 'Turo':
                        d1 = datetime.strptime(aheadDates[0], '%m-%d-%Y')
                    else:
                        d1 = datetime.strptime(aheadDates[0], '%Y-%m-%d')

                    currentDate = d1

                    if prevVal != 0 and prevVal != currentVal:
                        if 1:
                        # try:
                            dayDifference = currentDate-prevDate
                            dayDifference = str(dayDifference)
                            if 'day' in dayDifference:
                                dayDifference = int(dayDifference.split(' ')[0])
                            else:
                                dayDifference = 1
                            changes.append(abs(dayDifference))
                        # except Exception as e:
                        #     print(e, prevDate,currentDate, prevVal, currentVal, dayDifference)
                        #     time.sleep(1000000)

                        # changes2.append(currentRank-prevRank)
                    prevVal = currentVal
                    prevDate = currentDate
                totalVehiclesPrice[platform].append((changes, cityName, vehicleId, content[vehicleId]['constantVars']))

print(totalMeta)
savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/15-output/'
fx = open(savePath+'15l-priceChangeDict.txt','w')
fx.write(json.dumps(totalVehiclesPrice))
fx.close()
print('\t saving dict')
