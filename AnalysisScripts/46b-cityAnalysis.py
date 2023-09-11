from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'  


carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'suv']

studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1



analyzedData = {}

vc = 0
totalTrips = 0


currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


cityCurrencyMap = {}
cityCurrencyMap['Las Vegas'] = 1
cityCurrencyMap['Los Angeles'] =1 
cityCurrencyMap['Miami'] = 1
cityCurrencyMap['New York City'] =1 
cityCurrencyMap['Washington D.C.'] =1 
cityCurrencyMap['Toronto'] = 0.73
cityCurrencyMap['Ottawa'] = 0.73
cityCurrencyMap['Barcelona'] = 1.06
cityCurrencyMap['Berlin'] = 1.06
cityCurrencyMap['Hamburg'] = 1.06
cityCurrencyMap['Liverpool'] = 1.21
cityCurrencyMap['London'] = 1.21
cityCurrencyMap['Lyon'] = 1.06
cityCurrencyMap['Madrid'] = 1.06
cityCurrencyMap['Paris'] = 1.06




studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1


lengthMulMap = {}
lengthMulMap['GerAroundEurope'] = {}
lengthMulMap['GerAroundEurope']['sedan']= 7.17
lengthMulMap['GerAroundEurope']['suv']= 6.98
lengthMulMap['GerAroundEurope']['hatchback']= 6.78
lengthMulMap['GerAroundEurope']['wagon']= 4.8
lengthMulMap['GerAroundEurope']['van/minivan']= 5.5
lengthMulMap['GerAroundEurope']['coupe']= 3
lengthMulMap['GerAroundEurope']['truck']= 1

lengthMulMap['GetAround'] = {}
lengthMulMap['GetAround']['sedan']= 2.891
lengthMulMap['GetAround']['suv']= 2.72
lengthMulMap['GetAround']['hatchback']= 2.72
lengthMulMap['GetAround']['wagon']= 2.14
lengthMulMap['GetAround']['van/minivan']= 2.491
lengthMulMap['GetAround']['coupe']= 1.92
lengthMulMap['GetAround']['truck']= 3.3


lengthMulMap['Turo'] = {}
lengthMulMap['Turo']['sedan']= 7.973
lengthMulMap['Turo']['suv']= 7.22
lengthMulMap['Turo']['hatchback']= 8.21
lengthMulMap['Turo']['wagon']= 8.05
lengthMulMap['Turo']['van/minivan']= 6.87
lengthMulMap['Turo']['coupe']= 5.121
lengthMulMap['Turo']['truck']= 6.661



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
for platform in priceMulMap:
    for cat in priceMulMap[platform]:
        priceMulMap[platform][cat] *= 1.2


platFormCatTrip = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1

cityDict = {}
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for city in cityCurrencyMap.keys():
    cityDict[city] = {}
    for day in daysOfWeek:
        cityDict[city][day] = []
    cityDict[city]['totalTrips'] = 0


dateToDayDict = {}
v3 = []
v4 = []

totalTripsPerOwnerData = {}

for platform in studiedApps:
    vc = 0
    # print(platform)
    platFormCatTrip[platform] = {}
    totalTripsPerOwnerData[platform] = {}

    fx = open(loadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()
    catVehicleDict = {}
    v1 = []
    v2 = []
    for cityName in analyzedData[platform]:
        if cityName != 'New York':
            totalTripsPerOwnerData[platform][cityName] = {}
            # print('\t',cityName)
            fx = open(loadPath +platform+'-'+cityName+'-tripDetails.txt','r')
            tripDetailsDict = json.loads(fx.read())
            fx.close()
            for carId in analyzedData[platform][cityName]:
                vc += 1
                cat = 'sedan'
                try:
                    cat = cityServiceCat[platform][cityName][carId][0]
                except:
                    ijk = 10

                totalTrips += analyzedData[platform][cityName][carId]['trips'][1]
                ownerID = str(analyzedData[platform][cityName][carId]['ownerID'])

                try:
                    v10 = totalTripsPerOwnerData[platform][cityName][ownerID]
                except:
                    totalTripsPerOwnerData[platform][cityName][ownerID] = {}
                totalTripsPerOwnerData[platform][cityName][ownerID][carId] = []
                for tripObj in tripDetailsDict[platform][cityName][carId]:
                    tripDate = tripObj['StartDate']
                    try:
                        tripDay = dateToDayDict[tripDate]
                    except:
                        tripDay = pd.Timestamp(tripDate)
                        tripDay = tripDay.day_name()
                        dateToDayDict[tripDate] = tripDay
                    
                    cityDict[cityName]['totalTrips'] += 1
                    tripObj['length'] = tripObj['length'] * lengthMulMap[platform][cat]
                    tripObj['price'] = tripObj['price'] * priceMulMap[platform][cat]
                    tripObj['carId'] = carId
                    tripObj['carCat'] = cat
                    tripObj['platform'] = platform

                    
                    # print(tripObj)

                    v1.append(tripObj['length'])
                    v2.append(tripObj['price'])
                    v3.append(tripObj['length'])
                    v4.append(tripObj['price'])

                    totalTripsPerOwnerData[platform][cityName][ownerID][carId].append([tripObj['length'],tripObj['price'],  tripObj['StartDate']])
                    # time.sleep(1)
                    cityDict[cityName][tripDay].append(tripObj)
                    # print(tripObj['StartDate'], tripDay)
                    # time.sleep(1000)


#     print(platform, np.average(v1))
#     print(np.average(v2))
# print(np.average(v3))
# print(np.average(v4))
# print((np.average(v4)/np.average(v3)) * 24)

# time.sleep(100000)
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
newHeatMapData = []

cities = list(cityShort.keys())
cities.sort()

ylabels = []
shortDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
newDict = {}
totalVals = []


import matplotlib.pyplot as plt
import numpy as np
print('\n\n\n')




def my_autopct(pct):
    return (str('%.0f' % pct)+'') if pct > 2 else ''

newDict = {}
tc = 0
tt1 = 0
ttv =0 
mtr = 583891
tvc = 0
pt0 = 0
maxTupple = [0,0,0,0]
for platform in totalTripsPerOwnerData:
    # totalData = [[], [], [], [], [], [], [], [], [], [], []]
    # totalData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    newDict[platform] = {}
    totalData = [0, 0, 0, 0, 0, 0, ]

    ttr = 0

    
    totalTrips = 0

    ppt0 = 0
    ppv = 0
    for cityName in totalTripsPerOwnerData[platform]:
        newDict[platform][cityName] = {}
        for x in range(0, 6):
            newDict[platform][cityName]['owner of '+str(x+1)+'vehicles'] = 0
        to = 0
        t1 = 0
        vc = 0
        tpv = 0
        x1 = 0
        ptv = 1
        for ownerID in totalTripsPerOwnerData[platform][cityName]:
            tc += 1
            ownerCars = len(totalTripsPerOwnerData[platform][cityName][ownerID].keys())
            ownerTrips = 0
            for carID in totalTripsPerOwnerData[platform][cityName][ownerID].keys():
                tvc += 1
                
                x1 += 1
                ownerTrips += len(totalTripsPerOwnerData[platform][cityName][ownerID][carID])
                ttr += len(totalTripsPerOwnerData[platform][cityName][ownerID][carID])
                ptv += len(totalTripsPerOwnerData[platform][cityName][ownerID][carID])
                ppv += len(totalTripsPerOwnerData[platform][cityName][ownerID][carID])
                # mtr += len(totalTripsPerOwnerData[platform][cityName][ownerID][carID])
            totalData[min(5, ownerCars-1)] += ownerTrips
            to+=1

            if maxTupple[0] < ownerTrips:
                maxTupple = [ownerTrips, ownerCars, cityName, platform]
            if ownerCars == 1:
                pt0 += ownerTrips
                ppt0 += ownerTrips
            newDict[platform][cityName]['owner of '+str(min(6, ownerCars))+'vehicles']+=ownerTrips

            # newDict[platform]['owner of '+str(min(5, ownerCars-1))+'vehicles'].append(ownerTrips)
        # print(platform, cityName, x1/to, ttr/mtr)
        for i in range(0,6):
            newDict[platform][cityName]['owner of '+str(i+1)+'vehicles'] = round(newDict[platform][cityName]['owner of '+str(i+1)+'vehicles']/ptv,2)

        
    # sumTD= sum(totalData)
    # for i in range(0, len(totalData)):
    #     totalData[i] = round((totalData[i]/sumTD)*100,2)
    #     newDict[platform]['owner of '+str(i+1)+'vehicles'] = totalData[i]
    print(platform, ttr/mtr, ptv/x1, ppt0/ppv)
    # labelData = ['1','2','3','4','5','5+']
    # y = totalData
print(mtr, mtr/tvc, pt0/mtr)

print(newDict)

print(maxTupple)