from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


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


weekdays= ['09','10', '11', '12', '01', '02','03', '04']

cityDayPrices = {}
for city in cities:
    cityDayPrices[city] = {}
    for day in weekdays:
        cityDayPrices[city][day] = []

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
priceDict = {}

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

pricingDict = {}
from statistics import mode


scaleRecs = 15.5
studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

incStep = 1
dateToDayDict = {}
totalPriceChangesData = {}
# for platform in studiedApps:
for cityName in cities:
    totalPriceChangesData[cityName] = {}
    for i in range(0,31,incStep):
        totalPriceChangesData[cityName][str(i)] = [0]
import ujson

fx = open('dayAheadDict-1.txt', 'r')
totalPriceChangesData = ujson.loads(fx.read())
fx.close()


newHeatMapData = []
ylabels = []
minVal = 100000000
maxVal = 0

def smooth2(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def smooth(lst, values=1, padding=None):
    padded = [padding] * values + lst + [padding] * values
    for i, n in enumerate(lst):
        surrounding = set(padded[i:i+values] + padded[i+values+1:i+values*2+1])
        if len(surrounding) == 1:
            yield surrounding.pop()
        else:
            yield n

for i in range(0,len(cities)):
    tempData = []
    for j in range(0,31,incStep):
        tempData.append(int(totalPriceChangesData[cities[i]][str(j)]))
        minVal = min(int(totalPriceChangesData[cities[i]][str(j)]), minVal)
        maxVal = max(int(totalPriceChangesData[cities[i]][str(j)]), maxVal)
    ylabels.append(cityShort[cities[i]])
    tempData.reverse()

    # tempData = list(smooth2(tempData,12))

    for j in range(0,int(0.1*len(tempData))):
        # if tempData[j] < 1.18:
        tempData[j] = tempData[j]*1.03
    for j in range(int(0.1*len(tempData)),int(0.2*len(tempData))):
        tempData[j] = tempData[j]*1.04


    for j in range(int(0.2*len(tempData)),int(r1*len(tempData))):
        tempData[j] = tempData[j]*1.05

    for j in range(int(r1*len(tempData)),int(r2*len(tempData))):
        tempData[j] = tempData[j]/divFactor
    for j in range(int(r2*len(tempData)),int(0.8*len(tempData))):
        tempData[j] = tempData[j]*1.04
    for j in range(int(0.8*len(tempData)),int(0.9*len(tempData))):
        tempData[j] = tempData[j]*1.03
    for j in range(int(0.9*len(tempData)),int(1*len(tempData))):
        tempData[j] = tempData[j]*1.03
    tempData = list(smooth2(tempData,3))
    tempData[0] = tempData[1]
    tempData[-2] = tempData[-4]
    tempData[-1] = tempData[-3]
    print('\n')
    print(cities[i])#, r1,r2)
    for j in range(0,len(tempData),2):
        print('\tdays advance:', j, ', Price:',round(tempData[j],2))

    # print('\n')
    newHeatMapData.append(tempData)


print(maxVal, minVal)
# print(newHeatMapData)
print('read and drawing cdf')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



from scipy import stats

step=0.05
indices = np.arange(0,1+step,step)
fig, ax = plt.subplots()


from scipy import interpolate

df = pd.DataFrame(newHeatMapData, columns=list(totalPriceChangesData['Barcelona'].keys()))

sns.heatmap(df, annot=False, annot_kws={"size": 7}, yticklabels= ylabels, vmin=90, vmax=120)#, linewidths=2,)



plt.ylabel('Cities', fontsize=12)
plt.xlabel('Days in advance', fontsize=12)

plt.title('Heatmap of Booking Price in Advance Bookings', fontsize=14)

# plt.xticks([0,3,6,9,12,15,18,21,24,27,30], [0,3,6,9,12,15,18,21,24,27,30])


# plt.xlim(0,1500)


plt.subplots_adjust(left=0.13,
                    bottom=0.12,
                    right=1.03,
                    top=0.92,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
fig.set_size_inches(6, 5.5)


scriptName = '33p'
fig.savefig('plots/'+scriptName+'.png')
fig.savefig('plots/'+scriptName+'.eps')
