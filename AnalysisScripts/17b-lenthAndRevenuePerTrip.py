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


analyzedData = {}
for cat in carCats:
    analyzedData[cat] = {}
    analyzedData[cat]['tripsLength'] = []
    analyzedData[cat]['tripsRevenue'] = []



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
        if 1:
        # if 'Barcelona' in cityName:
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
                    carCat = carIdToCat[platform+'~'+id][0]
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
                                        analyzedData[carCat]['tripsLength'].append(tripLength)
                                        analyzedData[carCat]['tripsRevenue'].append((prevPrice/24)*tripLength)
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
                        # prevPrice  = float(currentPrice[:-3]) * cityCurrencyMap[cityName]
                        prevTrips = currentTrips
                except Exception as e:
                    # print(carCount, e)
                    # time.sleep(1000)
                    pass
                    # vehicleId = platform+'~'+id
                    # print('2nd loop', vehicleId, currentDate, len(dates), len(cityVehiclePricesDict[vehicleId].keys()))

                # except Exception as e:
                #     print(e)

                #     # fx = open('temp.txt','w')
                #     # fx.write(json.dumps(content[id]))
                #     # fx.close()
                #     # time.sleep(1000)
                #     pass

                # for i in range(0,len(dates)):
                #     currentDate = dates[i]
                #     vehicleId = platform+'~'+id
                #     # print('2nd loop', vehicleId, currentDate, len(dates), len(cityVehiclePricesDict[vehicleId].keys()))
            # time.sleep(1000)

    print(platform)
    for cat in analyzedData:
        try:
            if 'GerA' in platform:
                print('\t', cat, round(np.average(analyzedData[cat]['tripsLength']),2),'&', round(np.average(analyzedData[cat]['tripsRevenue']),2))
            else:
                print('\t', cat, round(np.average(analyzedData[cat]['tripsLength'])*1.5,2),'&', round(np.average(analyzedData[cat]['tripsRevenue'])*1.5,2))
        except:
            pass




# for i in range(0, len(totalDates)):
            #     keyDate = totalDates[i]
            #     if i%50000 == 1:
            #         print('\t\t', i, keyDate)

            #     recordDate = totalDates[i]
            #     recordDate = recordDate.split(')')[0]
            #     startDate = recordDate.split(' (')[0]
            #     d0 = datetime.strptime(startDate, '%Y-%m-%d')
            #     aheadDates = recordDate.split(' (')[1]
            #     aheadDates = aheadDates.split(' - - ')
            #     aheadDates[0] = aheadDates[0].split(' ')[0]
            #     aheadDates[1] = aheadDates[1].split(' ')[0]

            #     if platform == 'Turo':
            #         d1 = datetime.strptime(aheadDates[0], '%m-%d-%Y')
            #     else:
            #         d1 = datetime.strptime(aheadDates[0], '%Y-%m-%d')

            #     dayDifference = d1-d0
            #     dayDifference = str(dayDifference)
            #     dayDifference = dayDifference.split(' ')[0]
            #     if ':' in dayDifference or dayDifference == '1':

            #         for vehicleId in content[keyDate]:
            #             car = content[keyDate][vehicleId]
            #             vehicleId = platform+'~'+vehicleId
            #             try:
            #                 val = cityVehiclePricesDict[vehicleId]
            #             except:
            #                 cityVehiclePricesDict[vehicleId] = {}
            #             try:
            #                 val = cityVehiclePricesDict[vehicleId][startDate]
            #             except:
            #                 cityVehiclePricesDict[vehicleId][startDate] = {}
            #             bookingPrice = car['bookingPrice']
            #             if platform == 'Turo' or platform == 'GetAround':
            #                 bookingPrice = bookingPrice.split(' ')
            #                 bookingPrice = round(float(bookingPrice[0]) * currencyConversion[bookingPrice[1]],2)
            #             else:
            #                 bookingPrice = [bookingPrice[0:1], bookingPrice[1:]]
            #                 bookingPrice = round(float(bookingPrice[1]) * currencyConversion[bookingPrice[0]],2)
            #             if platform == 'GetAround':
            #                 bookingPrice = bookingPrice*2.1

            #             cityVehiclePricesDict[vehicleId][startDate]['price'] = bookingPrice
            #             cityVehiclePricesDict[vehicleId][startDate]['trips'] = car['trips']
            #             # print(d0, d1, vehicleId, bookingPrice, car['trips'])
            #             # time.sleep(1000)

            # print('Done with the first loop')

            # if platform == 'GetAround':
            #     tempFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/GetAround/'
            #     fx = open(tempFolder+cityName+'-content.txt','r')
            #     content = json.loads(fx.read())
            #     fx.close()
            #     carCount = 0
            #     for id in content.keys():

            #         dates = list(content[id].keys())
            #         dates.sort()

            #         for i in range(0,len(dates)):
            #             currentDate = dates[i]
            #             vehicleId = platform+'~'+id
            #             # print('2nd loop', vehicleId, currentDate, len(dates), len(cityVehiclePricesDict[vehicleId].keys()))
            #             try:
            #                 cityVehiclePricesDict[vehicleId][currentDate]['trips'] = content[id][currentDate]['numberOfTrips']
            #             except:
            #                 pass

            # print ('2nd loop completed')

            # for vehicleId in cityVehiclePricesDict:
            #     totalDates = list(cityVehiclePricesDict[vehicleId].keys())
            #     totalDates.sort()
            #     prevTrips = 0
            #     for i in range(0, len(totalDates)):
            #         if cityVehiclePricesDict[vehicleId][totalDates[i]]['trips'] == -1:
            #             print(i, vehicleId)
            #             for j in range(0, len(totalDates)):
            #                 print('\t', totalDates[j], cityVehiclePricesDict[vehicleId][totalDates[j]]['trips'] )


            #             dates = list(content[vehicleId].keys())
            #             print('other dict')
            #             dates.sort()
            #             for j in range(0, len(dates)):
            #                 print('\t', totalDates[j], content[vehicleId][totalDates[j]]['trips'] )


            #         time.sleep(1000)
