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
exptotalReviews = []
reviewRation = []
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
                cityTotalReview = []
                for id in content:
                    vehicleid = platform+'~'+id
                    dates = list(content[id].keys())
                    dates.sort()


                    # if 1:
                    try:
                        data = tripsDict[platform][cityName][id]
                        numberOfTrips = content[id][dates[-1]]['numberOfTrips'] 
                        # - content[id][dates[0]]['numberOfTrips']
                        totalReviews =  max(0, content[id][dates[-1]]['numberOfReviewes'])
                        if numberOfTrips != 0:
                            cityTotalReview.append(totalReviews/numberOfTrips)
                        # print(id, numberOfTrips, totalReviews)
                        # time.sleep(10
                    except:
                        pass
                print('\t\t', round(np.average(cityTotalReview),2))
                exptotalReviews+= cityTotalReview
print( round(np.average(exptotalReviews),2))