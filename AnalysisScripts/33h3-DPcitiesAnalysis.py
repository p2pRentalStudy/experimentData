from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

print(len(catDict.keys()))




dictKeys = list(catDict.keys())
dictKeys.sort()

for key in dictKeys:
    if len(catDict[key]['type']) == 0:
        del catDict[key]
studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
# cities = {'Barcelona', 'Berlin', 'Hamburg', 'Liverpool', 'London', 'Lyon', 'Madrid', 'Paris', 'Las Vegas', 'Los Angeles', 'Miami','New York City', 'Ottawa', 'Toronto','Washington D.C.' }
# targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData//13-output/'+platform+'/'



catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
notFound = {}
totalTypes = {}


cityAverage = {}
for city in cities:
    cityAverage[city] = {}
    for cat in catCats:
        cityAverage[city][cat] = []

totalModels = {}

moreThanOne = {}
totalVehicles = {}


ownerVehicles = {}
for city in cities:
    ownerVehicles[city] = {}
    for service in studiedApps.keys():
        ownerVehicles[city][service] = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1
possibleCats = ['sedan', 'SUV', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']

catDict = {}
for cat in catCats:
    catDict[cat] = []
currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


citiesPriceAverage = {}
platformAverage = {}

for platform in studiedApps:
    platformAverage[platform] = []
for city in cities:
    citiesPriceAverage[city] = []

totalPriceCDF = []

fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()

# fx = open('carPricesDict.txt', 'r')
# carPricingDict = json.loads(fx.read())
# fx.close()
# print('calculating averages')

values = []



carPrices = {}

dateValues = {}

totalReqs = 0 
combos = {}
# for i in range(0,200):
#     for x in range(0, 24):
#         for j in range(i,min(i+30,200)):
#             for k in range(0,24):
#                 try:
#                     val = combos[str(j)+str(k)]
#                 except:
#                     combos[str(j)+str(k)] = 0
#                 combos[str(j)+str(k)] += 1
#                 totalReqs += 1
# avrgTotal = []
# for key in combos:
#     avrgTotal.append(combos[key])
# print(totalReqs*0.67, np.average(avrgTotal)*0.67)

# time.sleep(100000)
from statistics import mode

#pre vehicle records 3209.094352423133, claimed = 2M
# per time stamp 28.770424924304738, claimed = 446

for city in cities:
    pricingDict = {}

    scaleRecs = 15.5
    plenList = []
    for platform in studiedApps:
        pricingDict[platform] = []
    # if 1:
        tempFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13c-output/'+platform+'/'
        listData = {}
        # tempFolder = targetFolder.replace('APPNAME',platform)
        filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
        filenames.sort()
        totalCarTrips = {}
        diffPricesMain = []
        # print(filenames)
        for fileName in filenames:
            cityName = fileName.split('-')[1]
            platform = fileName.split('-')[0]
            if city in fileName:
                fx = open(tempFolder+fileName,'r')
                carPricingDict = json.loads(fx.read())
                # print(platform, cityName, len(carPricingDict.keys()))
                fx.close()
                # print()
                
                differingPrices2 = 0
                maxUpdate = 0
                for vehicle in carPricingDict:
                    if 1:
                        try:
                            vehiclePrice = carPricingDict[vehicle]
                            plenList.append(len(vehiclePrice))
                            differingPrices = 0

                            for i in range(1, len(vehiclePrice)):
                                if vehiclePrice[i-1]   != vehiclePrice[i] : 
                                    differingPrices+=1

                            pricingDict[platform].append(differingPrices*24)
                        except:
                            pass

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    

    from scipy import stats

    step=0.05
    indices = np.arange(0,1+step,step)
    fig, ax = plt.subplots()

    # data_sorted = np.sort(data)

    # # calculate the proportional values of samples
    # p = 1. * np.arange(len(data)) / (len(data) - 1)
    # plt.plot(p, data_sorted)

    indices = np.arange(0,1+step,step)


    from scipy import interpolate

    totalV = 0
    selectedV =0
    checkVal= 201
    maxV = -1
    for platform in studiedApps:
        
        x = pricingDict[platform]
        if len(x) > 0:
            totalV += len(x)
            pv = len([x1 for x1 in x if x1 >=checkVal])
            maxV = max(maxV, max(x))
            selectedV += pv
            print('\t\t', platform, round(pv/len(x),2), max(x))
            y = list(range(0,len(x)))
    print(city, checkVal, round(selectedV/totalV,2), maxV)

