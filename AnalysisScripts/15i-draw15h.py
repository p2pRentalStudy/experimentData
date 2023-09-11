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
# studiedApps['Turo'] = 1
# studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/15-output/APPNAME/'
carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']


priceDict = {}


for city in cities:
    priceDict[city] = {}
    for cat in carCats:
        priceDict[city][cat] = []


savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/15-output/'         
fx = open(savePath+'15h-priceChangeDict.txt','r')
totalVehiclesPrice = json.loads(fx.read())
fx.close()

totalMeta = {'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}, 'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}}

totalDays = 1
maxChange = 0

# for platform in totalVehiclesPrice:
#     lesser = 0
#     myList = totalVehiclesPrice[platform]
#     print(platform)
#     # for i in range(0, len(myList)):
#         # maxChange = max(myList[i], maxChange)
#         # myList[i] = myList[i]/totalDays
#     for i in range(0, 1):
#         lesser += myList.count(i)
#         # print('\t\t', i,'changes', round(myList.count(i)/len(myList),2)*100)
#     print('\t', round(lesser/len(myList),2)*100)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
platformColor = {}
platformColor['Turo'] = 'red'
platformColor['GetAround'] = 'green'
platformColor['GerAroundEurope'] = 'blue'

for platform in platformColor:
    # for city 
    try:
        data = []
        for item in totalVehiclesPrice[platform]:
            if len(item[0])/totalDays > 10:
                # for i in range(len(item[0])):
                data += item[1]
        N = len(data)

        # data = totalVehiclesPrice[platform]
        # if 'Turo' not in platform:
        #     tempData = [50]#*int(10*(len(data)))
        #     data += tempData
        print(platform, len(data))
        count, bins_count = np.histogram(data, bins=10000)
        pdf = count / sum(count)
        cdf = np.cumsum(pdf)
        plt.plot(bins_count[1:], cdf, label=platform, color=platformColor[platform])
    except:
        pass
plt.legend()

plt.xlim([-200,200])
plt.title('Ranking Change CDF')
plt.subplots_adjust(left=0.08,
                    bottom=0.13,
                    right=0.9,
                    top=0.95,
                    wspace=0.4,
                    hspace=0.4)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '15i'
fig.savefig('plots/'+scriptName+'-cdfPriceChangePercent.png') 
fig.savefig('plots/'+scriptName+'-cdfPriceChangePercent.eps') 


