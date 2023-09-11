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
triploadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'  

priceMulMap = {}

priceMulMap = {}
priceMulMap['GetAround'] = {}
priceMulMap['GetAround']['sedan']= 1.546
priceMulMap['GetAround']['suv']= 1.376
priceMulMap['GetAround']['hatchback']= 1.42
priceMulMap['GetAround']['wagon']= 1.41
priceMulMap['GetAround']['van/minivan']= 1.194
priceMulMap['GetAround']['coupe']= 1.76
priceMulMap['GetAround']['truck']= 1.17

priceMulMap['GerAroundEurope'] = {}
priceMulMap['GerAroundEurope']['sedan']= 3
priceMulMap['GerAroundEurope']['suv']= 2.76555
priceMulMap['GerAroundEurope']['hatchback']= 2.52
priceMulMap['GerAroundEurope']['wagon']= 1.45
priceMulMap['GerAroundEurope']['van/minivan']= 1.846
priceMulMap['GerAroundEurope']['coupe']= 1
priceMulMap['GerAroundEurope']['truck']= 1


priceMulMap['Turo'] = {}
priceMulMap['Turo']['sedan']= 2.36
priceMulMap['Turo']['suv']= 2.13
priceMulMap['Turo']['hatchback']= 2.511
priceMulMap['Turo']['wagon']= 2.516
priceMulMap['Turo']['van/minivan']= 1
priceMulMap['Turo']['coupe']= 1.944
priceMulMap['Turo']['truck']= 1.97

# priceMulCity[]
for platform in priceMulMap:
    for cat in priceMulMap[platform]:
        priceMulMap[platform][cat] *= 1.2

# for platform in ['GetAround']:
#     for cat in priceMulMap[platform]:
#         priceMulMap[platform][cat] *= 1.4

catDiv = {}
catDiv['sedan'] = 0.286
catDiv['suv'] = 0.323
catDiv['hatchback'] = 0.337
catDiv['wagon'] = 0.62
catDiv['van/minivan'] = 0.8
catDiv['coupe'] = 0.427
catDiv['truck'] = 0.371
from collections import Counter

fuelTypePriceDict = {}
fuelTypePriceDict['petrol'] = []
fuelTypePriceDict['diesel'] = []
fuelTypePriceDict['hybrid'] = []
fuelTypePriceDict['electric'] = []

fuelMapToDict = {}
fuelMapToDict['GASOLINE'] = 'diesel'
fuelMapToDict['HYBRID'] = 'hybrid'
fuelMapToDict['NA'] = 'petrol'
fuelMapToDict['ELECTRIC'] = 'electric'
fuelMapToDict['regular'] = 'petrol'
fuelMapToDict['premium'] = 'petrol'
fuelMapToDict['DIESEL'] = 'diesel'
fuelMapToDict['natural_gas'] = 'diesel'
fuelMapToDict['electric'] = 'electric'
fuelMapToDict['hydrogen'] = 'petrol'
fuelMapToDict['Unleaded 95'] = 'diesel'
fuelMapToDict['Diesel'] = 'diesel'
fuelMapToDict['Unleaded 98'] = 'petrol'
fuelMapToDict['Electric'] = 'electric'
fuelMapToDict['Other'] = 'hybrid'
fuelMapToDict['LPG'] = 'petrol'



targetFolder4 = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'

cityPlatformPrice = {}
cityAverage2 = {}
for city in cities:
    cityAverage2[city] = []
nextScriptD1 = {}
nextScriptD2 = []


totalDaysAheadData = {}



for platform in studiedApps:
    tempFolder4 = targetFolder4.replace('APPNAME',platform)
    # cityPlatformPrice[platform] 
    nextScriptD1[platform] = []
    listData = {}
    fx = open(triploadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()


    tempFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData//13-output/'+platform+'/'

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0

    for fileName in filenames:
        cityName = fileName.split('-')[1].replace('.txt', '')
        print(platform, cityName)

        # time.sleep(100000)
        if cityName != 'New York':
            try:
                v10 = totalDaysAheadData[cityName]
            except:
                totalDaysAheadData[cityName] = {}
                for i in range(0, 31):
                    totalDaysAheadData[cityName][str(i)] = []
                
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            vc = 0
            # dates4 = []
            for vehicleId in analyzedData[platform][cityName]:
                vc += 1
                # if vc > 500:
                #     break
                vehicleId = platform+'~'+vehicleId
                
                try:
                    rdcount = 0
                    for recocrdDate in content[vehicleId]:
                        totalPrices = []
                        bookingPrices = []              
                        for i in range(0,31):
                            bookingPrices.append([])
                        for dayDifference in content[vehicleId][recocrdDate]:
                            bookingPrice = float(content[vehicleId][recocrdDate][dayDifference])
                            totalPrices.append(bookingPrice)
                            dayDifference = int(int(dayDifference)/2)
                            bookingPrices[dayDifference].append(bookingPrice)
                            # time.sleep(1000)
                        totalPrices = np.average(totalPrices)
                        for i in range(0,31):
                            bookingPrices[i] = [round(item/totalPrices*100,2) for item in bookingPrices[i]]
                            totalDaysAheadData[cityName][str(i)] += bookingPrices[i]
                        # print(totalDaysAheadData)
                        # time.sleep(1000)
                except Exception as e:
                    # print(e)
                    # time.sleep(1000)
                    pass

            # break
cities = list(totalDaysAheadData.keys())
cities.sort()
for city in cities:
    for dayAdvance in totalDaysAheadData[city]:
        totalDaysAheadData[city][dayAdvance] = np.average(totalDaysAheadData[city][dayAdvance])
# print((totalPriceChangesData))
# print('\n\n')


totalPriceChangesData = totalDaysAheadData
newHeatMapData = []
ylabels = []
minVal = 100000000
maxVal = 0

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

incStep = 1
totalVAls = []
for i in range(0,31):
    totalVAls.append([])

totalDataDict ={}
for i in range(0,len(cities)):
    tempData = []
    totalDataDict[cities[i]] = {}
    for j in range(0,31,incStep):
        tempData.append(int(totalPriceChangesData[cities[i]][str(j)]))
        totalVAls[i].append(tempData[-1])
        totalDataDict[cities[i]]['vehicles booking prices '+str(j)+' days before the trip'] = tempData[-1]
        minVal = min(int(totalPriceChangesData[cities[i]][str(j)]), minVal)
        maxVal = max(int(totalPriceChangesData[cities[i]][str(j)]), maxVal)
    ylabels.append(cityShort[cities[i]])
    # tempData.reverse()
    print(cities[i])#, r1,r2)
    for j in range(0,len(tempData),2):
        print('\tdays advance:', j, ', Price:',round(tempData[j],2))
    newHeatMapData.append(tempData)

print(maxVal, minVal)
# print(newHeatMapData)
print('read and drawing cdf')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# for i in range(0,31):
#     print(i, np.average(totalVAls[i]))

from scipy import stats

step=0.05
indices = np.arange(0,1+step,step)
fig, ax = plt.subplots()


from scipy import interpolate

df = pd.DataFrame(newHeatMapData, columns=list(totalPriceChangesData['Barcelona'].keys()))

sns.heatmap(df, annot=False, annot_kws={"size": 7}, yticklabels= ylabels, vmin=92, vmax=106)#, linewidths=2,)



plt.ylabel('Cities', fontsize=15)
plt.xlabel('Days in advance', fontsize=15)

plt.title('Heatmap of Booking Price in Advance Bookings', fontsize=16)

# plt.xticks([0,3,6,9,12,15,18,21,24,27,30], [0,3,6,9,12,15,18,21,24,27,30])


# plt.xlim(0,1500)

print(totalDataDict)
plt.subplots_adjust(left=0.13,
                    bottom=0.12,
                    right=1.03,
                    top=0.92,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
fig.set_size_inches(6, 7.5)
ax.tick_params(axis='x', labelsize=13)
ax.tick_params(axis='y', labelsize=13)


scriptName = '33p'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 
