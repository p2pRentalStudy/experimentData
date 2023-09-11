from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
import numpy as np
import time


loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/vehicleTrips.txt'
fx = open(loadPath,'r')
tripsDict = json.loads(fx.read())
fx.close()

combinedDesc = ''

carCount = 0
breakLoop = 0

totalUtil = []
totalVehiclesPrice = {}
for platform in tripsDict:
    print(1,platform)
    totalVehiclesPrice[platform] = {}
    for city in tripsDict[platform]:
        totalUtil = []

        totalVehiclesPrice[platform][city] = []
        print('\t', city)
        for vehicleId in tripsDict[platform][city]:
            carCount += 1
            data = tripsDict[platform][city][vehicleId]
            # print(data)
            # time.sleep(1000)
            totalUtil.append(data[1]/(data[0]/30))
            totalVehiclesPrice[platform][city].append(totalUtil[-1])

        print(np.average(totalUtil))



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
platformColor = {}
platformColor['Turo'] = 'red'
platformColor['GetAround'] = 'green'
platformColor['GerAroundEurope'] = 'blue'

totalMeta = {'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}, 'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}}

totalDays = 1
maxChange = 0

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

priceDict = {}

import matplotlib.pyplot as plt
import numpy as np


species = list(cityShort.keys())
speciesShort = []
for i in range(len(species)):
    speciesShort.append(cityShort[ species[i]])
penguin_means = {
    'Turo': [0]*len(species),
    'GetAround': [0]*len(species),
    'GerAroundEurope': [0]*len(species),
}

for platform in platformColor:
    print(platform)
    for cityi in range(0,len(species)):
        city = species[cityi]
        try:
            penguin_means[platform][cityi] = np.average(totalVehiclesPrice[platform][city])
        except:
            pass

                

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0


x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    # ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, speciesShort)
ax.legend(loc='upper left', ncol=3)
# ax.set_ylim(0, 250)

plt.xticks(x, speciesShort, rotation='vertical')

plt.title('owner per city')
# plt.subplots_adjust(left=0.08,
#                     bottom=0.13,
#                     right=0.9,
#                     top=0.95,
#                     wspace=0.4,
#                     hspace=0.4)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '24a'
fig.savefig('plots/'+scriptName+'-perOwnerTrips.png') 
fig.savefig('plots/'+scriptName+'-perOwnerTrips.eps') 