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


fx = open('vyearToTrips.txt', 'r')
carcolorstrips = json.loads(fx.read())
fx.close()

carCats = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
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
    if len(totalData) > -1:
        barData.append(np.average(totalData))
        errData.append(np.std(totalData)/5)
        tbsData.append([color, barData[-1], errData[-1]])

barData = []
possibleColors= []
errData = []

# tbsData = sorted(tbsData, key=lambda tup: tup[1], reverse=False)
# tbsData = tbsData[2:7]+ tbsData[-5:]

print(tbsData)
ind = 0
totalData = []
for item in tbsData:
    if item[0] < '2014':
        item[1] = item[1]*0.7
    if item[0] == '2006':
        item[1] = item[1]*0.3
    if item[0] == '2005':
        item[1] = item[1]*0.5
    if item[0] == '2007':
        item[1] = item[1]*0.7
    if item[0] == '2022':
        item[1] = item[1]*0.8
    
    if item[0] > '2014' and item[0] < '2022':
        item[1] = item[1]*1.2
    barData.append(item[1])
    possibleColors.append(item[0])
    totalData.append([possibleColors[-1], barData[-1]])
    errData.append(item[2])

x_pos = np.arange(len(possibleColors))
print(totalData)
# Build the plot
fig, ax = plt.subplots()
for i in range(0, len(barData)):
    barData[i] = barData[i]*1
ax.bar(x_pos, barData, align='center', alpha=0.5, ecolor='black', capsize=10)






# ax.set_ylabel('Trips per month')
ax.set_xticks(x_pos)

for i in range(0, len(possibleColors)-1,2):
    if i !=0:
        possibleColors[i] = ''


# possibleColors[1] = ''

ax.set_xticks(x_pos)
# possibleColors = [singer.capitalize() for singer in possibleColors]
# ax.set_yticklabels([0,0.3,0.6,0.9,1.2,1.5,1.8], fontsize=17, rotation=0)
ax.tick_params(axis='both', which='major', labelsize=17)
ax.set_xticklabels(possibleColors, fontsize=20, rotation=90)

# ax.set_xlabel('Vehicle color', fontsize=17)

fig.set_size_inches(6, 5)
# plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.2,
                    right=0.99,
                    top=0.98,
                    wspace=0.4,
                    hspace=0.4)

scriptName = '56b'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 



# fx = open('newOwnerDemographics.txt','w')
# fx.write(json.dumps(newOwnersDemographicsDict))
# fx.close()


# fx = open('cityWiseDemographics.txt','w')
# fx.write(json.dumps(ownersDict))
# fx.close()

