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


weekdays= ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

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

dateToDayDict = {}
triploadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'  

cityDayPrices = {}

for platform in studiedApps:
    fx = open(triploadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()

    pricingDict[platform] = []
    tempFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13b-output/'+platform+'/'
    listData = {}
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    totalCarTrips = {}
    diffPricesMain = []
    # print(filenames)
    for fileName in filenames:
        cityName = fileName.split('-')[1]
        cityName = cityName.replace('.txt', '')
        platform = fileName.split('-')[0]
        
        fx = open(tempFolder+fileName,'r')
        carPricingDict = json.loads(fx.read())
        print(platform, cityName, len(carPricingDict.keys()))
        fx.close()
        # print()
        try:
            v10 = cityDayPrices[cityName]
        except:
            cityDayPrices[cityName] = []
            for i in range(7):
                cityDayPrices[cityName] .append([])
        
        differingPrices2 = 0
        maxUpdate = 0
        vc = 0
        for vehicle in carPricingDict:
            vid = vehicle.replace(platform,'')
            vid = vid.replace(cityName,'')
            vid = vid.replace('~','')
            # if 1:
            try:
                v10 = analyzedData[platform][cityName][vid]

                totalPrice = []
                for i in range(7):
                    totalPrice.append([])
                vprices=  []
                for recDate in carPricingDict[vehicle]:
                    pricesList = carPricingDict[vehicle][recDate]
                    # print(recDate, pricesList)
                    # time.sleep(1)
                    recDate = recDate.split(' ')[0]
                    vprices += pricesList

                    try:
                        x = dateToDayDict[recDate]
                    except:
                        if 'Turo' in platform:
                            date_object = datetime.strptime(recDate, '%m-%d-%Y').date()
                        else:
                            date_object = datetime.strptime(recDate, '%Y-%m-%d').date()
                        x = int(date_object.weekday())
                        dateToDayDict[recDate] = x
                    for item in pricesList:
                        totalPrice[x].append(item)
                    vc += 1
                vprices = np.average(vprices)
                for i in range(0,7):
                    # print(totalPrice[i])
                    # print(vprices)
                    totalPrice[i] = [(item/vprices)*100 for item in totalPrice[i]]
                    # print(totalPrice[i])
                    # time.sleep(1000)
                    if len(totalPrice[i]) > 0:
                        cityDayPrices[cityName][i].append(np.average(totalPrice[i]))
                
            except Exception as e:
                # print(e)
                # time.sleep(1000)
                pass
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


plt.rcdefaults()
fig, ax = plt.subplots()
print('\n\n')

daysPrices = []
for i in range(0,len(weekdays)):
    daysPrices.append([])

heatmapData = []
cities.sort()
for city in cities:
    heatmapData.append([])
        
ylabels = []

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


for cityin in range(len(cities)):
    city = cities[cityin]
    ylabels.append(cityShort[city])
    print(city)
    for i in range(0,len(weekdays)):
        day = weekdays[i]
        print('\t',day, np.average(cityDayPrices[city][i]), len(cityDayPrices[city][i]))
        if len(cityDayPrices[city][i]) > 0:
            daysPrices[i].append(np.average(cityDayPrices[city][i]))
            
        heatmapData[cityin].append(np.average(cityDayPrices[city][i]))
    
for i in range(0,len(weekdays)):
    daysPrices[i] = round(np.average(daysPrices[i]),2)
    print(weekdays[i], daysPrices[i])
# Example data
weekdaysShorts = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


df = pd.DataFrame(heatmapData, columns=list(weekdaysShorts))

sns.heatmap(df, annot=False, annot_kws={"size": 7}, yticklabels= ylabels, vmin=90, vmax=125)#, linewidths=2,)



plt.xlabel('Days of the week', fontsize=12)
plt.ylabel('Cities', fontsize=12)

plt.title('Booking Prices Percentage on Different Week Days', fontsize=13)

# plt.xlim(0,1500)


plt.subplots_adjust(left=0.14,
                    bottom=0.13,
                    right=0.98,
                    top=0.93,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
fig.set_size_inches(5, 4.5)


scriptName = '33k'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 


fx = open('dynamicPricingFrequency.txt', 'w')
fx.write(json.dumps(pricingDict))
fx.close()
