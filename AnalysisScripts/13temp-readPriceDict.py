from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


studiedApps = {}
studiedApps['Turo'] = 1
# studiedApps['GetAround'] = 1
# studiedApps['GerAroundEurope'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13-output/APPNAME/'


carPrices = {}
for platform in studiedApps:
    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13-output/'+platform+'/'
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    totalCarTrips = {}
    
    for fileName in filenames:
        cityName = fileName.split('-')[1]
        
        if 1:
        # try:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            carCount = 0
            carPrices = {}
            print(platform, cityName, len(content.keys()))
            dynamicPricingCars = 0
            nonDynamicVehicles = {}
            for carID in content.keys():
                breakIt = 0
                for firstDate in content[carID]:
                    prevPrice = ''
                    breakIt = 0
                    for secondDate in content[carID][firstDate]:
                        currentPrice = content[carID][firstDate][secondDate]
                        
                        if prevPrice != currentPrice and prevPrice!='':
                            print(carID, firstDate, secondDate, prevPrice,  currentPrice)
                            time.sleep(1)
                            breakIt = 1
                            dynamicPricingCars += 1
                            break
                        prevPrice = currentPrice
                    if breakIt == 1:
                        break
                if breakIt == 0:
                    nonDynamicVehicles[carID] = 1

            print('\t', dynamicPricingCars)

            # for id in nonDynamicVehicles:
                # print('\t\t', id, len(content.keys()))

        break
    