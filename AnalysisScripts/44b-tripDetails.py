from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/vehicleCat-output/'
fx = open(loadPath + 'vehicleCategories.txt','r')
carIdToCat = json.loads(fx.read())
fx.close()

carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']

studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1

from datetime import timedelta


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'
analyzedData = {}


lengthMulMap = {}
lengthMulMap['GerAroundEurope'] = 1
lengthMulMap['GetAround'] = 1
lengthMulMap['Turo'] = 1

priceMulMap = {}
priceMulMap['GerAroundEurope'] = 1
priceMulMap['GetAround'] = 1
priceMulMap['Turo'] = 1

# print(platformAverage['Turo'][:10])
# time.sleep(10000)
from difflib import get_close_matches


def findRightDate(l1,d1):
    # print(d1, list(l1.keys())[:3])
    n = 1
    cutoff = 0.7
    close_matches = get_close_matches( d1, list(l1.keys()))
    # print(close_matches)
    return close_matches[0]


studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1

fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()


for platform in studiedApps:

    catPrices = {}
    listData = {}
    analyzedData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    analyzedData[platform] = {}

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    totalCarTrips = {}
    carCt = 0
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName)

        fx = open(tempFolder+fileName,'r')
        content = json.loads(fx.read())
        fx.close()

        tempFolder2 = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13-output/'+platform+'/'

        fx = open(tempFolder2+platform+'-'+cityName+'.txt','r')
        pricingDict = json.loads(fx.read())
        fx.close()

        carCount = 0
        analyzedData[platform][cityName] = {}

        for id in content.keys():



            dates = list(content[id].keys())
            dates.sort()
            startTrips = 0
            endTrips = 0
            carId = str(id)

            cat = 'sedan'
            try:
                cat = cityServiceCat[platform][cityName][carId][0]
            except:
                pass

            startTrips = int(content[id][dates[0]]['numberOfTrips'])
            endTrips = int(content[id][dates[-1]]['numberOfTrips'])


            d1 = datetime.strptime(dates[0], "%Y-%m-%d")
            d2 = datetime.strptime(dates[-1], "%Y-%m-%d")
            # print(d1,d2)
            # difference between dates in timedelta
            delta = d2 - d1
            totalTrips = endTrips-startTrips
            tempDictObj = {}
            if delta.days >34:
                analyzedData[platform][cityName][carId] = []
                prevTrips = 0
                prevPrice = 0
                prevDate = ''
                for i in range(0,len(dates)):
                    carObj = content[id][dates[i]]

                    currentDate = dates[i]
                    currentDate = currentDate.replace(' (2)', '')
                    currentTrips = carObj['numberOfTrips']
                    if prevDate != '':
                        # print(carObj)
                        # time.sleep(1000)
                        if prevTrips != currentTrips:
                            try:
                                d1 = datetime.strptime(prevDate, '%Y-%m-%d')
                                d2 = datetime.strptime(currentDate, '%Y-%m-%d')
                                dayDifference = d2-d1
                                dayDifference = dayDifference.days
                                tripDifference = int(currentTrips) - int(prevTrips)
                                tripLength = tripDifference/(dayDifference)
                                tripLength = tripLength * 24

                                t1Date = d1

                                for x in range(tripDifference):

                                    if tripLength < 3:
                                        tripLength = round(tripLength*3,2)

                                    tripObj = {}
                                    tripLength = round(tripLength * lengthMulMap[platform],2)
                                    tripObj['length'] = tripLength
                                    tripObj['StartDate'] = str(t1Date).split(' ')[0]
                                    tripObj['price'] = (124/24) #* tripLength

                                    pricesObj = {}
                                    try:
                                        pricesObj = pricingDict[platform+'~'+carId]
                                        key1 = findRightDate(pricesObj, tripObj['StartDate'])

                                        key2 = list(pricesObj[key1].keys())
                                        key2.sort()
                                        key2 = key2[0]
                                        # tripObj['price'] = pricesObj[key1][key2]
                                        tripObj['price'] = pricesObj[key1][key2]/24

                                        try:
                                            v10 = catPrices[cat]
                                        except:
                                            catPrices[cat] = []
                                        catPrices[cat].append(pricesObj[key1][key2])
                                        #, round(pricesObj[key1][key2]/24 * tripLength, 2))
                                        # print(id, tripObj['price'])
                                        # time.sleep(10000)

                                        # tripObj['price'] = max(pricesObj[key1][key2])#, round(pricesObj[key1][key2]/24 * tripLength, 2))

                                        # if platform == 'GetAround':
                                        # tripObj['price'] = tripObj['price']#*priceMulMap[platform]
                                    except:
                                        pass
                                    #, list(pricingDict.keys())[:10])

                                    t1Date = t1Date + timedelta(hours = int(tripLength))



                                    analyzedData[platform][cityName][carId].append(tripObj)
                            except Exception as e:
                                print(e,'--',prevDate,'--', currentDate)
                                time.sleep(10000)

                    prevDate = currentDate
                    prevTrips = currentTrips
        savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'
        # print(analyzedData)
        fx = open(savePath +platform+'-'+cityName+'-tripDetails.txt','w')
        fx.write(json.dumps(analyzedData))
        fx.close()
        analyzedData[platform] = {}
    for cat in catPrices:
        print('\t', cat, np.average(catPrices[cat]))
