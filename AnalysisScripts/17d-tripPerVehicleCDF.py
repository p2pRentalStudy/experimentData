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

                    differenceTrips = content[id][dates[-1]]['numberOfTrips'] - content[id][dates[0]]['numberOfTrips']
                    
                    analyzedData[platform].append(differenceTrips)
                    #                     
                except Exception as e:
                    print(carCount, e)
                    time.sleep(1000)
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
plt.title('CDF of trip per vehicle')
plt.subplots_adjust(left=0.08,
                    bottom=0.13,
                    right=0.9,
                    top=0.95,
                    wspace=0.4,
                    hspace=0.4)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '17d'
fig.savefig('plots/'+scriptName+'-tripPerVehicle.png') 
fig.savefig('plots/'+scriptName+'-tripPerVehicle.eps') 



                    