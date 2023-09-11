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

studiedApps = {}
# studiedApps['Turo'] = 1
# studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1

for platform in studiedApps:
    platFormCatTrip[platform] = {}
    for cat in carCats:
        platFormCatTrip[platform][cat] = {}
        platFormCatTrip[platform][cat]['pre'] = 0
        platFormCatTrip[platform][cat]['post'] = 0
        platFormCatTrip[platform][cat]['perVehicle'] =  0
        platFormCatTrip[platform][cat]['perMonthTrips'] = [0]
        platFormCatTrip[platform][cat]['tripLengths'] = [0]
        platFormCatTrip[platform][cat]['tripPrices'] = [0]

    fx = open(loadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()


    catVehicleDict = {}
    for cat in carCats:
        catVehicleDict[cat] = {}
        catVehicleDict[cat]['cars'] = {}
        catVehicleDict[cat]['trips'] = 0
        # catVehicleDict[cat]['tripLengths'] = 0
    for cityName in analyzedData[platform]:
        if cityName != 'New York':
            fx = open(loadPath +platform+'-'+cityName+'-tripDetails.txt','r')
            tripDetailsDict = json.loads(fx.read())
            fx.close()
            for carId in analyzedData[platform][cityName]:
                vc += 1
                totalTrips += analyzedData[platform][cityName][carId]['trips'][1]
                cat = 'sedan'

                try:
                    cat = cityServiceCat[platform][cityName][carId][0]
                except:
                    pass

                experimentTripsVehicle = 0 
                experimentTripsVehicle = analyzedData[platform][cityName][carId]['trips'][1]-analyzedData[platform][cityName][carId]['trips'][0]

                
                platFormCatTrip[platform][cat]['pre']+= analyzedData[platform][cityName][carId]['trips'][0]
                platFormCatTrip[platform][cat]['post']+= experimentTripsVehicle
                
                
                catVehicleDict[cat]['cars'][cityName+carId] = 1
                catVehicleDict[cat]['trips'] += experimentTripsVehicle


                platFormCatTrip[platform][cat]['perMonthTrips'].append(experimentTripsVehicle/analyzedData[platform][cityName][carId]['dates'][2])


                for tripObj in tripDetailsDict[platform][cityName][carId]:
                    # print
                    platFormCatTrip[platform][cat]['tripLengths'].append(lengthMulMap[platform][cat]*tripObj['length'])
                    platFormCatTrip[platform][cat]['tripPrices'].append(priceMulMap[platform][cat]*tripObj['price'])

    for cat in carCats:
        platFormCatTrip[platform][cat]['perVehicle'] =  round(catVehicleDict[cat]['trips']/max(1,len(catVehicleDict[cat]['cars'].keys())),1)
# print(vc, totalTrips)





pre = 0
post = 0
# for cat in carCats:
#     print(cat)
#     for platform in studiedApps:
#         print('\t', platform, platFormCatTrip[platform][cat]['pre'], '&', platFormCatTrip[platform][cat]['post'])

#         pre += platFormCatTrip[platform][cat]['pre']
#         post += platFormCatTrip[platform][cat]['post']
    
# print(pre, post)



# avrg = []
# for cat in carCats:
#     print(cat)
#     for platform in studiedApps:
#         print('\t', platform, platFormCatTrip[platform][cat]['perVehicle'])
#         avrg.append(platFormCatTrip[platform][cat]['perVehicle'])
# print('trip per vehicle', np.average(avrg))


# avrg = []
# for cat in carCats:
#     print(cat)
#     for platform in studiedApps:
#         print('\t', platform, round(np.average(platFormCatTrip[platform][cat]['perMonthTrips'])*30,1))

#         avrg+= platFormCatTrip[platform][cat]['perMonthTrips']
# print('per month trips', np.average(avrg)*30)



# avrg = []
# for cat in carCats:
#     print(cat)
#     for platform in studiedApps:
#         print('\t', platform, round(np.average(platFormCatTrip[platform][cat]['tripLengths']),1))
#         avrg += platFormCatTrip[platform][cat]['tripLengths']
# print('length average', np.average(avrg))


avrg = []
for cat in carCats:
    print(cat)
    for platform in studiedApps:
        print('\t', platform, round(np.average(platFormCatTrip[platform][cat]['tripPrices']),1))
        avrg+=platFormCatTrip[platform][cat]['tripPrices']
print('price average', np.average(avrg))

# print(vc)