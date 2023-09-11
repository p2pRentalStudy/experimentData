from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

print(len(catDict.keys()))




dictKeys = list(catDict.keys())
dictKeys.sort()

for key in dictKeys:
    if len(catDict[key]['type']) == 0:
        del catDict[key]
studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
# cities = {'Barcelona', 'Berlin', 'Hamburg', 'Liverpool', 'London', 'Lyon', 'Madrid', 'Paris', 'Las Vegas', 'Los Angeles', 'Miami','New York City', 'Ottawa', 'Toronto','Washington D.C.' }
# targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData//13-output/'+platform+'/'



catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
notFound = {}
totalTypes = {}


cityAverage = {}
for city in cities:
    cityAverage[city] = {}
    for cat in catCats:
        cityAverage[city][cat] = []

totalModels = {}

moreThanOne = {}
totalVehicles = {}


ownerVehicles = {}
for city in cities:
    ownerVehicles[city] = {}
    for service in studiedApps.keys():
        ownerVehicles[city][service] = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1
possibleCats = ['sedan', 'SUV', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
priceDict = {}

catDict = {}
for cat in catCats:
    catDict[cat] = []
currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


citiesPriceAverage = {}
platformAverage = {}

for platform in studiedApps:
    platformAverage[platform] = []
for city in cities:
    citiesPriceAverage[city] = []

totalPriceCDF = []

fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()
triploadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'  

priceMulMap = {}

priceMulMap = {}
priceMulMap['GetAround'] = {}
priceMulMap['GetAround']['sedan']= 1.546
priceMulMap['GetAround']['suv']= 1.376
priceMulMap['GetAround']['hatchback']= 1.42
priceMulMap['GetAround']['wagon']= 1.41
priceMulMap['GetAround']['van/minivan']= 1.194
priceMulMap['GetAround']['coupe']= 1.76
priceMulMap['GetAround']['truck']= 1.17

priceMulMap['GerAroundEurope'] = {}
priceMulMap['GerAroundEurope']['sedan']= 3
priceMulMap['GerAroundEurope']['suv']= 2.76555
priceMulMap['GerAroundEurope']['hatchback']= 2.52
priceMulMap['GerAroundEurope']['wagon']= 1.45
priceMulMap['GerAroundEurope']['van/minivan']= 1.846
priceMulMap['GerAroundEurope']['coupe']= 1
priceMulMap['GerAroundEurope']['truck']= 1


priceMulMap['Turo'] = {}
priceMulMap['Turo']['sedan']= 2.36
priceMulMap['Turo']['suv']= 2.13
priceMulMap['Turo']['hatchback']= 2.511
priceMulMap['Turo']['wagon']= 2.516
priceMulMap['Turo']['van/minivan']= 1
priceMulMap['Turo']['coupe']= 1.944
priceMulMap['Turo']['truck']= 1.97

# priceMulCity[]
for platform in priceMulMap:
    for cat in priceMulMap[platform]:
        priceMulMap[platform][cat] *= 1.2

# for platform in ['GetAround']:
#     for cat in priceMulMap[platform]:
#         priceMulMap[platform][cat] *= 1.4

catDiv = {}
catDiv['sedan'] = 0.286
catDiv['suv'] = 0.323
catDiv['hatchback'] = 0.337
catDiv['wagon'] = 0.62
catDiv['van/minivan'] = 0.8
catDiv['coupe'] = 0.427
catDiv['truck'] = 0.371
from collections import Counter

fuelTypePriceDict = {}
fuelTypePriceDict['petrol'] = []
fuelTypePriceDict['diesel'] = []
fuelTypePriceDict['hybrid'] = []
fuelTypePriceDict['electric'] = []

fuelMapToDict = {}
fuelMapToDict['GASOLINE'] = 'diesel'
fuelMapToDict['HYBRID'] = 'hybrid'
fuelMapToDict['NA'] = 'petrol'
fuelMapToDict['ELECTRIC'] = 'electric'
fuelMapToDict['regular'] = 'petrol'
fuelMapToDict['premium'] = 'petrol'
fuelMapToDict['DIESEL'] = 'diesel'
fuelMapToDict['natural_gas'] = 'diesel'
fuelMapToDict['electric'] = 'electric'
fuelMapToDict['hydrogen'] = 'petrol'
fuelMapToDict['Unleaded 95'] = 'diesel'
fuelMapToDict['Diesel'] = 'diesel'
fuelMapToDict['Unleaded 98'] = 'petrol'
fuelMapToDict['Electric'] = 'electric'
fuelMapToDict['Other'] = 'hybrid'
fuelMapToDict['LPG'] = 'petrol'



targetFolder4 = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'

cityPlatformPrice = {}
cityAverage2 = {}
for city in cities:
    cityAverage2[city] = []
nextScriptD1 = {}
nextScriptD2 = []
platformCityVehiclePrices = {}
for platform in studiedApps:
    tempFolder4 = targetFolder4.replace('APPNAME',platform)
    # cityPlatformPrice[platform] 
    nextScriptD1[platform] = []
    listData = {}
    fx = open(triploadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()


    tempFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData//13b-output/'+platform+'/'

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0

    for fileName in filenames:
        cityName = fileName.split('-')[1].replace('.txt', '')
        print(platform, cityName)

        # time.sleep(100000)
        if cityName != 'New York':
            try:
                v10 = cityPlatformPrice[cityName]
                
            except:
                cityPlatformPrice[cityName] = {}
                platformCityVehiclePrices[cityName] = []

            cityPlatformPrice[cityName][platform] = []
            # for cat in possibleCats:
            #     cityPlatformPrice[cityName][cat] = []
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            vc = 0
            # dates4 = []
            print(len(content.keys()))
            vc = 0
            for vehicleId in analyzedData[platform][cityName]:
                vc += 1
                if vc % 1000 == 0:
                    print(vc, '/', len(content.keys()))
                vehicleId = platform+'~'+vehicleId
                bookingPrices = []
                try:
                    rdcount = 0
                    
                    for recocrdDate in content[vehicleId]:
                        testList = content[vehicleId][recocrdDate]
                        if 1:#len(testList) > 10:
                            pavrg = np.average(testList)

                            testList = [round(x/pavrg,1) for x in testList]

                            overUnder = len([1 for i in testList if i > 1.1])
                            overUnder += len([1 for i in testList if i < 0.9])

                            overUnder = round(overUnder/len(testList),2)
                            # print(vehicleId, recocrdDate, overUnder)
                            platformCityVehiclePrices[cityName].append(overUnder)                    
                    
                except Exception as e:
                    # print(e)
                    # time.sleep(1000)
                    pass
    #         break
    #     break
    # break

totalAverage = []
def most_common(lst):
    return max(set(lst), key=lst.count)

totalAverage = []
lenavrg = []
for city in platformCityVehiclePrices:
    totalAverage += platformCityVehiclePrices[city]
    print('\t', city, np.average(platformCityVehiclePrices[city]))
print(np.average(totalAverage))

