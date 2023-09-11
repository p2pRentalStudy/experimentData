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


savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/22-output/'         
fx = open(savePath+'ownerTrips.txt','r')
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
    print(platform)
    # for city 
    try:
        data = []
        for city in totalVehiclesPrice[platform]:
            cityOwnerTrips = []
            # if 1:
            try:
                # if (totalVehiclesPrice[platform][city]) > 0:
                
                print(len(totalVehiclesPrice[platform][city]))
                for owner in totalVehiclesPrice[platform][city]: 
                    currentOwnerTrips = 0
                    myList = totalVehiclesPrice[platform][city][owner]
                    # print(owner, len(myList))
                    # time.sleep(1)
                    for item in myList:
                        currentOwnerTrips += item[1]
                    cityOwnerTrips.append(currentOwnerTrips)
                    data.append(currentOwnerTrips)
                        
                print('\t',city, np.average(cityOwnerTrips))
                # else:
                #     print('\t',city, 'no data')
            except Exception as e:
                print('\t',city, 'no data', e)
                # time.sleep(1000)

        # data = totalVehiclesPrice[platform]
        N = len(data)
        print(platform, len(data))
        count, bins_count = np.histogram(data, bins=10000)
        pdf = count / sum(count)
        cdf = np.cumsum(pdf)
        plt.plot(bins_count[1:], cdf, label=platform, color=platformColor[platform])
    except:
        pass
plt.legend()

plt.xlim([-10, 500])
plt.title('trips per owner')
plt.subplots_adjust(left=0.08,
                    bottom=0.13,
                    right=0.9,
                    top=0.95,
                    wspace=0.4,
                    hspace=0.4)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '22b'
fig.savefig('plots/'+scriptName+'-perOwnerTrips.png') 
fig.savefig('plots/'+scriptName+'-perOwnerTrips.eps') 


