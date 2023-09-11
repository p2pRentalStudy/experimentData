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


fx = open('vcatsToTrips.txt', 'r')
carcolorstrips = json.loads(fx.read())
fx.close()

carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'suv']


possibleColors = carCats

x_pos = np.arange(len(possibleColors))
barData = []
errData = []
barData = []
errData = []
ciut = {}
for platform in carcolorstrips:
    for city in carcolorstrips[platform]:
        ciut[city] = {}
possibleColors = carCats
cut = {}
for color in possibleColors:
    cut[color] = []
    totalData = []
    
    for platform in carcolorstrips:
        for city in carcolorstrips[platform]:
            try:
                v10 = ciut[city][color]
            except:
                ciut[city][color] = []
            totalData += carcolorstrips[platform][city][color]['trips']
            ciut[city][color] += carcolorstrips[platform][city][color]['trips']
    barData.append(np.average(totalData))
    cut[color] = barData[-1]
    errData.append(np.std(totalData)/5)

for city in ciut:
    for color in possibleColors:
        ciut[city][color] = round(np.average(ciut[city][color] ),2)
print(cut)

print(ciut)
# Build the plot
fig, ax = plt.subplots()
for i in range(0, len(barData)):
    barData[i] = barData[i]*1
ax.bar(x_pos, barData, align='center', alpha=0.5, ecolor='black', capsize=10)



ax.set_xticks(x_pos)
possibleColors = [singer.capitalize() for singer in possibleColors]
possibleColors[2] = 'HB'
possibleColors[4] = 'V/M'

ax.set_xticklabels(possibleColors, fontsize=18, rotation=45)
ax.set_yticklabels([0,.5,1,1.5,2,2.5, 3], fontsize=17, rotation=0)

# ax.set_xlabel('Vehicle color', fontsize=17)
ax.tick_params(axis='both', which='major', labelsize=17)
ax.set_xticklabels(possibleColors, fontsize=20, rotation=90)

fig.set_size_inches(6, 5)
# plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.21,
                    right=0.99,
                    top=0.98,
                    wspace=0.4,
                    hspace=0.4)

scriptName = '54b'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 


# fx = open('newOwnerDemographics.txt','w')
# fx.write(json.dumps(newOwnersDemographicsDict))
# fx.close()


# fx = open('cityWiseDemographics.txt','w')
# fx.write(json.dumps(ownersDict))
# fx.close()


# fx.write(json.dumps(newOwnersDemographicsDict))
# fx.close()


# fx = open('cityWiseDemographics.txt','w')
# fx.write(json.dumps(ownersDict))
# fx.close()

