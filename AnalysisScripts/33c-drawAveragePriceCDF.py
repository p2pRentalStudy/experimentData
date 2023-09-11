from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


import ast


studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]



catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
notFound = {}
totalTypes = {}

import ujson
totalPriceCDF = []
fx = open('totalPrices2.txt','r')
totalPriceCDF = ujson.loads(fx.read())['totalPrices']
fx.close()


platformAverage = {}
fx = open('platformPrices2.txt','r')
platformAverage = ujson.loads(fx.read())
fx.close()
# print(platformAverage['Turo'][:10])
# time.sleep(10000)
# totalPriceCDF = eval(totalPriceCDF)


data = totalPriceCDF
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
  
# No of Data points
# totalPriceCDF.sort()
# totalPriceCDF = totalPriceCDF[1000:]
tempArr = []
addI = 0


# totalPriceCDF.sort()

# for i in range(0,len(totalPriceCDF)):
#     if totalPriceCDF[i] > 20:
#         addI += 1
#         if addI %100 == 0:
#             tempArr.append(totalPriceCDF[i]*0.88)
            

# totalPriceCDF = tempArr
from scipy.ndimage.filters import gaussian_filter1d
from scipy import stats

df_describe = pd.DataFrame(totalPriceCDF)
# print(stats.describe(df_describe))
# totalPriceCDF = filter(lambda x: x >= 15, totalPriceCDF)
totalPriceCDF = [i * 1 for i in totalPriceCDF]
print(np.average(totalPriceCDF))
print(np.std(totalPriceCDF))
N = len(totalPriceCDF)

print(N)


step=0.05
indices = np.arange(0,1+step,step)


fig, ax = plt.subplots()

# data_sorted = np.sort(data)

# # calculate the proportional values of samples
# p = 1. * np.arange(len(data)) / (len(data) - 1)
# plt.plot(p, data_sorted)

indices = np.arange(0,1+step,step)

maxVal = 0
for platform in studiedApps:
    lineData = platformAverage[platform]
    maxVal = max(max(lineData), maxVal)
from scipy.interpolate import make_interp_spline


maxVal = [maxVal] * 10
for platform in studiedApps:
    
    plabel = 'GA-E'
    pcolor = 'olive'
    if platform == 'Turo':
        plabel = 'TR'
        pcolor= 'maroon'
    elif platform == 'GetAround':
        plabel = 'GA'
        pcolor= 'mediumblue'

    lineData = platformAverage[platform] 
    lineData = [i * 1 for i in lineData]
    print(platform, np.average(lineData))
    # if 'Tu' not in platformAverage:
    #     lineData += maxVal

    # lineData = gaussian_filter1d(lineData, sigma=2)
    # poly = np.polyfit(x,y,n)
    # poly_y = np.poly1d(poly)(x)

    # CDF = pd.DataFrame({'dummy':lineData})['dummy'].quantile(indices)
    # plt.plot(CDF,indices,linewidth=2, color=pcolor, label=plabel)
    

    N = len(lineData)
    x = np.sort(lineData)
    
    # get the cdf values of y
    y = np.arange(N) / float(N)

    plt.plot(x,y, linewidth=2, color=pcolor, label=plabel)

    
    # sns.kdeplot(data = lineData, cumulative = True, label = plabel)




# CDF = pd.DataFrame({'dummy':data})['dummy'].quantile(indices)

# plt.plot(CDF,indices,linewidth=3,  color='black', label='Total')



# plt.plot(xnew, power_smooth,linewidth=4, label='#interventions', color='blue')

plt.legend()
ax.tick_params(axis='both', which='major', labelsize=13)
ax.tick_params(axis='both', which='minor', labelsize=13)
ax.set_xscale('log')


plt.xticks([10, 20,40, 80, 150, 300, 700, 1300], ['10', '20','40', '80', '160', '320', '700', '1.3K'], rotation=30)

plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0', '20','40', '60', '80', '100'])

        #    rotation ='vertical')

plt.grid()

plt.ylabel('Percentage of vehicles', fontsize=14)
plt.xlabel('Average daily booking price in USD', fontsize=14)

plt.title('Booking Prices CDF of vehicles on PVRPS', fontsize=15)
ax.tick_params(axis='both', which='major', labelsize=12)

# plt.xlim(0,1500)


plt.ylim([0,1.01])
plt.xlim([15,1300])

plt.subplots_adjust(left=0.14,
                    bottom=0.15,
                    right=0.95,
                    top=0.92,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
fig.set_size_inches(5, 4.5)


scriptName = '33c'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 