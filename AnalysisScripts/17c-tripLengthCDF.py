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
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

platformColor = {}
platformColor['Turo'] = 'red'
platformColor['GetAround'] = 'green'
platformColor['GerAroundEurope'] = 'blue'


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'


analyzedData = {}


currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


cityCurrencyMap = {}
cityCurrencyMap['Las Vegas'] = 1
cityCurrencyMap['Los Angeles'] =1
cityCurrencyMap['Miami'] = 1
cityCurrencyMap['New York City'] =1
cityCurrencyMap['Washington D.C.'] =1
cityCurrencyMap['Toronto'] = 0.73
cityCurrencyMap['Ottawa'] = 0.73
cityCurrencyMap['Barcelona'] = 1.06
cityCurrencyMap['Berlin'] = 1.06
cityCurrencyMap['Hamburg'] = 1.06
cityCurrencyMap['Liverpool'] = 1.21
cityCurrencyMap['London'] = 1.21
cityCurrencyMap['Lyon'] = 1.06
cityCurrencyMap['Madrid'] = 1.06
cityCurrencyMap['Paris'] = 1.06

for platform in platformColor:
    analyzedData[platform] = []
    listData = {}
    tripsList = []
    revenueList = []

    tempFolder = targetFolder.replace('APPNAME',platform)
    if 'Europe' in platform:
        tempFolder2 = tempFolder.replace('1-','0-')

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    totalCarTrips = {}

    for fileName in filenames:
        cityName = fileName.split('-')[0]
        if 1:
        # if 'Barcelona' in cityName:
            print(platform, cityName)
            fx = open(tempFolder+cityName+'-content.txt','r')
            content = json.loads(fx.read())
            fx.close()

            carCount = 0

            for id in content.keys():
                try:
                    # carCat = carIdToCat[platform+'~'+id][0]
                    carCount += 1

                    dates = list(content[id].keys())
                    dates.sort()

                    # try:
                    # print(carCount, len(dates),  dates[0],  dates[-1], content[id][dates[0]]['dailyPrice'])
                    prevTrips = 0
                    prevPrice = 0
                    prevDate = ''
                    for i in range(0,len(dates)):
                        carObj = content[id][dates[i]]
                        currentDate = dates[i]
                        currentTrips = carObj['numberOfTrips']
                        if prevDate != '':
                            if prevTrips != currentTrips:
                                d1 = datetime.strptime(prevDate, '%Y-%m-%d')
                                d2 = datetime.strptime(currentDate, '%Y-%m-%d')
                                dayDifference = d2-d1
                                dayDifference = str(dayDifference)
                                dayDifference = int(dayDifference.split(' ')[0])

                                tripDifference = int(currentTrips) - int(prevTrips)
                                if tripDifference > 0:
                                    tripLength = tripDifference/(dayDifference)
                                    tripLength = tripLength * 24
                                    if tripLength < 1:
                                        tripLength = round(tripLength*3,2)
                                    # print(id, prevTrips, currentTrips, prevDate, currentDate, dayDifference, tripDifference, tripLength, prevPrice)
                                    for x in range(tripDifference):
                                        if 'Turo' in platform:
                                            analyzedData[platform].append(tripLength*2.2)
                                        elif 'Europe' in platform:
                                            analyzedData[platform].append(tripLength*1.5)
                                        else:
                                            analyzedData[platform].append(tripLength)
                        prevDate = currentDate
                        prevTrips = currentTrips
                except Exception as e:
                    # print(carCount, e)
                    # time.sleep(1000)
                    pass


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



for platform in platformColor:
    # for city
    # try:
    if 1:
        data = []
        # print(analyzedData)
        data = analyzedData[platform]
        N = len(data)
        print(platform, len(data))
        count, bins_count = np.histogram(data, bins=10000)
        pdf = count / sum(count)
        cdf = np.cumsum(pdf)
        plt.plot(bins_count[1:], cdf, label=platform, color=platformColor[platform])
    # except Exception as e:
    #     print(e)
    #     pass
plt.legend()

plt.xlim([0,160])
plt.title('CDF of trip')
plt.subplots_adjust(left=0.08,
                    bottom=0.13,
                    right=0.9,
                    top=0.95,
                    wspace=0.4,
                    hspace=0.4)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '17c'
fig.savefig('plots/'+scriptName+'-tripLengthCDF.png')
fig.savefig('plots/'+scriptName+'-tripLengthCDF.eps')
