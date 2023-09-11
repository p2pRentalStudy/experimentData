from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/vehicleDesctiption.txt'
fx = open(loadPath,'r')
vehicleDescription = json.loads(fx.read())
fx.close()

combinedDesc = ''

carCount = 0
breakLoop = 0
for platform in vehicleDescription:#['GetAround']:
    print(platform)
    for city in vehicleDescription[platform]:
        print('\t', city)
        for vehicleId in vehicleDescription[platform][city]:
            carCount += 1
            if carCount == 1000:
                ijk = 10
                # breakLoop = 1
                # break
            vehicleDescription[platform][city][vehicleId] = vehicleDescription[platform][city][vehicleId].lower()
            for word in ['Las Vegas', 'will', 'vehicle', 'car', 'come', 's ', 'need', 'drive', 'make', 'this', ' . ', 'trip', 'rent']:
                vehicleDescription[platform][city][vehicleId] = vehicleDescription[platform][city][vehicleId].replace(word, '')

            combinedDesc += ' '+vehicleDescription[platform][city][vehicleId]
        if breakLoop:
            break
    if breakLoop:
        break

# Create a list of word
text=(combinedDesc)


# Create the wordcloud object
wordcloud = WordCloud(width=750, height=480, margin=0, background_color="white").generate(text)

# print(wordcloud)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
fig = plt.gcf()
fig.set_size_inches(6, 4)

scriptName = '23d'
fig.savefig('plots/'+scriptName+'-pricepertrip.png') 
fig.savefig('plots/'+scriptName+'-pricepertrip.eps') 

