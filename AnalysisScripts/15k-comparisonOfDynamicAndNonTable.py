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


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
platformColor = {}
platformColor['Turo'] = 'red'
platformColor['GetAround'] = 'green'
platformColor['GerAroundEurope'] = 'blue'

for platform in platformColor:
    # for city 
    if 1:
    # try:
        data = {}
        data['nd'] = {}
        data['d'] = {}

        for item in ['price', 'rating', 'trips']:
            for key in data.keys():
                data[key][item] = []

        for item in totalVehiclesPrice[platform]:
            if len(item[0])/totalDays > 100:
                key = 'd'
            else:
                key = 'nd'

            newData = item[5]
            if len(newData) > 0:
                newData = newData[0]
                # print(newData)
                if newData[1] is not None and newData[1] > 0:
                    data[key]['trips'].append(newData[0])
                    data[key]['rating'].append(newData[1])
                    data[key]['price'].append(item[2])
                
        print(platform)
        for key in data['nd']:
            print('\t', key, round(np.average(data['nd'][key]),2),'&', round(np.average(data['d'][key]),2))

        # plt.plot(data, label=platform, color=platformColor[platform])
    # except Exception as e:
    #     print(e)
    #     time.sleep(1000)
    #     pass
# plt.legend()

# # plt.xlim([-20,30])
# plt.title('Rank change VS Price')
# plt.subplots_adjust(left=0.08,
#                     bottom=0.13,
#                     right=0.9,
#                     top=0.95,
#                     wspace=0.4,
#                     hspace=0.4)
# fig = plt.gcf()
# fig.set_size_inches(6, 4)

# scriptName = '15k'
# fig.savefig('plots/'+scriptName+'-cdfPriceChangePercent.png') 
# fig.savefig('plots/'+scriptName+'-cdfPriceChangePercent.eps') 


