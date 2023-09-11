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


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/APPNAME/'


carPrices = {}
for platform in studiedApps:
    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13-output/'+platform+'/'
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
            carPrices = {}
            for date in content.keys():
                for car in content[date]:
                    carObj = content[date][car]
                    # print(date, carObj['bookingPrice'])
                    try:
                        val = carPrices[car]
                    except:
                        carPrices[car] = {}
                    firstDate = date.split(' ')[0]

                    try:
                        val = carPrices[car][firstDate]
                    except:
                        carPrices[car][firstDate] = {}

                    # print(date.split(' '))
                    secondDate = date
                    secondDate = secondDate.replace(' - - ',' ')
                    secondDate = secondDate.replace('(','')
                    secondDate = secondDate.replace(')',' ')

                    tempate = secondDate[:]
                    tempate = tempate.split(' ')

                    if 'GetAround' in platform:
                        # print(secondDate)
                        secondDate = secondDate.split(' ')[1]+'~'+secondDate.split(' ')[3]
                    elif 'Europe' in platform:
                        # print(secondDate)
                        secondDate = secondDate.split(' ')[1]+'~'+secondDate.split(' ')[2]
                        # secondDate = secondDate.split('~')[0]
                    else:
                        # secondDate = secondDate.split('Price')[0]
                        secondDate = secondDate.split(' ')[1]+'~'+secondDate.split(' ')[2]
                        # secondDate = secondDate.split('~')[0]

                    carPrices[car][firstDate][secondDate] = carObj['bookingPrice']

                    # print(car, tempate, 'adasdasd', firstDate, secondDate)
                    # time.sleep(1000000)


            fx = open(savePath + platform+'-'+cityName+'.txt','w')
            fx.write(json.dumps(carPrices))
            fx.close()