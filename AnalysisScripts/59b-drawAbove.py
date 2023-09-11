import numpy as np
import matplotlib.pyplot as plt
import json
from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


fx = open('vpicsNumberToTrips.txt', 'r')
carcolorstrips = json.loads(fx.read())
fx.close()

carCats = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
possibleColors = carCats

x_pos = np.arange(len(possibleColors))
barData = []
errData = []

tbsData = []
for color in possibleColors:
    totalData = []
    for platform in carcolorstrips:
        for city in carcolorstrips[platform]:
            totalData += carcolorstrips[platform][city][color]['trips']
    if len(totalData) > 3:
        barData.append(np.average(totalData))
        errData.append(np.std(totalData)/5)
        tbsData.append([color, barData[-1], errData[-1]])

barData = []
possibleColors= []
errData = []

# tbsData = sorted(tbsData, key=lambda tup: tup[1], reverse=False)
# tbsData = tbsData[2:7]+ tbsData[-5:]
xlabels = []
# print(tbsData)

totalData = []
ind = 0
for item in tbsData:
    # if item[0] == '2.5':
    #     item[1] = item[1]*0.2
    # if item[0] == '3.5':
    #     item[1] = item[1]*0.4
    # if item[0] == '3.0':
    #     item[1] = item[1]*0.7
    # if item[0] == '4.0':
    #     item[1] = item[1]*0.8
    # if item[0] == '4.5':
    #     item[1] = item[1]*0.6
    # if item[0] == '2005':
    #     item[1] = item[1]*0.5
    # if item[0] == '2007':
    #     item[1] = item[1]*0.7
    # if item[0] == '2022':
    #     item[1] = item[1]*0.8
    
    # if item[0] > '2014' and item[0] < '2022':
    #     item[1] = item[1]*1.2
    barData.append(item[1])

    totalData.append(['pics '+str(item[0]), barData[-1]])
    if ind % 3 == 0:
        possibleColors.append(item[0])
        xlabels.append(ind)
    errData.append(item[2])
    ind += 1

x_pos = np.arange(len(barData))


# print(totalData[:300])


# Build the plot
fig, ax = plt.subplots()
from scipy.ndimage.filters import gaussian_filter1d
for i in range(0, len(barData)):
    barData[i] = barData[i]*1
barData = gaussian_filter1d(barData, sigma=1)

ax.bar(x_pos, barData, align='center', alpha=0.5, ecolor='black', capsize=10)
# ax.set_ylabel('Trips per month', fontsize=20)
ax.set_xticks(xlabels)
# ax.set_xticks(x_pos)
# possibleColors = [singer.capitalize() for singer in possibleColors]
# ax.set_yticklabels([0,0.3,0.6,0.9,1.2,1.5,1.8], fontsize=17, rotation=0)
ax.tick_params(axis='both', which='major', labelsize=17)
ax.set_xticklabels(possibleColors, fontsize=20, rotation=90)

fig.set_size_inches(6, 5)
# plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.13,
                    right=0.98,
                    top=0.98,
                    wspace=0.4,
                    hspace=0.4)


scriptName = '59b'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 



# fx = open('newOwnerDemographics.txt','w')
# fx.write(json.dumps(newOwnersDemographicsDict))
# fx.close()


# fx = open('cityWiseDemographics.txt','w')
# fx.write(json.dumps(ownersDict))
# fx.close()

