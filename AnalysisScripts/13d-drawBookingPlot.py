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
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13-output/APPNAME/'
carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']


priceDict = {}


for city in cities:
    priceDict[city] = {}
    for cat in carCats:
        priceDict[city][cat] = []

exceptionCount = {}
totalVehicles = {}

fx = open('priceDict.txt','r')
priceDict = json.loads(fx.read())
fx.close()
# print('saved updated cats dictionary too')

# print(len(exceptionCount.keys()), len(totalVehicles.keys()))

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

#overall price average
overAllcityPrice = []
catPrice = {}
cityPrice = {}


for i in range(0,len(cities)):
    city = cities[i]
    try:
        val = cityPrice[city]
    except:
        cityPrice[city] = []
    for j in range(0, len(carCats)):
        ccat = carCats[j]
        try:
            val = catPrice[ccat]
        except:
            catPrice[ccat] = []
        for price in priceDict[cities[i]][carCats[j]]:
            overAllcityPrice.append(price)
            if price > -1:
                catPrice[ccat].append(price)
                cityPrice[city].append(price)
print(np.average(overAllcityPrice), np.std(overAllcityPrice))
print(len(overAllcityPrice), '\n\n')
for cat in catPrice:
    print(cat, np.average(catPrice[cat]))
print('\n\n')

for city in cityPrice:
    print(city, np.average(cityPrice[city]))

time.sleep(1000)


for city in priceDict:
    for cat in priceDict[city]:
        if len(priceDict[city][cat]) > 0:
            priceDict[city][cat] = round(np.average(priceDict[city][cat]),2)
        else:
            priceDict[city][cat] = -1



import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



listOfPrices =  []
carCats.sort()
cities.sort()
ytickLabels = []





for i in range(0,len(cities)):
    cityPrice = []
    for j in range(0, len(carCats)):
        cityPrice.append(priceDict[cities[i]][carCats[j]])
    listOfPrices.append(cityPrice)
    ytickLabels.append(cityShort[cities[i]])


carCats2 = carCats[:]
carCats2[-2] = 'mini/van'
df = pd.DataFrame(listOfPrices, columns=carCats2)

# plot a heatmap with custom grid lines
drawnHeatmap = sns.heatmap(df, linewidths=2, linecolor='black')
fig = drawnHeatmap.get_figure()

plt.yticks(np.arange(0.5,15.5,1), ytickLabels, rotation=0)
# plt.xticks(np.arange(15), ytickLabels, rotation=90)

# set the spacing between subplots
plt.title('Heatmap of averave booking of vehicles (price/day in USD)')
plt.subplots_adjust(left=0.08,
                    bottom=0.13,
                    right=1.03,
                    top=0.95,
                    wspace=0.4,
                    hspace=0.4)

fig.set_size_inches(7, 7.5)

scriptName = '13d'
fig.savefig('plots/'+scriptName+'-heatmapPrice.png') 
fig.savefig('plots/'+scriptName+'-heatmapPrice.eps') 