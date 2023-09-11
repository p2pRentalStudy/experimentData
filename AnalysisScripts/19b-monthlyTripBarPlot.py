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



totalMeta = {'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}, 'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}}

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'
analyzedData = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


import numpy as np
import matplotlib.pyplot as plt


loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/19-output/monthlyTripDict.txt'
fx = open(loadPath,'r')
analyzedData = json.loads(fx.read())
fx.close()

months= ['10','11','12','01','02','03','04']



N = 7
ind = np.arange(N)


colors =['red', 'green','blue']
apps = ['Turo', 'GetAround','GerAroundEurope']
width = 0.25
bars = []
# print()
for pi in range(len(apps)):
    platform = apps[pi]
    monthsDict = {}
    for month in months:
        monthsDict[month] = 10

    print(platform)
    for city in analyzedData[platform]:
        print('\t', city)
        totalTrips = 0
        for month in analyzedData[platform][city]:
            try:
                # print(month, analyzedData[platform][city][month])
                monthsDict[month] += analyzedData[platform][city][month]['trips']/len(analyzedData[platform][city][month]['days'])
            except Exception as e:
                # print(e)
                # time.sleep(100)
                pass
    xvals = []
    for i in range(0, len(months)):
        xvals.append(monthsDict[months[i]])


    print(xvals)
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

plt.xticks(ind+width,['10','11','12','01','02','03','04'])
plt.legend( bars, apps )
# plt.show()
fig = plt.gcf()

scriptName = '19b'
fig.savefig('plots/'+scriptName+'-monthlyTrips.png')
fig.savefig('plots/'+scriptName+'-monthlyTrips.eps')
