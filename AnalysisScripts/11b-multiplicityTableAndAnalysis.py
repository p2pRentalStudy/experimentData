from basicImports import *
import requests
import random
import string
from os import walk
import requests # request img from web
import shutil # save img locally

import urllib.request


studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'

def readCars(content, platform):
    carsDict = {}
    # content = content[platform]
    # for country in content.keys():
    #     for city in content[country].keys():
    for date in content:
        for id in content[date]:
            try:
                val = content[date][id]['ownerPic']

                car = content[date][id]
                carsDict[id] = car
            except:
                pass
    return carsDict

totalOwnersDict = {}


fx = open('platformCarCat.txt', 'r')
catDict = json.loads(fx.read())
fx.close()


fx = open('citiesAndServicesCats.txt','r')
citiesAndServices = citiesAndServicesCats = json.loads(fx.read())
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


cities = [
    'Barcelona', 
    'Berlin', 
    'Hamburg', 
    'Los Angeles',
    'London', 
    'Liverpool', 
    'Las Vegas', 
    'Lyon', 
    'Madrid',
    'Miami', 
    'New York City', 
    'Ottawa',  
    'Paris',  
    'Toronto',
    'Washington D.C.' ]

catCats = ['sedan', 'suv', 'hatchback', 'van/minivan',  'truck',  'coupe', 'wagon']
citiesAndServicesMeta = {}
citiesAndServicesMeta['Turo'] = ['Las Vegas', 'Liverpool', 'London', 'Los Angeles','New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']
citiesAndServicesMeta['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
citiesAndServicesMeta['GerAroundEurope'] = ['London','Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris']

catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}

fx = open('multiplicityDict.txt','r')
totalOwnersDict  = json.loads(fx.read())
fx.close()

cityMax = ''
maxCars = 0
totalCitiesMultiplicity = {}
p1= 'GerAroundEurope'

tempList2 = [[],[],[],[],[],[],[],[]]
mmcity = {}

totalCitiesMultiplicity4 = {}
totalCitiesMultiplicity4['1'] = []
totalCitiesMultiplicity4['2'] = []
totalCitiesMultiplicity4['3'] =[]
totalCitiesMultiplicity4['4'] = []
totalCitiesMultiplicity4['5'] = []
totalCitiesMultiplicity4['6'] = []

totalMul = []
totalOwners = 0
totalCitiesMultiplicity5 = {}

p1 = 'GerAroundEurope'
for city in cities: #citiesAndServicesMeta[p1]:
    mmcity[city] = 0
    totalCitiesMultiplicity[city] = [0]
    totalCitiesMultiplicity5[city] = [0]
    for platform in [p1]:#totalOwnersDict:# [p1]: #totalOwnersDict:
        for city2 in totalOwnersDict[platform]:
            if city == city2:
                for key in totalOwnersDict[platform][city2]:
                    carsCount = len(totalOwnersDict[platform][city2][key]['vehicles'].keys())
                    totalOwners += 1
                    if carsCount > maxCars:
                        cityMax = (city, key)
                    maxCars = max(maxCars, carsCount)
                    totalMul.append(carsCount)
                    mmcity[city] = max(carsCount, mmcity[city])
                    tempList2[6].append(carsCount)
                    if carsCount > 5:
                        carsCount = 6
                    totalCitiesMultiplicity[city].append(carsCount)
                    totalCitiesMultiplicity5[city].append(tempList2[6][-1])
                    totalCitiesMultiplicity4[str(carsCount)].append(tempList2[6][-1])
                    
                    

# print(np.average(totalMul), sum(totalMul), totalOwners)
# time.sleep(1000)
from collections import Counter
totalSupplyColorsMulti = []
cityMax = {}

for city in cities:
    cityMax[city] = 0
for city in totalCitiesMultiplicity:
        cityMax[city] = max(totalCitiesMultiplicity[city])
# print(cityMax)
# time.sleep(10000)
for city in totalCitiesMultiplicity:
    for item in totalCitiesMultiplicity[city]:
        # print(item)
        totalSupplyColorsMulti.append(item)


totalLength = len(totalSupplyColorsMulti)
totalSupplyColorsMult2 = Counter(totalCitiesMultiplicity4) 

totalSupplyColorsMulti = Counter(totalSupplyColorsMulti) 

tempList = []
for key in totalSupplyColorsMulti:
    tempList.append([key,totalSupplyColorsMulti[key]])
for i in range(0, len(tempList)):
    tempList[i] = [tempList[i][0], round(tempList[i][1]/totalLength * 100,2)]
    
tempList.sort(key=lambda x:x[0])#, reverse=True)
title = 'total'
print(title, tempList, maxCars, cityMax)
print()   
print()   

# cityMax = {'Barcelona': 34, 'Berlin': 21, 'Hamburg': 61, 'Los Angeles': 328, 'London': 38, 'Liverpool': 14, 'Las Vegas': 106, 'Lyon': 96, 'Madrid': 15, 'Miami': 108, 'New York City': 288, 'Ottawa': 6, 'Paris': 327, 'Toronto': 65, 'Washington D.C.': 112}

totalSum= 0
totalCount = 0
oneItem = totalSupplyColorsMult2['1']

total2Length = 0
for city in totalCitiesMultiplicity:
    totalSupplyColors = totalCitiesMultiplicity[city]
    totalLength = len(totalSupplyColors)
    total2Length += totalLength
    if totalLength > 0:
        totalSum += sum(totalSupplyColors)
        totalCount += totalLength
        perOwnerVehicle = sum(totalSupplyColors)/totalLength

        totalSupplyColors = Counter(totalSupplyColors) 
        # print(totalSupplyColors)
        # time.sleep(1000)
        tempList = []
        for i in range(0, 6):
        # for key in totalSupplyColors:
            key = (i+1)
            try:
                tempList.append([key,totalSupplyColors[key]])
            except:
                tempList.append([key,0])
    
        for i in range(0, len(tempList)):
            # if i 
            tempList2[i].append(tempList[i][1])
            tempList[i] = [tempList[i][0], round(tempList[i][1]/totalLength * 100,1)]
       
        # tempList2[6]+= totalSupplyColors
        tempList2[7].append(cityMax[city])
        tempList.sort(key=lambda x:x[0])#, reverse=True)
        # if city == 
        title = cityShort[city]
        print(title, '&', str(tempList[0][1])+'\\% &', str(tempList[1][1])+'\\% &', str(tempList[2][1])+'\\% &', str(tempList[3][1])+'\\% &', str(tempList[4][1])+'\\% &', str(tempList[5][1])+'\\% &', round(np.average(totalCitiesMultiplicity5[city]),1), ' &', mmcity[city] , ' \\\\' )


# print(totalSum/totalCount)   
# print(oneItem, totalSum, totalSupplyColorsMult2)
print()   

# print(tempList2[6])
for i in range(0, 6):
    print(str(round(sum(tempList2[i])/total2Length*100,1))+'\%', end =' & ')
print(round(np.average(tempList2[6]),1), ' & ',max(tempList2[6]))


totalCars = 0
for key in totalCitiesMultiplicity4:
    print(key, sum(totalCitiesMultiplicity4[key])/63600,  len(totalCitiesMultiplicity4[key])/35117)
    totalCars += sum(totalCitiesMultiplicity4[key])

print(totalCars)

# for city in totalCitiesMultiplicity:
#     pri