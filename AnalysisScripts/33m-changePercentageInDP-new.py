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
pricingDict = {}
from statistics import mode

#pre vehicle records 3209.094352423133, claimed = 2M
# per time stamp 28.770424924304738, claimed = 446

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
        
        fx = open(tempFolder+fileName,'r')
        carPricingDict = json.loads(fx.read())
        print(platform, cityName, len(carPricingDict.keys()))
        fx.close()
        # print()
        
        differingPrices2 = 0
        maxUpdate = 0
        for vehicle in carPricingDict:
            try:
                vehiclePrice = carPricingDict[vehicle]
                plenList.append(len(vehiclePrice))
                differingPrices = []
                for i in range(1, len(vehiclePrice)):
                    if vehiclePrice[i-1]   != vehiclePrice[i] : 
                        differingPrices.append(int((abs(1-(vehiclePrice[i] / vehiclePrice[i-1]))*100)))
                if len(differingPrices)> 0:
                    pricingDict[platform]+=differingPrices
            except Exception as e: 
                # print(e)
                # time.sleep(1000)
                pass
        #tbc
        # break
        # print('\t', platform, cityName, differingPrices2/len(carPricingDict.keys()), maxUpdate)

print(np.average(plenList), max(plenList))
print('read and drawing cdf')

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
checkVal= 50
for platform in studiedApps:
    avrgHigherVals = []

    plabel = 'GA-E'
    pcolor = 'olive'
    if platform == 'Turo':
        plabel = 'TR'
        pcolor= 'maroon'
    elif platform == 'GetAround':
        plabel = 'GA'
        pcolor= 'mediumblue'


    x = pricingDict[platform]

    totalV += len(x)
    pv = [x1 for x1 in x if x1 > checkVal]
    avrgHigherVals += pv
    pv = len(pv)
    selectedV += pv
    print(platform, np.average(x), max(x))#pv/len(x), np.average(avrgHigherVals), max(x))
    print('\t',pv/len(x), np.average(avrgHigherVals), max(x))

    # y = list(range(0,len(x)))

    x2 = np.histogram(x, bins = 1000)
    sns.ecdfplot(data=x, color=pcolor, label=plabel)


# plt.plot(xnew, power_smooth,linewidth=4, label='#interventions', color='blue')
print(checkVal, selectedV/totalV)
plt.legend(fontsize =13)
ax.tick_params(axis='both', which='major', labelsize=13)
ax.tick_params(axis='both', which='minor', labelsize=13)
# ax.set_xscale('log')
plt.grid()


# plt.xticks([10, 20,40, 80, 150, 300, 500, 750, 1000], ['10', '20','40', '80', '150', '300', '500', '750', '1K'])

# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0', '20','40', '60', '80', '100'])


plt.yticks([0,0.2,0.4,0.6,0.8,1.0], ['0','20','40','60','80','100'])

plt.ylabel('Percentage of Price Updates', fontsize=15)
plt.xlabel('Abosulte Percentage of Price Change', fontsize=15)

plt.title('CDF of Price Update Intensity', fontsize=16)

plt.xlim(0,150)


plt.subplots_adjust(left=0.14,
                    bottom=0.15,
                    right=0.95,
                    top=0.93,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
fig.set_size_inches(5, 4.5)


scriptName = '33m'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 


fx = open('dynamicPricingFrequency.txt', 'w')
fx.write(json.dumps(pricingDict))
fx.close()
