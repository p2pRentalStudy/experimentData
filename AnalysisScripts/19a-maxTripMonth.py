from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


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
        for month in ['10','11','12','01','02','03','04']:
            analyzedData[platform][city][month] = {}
            analyzedData[platform][city][month]['days'] = {}
            analyzedData[platform][city][month]['trips'] = 0




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
                dates.sort()
                prevTrips = 0
                for i in range(len(dates)):
                    date = dates[i]
                    car = content[id][date]
                    month = date.split('-')[1]
                    currenTrips = car['numberOfTrips']
                    try:
                        val = analyzedData[platform][city][month]['days'][date]
                    except:
                        analyzedData[platform][city][month]['days'][date] = 0
                    if prevTrips != 0 and prevTrips != currenTrips:
                        analyzedData[platform][city][month]['trips'] += currenTrips- prevTrips
                        # print(date, id, currenTrips, prevTrips)
                        # time.sleep(1000)
                        analyzedData[platform][city][month]['days'][date] += currenTrips- prevTrips
                    prevTrips = currenTrips

totaltotal = 0
for platform in analyzedData:
    print(platform)
    for city in analyzedData[platform]:
        print('\t', city)
        totalTrips = 0
        for month in analyzedData[platform][city]:
            try:
                print('\t\t\t',month, analyzedData[platform][city][month]['trips'], analyzedData[platform][city][month]['trips']/len(analyzedData[platform][city][month]['days'])) 
                totalTrips += analyzedData[platform][city][month]['trips']
                totaltotal += analyzedData[platform][city][month]['trips']
            except:
                pass
                # print('\t\t', month, 'no data')
        print('\t\t total trips: ', totalTrips)
            
        # time.sleep(1000)
print(totaltotal)         
savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/19-output/'         
fx = open(savePath+'monthlyTripDict.txt','w')
fx.write(json.dumps(analyzedData))
fx.close()
print('\t saving monthly trip dict for', platform)


# for cat in analyzedData:
#     print(cat)
#     for platform in analyzedData[cat]:
#         try:
#         # TOTAL BEFORE, TOTAL AFTER, PER VEHICLE, PER WEEK per vehicle
#             print('\t', platform, round(sum(analyzedData[cat][platform]['totalTrips']['before']),2),'&', round(sum(analyzedData[cat][platform]['totalTrips']['after']),2),'&', round(sum(analyzedData[cat][platform]['totalTrips']['after'])/len(analyzedData[cat][platform]['totalVehicles'].keys()),2),'&', round(sum(analyzedData[cat][platform]['perWeekTrips']['after'])/len(analyzedData[cat][platform]['totalVehicles'].keys()),2))

#         except:
#             pass