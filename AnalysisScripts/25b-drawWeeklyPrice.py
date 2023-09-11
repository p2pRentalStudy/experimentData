from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/vehicleCat-output/'
fx = open(loadPath + 'vehicleCategories.txt','r')
carIdToCat = json.loads(fx.read())
fx.close()

carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']


analyzedData = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


import numpy as np
import matplotlib.pyplot as plt

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/vehicleTrips.txt'
fx = open(loadPath,'r')
tripsDict = json.loads(fx.read())
fx.close()




weekdays= ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']



N = 7
ind = np.arange(N)


colors =['red', 'green','blue']
apps = ['GerAroundEurope', 'Turo', 'GetAround']
width = 0.25
bars = []
# print()

totalMeta = {'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}, 'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}}


for pi in range(len(apps)):
    platform = apps[pi]
    weekdaysDict = {}
    for weekday in weekdays:
        weekdaysDict[weekday] = []

    print(platform)


    for city in totalMeta[platform]:
        print('\t', city)
        totalTrips = 0

        savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/25-output/'+platform+'/'
        fx = open(savePath + platform+'-'+city+'.txt','r')
        analyzedData = json.loads(fx.read())
        fx.close()
        # print('\t loaded ', platform, city)

        # for weekday in analyzedData:
        for day in weekdays:
            dayVals = []
            totalVals =  analyzedData[day]
            for bookingPriceItem in totalVals:
                weekdaysDict[day].append(bookingPriceItem[2])
                dayVals.append(bookingPriceItem[2])
            print('\t\t', day, np.average(dayVals))
        # break

    xvals = []
    for i in range(0, len(weekdays)):
        # print(weekdaysDict[weekdays[i]][:10])
        xvals.append(np.average(weekdaysDict[weekdays[i]]))

    # print(xvals)
    bar = plt.bar(ind+(pi*width), xvals, width, color = colors[pi])

    # yvals = [10, 20, 30]
    # bar2 = plt.bar(ind+width, yvals, width, color='g')

    # zvals = [11, 12, 13]
    # bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')
    # width += 0.25
    bars.append(bar)
    # break/


plt.xlabel("Dates")
plt.ylabel('Scores')
plt.title("Players Score")

plt.xticks(ind+width,weekdays)
plt.legend( bars, apps )
# plt.show()
fig = plt.gcf()

scriptName = '25b'
fig.savefig('plots/'+scriptName+'-weekdaylyPrices.png')
fig.savefig('plots/'+scriptName+'-weekdaylyPrices.eps')
