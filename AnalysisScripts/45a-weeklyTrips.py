from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'  


carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'suv']

studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1



analyzedData = {}

vc = 0
totalTrips = 0


currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


cityCurrencyMap = {}
cityCurrencyMap['Las Vegas'] = 1
cityCurrencyMap['Los Angeles'] =1 
cityCurrencyMap['Miami'] = 1
cityCurrencyMap['New York City'] =1 
cityCurrencyMap['Washington D.C.'] =1 
cityCurrencyMap['Toronto'] = 0.73
cityCurrencyMap['Ottawa'] = 0.73
cityCurrencyMap['Barcelona'] = 1.06
cityCurrencyMap['Berlin'] = 1.06
cityCurrencyMap['Hamburg'] = 1.06
cityCurrencyMap['Liverpool'] = 1.21
cityCurrencyMap['London'] = 1.21
cityCurrencyMap['Lyon'] = 1.06
cityCurrencyMap['Madrid'] = 1.06
cityCurrencyMap['Paris'] = 1.06




studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1

lengthMulMap = {}
lengthMulMap['GerAroundEurope'] = 0.7
lengthMulMap['GetAround'] = 0.8
lengthMulMap['Turo'] = 1.1

priceMulMap = {}
priceMulMap['GerAroundEurope'] = 0.8
priceMulMap['GetAround'] = 0.7
priceMulMap['Turo'] = 1.1

platFormCatTrip = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1

cityDict = {}
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for city in cityCurrencyMap.keys():
    cityDict[city] = {}
    for day in daysOfWeek:
        cityDict[city][day] = []
    cityDict[city]['totalTrips'] = 0


dateToDayDict = {}
for platform in studiedApps:
    # print(platform)
    platFormCatTrip[platform] = {}
    fx = open(loadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()
    catVehicleDict = {}
    for cityName in analyzedData[platform]:
        if cityName != 'New York':
            # print('\t',cityName)
            fx = open(loadPath +platform+'-'+cityName+'-tripDetails.txt','r')
            tripDetailsDict = json.loads(fx.read())
            fx.close()
            for carId in analyzedData[platform][cityName]:
                vc += 1
                cat = 'sedan'
                try:
                    cat = cityServiceCat[platform][cityName][carId][0]
                except:
                    pass

                totalTrips += analyzedData[platform][cityName][carId]['trips'][1]
                for tripObj in tripDetailsDict[platform][cityName][carId]:
                    
                    tripDate = tripObj['StartDate']
                    try:
                        tripDay = dateToDayDict[tripDate]
                    except:
                        tripDay = pd.Timestamp(tripDate)
                        tripDay = tripDay.day_name()
                        dateToDayDict[tripDate] = tripDay
                    
                    cityDict[cityName]['totalTrips'] += 1
                    tripObj['length'] *= lengthMulMap[platform]
                    tripObj['price'] *= priceMulMap[platform]
                    tripObj['carId'] = carId
                    tripObj['carCat'] = cat
                    tripObj['platform'] = platform
                    cityDict[cityName][tripDay].append(tripObj)
                    # print(tripObj['StartDate'], tripDay)
                    # time.sleep(1000)





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
newHeatMapData = []

cities = list(cityShort.keys())
cities.sort()

ylabels = []
shortDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
newDict = {}
totalVals = []
for i in range(0,len(cities)):
    cityData = []
    newDict[cities[i]] = {}
    for j in range(0, len(daysOfWeek)):
        tba = int((len(cityDict[cities[i]][daysOfWeek[j]])/cityDict[cities[i]]['totalTrips'])*100)
        cityData.append(tba)
        totalVals.append(tba)

        newDict[cities[i]][daysOfWeek[j]] = tba

    
    newHeatMapData.append(cityData)
    ylabels.append(cityShort[cities[i]])
        



from scipy import stats

step=0.05
indices = np.arange(0,1+step,step)
fig, ax = plt.subplots()
fig.set_size_inches(1.4*3, 1.25*3)



from scipy import interpolate

df = pd.DataFrame(newHeatMapData, columns=list(shortDays))

sns.heatmap(df, cbar=False, annot=True, annot_kws={"size": 12}, yticklabels= ylabels, vmin=8, vmax=25)#, linewidths=2,)



plt.ylabel('Cities', fontsize=12)
plt.xlabel('Days of the week', fontsize=12)

plt.title('Heatmap of Trips% across days of week', fontsize=14)

# plt.xticks([0,3,6,9,12,15,18,21,24,27,30], [0,3,6,9,12,15,18,21,24,27,30])


# plt.xlim(0,1500)


plt.subplots_adjust(left=0.17,
                    bottom=0.14,
                    right=0.89,
                    top=0.93,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
# fig.set_size_inches(6, 5.5)


scriptName = '45a'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 

# print(newDict)
from scipy.stats.stats import pearsonr   

for cat in carCats:
    catVals = []
    ylabels = []
    shortDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    newDict = {}
    newHeatMapData = []
    for i in range(0,len(cities)):
        cityData = []
        newDict[cities[i]] = {}
        city = cityName = cities[i]
        totalTrips = 1
        for j in range(0, len(daysOfWeek)):
            
            for item in cityDict[cities[i]][daysOfWeek[j]]:
                if item['carCat'] == cat:
                    totalTrips += 1
        totalTrips = max(1, totalTrips)
        for j in range(0, len(daysOfWeek)):
            rightTrips = []
            for item in cityDict[cities[i]][daysOfWeek[j]]:
                if item['carCat'] == cat:
                    rightTrips.append(item)
            # print(cat, cityName,  len(rightTrips), totalTrips)
            tba = int((len(rightTrips)/totalTrips)*100)
            catVals.append(tba)
            cityData.append(tba)

            newDict[cities[i]][daysOfWeek[j]] = tba

        
        newHeatMapData.append(cityData)
        ylabels.append(cityShort[cities[i]])
            



    from scipy import stats
    plt.clf()
    step=0.05
    indices = np.arange(0,1+step,step)
    fig, ax = plt.subplots()



    from scipy import interpolate

    df = pd.DataFrame(newHeatMapData, columns=list(shortDays))

    sns.heatmap(df, annot=True, annot_kws={"size": 7}, yticklabels= ylabels, vmin=8, vmax=25)#, linewidths=2,)



    plt.ylabel('Cities', fontsize=12)
    plt.xlabel('Days of the week', fontsize=12)

    plt.title('Heatmap of '+cat+' Trips Percentages across days of the week', fontsize=14)

    # plt.xticks([0,3,6,9,12,15,18,21,24,27,30], [0,3,6,9,12,15,18,21,24,27,30])


    # plt.xlim(0,1500)


    plt.subplots_adjust(left=0.15,
                        bottom=0.16,
                        right=1.03,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)

    fig = plt.gcf()
    fig.set_size_inches(6.1, 5.4)


    scriptName = '45a-cat'
    cat = cat.replace('/','-')
    fig.savefig('plots/'+scriptName+'-'+cat+'.png') 
    fig.savefig('plots/'+scriptName+'-'+cat+'.eps') 
    plt.clf()
    # print(cat)
    print(cat, pearsonr(totalVals,catVals)[0])
    # time.sleep(1000)