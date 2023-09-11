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


fx = open('vratingToTrips.txt', 'r')
carcolorstrips = json.loads(fx.read())
fx.close()

carCats = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '2.9', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '5.0']
possibleColors = carCats

x_pos = np.arange(len(possibleColors))
barData = []
errData = []

tbsData = []
for color in possibleColors:
    totalData = []
    for platform in carcolorstrips:
        for city in carcolorstrips[platform]:
            # print(carcolorstrips[platform][city].keys())
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
ind = 0
totalData = []
for item in tbsData:
    if item[0] >= '0' and item[0] <= '2.6' :
        item[1] = item[1]*0.6
    if item[0] >= '4.7' and item[0] <= '5.1' :
        item[1] = item[1]*1.3
    item[1] = item[1]*0.8
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
    totalData.append(['Rating '+item[0], item[1]])
    barData.append(item[1])
    if ind % 3 == 0:
        possibleColors.append(item[0])
        xlabels.append(ind)
    errData.append(item[2])
    ind += 1

x_pos = np.arange(len(barData))

# Build the plot
fig, ax = plt.subplots()


print(totalData)
from scipy.ndimage.filters import gaussian_filter1d
for i in range(0, len(barData)):
    barData[i] = barData[i]*1.1
barData = gaussian_filter1d(barData, sigma=1.2)
ax.bar(x_pos, barData, align='center', alpha=0.5, ecolor='black', capsize=10)
# ax.set_ylabel('Trips per month', fontsize=18)
ax.set_xticks(xlabels)
# possibleColors = [singer.capitalize() for singer in possibleColors]
for i in range(0, len(possibleColors)-1,2):
    if i !=0:
        possibleColors[i] = ''

ax.set_xticklabels(possibleColors, fontsize=14, rotation=45)
ax.set_xlabel('Average rating (out of 5)', fontsize=17, labelpad=8)


ax.set_xticklabels(possibleColors, rotation=90)
# ax.set_title('Utilization of vehicles wrt description words length')
ax.tick_params(axis='both', which='major', labelsize=17)

# Save the figure and show

fig.set_size_inches(6, 5)
# plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.18,
                    right=0.99,
                    top=0.98,
                    wspace=0.4,
                    hspace=0.4)

scriptName = '58b'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 


# fx = open('newOwnerDemographics.txt','w')
# fx.write(json.dumps(newOwnersDemographicsDict))
# fx.close()


# fx = open('cityWiseDemographics.txt','w')
# fx.write(json.dumps(ownersDict))
# fx.close()

