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
for platform in studiedApps:
    tempFolder4 = targetFolder4.replace('APPNAME',platform)
    # cityPlatformPrice[platform] 
    nextScriptD1[platform] = []
    listData = {}
    fx = open(triploadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()


    tempFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData//13-output/'+platform+'/'

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0

    for fileName in filenames:
        cityName = fileName.split('-')[1].replace('.txt', '')
        print(platform, cityName)

        fx = open(tempFolder4+cityName+'-content.txt','r')
        carDetailsDict = json.loads(fx.read())
        fx.close()
        # time.sleep(100000)
        if cityName != 'New York':
            try:
                v10 = cityPlatformPrice[cityName]
            except:
                cityPlatformPrice[cityName] = {}

            cityPlatformPrice[cityName][platform] = []
            # for cat in possibleCats:
            #     cityPlatformPrice[cityName][cat] = []
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            vc = 0
            # dates4 = []
            for vehicleId in analyzedData[platform][cityName]:
                car = carDetailsDict[vehicleId]
                # if len(dates4) == 0:
                dates4 = list(carDetailsDict[vehicleId].keys())
                dates4.sort()
                fuelType = car[dates4[0]]['fuelType']
                # try:
                #     v10 = fuelTypePriceDict[fuelType]
                # except:
                    # fuelTypePriceDict[fuelMapToDict[fuelType]]= []
                
                vc += 1
                # if vc > 50:
                #     break
                # print(vehicleId, list(content.keys())[:10])
                vehicleId = platform+'~'+vehicleId
                bookingPrices = []
                # print(vehicleId)
                # if 1:
                try:
                    rdcount = 0
                    for recocrdDate in content[vehicleId]:
                        for dayDifference in content[vehicleId][recocrdDate]:
                            bookingPrice = float(content[vehicleId][recocrdDate][dayDifference])
                            
                            if rdcount % 50 == 0:
                                fuelTypePriceDict[fuelMapToDict[fuelType]].append(bookingPrice)
                            rdcount +=1 
                            cat = 'sedan'
                            tid = vehicleId.replace(platform+'~','')
                            # print(cityServiceCat[platform][cityName].keys())
                            # cat = cityServiceCat[platform][cityName][tid][0]
                            try:
                                cat = cityServiceCat[platform][cityName][tid][0]
                            except:
                                ijk = 10
                           
                            # divFactor = 2
                            # bookingPrice = round(bookingPrice*priceMulMap[platform][cat]*catDiv[cat],1)
                            # if bookingPrice < 20:
                            #     bookingPrice = random.uniform(20,60)

                            # if 'Ger' in platform:
                            #     bookingPrice *= 1.4
                            # elif 'GetA' in platform:
                            #     bookingPrice *= 1.95
                            
                            bookingPrices.append(int(bookingPrice))

                            totalPriceCDF.append(bookingPrice)
                            
                            platformAverage[platform].append(bookingPrice)

                            catDict[cat].append(bookingPrice)
                            cityAverage[cityName][cat].append(bookingPrice)
                            cityAverage2[cityName].append(bookingPrice)

                            cityPlatformPrice[cityName][platform].append(bookingPrice)


                    dummyList = []
                    tlen = len(bookingPrices)
                    bookingPrices = Counter(bookingPrices)
                    for x in bookingPrices.keys():
                        reps = int((bookingPrices[x]/tlen)*1000)
                        dummyList += [int(x)]*reps

                    nextScriptD2 += dummyList
                    nextScriptD1[platform] += dummyList
                    # nextScriptD2.append(np.average(bookingPrices))
                    # nextScriptD1[platform].append(np.average(bookingPrices))
     
                        

     
                    #priceMulMap[platform][cat],2)
                    # temp1 =[round(np.average(bookingPrices),1)]*100
                    # minv = [round(min(bookingPrices),1)]*2
                    # maxv = [round(max(bookingPrices),1)]*2
                    # totalPriceCDF+=temp1
                    # totalPriceCDF+=minv
                    # totalPriceCDF+=maxv

                    # platformAverage[platform]+=temp1
                    # platformAverage[platform]+=minv
                    # platformAverage[platform]+=maxv

                    # catDict[cat]+=temp1
                    # catDict[cat]+=minv
                    # catDict[cat]+=maxv


                    # cityAverage[cityName][cat]+=temp1
                    # cityAverage[cityName][cat]+=minv
                    # cityAverage[cityName][cat]+=maxv

                        
                except Exception as e:
                    # print(e)
                    # time.sleep(1000)
                    pass

print('\n\n', np.average(totalPriceCDF), '\n\n')

for platform in studiedApps:
    print(platform, np.average(platformAverage[platform]))
print('\n\n\n')

citiesAvrg = []

for cat in catCats:
    print(cat, np.average(catDict[cat]))
print('\n\n')

for cityName in cities:
    print(cityName)
    for cat in cityAverage[cityName]:
        print('\t',cat, np.average(cityAverage[cityName][cat]))

#     citiesAvrg.append(np.average(cityAverage[cityName]))
# print(np.average(citiesAvrg))


avrg = []
for city in cityAverage2:
    print(city, np.average(cityAverage2[city]))
    avrg.append(np.average(cityAverage2[city]))
print(np.average(avrg))


for city in cityPlatformPrice:
    print(city)
    t = 1
    other = 0
    for p1 in cityPlatformPrice[city]:
        print('\t', p1, np.average(cityPlatformPrice[city][p1]))
        if p1 == 'Turo':
            t = np.average(cityPlatformPrice[city][p1])
        else:
            o = np.average(cityPlatformPrice[city][p1])
    print('\t', t/o)






for fuelType in fuelTypePriceDict:
    print(fuelType, np.average(fuelTypePriceDict[fuelType]))
myData = {}

myData['totalPrices'] = totalPriceCDF
fx = open('totalPrices.txt','w')
fx.write(json.dumps(myData))
fx.close()


fx = open('platformPrices.txt','w')
fx.write(json.dumps(platformAverage))
fx.close()



myData = {}
myData['totalPrices'] = nextScriptD2
fx = open('totalPrices2.txt','w')
fx.write(json.dumps(myData))
fx.close()


fx = open('platformPrices2.txt','w')
fx.write(json.dumps(nextScriptD1))
fx.close()


fx = open('cityPlatformPrice.txt','w')
fx.write(json.dumps(cityPlatformPrice))
fx.close()



# for cat in catDict:
#     print(cat, np.average(catDict))
