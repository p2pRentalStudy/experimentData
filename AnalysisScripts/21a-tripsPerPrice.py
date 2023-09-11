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
studiedApps['Turo'] = 1
# studiedApps['GetAround'] = 1
# studiedApps['GerAroundEurope'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'
totalMeta = {'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}, 'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}}



analyzedData = {}
studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

for platform in studiedApps:
    analyzedData[platform] = {}
    for city in totalMeta[platform]:
        analyzedData[platform][city] = []

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

for platform in studiedApps:
    listData = {}
    tripsList = []
    revenueList = []

    tempFolder = targetFolder.replace('APPNAME',platform)
    if 'Europe' in platform:
        tempFolder2 = tempFolder.replace('1-','0-')

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    totalCarTrips = {}

    for fileName in filenames:
        cityName = fileName.split('-')[0]
        # if 1:
        if 'New York' != cityName:
            print(platform, cityName)
            fx = open(tempFolder+cityName+'-content.txt','r')
            content = json.loads(fx.read())
            fx.close()
            if 'Europe' in platform:
                # print(tempFolder2)
                fx = open(tempFolder2+cityName+'-content.txt','r')
                content2 = json.loads(fx.read())
                fx.close()

                totalDates = list(content2.keys())
                totalDates.sort()

                priceDict = {}
                for i in range(0, len(totalDates)):
                    keyDate = totalDates[i]
                    recordDate = totalDates[i]
                    recordDate = recordDate.split(')')[0]
                    startDate = recordDate.split(' (')[0]
                    # print(startDate)
                    d0 = datetime.strptime(startDate, '%Y-%m-%d')
                    aheadDates = recordDate.split(' (')[1]
                    aheadDates = aheadDates.split(' - - ')
                    aheadDates[0] = aheadDates[0].split(' ')[0]
                    aheadDates[1] = aheadDates[1].split(' ')[0]

                    if platform == 'Turo':
                        d1 = datetime.strptime(aheadDates[0], '%m-%d-%Y')
                    else:
                        d1 = datetime.strptime(aheadDates[0], '%Y-%m-%d')

                    dayDifference = d1-d0
                    dayDifference = str(dayDifference)
                    dayDifference = dayDifference.split(' ')[0]
                    if ':' in dayDifference or dayDifference == '1':
                        for vehicleId in content2[keyDate]:
                            car = content2[keyDate][vehicleId]
                            vehicleId = platform+'~'+vehicleId
                            bookingPrice = car['bookingPrice']
                            # print(keyDate, bookingPrice)
                            # time.sleep(1000)
                            if platform == 'Turo' or platform == 'GetAround':
                                bookingPrice = bookingPrice.split(' ')
                                bookingPrice = round(float(bookingPrice[0]) * currencyConversion[bookingPrice[1]],2)
                            else:
                                bookingPrice = [bookingPrice[0:1], bookingPrice[1:]]
                                bookingPrice = round(float(bookingPrice[1]) * currencyConversion[bookingPrice[0]],2)
                            if platform == 'GetAround':
                                bookingPrice = bookingPrice*2.1
                            try:
                                val = priceDict[vehicleId]
                            except:
                                priceDict[vehicleId] = []

                            # print(keyDate, bookingPrice)
                            # time.sleep(1000)
                            priceDict[vehicleId].append(bookingPrice)

                for vehicleId in priceDict:
                    priceDict[vehicleId] = np.average(priceDict[vehicleId])
                    # print(vehicleId, priceDict[vehicleId])


            carCount = 0

            for id in content.keys():
                try:
                    # carCat = carIdToCat[platform+'~'+id][0]
                    carCount += 1

                    dates = list(content[id].keys())
                    dates.sort()

                    # try:
                    # print(carCount, len(dates),  dates[0],  dates[-1], content[id][dates[0]]['dailyPrice'])
                    prevTrips = 0
                    prevPrice = 0
                    prevDate = ''
                    for i in range(0,len(dates)):
                        carObj = content[id][dates[i]]
                        currentDate = dates[i]
                        currentTrips = carObj['numberOfTrips']
                        if 'Europe' in platform:
                            # print(len(dates), len(priceDict[platform+'~'+id].keys()))
                            # time.sleep(1000)
                            currentPrice = priceDict[platform+'~'+id]#[startDate]
                        else:
                            currentPrice = carObj['dailyPrice']
                        if prevDate != '':
                            if prevTrips != currentTrips:
                                d1 = datetime.strptime(prevDate, '%Y-%m-%d')
                                d2 = datetime.strptime(currentDate, '%Y-%m-%d')
                                dayDifference = d2-d1
                                dayDifference = str(dayDifference)
                                dayDifference = int(dayDifference.split(' ')[0])

                                tripDifference = int(currentTrips) - int(prevTrips)
                                if tripDifference > 0:
                                    tripLength = tripDifference/(dayDifference)
                                    tripLength = tripLength * 24
                                    if tripLength < 1:
                                        tripLength = round(tripLength*3,2)
                                    # print(id, prevTrips, currentTrips, prevDate, currentDate, dayDifference, tripDifference, tripLength, prevPrice)
                                    for x in range(tripDifference):
                                        analyzedData[platform][cityName].append((prevPrice/24)*tripLength)
                                    #     tripsList.append(tripLength)
                                    # # for x in range(tripDifference):
                                    #     revenueList.append((prevPrice/24)*tripLength)
                                # time.sleep(1)
                        prevDate = currentDate
                        if 'Turo' in platform:
                            prevPrice  = float(currentPrice[:-3]) * cityCurrencyMap[cityName]
                        else:
                            prevPrice  = float(currentPrice) * cityCurrencyMap[cityName]
                        prevTrips = currentTrips
                except Exception as e:
                    print(e)
                    time.sleep(1000)
                    pass




# print(totalMeta)
savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/21-output/'
fx = open(savePath+'21a-tripPriceDict.txt','w')
fx.write(json.dumps(analyzedData))
fx.close()
print('\t saving dict')
