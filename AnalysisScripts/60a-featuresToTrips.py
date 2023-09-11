from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally

totalFeatues = ['4-wheel drive', 'ABS brakes', 'AUX input', 'AUX/MP3 enabled', 'Air conditioning', 'All-wheel drive', 'Android Auto', 'Apple CarPlay', 'Audio / iPod input', 'Baby seat', 'Backup camera', 'Bike rack', 'Blind spot warning', 'Bluetooth', 'Bluetooth audio', 'Bluetooth wireless', 'CD player', 'Child seat', 'Convertible', 'Cruise control', 'DVD system', 'Dashcam', 'Dual air bags', 'GPS', 'GPS navigation system', 'Heated seats', 'Hitch', 'Keyless entry', 'Leather interior', 'Long-term car', 'Pet friendly', 'Power seats', 'Power windows', 'Premium sound', 'Premium wheels', 'Roof box', 'Roof rack', 'Side air bags', 'Ski rack', 'Ski racks', 'Snow chains', 'Snow tires', 'Snow tires or chains', 'Sunroof', 'Sunroof / moonroof', 'Tinted windows', 'Toll pass', 'USB charger', 'USB input', 'Wheelchair accessible', 'XM radio']

featuresMapDict = {}

featuresMapDict['4-wheel drive'] = 'AWD'
featuresMapDict['AWD'] = 'AWD'
featuresMapDict['ABS brakes'] = 'ABS brakes'
featuresMapDict['AUX input'] = 'AUX'
featuresMapDict['AUX'] = 'AUX'
featuresMapDict['AUX/MP3 enabled'] = 'AUX'
featuresMapDict['Air conditioning'] = 'Air conditioning'
featuresMapDict['All-wheel drive'] = 'AWD'
featuresMapDict['Android Auto'] = 'Android Auto'
featuresMapDict['Apple CarPlay'] = 'Apple CarPlay'
featuresMapDict['Audio / iPod input'] = 'AUX'
featuresMapDict['Baby seat'] = 'Baby seat'
featuresMapDict['Backup camera'] = 'Dashcam'
featuresMapDict['Bike rack'] = 'Bike rack'
featuresMapDict['Blind spot warning'] = 'Blind spot warning'
featuresMapDict['Bluetooth'] = 'Bluetooth'
featuresMapDict['Bluetooth audio'] = 'Bluetooth'
featuresMapDict['Bluetooth wireless'] = 'Bluetooth'
featuresMapDict['CD player'] = 'CD player'
featuresMapDict['Child seat'] = 'Baby seat'
featuresMapDict['Convertible'] = 'Convertible'
featuresMapDict['Cruise control'] = 'Cruise control'
featuresMapDict['DVD system'] = 'CD player'
featuresMapDict['Dashcam'] = 'Dashcam'
featuresMapDict['Dual air bags'] = 'Dual air bags'
featuresMapDict['GPS'] = 'GPS'
featuresMapDict['GPS navigation system'] = 'GPS navigation system'
featuresMapDict['Heated seats'] = 'Heated seats'
featuresMapDict['Hitch'] = 'Hitch'
featuresMapDict['Keyless entry'] = 'Keyless entry'
featuresMapDict['Leather interior'] = 'Leather interior'
featuresMapDict['Long-term car'] = 'Long-term car'
featuresMapDict['Pet friendly'] = 'Pet friendly'
featuresMapDict['Power seats'] = 'Power seats'
featuresMapDict['Power windows'] = 'Power windows'
featuresMapDict['Premium sound'] = 'Premium sound'
featuresMapDict['Premium wheels'] = 'Premium wheels'
featuresMapDict['Roof box'] = 'Roof box'
featuresMapDict['Roof rack'] = 'Roof rack'
featuresMapDict['Side air bags'] = 'Side air bags'
featuresMapDict['Ski rack'] = 'Ski rack'
featuresMapDict['Ski racks'] = 'Ski rack'
featuresMapDict['Snow chains'] = 'Snow chains'
featuresMapDict['Snow tires'] = 'Snow tires'
featuresMapDict['Snow tires or chains'] = 'Snow tires'
featuresMapDict['Sunroof'] = 'Sunroof'
featuresMapDict['Sunroof / moonroof'] = 'Sunroof'
featuresMapDict['Tinted windows'] = 'Tinted windows'
featuresMapDict['Toll pass'] = 'Toll pass'
featuresMapDict['USB charger'] = 'USB charger'
featuresMapDict['USB input'] = 'USB charger'
featuresMapDict['Wheelchair accessible'] = 'Wheelchair accessible'
featuresMapDict['XM radio'] = 'Radio'
featuresMapDict['Radio'] = 'Radio'
featuresMapDict['Fuel efficient'] = 'Fuel efficient'
featuresMapDict['hybrid'] = 'Fuel efficient'
featuresMapDict['hybrid'] = 'Fuel efficient'
featuresMapDict['hybrid'] = 'Fuel efficient'
featuresMapDict['hybrid'] = 'Fuel efficient'
featuresMapDict['hybrid'] = 'Fuel efficient'




fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()


fx = open('finalCarColors.txt', 'r')
carColors = json.loads(fx.read())
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


exceptKeys = {}
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
makersTypes = {}
for key in featuresMapDict:
    makersTypes[featuresMapDict[key]] = 1
makersTypes = list(makersTypes.keys())
colorVehicleTripsDict = {}
possibleColors = {}



possibleColors = makersTypes
# # for color in possibleColors:
# #     possibleColors[color] = {}
# time.sleep(100000)


studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1

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
            fx = open(targetFolder2+platform+'/'+cityName+'-content.txt','r')
            f2Content = json.loads(fx.read())
            fx.close()

            for color in possibleColors:
                colorVehicleTripsDict[platform][cityName][color] = {}
                # colorVehicleTripsDict[platform][cityName][color]['vehicleIDs'] = []
                colorVehicleTripsDict[platform][cityName][color]['trips'] = []
            # print('\t',cityName)
            fx = open(loadPath +platform+'-'+cityName+'-tripDetails.txt','r')
            tripDetailsDict = json.loads(fx.read())
            fx.close()
            for carId in analyzedData[platform][cityName]:
                vc += 1
                cat = 'sedan'
                make = 'ford'
                catObj = []
                try:
                    cat = cityServiceCat[platform][cityName][carId][0]
                    catObj = cityServiceCat[platform][cityName][carId]
                    make = catObj[1].split('~')[1]
                except:
                    pass
                
                carDays = analyzedData[platform][cityName][carId]['dates'][2]
                experimentTripsVehicle = analyzedData[platform][cityName][carId]['trips'][1]-analyzedData[platform][cityName][carId]['trips'][0]

                carColor = 'white'

                #get year of vehicle
                # print(f2Content.keys())
                carObj = f2Content[carId]
                dates = list(carObj.keys())
                dates.sort()

                carObj = carObj[dates[0]]

                items = []
                
                # print(platform, city,carId, carRating, catObj)
                # time.sleep(10000)
                if experimentTripsVehicle > -1:
                    try:
                        if 'GetAround' in platform:
                            items = carObj['features'].split(',')
                        else: 
                            items = carObj['features']
                
                        for item in items:
                            try:
                                itemLabel = ''
                                if 'Turo' in platform:
                                    itemLabel = item['label']
                                elif 'GetAround' in platform:
                                    itemLabel= item
                                else:
                                    itemLabel = item['title']
                                # print(itemLabel)
                                # time.sleep(1000)
                                if itemLabel != '':
                                    experimentTripsVehicle = (experimentTripsVehicle/carDays)*30
                                    colorVehicleTripsDict[platform][cityName][featuresMapDict[itemLabel]]['trips'].append(round(experimentTripsVehicle,2))
                            except Exception as e:
                                exceptKeys[e] = 1
                                # print(e)
                                # time.sleep(1000)
                                pass
                    except:
                        pass


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


fx = open('vfeaturesToTrips.txt','w')
fx.write(json.dumps(colorVehicleTripsDict))
fx.close()

print(makersTypes)

print('\n\n', exceptKeys)