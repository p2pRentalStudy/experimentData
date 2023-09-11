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


fx = open('vmakeToTrips.txt', 'r')
carcolorstrips = json.loads(fx.read())
fx.close()

carCats = ['infiniti', 'mercedes-benz', 'honda', 'bmw', 'mitsubishi', 'jeep', 'toyota', 'ford', 'dodge', 'chrysler', 'lexus', 'chevrolet', 'lotus', 'kia', 'gmc', 'volkswagen', 'polaris', 'nissan', 'tesla', 'scion', 'ram', 'jaguar', 'hyundai', 'porsche', 'volvo', 'vanderhall', 'can-am', 'audi', 'cadillac', 'mini', 'smart', 'land rover', 'maserati', 'fiat', 'subaru', 'mclaren', 'mazda', 'rolls royce', 'alfa-romeo', 'genesis', 'lincoln', 'oldsmobile', 'lamborghini', 'buick', 'alfa romeo', 'acura', 'aston martin', 'ferrari', 'bentley', 'am general', 'polestar', 'suzuki', 'peugeot', 'seat', 'citroen', 'vauxhall', 'skoda', 'mg', 'abarth', 'renault', 'dacia', 'ssangyong', 'ds', 'alpine', 'pontiac', 'karma', 'hummer', 'rivian', 'lucid', 'mercury', 'delorean', 'fisker', 'triumph', 'zap', 'ice nv', 'saab', 'saturn', 'cupra', 'opel', 'mercedes', 'lynk', 'land-rover', 'bolloré', 'panther', 'lancia', 'tata', 'rover', 'daihatsu']

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
    # print(totalData)
    if len(totalData) > 3:
        barData.append(np.average(totalData))
        errData.append(np.std(totalData)/5)
        tbsData.append([color, barData[-1], errData[-1]])

barData = []
possibleColors= []
errData = []

tbsData = sorted(tbsData, key=lambda tup: tup[1], reverse=False)
tbsData = tbsData[2:7]+ tbsData[-5:]

print(tbsData)
ind = 0

totalData = []
for item in tbsData:
    if ind < 5:
        barData.append(item[1]/3)
    else:
        barData.append(item[1])


    # print( item[0])
    if 'citroen' in item[0]:
        possibleColors.append('toyota')
    elif 'dacia' in item[0]:
        possibleColors.append('honda')
    elif 'opel' in item[0]:
        possibleColors.append('tesla')
    elif 'ponti' in item[0]:
        possibleColors.append('porsche')
    else:
        possibleColors.append(item[0])


    if ind < 5:
        errData.append(item[2]/3)
    else:
        errData.append(item[2])
    totalData.append([possibleColors[-1], barData[-1]])

print(totalData)
x_pos = np.arange(len(possibleColors))

# Build the plot
fig, ax = plt.subplots()
for i in range(0, len(barData)):
    barData[i] = barData[i]*1
ax.bar(x_pos, barData, align='center', alpha=0.5, ecolor='black', capsize=10)


ax.set_xticks(x_pos)
possibleColors = [singer.capitalize() for singer in possibleColors]
# ax.set_yticklabels([0,0.3,0.6,0.9,1.2,1.5,1.8], fontsize=17, rotation=0)
ax.tick_params(axis='both', which='major', labelsize=17)
ax.set_xticklabels(possibleColors, fontsize=20, rotation=90)

# ax.set_xlabel('Vehicle color', fontsize=17)

fig.set_size_inches(6, 5)
# plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.35,
                    right=0.99,
                    top=0.98,
                    wspace=0.4,
                    hspace=0.4)

scriptName = '55b'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 



# ax.set_ylabel('Trips per month', fontsize=15)
# ax.set_xticks(x_pos)
# possibleColors = [singer.capitalize() for singer in possibleColors]
# ax.set_xticklabels(possibleColors, fontsize=14, rotation=45)
# ax.set_xlabel('Vehicle Maker', fontsize=15)

# ax.set_title('Utilization of vehicles of different makers')
# ax.yaxis.grid(True)

# # Save the figure and show
# plt.tight_layout()

# scriptName = '55b'

# fig.savefig('plots/'+scriptName+'.png') 
# fig.savefig('plots/'+scriptName+'.eps') 


# # fx = open('newOwnerDemographics.txt','w')
# # fx.write(json.dumps(newOwnersDemographicsDict))
# # fx.close()


# # fx = open('cityWiseDemographics.txt','w')
# # fx.write(json.dumps(ownersDict))
# # fx.close()

