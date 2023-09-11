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

studiedApps = {}
studiedApps['Turo'] = 1
# studiedApps['GetAround'] = 1
# studiedApps['GerAroundEurope'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'
analyzedData = {}
for cat in carCats:
    analyzedData[cat] = {}
    for platform in studiedApps:
        analyzedData[cat][platform] = {}
        analyzedData[cat][platform]['totalVehicles'] = {}
        analyzedData[cat][platform]['totalTrips'] = {}
        analyzedData[cat][platform]['totalTrips']['before'] = []
        analyzedData[cat][platform]['totalTrips']['after'] = []

        analyzedData[cat][platform]['perVehicleTrips'] = {}
    
        analyzedData[cat][platform]['perVehicleTrips']['after'] = []

        analyzedData[cat][platform]['perWeekTrips'] = {}
        analyzedData[cat][platform]['perWeekTrips']['after'] = []

        analyzedData[cat][platform]['tripLength'] = {}
        analyzedData[cat][platform]['tripLength']['after'] = []

        analyzedData[cat][platform]['earning'] = {}
        analyzedData[cat][platform]['earning']['after'] = []
        


for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    totalCarTrips = {}
    carCt = 0
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName)
        if 1:
        # try:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            carCount = 0
            for id in content.keys():
                
                dates = list(content[id].keys())
                dates.sort()

                startTrips = 0
                endTrips = 0
                try:
                    startTrips = content[id][dates[0]]['numberOfTrips']
                except:
                    pass 

                try:
                    endTrips = content[id][dates[-1]]['numberOfTrips']
                except:
                    pass 

                d1 = datetime.strptime(dates[0], "%Y-%m-%d")
                d2 = datetime.strptime(dates[-1], "%Y-%m-%d")
                # print(d1,d2)
                # difference between dates in timedelta
                delta = d2 - d1
                totalTrips = endTrips-startTrips
                tempDictObj = {}
                try:
                    currentCat = carIdToCat[platform+'~'+id][0]

                    analyzedData[currentCat][platform]['totalVehicles'][id] = 1

                    analyzedData[currentCat][platform]['totalTrips']['before'].append(startTrips)
                    analyzedData[currentCat][platform]['totalTrips']['after'].append(totalTrips)
                    analyzedData[currentCat][platform]['perWeekTrips']['after'].append(round(totalTrips/(delta.days/7), 2))
                except Exception as e:
                    if '~' not in str(e) and 'zero' not in str(e):
                        print(e, d1, d2)
                    pass

for cat in analyzedData:
    print(cat)
    for platform in analyzedData[cat]:
        try:
        # TOTAL BEFORE, TOTAL AFTER, PER VEHICLE, PER WEEK per vehicle
            print('\t', platform, round(sum(analyzedData[cat][platform]['totalTrips']['before']),2),'&', round(sum(analyzedData[cat][platform]['totalTrips']['after']),2),'&', round(sum(analyzedData[cat][platform]['totalTrips']['after'])/len(analyzedData[cat][platform]['totalVehicles'].keys()),2),'&', round(sum(analyzedData[cat][platform]['perWeekTrips']['after'])/len(analyzedData[cat][platform]['totalVehicles'].keys()),2))

        except:
            pass