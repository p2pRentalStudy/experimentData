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
lengthMulMap['GerAroundEurope'] = {}
lengthMulMap['GerAroundEurope']['sedan']= 7.17
lengthMulMap['GerAroundEurope']['suv']= 6.98
lengthMulMap['GerAroundEurope']['hatchback']= 6.78
lengthMulMap['GerAroundEurope']['wagon']= 4.8
lengthMulMap['GerAroundEurope']['van/minivan']= 5.5
lengthMulMap['GerAroundEurope']['coupe']= 3
lengthMulMap['GerAroundEurope']['truck']= 1

lengthMulMap['GetAround'] = {}
lengthMulMap['GetAround']['sedan']= 2.891
lengthMulMap['GetAround']['suv']= 2.72
lengthMulMap['GetAround']['hatchback']= 2.72
lengthMulMap['GetAround']['wagon']= 2.14
lengthMulMap['GetAround']['van/minivan']= 2.491
lengthMulMap['GetAround']['coupe']= 1.92
lengthMulMap['GetAround']['truck']= 3.3


lengthMulMap['Turo'] = {}
lengthMulMap['Turo']['sedan']= 7.973
lengthMulMap['Turo']['suv']= 7.22
lengthMulMap['Turo']['hatchback']= 8.21
lengthMulMap['Turo']['wagon']= 8.05
lengthMulMap['Turo']['van/minivan']= 6.87
lengthMulMap['Turo']['coupe']= 5.121
lengthMulMap['Turo']['truck']= 6.661



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
for platform in priceMulMap:
    for cat in priceMulMap[platform]:
        priceMulMap[platform][cat] *= 1.2


platFormCatTrip = {}


cityDict = {}
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

makersTypes = []

for i in range(20, 1500):
    makersTypes.append(str(i))



# 
possibleColors = makersTypes

colorVehicleTripsDict = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1

pricingDict = {}
# for platform in studiedApps:
#     tempFolder2 = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13-output/'+platform+'/'
#     fx = open(loadPath +platform+'-trips.txt', 'r')
#     analyzedData = json.loads(fx.read())
#     fx.close()
#     print(platform)
#     for cityName in analyzedData[platform]:
#         if cityName != 'New York':
#             print('\t', cityName)
#             fx = open(tempFolder2+platform+'-'+cityName+'.txt','r')
#             pricingDictTemp = json.loads(fx.read())
#             fx.close()
#             for carId in  pricingDictTemp:
#                 carAvg = []
#                 for d1 in pricingDictTemp[carId]:
#                     for d2 in pricingDictTemp[carId][d1]:
#                         carAvg.append(pricingDictTemp[carId][d1][d2])
#                 carAvg = np.average(carAvg)
#                 pricingDict[platform+cityName+carId] = round(carAvg,2)
#                 # print(pricingDict)
#                 # time.sleep(1000)

# fx = open('carPricesDict2.txt', 'w')
# fx.write(json.dumps(pricingDict))
# fx.close()


# print('created new pricing dict')
# time.sleep(10000)

fx = open('carPricesDict2.txt', 'r')
priceDict = json.loads(fx.read())
fx.close()

# xa = 30000
# print(len(list(priceDict.keys())))

# print(list(priceDict.keys())[xa:xa+10])
# time.sleep(1000)
sc = 0
for platform in studiedApps:
    colorVehicleTripsDict[platform] = {}
    # print(platform)
    platFormCatTrip[platform] = {}
    fx = open(loadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()
    catVehicleDict = {}
    v1 = []
    v2 = []
    for cityName in analyzedData[platform]:
        if cityName != 'New York':
            city = cityName
            colorVehicleTripsDict[platform][cityName] = {}
            for color in possibleColors:
                colorVehicleTripsDict[platform][cityName][color] = {}
                # colorVehicleTripsDict[platform][cityName][color]['vehicleIDs'] = []
                colorVehicleTripsDict[platform][cityName][color]['trips'] = [0]
            # print('\t',cityName)
            
            
            for carId in analyzedData[platform][cityName]:

                vc += 1
                cat = 'sedan'
                make = 'ford'
                try:
                    cat = cityServiceCat[platform][cityName][carId][0]
                    catObj = cityServiceCat[platform][cityName][carId]
                    make = catObj[1].split('~')[1]
                except:
                    pass
                
                carDays = analyzedData[platform][cityName][carId]['dates'][2]
                experimentTripsVehicle = analyzedData[platform][cityName][carId]['trips'][1]-analyzedData[platform][cityName][carId]['trips'][0]

                carColor = 'white' 

                

                
                if experimentTripsVehicle > -1:
                    try:
                    # if 1:
                        newCarid = platform+cityName+platform+'~'+carId
                        pvarg = int(priceDict[newCarid])
                        # print(platform+cityName+carId, pvarg)
                        # time.sleep(1000)
                        # # time.sleep(1000)
                        sc+=1
                        experimentTripsVehicle = (experimentTripsVehicle/carDays)*30
                        colorVehicleTripsDict[platform][cityName][str(pvarg)]['trips'].append(round(experimentTripsVehicle,2))
                    except:
                        pass
                    

print(sc)
# print(colorVehicleTripsDict)
fx = open('vpriceToTrips.txt','w')
fx.write(json.dumps(colorVehicleTripsDict))
fx.close()

print(makersTypes)