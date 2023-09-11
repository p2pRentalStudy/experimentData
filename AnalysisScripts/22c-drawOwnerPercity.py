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

cityShort = {}
cityShort['Barcelona'] = 'BAR'
cityShort['Berlin'] = 'BER'
cityShort['Hamburg'] = 'HAM'
cityShort['Los Angeles'] = 'LAX'
cityShort['London'] = 'LDN'
cityShort['Liverpool'] = 'LPL'
cityShort['Las Vegas'] = 'LVX'
cityShort['Lyon'] = 'LYN'
cityShort['Madrid'] = 'MAD'
cityShort['Miami'] = 'MIA'
cityShort['New York City'] = 'NYC'
cityShort['Ottawa'] = 'OTW'
cityShort['Paris'] = 'PAR'
cityShort['Toronto'] = 'TRT'
cityShort['Washington D.C.'] = 'WDC'

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


import matplotlib.pyplot as plt
import numpy as np


species = list(cityShort.keys())
speciesShort = []
for i in range(len(species)):
    speciesShort.append(cityShort[ species[i]])
penguin_means = {
    'Turo': [0]*len(species),
    'GetAround': [0]*len(species),
    'GerAroundEurope': [0]*len(species),
}

for platform in platformColor:
    print(platform)
    for cityi in range(0,len(species)):
        city = species[cityi]
        try:
            penguin_means[platform][cityi] = len(totalVehiclesPrice[platform][city])
        except:
            pass

                

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0


x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    # ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, speciesShort)
ax.legend(loc='upper left', ncol=3)
# ax.set_ylim(0, 250)

plt.xticks(x, speciesShort, rotation='vertical')

plt.title('owner per city')
# plt.subplots_adjust(left=0.08,
#                     bottom=0.13,
#                     right=0.9,
#                     top=0.95,
#                     wspace=0.4,
#                     hspace=0.4)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '22c'
fig.savefig('plots/'+scriptName+'-perOwnerTrips.png') 
fig.savefig('plots/'+scriptName+'-perOwnerTrips.eps') 


