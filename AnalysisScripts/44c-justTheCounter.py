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
                # obj = tripDetailsDict[platform][cityName][carId]
                vc += 1


print(vc)