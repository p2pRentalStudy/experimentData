from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from dateutil import parser

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/vehicleCat-output/'
fx = open(loadPath + 'vehicleCategories.txt','r')
carIdToCat = json.loads(fx.read())
fx.close()

carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']



totalMeta = {'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}, 'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}}

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'
analyzedData = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

for platform in studiedApps:
    analyzedData[platform] = {}
    for city in totalMeta[platform]:
        analyzedData[platform][city] = {}




for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    totalCarTrips = {}
    carCt = 0
    print(platform)
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        city = cityName
        # print(platform, cityName)
        if cityName == 'New York':
            city = cityName= 'New York City'
        # try:
        if 1:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            carCount = 0
            for id in content.keys():
                dates = list(content[id].keys())
                ownerId = content[id][dates[0]]['ownerID']
                dates.sort()
                prevTrips = 0

                tripsTaken = content[id][dates[-1]]['numberOfTrips'] - content[id][dates[0]]['numberOfTrips']

                # print(date2, date)
                try:
                    val = analyzedData[platform][cityName][ownerId]
                except:
                    analyzedData[platform][cityName][ownerId] = []
                if len(analyzedData[platform][cityName][ownerId]) > 1000:
                    id2 = analyzedData[platform][cityName][ownerId][99][0]
                    print(ownerId,  content[id2][dates[0]]['ownerID'])
                    time.sleep(1)

                analyzedData[platform][cityName][ownerId].append([id,tripsTaken])

                # print(analyzedData)
                # time.sleep(1000)
totaltotal = 0

print(totaltotal)         
savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/22-output/'         
fx = open(savePath+'ownerTrips.txt','w')
fx.write(json.dumps(analyzedData))
fx.close()
print('\t saving ownerTrips dict')


# for cat in analyzedData:
#     print(cat)
#     for platform in analyzedData[cat]:
#         try:
#         # TOTAL BEFORE, TOTAL AFTER, PER VEHICLE, PER WEEK per vehicle
#             print('\t', platform, round(sum(analyzedData[cat][platform]['totalTrips']['before']),2),'&', round(sum(analyzedData[cat][platform]['totalTrips']['after']),2),'&', round(sum(analyzedData[cat][platform]['totalTrips']['after'])/len(analyzedData[cat][platform]['totalVehicles'].keys()),2),'&', round(sum(analyzedData[cat][platform]['perWeekTrips']['after'])/len(analyzedData[cat][platform]['totalVehicles'].keys()),2))

#         except:
#             pass