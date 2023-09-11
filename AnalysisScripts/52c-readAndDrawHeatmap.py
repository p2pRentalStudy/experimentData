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

currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


citiesPriceAverage = {}


import orjson 



dateToObj = {}

advanceDaysBookings = {}

platformService = {'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}, 'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}}

# platformService['Turo'] = {}
# platformService['Turo']['Miami'] = 1

fx = open('carAdvanceBookingHoursDict.txt', 'r')
hoursData = json.loads(fx.read())
fx.close()

fig, ax = plt.subplots()


zeroes = 0

explainData = {}
tc = 0
lc = 0

totalData = {}
totalCityTrips = {}
maxp = 1000
for platform in studiedApps:
    explainData[platform]  = {}
    print(platform)
    plabel = 'GA-E'
    pcolor = 'olive'
    if platform == 'Turo':
        plabel = 'TR'
        pcolor= 'maroon'
    elif platform == 'GetAround':
        plabel = 'GA'
        pcolor= 'mediumblue'

    # totalData = []
    
    for city in platformService[platform]:
        try:
            v10 = totalData[city]
        except:
            totalData[city] = []
            totalCityTrips[city] = 0
            for i in range(30):
                totalData[city].append(0)
        # print('\t', city)
        explainData[platform][city] = {}
        cityData = []
        for item in hoursData[platform][city]:
            
            tba = item[0]
            # print(item)
            # maxp = m
            # ax(maxp,tba)
            tba = (tba/(maxp))*720

            tba = int((tba/1)/24)
            # tba = tba/2
            try:
                totalData[city][tba] +=1
                totalCityTrips[city] += 1
            except:
                pass
            
        # explainData[platform][city] = []
        # onePercentLen = int(len(cityData)*0.02)
        # for j in range(0,len(cityData),onePercentLen):
        #     explainData[platform][city].append(round(np.average(cityData[j:j+onePercentLen]),2))
        # totalData += cityData
    
print(maxp)
    # print((x))
print('read and drawing cdf')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

cities = list(cityShort.keys())
cities.sort()
newHeatMapData = []

xlabels = []
ylabels = []
maxval = 0

fractionTrips = []


targetCity = ['Barcelona', 'Berlin', 'Hamburg', 'Lyon', 'Madrid', 'Paris', 'London', 'Paris' ]


explainDict = {}
for i in range(0, len(cities)):
    city = cities[i]
    ylabels.append(cityShort[city])
    tt = totalCityTrips[city]
    daysTrips = totalData[city]
    xlabels = []
    explainDict[city] = {}
    for j in range(0,len(daysTrips)):
        xlabels.append(j+1)
        daysTrips[j] = int((daysTrips[j]/tt)*100)
        explainDict[city]['% of bookings '+str(j)+' days before the trips'] = daysTrips[j]
        maxval = max(maxval, daysTrips[j] )
    newHeatMapData.append(daysTrips)
    if city in targetCity:
        fractionTrips.append(sum(daysTrips[15:]))
        print(city, fractionTrips[-1])

# print(explainDict)
print(min(fractionTrips), max(fractionTrips))   
from scipy import stats

print(maxval)
step=0.05
indices = np.arange(0,1+step,step)
fig, ax = plt.subplots()


from scipy import interpolate

df = pd.DataFrame(newHeatMapData, columns=list(xlabels))

sns.heatmap(df, cbar=False, annot=True, annot_kws={"size": 10}, yticklabels= ylabels, vmin=0, vmax=22)#, linewidths=2,)

for t in ax.texts:
    if float(t.get_text())<1 and float(t.get_text())>0:
        t.set_text('') # if not it sets an empty text


# plt.ylabel('Cities', fontsize=12)
plt.xlabel('Advance booking days', fontsize=12)

# plt.title('Heatmap of Booking Price in Advance Bookings', fontsize=14)

plt.xticks([0,3,6,9,12,15,18,21,24,27,30], [0,3,6,9,12,15,18,21,24,27,30], rotation=0)


# plt.xlim(0,1500)


plt.subplots_adjust(left=0.09,
                    bottom=0.12,
                    right=0.99,
                    top=0.98,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
fig.set_size_inches(6, 4.5)


scriptName = '52c'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 


# print(explainData)

                


            
