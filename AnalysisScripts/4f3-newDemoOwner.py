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


fx = open('finalCarColors.txt', 'r')
carColors = json.loads(fx.read())
fx.close()

lp2 = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/'    

fx = open(lp2+'translatedDescription.txt', 'r')
translatedDescription = json.loads(fx.read())
fx.close()


targetFolder2 = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/'


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

makersTypes = {}

for platform in cityServiceCat:
    for city in cityServiceCat[platform]:
        for carID in cityServiceCat[platform][city]:
            catObj = cityServiceCat[platform][city][carID]
            
            make = catObj[1].split('~')[1]
            # print(catObj, make)
            makersTypes[make] = 1
            # time.sleep(1000)
makersTypes = list(makersTypes.keys())
colorVehicleTripsDict = {}
possibleColors = {}


makersTypes = []
i = 0
while i < 36:
    makersTypes.append(str(i))
    i += 1




possibleColors = makersTypes
# # for color in possibleColors:
# #     possibleColors[color] = {}
# time.sleep(100000)


studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1

desAccordingToUtil = {}



platforLowHighUtil = {}
platforLowHighUtil['Turo'] = [0.2,2]
platforLowHighUtil['GerAroundEurope'] =  [0.2,2]
platforLowHighUtil['GetAround'] =  [0.2,2]

detailsFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/'

genderPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/4a2-output/'


vehicleOwnerDemoDict = {}
for city in cityCurrencyMap:
    vehicleOwnerDemoDict[city] = {}
for platform in studiedApps:
    # vehicleOwnerDemoDict[platform] = {}
    desAccordingToUtil[platform] = {}
    colorVehicleTripsDict[platform] = {}
    # print(platform)
    platFormCatTrip[platform] = {}
    fx = open(loadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()
    catVehicleDict = {}
    v1 = []
    v2 = []
    fx = open(genderPath+platform+'-demographics.txt','r')
    ownerDemographics = json.loads(fx.read())
    ownerDemographics = ownerDemographics[platform]
    fx.close()
    print(platform)
    
    for cityName in analyzedData[platform]:
        if cityName != 'New York':
            city = cityName

            print('\t', cityName)
            vehicleOwnerDemoDict[cityName][platform] = {}
            desAccordingToUtil[platform][cityName] = {}
            desAccordingToUtil[platform][cityName]['lowUtil'] = []
            desAccordingToUtil[platform][cityName]['highUtil'] = []

            fx = open(detailsFolder+platform+'/'+city+'-content.txt','r')
            content2 = json.loads(fx.read())
            fx.close()


            
            for carId in analyzedData[platform][cityName]:
                # vehicleOwnerDemoDict[cityName][platform][carId] = {}
                carDays = analyzedData[platform][cityName][carId]['dates'][2]
                experimentTripsVehicle = abs(analyzedData[platform][cityName][carId]['trips'][1]-analyzedData[platform][cityName][carId]['trips'][0])
                
                ownerID = str(analyzedData[platform][cityName][carId]['ownerID'])

                dates = list(content2[carId].keys())
                dates.sort()
                date = dates[0]
                carNew = content2[carId][date]
                ownerName = carNew['ownerName']
                ownerIdNew = cityName+'~'+ownerName+'~'+str(ownerID)+'.jpg'
                ownerDemoDict = {}
                try:
                    ownerDemoObj = ownerDemographics[ownerIdNew]
                except:
                    ownerDemoObj = {}
                ownerDemoDict['demographicsId'] = ownerIdNew
                ownerDemoDict['peopleInDp'] = len(ownerDemoObj.keys())
                ownerDemoDict['ownerGenders'] = []
                ownerObjs = list(ownerDemoObj.keys())
                ownerObjs.sort()
                for x in range(len(ownerObjs)):
                    currentOwnerId = ownerObjs[x]
                    ownerDemoDict['ownerGenders'].append([ownerDemoObj[currentOwnerId]['gender'], ownerDemoObj[currentOwnerId]['age'], ownerDemoObj[currentOwnerId]['race']])
                vehicleOwnerDemoDict[cityName][platform][ownerIdNew] = {}
                vehicleOwnerDemoDict[cityName][platform][ownerIdNew] = ownerDemoDict   

fx = open('supplyOwnerDemo.txt','w')
fx.write(json.dumps(vehicleOwnerDemoDict))
fx.close()

# print(makersTypes)