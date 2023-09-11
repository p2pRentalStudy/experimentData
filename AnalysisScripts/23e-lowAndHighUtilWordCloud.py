from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
import numpy as np
import time


loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/vehicleDesctiption.txt'
fx = open(loadPath,'r')
vehicleDescription = json.loads(fx.read())
fx.close()

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/vehicleTrips.txt'
fx = open(loadPath,'r')
tripsDict = json.loads(fx.read())
fx.close()

combinedDesc = ''

carCount = 0
breakLoop = 0

totalUtil = []
for platform in tripsDict:
    print(1,platform)
    for city in tripsDict[platform]:
        print('\t', city)
        for vehicleId in tripsDict[platform][city]:
            carCount += 1
            data = tripsDict[platform][city][vehicleId]
            # print(data)
            # time.sleep(1000)
            totalUtil.append(data[1]/(data[0]/7))

print(np.average(totalUtil))
totalUtil = np.average(totalUtil)
lowAverageDesc = ''
highAverageDesc = ''
lowDict = {}
highDict = {}

descList = ['', '']

delta = 0.7
for platform in tripsDict:
    print(2, platform)
    for city in tripsDict[platform]:
        # print('\t', city)
        for vehicleId in tripsDict[platform][city]:
            data = tripsDict[platform][city][vehicleId]
            if data[1]/(data[0]/7) < delta * totalUtil:
                lowDict[vehicleId] = 1
            elif data[1]/(data[0]/7) >= (1+(1-delta)) * totalUtil:
                highDict[vehicleId] = 1

print('low', len(lowDict.keys())/carCount, 'high', len(highDict.keys())/carCount)
for platform in vehicleDescription:
    print(3, platform)
    for city in vehicleDescription[platform]:
        print('\t', city)
        for vehicleId in vehicleDescription[platform][city]:
            index = -1
            try:
                val = highDict[vehicleId]
                index = 1
            except:
                try:
                    val = lowDict[vehicleId]
                    index = 0
                except:
                    ijk = 10
            if index != -1:
                carCount += 1
                # if carCount > 1000:
                #     ijk = 10
                #     breakLoop = 1
                #     break
                vehicleDescription[platform][city][vehicleId] = vehicleDescription[platform][city][vehicleId].lower()
                for word in ['Las Vegas', 'will', 'vehicle', 'car', 'come', 's ', 'need', 'drive', 'make', 'this', ' . ', 'trip', 'rent']:
                    vehicleDescription[platform][city][vehicleId] = vehicleDescription[platform][city][vehicleId].replace(word, '')

                descList[index] += ' '+vehicleDescription[platform][city][vehicleId]
        if breakLoop:
            break
    if breakLoop:
        break

# Create the wordcloud object
wordcloud = WordCloud(width=750, height=480, margin=0, background_color="white").generate(descList[0])

# print(wordcloud)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '23e'
fig.savefig('plots/'+scriptName+'-low.png') 
fig.savefig('plots/'+scriptName+'-low.eps') 



# Create the wordcloud object
wordcloud = WordCloud(width=750, height=480, margin=0, background_color="white").generate(descList[1])

# print(wordcloud)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '23e'
fig.savefig('plots/'+scriptName+'-high.png') 
fig.savefig('plots/'+scriptName+'-high.eps') 

