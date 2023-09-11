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
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1



targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'
analyzedData = {}


for platform in studiedApps:
    listData = {}
    analyzedData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    analyzedData[platform] = {}

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    totalCarTrips = {}
    carCt = 0
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName)

        fx = open(tempFolder+fileName,'r')
        content = json.loads(fx.read())
        fx.close()
        carCount = 0
        analyzedData[platform][cityName] = {}
        for id in content.keys():
            
            dates = list(content[id].keys())
            dates.sort()

            startTrips = 0
            endTrips = 0

            startTrips = int(content[id][dates[0]]['numberOfTrips'])
            endTrips = int(content[id][dates[-1]]['numberOfTrips'])


            d1 = datetime.strptime(dates[0], "%Y-%m-%d")
            d2 = datetime.strptime(dates[-1], "%Y-%m-%d")
            # print(d1,d2)
            # difference between dates in timedelta
            delta = d2 - d1
            totalTrips = endTrips-startTrips
            tempDictObj = {}
            if delta.days >34:
                carId = str(id)
                analyzedData[platform][cityName][carId] = {}
                analyzedData[platform][cityName][carId]['trips'] = [startTrips,endTrips]
                analyzedData[platform][cityName][carId]['dates'] = [dates[0], dates[-1], delta.days]
                analyzedData[platform][cityName][carId]['ownerID'] = content[id][dates[0]]['ownerID']

    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'    
    # print(analyzedData)
    fx = open(savePath +platform+'-trips.txt','w')
    fx.write(json.dumps(analyzedData))
    fx.close()
