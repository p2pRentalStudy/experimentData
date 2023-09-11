from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


studiedApps = {}
# studiedApps['Turo'] = 1
# studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'

# totalFeatues = []
totalFeatues = ['4-wheel drive', 'ABS brakes', 'AUX input', 'AUX/MP3 enabled', 'Air conditioning', 'All-wheel drive', 'Android Auto', 'Apple CarPlay', 'Audio / iPod input', 'Baby seat', 'Backup camera', 'Bike rack', 'Blind spot warning', 'Bluetooth', 'Bluetooth audio', 'Bluetooth wireless', 'CD player', 'Child seat', 'Convertible', 'Cruise control', 'DVD system', 'Dashcam', 'Dual air bags', 'GPS', 'GPS navigation system', 'Heated seats', 'Hitch', 'Keyless entry', 'Leather interior', 'Long-term car', 'Pet friendly', 'Power seats', 'Power windows', 'Premium sound', 'Premium wheels', 'Roof box', 'Roof rack', 'Side air bags', 'Ski rack', 'Ski racks', 'Snow chains', 'Snow tires', 'Snow tires or chains', 'Sunroof', 'Sunroof / moonroof', 'Tinted windows', 'Toll pass', 'USB charger', 'USB input', 'Wheelchair accessible', 'XM radio']

featuresMapDict = {}

featuresMapDict['4-wheel drive'] = 'AWD'
featuresMapDict['ABS brakes'] = 'ABS brakes'
featuresMapDict['AUX input'] = 'AUX'
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

'Premium wheels', 'Roof box', 'Roof rack', 'Side air bags', 'Ski rack', 'Ski racks', 'Snow chains', 'Snow tires', 'Snow tires or chains', 'Sunroof', 'Sunroof / moonroof', 'Tinted windows', 'Toll pass', 'USB charger', 'USB input', 'Wheelchair accessible', 'XM radio']

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



for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    totalCarTrips = {}
    
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName)
        if 1:
        # try:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            carCount = 0
            for id in content.keys():
                dates = list(content[id].keys())
                dates.sort()
                carObj = content[id][dates[0]]
                # print(carObj['features'])
                # time.sleep(10000)
                if 'Turo' in platform:
                    for item in carObj['features']:
                        if item['label'] not in totalFeatues:
                            totalFeatues.append(item['label'])
                elif 'GetAround' in platform:
                    items = carObj['features'].split(',')
                    for item in items:
                        if item!= '' and item not in totalFeatues:
                            totalFeatues.append(item)
                else:
                    # # items = carObj['features'].split(',')
                    # print(carObj['features'])
                    # time.sleep(10000)
                    if 'features' in carObj.keys():
                        for item in carObj['features']:
                            if item['title'] not in totalFeatues:
                                totalFeatues.append(item['title'])

                # 
        break
totalFeatues.sort()
print(totalFeatues)

               

                