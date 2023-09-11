from basicImports import *
import requests
import random
import string
from os import walk

import random

studiedApps = {}
# studiedApps['Turo'] = 1
# studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1

# jvs4v1q5

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/APPNAME/vehiclesList'
'/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/GerAroundEurope/vehiclesList'
'/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/GetAround/vehiclesList'

def writeCityRecords(currentCity, listData):

    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'+platform+'/'

    print('writing record', len(listData[platform][country][city].keys()))
    fx = open(savePath+currentCity+'-content.txt','w')
    print()
    fx.write(json.dumps(listData[platform][country][city]))
    fx.close()

    return 0
import random


for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    # print(tempFolder)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    # #TO BE COMMENTED
    # filenames = [i for i in filenames if 'shington D.C' in i]


    print(platform, len(filenames))
    # for fn in filenames:
    #     print(fn)
    # time.sleep(1000)
    listData[platform] = {}
    totalCars = {}
    currentCity = ''
    if 'Europe' in platform:
        filesChecked = 0
        for file in filenames:
            if 'Encoded' in file:
                recordCity = file.split('-')[1]
                if recordCity != currentCity:
                    if currentCity != '':
                        print('saving for', currentCity)
                        writeCityRecords(currentCity,listData)
                        totalCars = {}
                        listData[platform] = {}
                    currentCity = recordCity
                #decompile file
                print('Reading:  ',filesChecked,'/', len(filenames), platform, file)
                fileContent = open(tempFolder+'/'+file, 'rb').read()
                fileContent = fileContent.split(b'0x0A')
                realDate = file.split('responseEncoded-')[1]
                realDate = realDate.replace('.txt','')
                # print(len(fileContent))
                for itemI in range(0, len(fileContent)):
                    item = fileContent[itemI]
                    checkObject = 1
                    try:
                        item = zlib.decompress(item)
                        # print(item)
                        item = json.loads(item)
                        keysList = list(item.keys())
                        keysList.sort()
                    except:
                        checkObject = 0

                    if checkObject == 1:

                    # if len(item) > 10:
                    # try:

                        for metaKey in keysList:
                            partsOfKey = metaKey.split('~')
                            country = partsOfKey[0]
                            city = partsOfKey[1]
                            recordDate = realDate + ' ('+partsOfKey[3]+' - - '+partsOfKey[4]+') PaheNumber='+partsOfKey[-1]
                            recordPage = 1
                            recordsPerPage = 0
                            if partsOfKey[3]< '2023-04-17' and partsOfKey[4] < '2023-04-17':
                                # print(realDate, metaKey, recordDate)
                                # time.sleep(1000)

                                if 'Europe' in platform:
                                    recordPage = int(partsOfKey[-1]) -1
                                    recordsPerPage = 20
                                try:
                                    v1 = listData[platform][country]
                                except:
                                    listData[platform][country] = {}

                                try:
                                    v1 = listData[platform][country][city]
                                except:
                                    listData[platform][country][city] = {}

                                try:
                                    v1 = listData[platform][country][city][recordDate]
                                except:
                                    listData[platform][country][city][recordDate] = {}

                                keyContent = item[metaKey]
                                keyContent = keyContent['cars']

                                rankOfCar = 0
                                for car in keyContent:

                                    # print(recordPage, rankOfCar)
                                    # print(car)
                                    # fx = open('temp.txt','w')
                                    # fx.write(json.dumps(car))
                                    # fx.close()
                                    # print('sleeping')
                                    # time.sleep(1000)
                                    carId = car['id']
                                    # totalCars[carId] = 1
                                    listData[platform][country][city][recordDate][carId] = {}
                                    listData[platform][country][city][recordDate][carId]['trips'] = car['stats']['ended_rentals_count']
                                    listData[platform][country][city][recordDate][carId] ['averageRating'] = car['stats']['ratings_average']
                                    listData[platform][country][city][recordDate][carId] ['ratingCount'] = car['stats']['ratings_count']
                                    listData[platform][country][city][recordDate][carId] ['carRankInSearch'] = (recordPage*recordsPerPage) + rankOfCar
                                    listData[platform][country][city][recordDate][carId] ['isAvailable'] = car['is_open']
                                    listData[platform][country][city][recordDate][carId] ['bookingPrice'] = car['price_info']['main_price']
                                    try:
                                        val = totalCars[carId]
                                    except:
                                        listData[platform][country][city][recordDate][carId]['ownerPic'] = car['owner_avatar']['thumb_url']
                                        # listData[platform][country][city][recordDate][carId] ['ownerID'] = -1
                                        try:
                                            listData[platform][country][city][recordDate][carId]['ownerID'] = car['owner_avatar']['thumb_url'].split('/')[5]
                                            listData[platform][country][city][recordDate][carId]['ownerID'] = listData[platform][country][city][recordDate][carId] ['ownerID'].split('.')[0]
                                        except:
                                            fx = open('temp.txt','w')
                                            fx.write(json.dumps(car))
                                            fx.close()
                                            # print(recordDate, 'photo url', car['owner_avatar']['thumb_url'])
                                            # time.sleep(1000)

                                        listData[platform][country][city][recordDate][carId] ['carTitle'] = car['title']

                                        listData[platform][country][city][recordDate][carId] ['makeYear'] = car['display_specs']

                                        listData[platform][country][city][recordDate][carId] ['carPhotos'] = car['photos']



                                        listData[platform][country][city][recordDate][carId] ['allowedMiles'] = car['display_price_details']



                                        listData[platform][country][city][recordDate][carId] ['bookingPeriod'] = car['price_info']['main_price_label']



                                        listData[platform][country][city][recordDate][carId] ['seats'] = car['display_specs']

                                        listData[platform][country][city][recordDate][carId] ['FuelType'] = car['display_specs']

                                        listData[platform][country][city][recordDate][carId] ['vehicleCategory'] = 'TBA'

                                        totalCars[carId] = 1

                                    rankOfCar += 1
                                    # print('\n\n\n')
                                    # print(car)

                                    # fx = open('temp.txt','w')
                                    # fx.write(json.dumps(item[metaKey]))
                                    # fx.close()
                                    # print(listData)
                                    # print('Sleeping')
                                    # time.sleep(1000)
                        # except Exception as e:
                        #     print(e)
                    # print('cars',len(totalCars.keys()))
                filesChecked += 1
                # if filesChecked > 5:
                #     break

        # savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'+platform+'/'

        # fx = open(savePath+'content.txt','w')
        # fx.write(json.dumps(listData))
        # fx.close()

    #Turo
    elif 'Turo' in platform:
        filesChecked = 0
        for file in filenames:
            if 'Encoded' in file:
                recordCity = file.split('-')[1]
                if recordCity != currentCity:
                    if currentCity != '':
                        print('saving for', currentCity)
                        writeCityRecords(currentCity,listData)
                        listData[platform] = {}
                        totalCars = {}
                    currentCity = recordCity
                #decompile file
                print('Reading:  ',filesChecked,'/', len(filenames), platform, file)
                fileContent = open(tempFolder+'/'+file, 'rb').read()
                fileContent = fileContent.split(b'0x0A')
                # print(len(fileContent))
                realDate = file.split('responseEncoded-')[1]
                realDate = realDate.replace('.txt','')
                # try:
                #     print(len(listData[platform][country][city].keys()))
                # except:
                #     pass

                for itemI in range(0, len(fileContent)):
                    item = fileContent[itemI]
                    checkObject = 1
                    try:
                        item = zlib.decompress(item)
                        # print(item)
                        item = item.decode()
                        item = json.loads(item)
                        keysList = list(item.keys())
                        keysList.sort()
                    except:
                        checkObject = 0

                    if checkObject == 1:

                        for metaKey in keysList:

                            # fx = open('temp.txt','w')
                            # fx.write(json.dumps(item[metaKey]))
                            # fx.close()
                            # print('sleeping')
                            # time.sleep(10000)

                            partsOfKey = metaKey.split('~')
                            country = partsOfKey[0]
                            city = partsOfKey[1]
                            recordDate = realDate + ' ('+partsOfKey[3]+' - - '+partsOfKey[4]+') PriceLow='+partsOfKey[-2]+' PriceHigh='+partsOfKey[-1]
                            recordDate = recordDate.replace('%2F','-')
                            recordPage = 1
                            recordsPerPage = 0
                            if partsOfKey[3]< '2023-04-17' and partsOfKey[4] < '2023-04-17':

                                # print(realDate, metaKey, recordDate)

                                # time.sleep(10000)

                                try:
                                    v1 = listData[platform][country]
                                except:
                                    listData[platform][country] = {}

                                try:
                                    v1 = listData[platform][country][city]
                                except:
                                    listData[platform][country][city] = {}

                                try:
                                    v1 = listData[platform][country][city][recordDate]
                                except:
                                    listData[platform][country][city][recordDate] = {}

                                keyContent = item[metaKey]
                                keyContent = keyContent['list']

                                rankOfCar = 0


                                for car in keyContent:
                                    fx = open('temp.txt','w')
                                    fx.write(json.dumps(car))
                                    fx.close()
                                    print('sleeping')
                                    time.sleep(1000)

                                    # print(recordPage, rankOfCar)
                                    carId = car['vehicle']['id']
                                    # totalCars[carId] = 1
                                    listData[platform][country][city][recordDate][carId] = {}
                                    listData[platform][country][city][recordDate][carId] ['trips'] = car['renterTripsTaken']
                                    listData[platform][country][city][recordDate][carId] ['averageRating'] = car['rating']
                                    listData[platform][country][city][recordDate][carId] ['ratingCount'] = -1
                                    listData[platform][country][city][recordDate][carId] ['carRankInSearch'] = rankOfCar
                                    listData[platform][country][city][recordDate][carId] ['isAvailable'] = 'Yes'
                                    listData[platform][country][city][recordDate][carId] ['bookingPrice'] = str(car['rate']['averageDailyPriceWithCurrency']['amount'])+' '+car['rate']['averageDailyPriceWithCurrency']['currencyCode']

                                    try:
                                        val = totalCars[carId]
                                    except:
                                        listData[platform][country][city][recordDate][carId] ['ownerPic'] = -1
                                        listData[platform][country][city][recordDate][carId] ['ownerID'] = car['owner']['id']


                                        listData[platform][country][city][recordDate][carId] ['carTitle'] = car['vehicle']['model']
                                        listData[platform][country][city][recordDate][carId] ['makeYear'] = car['vehicle']['year']
                                        listData[platform][country][city][recordDate][carId] ['carCompany'] = car['vehicle']['make']


                                        #
                                        listData[platform][country][city][recordDate][carId] ['carPhotos'] = car['images'][0]['originalImageUrl']



                                        listData[platform][country][city][recordDate][carId] ['allowedMiles'] = -1



                                        listData[platform][country][city][recordDate][carId] ['bookingPeriod'] = '1 day'



                                        listData[platform][country][city][recordDate][carId] ['seats'] = -1

                                        listData[platform][country][city][recordDate][carId] ['FuelType'] = -1

                                        listData[platform][country][city][recordDate][carId] ['vehicleCategory'] = car['vehicle']['type']

                                        totalCars[carId] = 1

                                    rankOfCar += 1
                                    # print(metaKey, recordDate, len(keyContent))
                                    # time.sleep(10000)

                filesChecked += 1
                # if filesChecked >3:
                    # break

    #GetAround
    elif 'GetAround' in platform:
        filesChecked = 0
        for file in filenames:
            if 'Encoded' in file:
                recordCity = file.split('-')[1]
                if recordCity != currentCity:
                    if currentCity != '':
                        print('saving for', currentCity)
                        writeCityRecords(currentCity,listData)
                        listData[platform] = {}
                        totalCars = {}
                    currentCity = recordCity
                #decompile file
                print('Reading:  ',filesChecked,'/', len(filenames), platform, file)
                fileContent = open(tempFolder+'/'+file, 'rb').read()
                fileContent = fileContent.split(b'0x0A')
                # print(len(fileContent))
                realDate = file.split('responseEncoded-')[1]
                realDate = realDate.replace('.txt','')

                for itemI in range(0, len(fileContent)):
                    item = fileContent[itemI]
                    checkObject = 1
                    try:
                        item = zlib.decompress(item)
                        item = item.decode()
                        # print(item)
                        item = json.loads(item)
                        keysList = list(item.keys())
                        keysList.sort()
                    except:
                        checkObject = 0

                    if checkObject == 1:


                        for metaKey in keysList:
                            # print(metaKey)
                            # fx = open('temp.txt','w')
                            # fx.write(json.dumps(item[metaKey]))
                            # fx.close()
                            # print('sleeping')
                            # time.sleep(10000)
                            # print(metaKey)
                            if len(metaKey) > 20:
                                partsOfKey = metaKey.split('~')
                                country = partsOfKey[0]
                                city = partsOfKey[1]
                                recordDate = realDate + ' ('+partsOfKey[3]+' - - '+partsOfKey[4]+')'

                                recordDate = recordDate.replace('T',' ')
                                # recordDate = recordDate.replace('T21','')
                                recordPage = 1
                                recordsPerPage = 0
                                if partsOfKey[3].split('T')[0] < '2023-04-17' and partsOfKey[4].split('T')[0] < '2023-04-17':
                                    # print(metaKey, recordDate,  partsOfKey[3].split('T')[0] )
                                    # time.sleep(30000)
                                    try:
                                        v1 = listData[platform][country]
                                    except:
                                        listData[platform][country] = {}

                                    try:
                                        v1 = listData[platform][country][city]
                                    except:
                                        listData[platform][country][city] = {}

                                    try:
                                        v1 = listData[platform][country][city][recordDate]
                                    except:
                                        listData[platform][country][city][recordDate] = {}

                                    keyContent = item[metaKey]
                                    keyContent = keyContent['cars']

                                    rankOfCar = 0


                                    for car in keyContent:
                                        # print(recordPage, rankOfCar)
                                        carId = car['car_id']
                                        # if len(car['features']) > 0:
                                        #     fx = open('temp.txt','w')
                                        #     fx.write(json.dumps(car))
                                        #     fx.close()
                                        #     print('Sleeping')
                                        #     time.sleep(1000)

                                        # fx = open('temp.txt','w')
                                        # fx.write(json.dumps(car))
                                        # fx.close()

                                        # totalCars[carId] = 1
                                        listData[platform][country][city][recordDate][carId] = {}
                                        # listData[platform][country][city][recordDate][carId] ['trips'] = -1
                                        try:
                                            listData[platform][country][city][recordDate][carId] ['trips'] = car['rating_count']
                                        except:
                                            listData[platform][country][city][recordDate][carId] ['trips'] = -1

                                        try:
                                            listData[platform][country][city][recordDate][carId] ['averageRating'] = car['stars_rating']
                                        except:
                                            listData[platform][country][city][recordDate][carId] ['averageRating'] = -1
                                        listData[platform][country][city][recordDate][carId] ['carRankInSearch'] = rankOfCar

                                        try:
                                            listData[platform][country][city][recordDate][carId] ['ratingCount'] = car['rating_count']
                                        except:
                                            listData[platform][country][city][recordDate][carId] ['ratingCount'] = 0
                                        listData[platform][country][city][recordDate][carId] ['isAvailable'] = 'Yes'

                                        # print(car['price_hourly'])
                                        listData[platform][country][city][recordDate][carId] ['bookingPrice'] = str(round(float(car['price_hourly'])*8.8,1))+' '+car['country']
                                        # print( listData[platform][country][city][recordDate][carId] ['bookingPrice'])
                                        # print(recordDate)
                                        # fx = open('temp.txt','w')
                                        # fx.write(json.dumps(car))
                                        # fx.close()

                                        # print('Sleeping')
                                        # time.sleep(1000)

                                        try:
                                            val = totalCars[carId]
                                        except:
                                            listData[platform][country][city][recordDate][carId] ['ownerPic'] = car['owner_photo_v2']
                                            listData[platform][country][city][recordDate][carId] ['ownerName'] = car['owner_name']
                                            listData[platform][country][city][recordDate][carId] ['ownerID'] = car['owner_id']


                                            listData[platform][country][city][recordDate][carId] ['carTitle'] = car['model']
                                            listData[platform][country][city][recordDate][carId] ['carFeatures'] = car['features']
                                            listData[platform][country][city][recordDate][carId] ['makeYear'] = car['year']
                                            listData[platform][country][city][recordDate][carId] ['carCompany'] = car['make']


                                            #
                                            try:
                                                listData[platform][country][city][recordDate][carId] ['carPhotos'] = car['car_photo_v2']
                                            except:
                                                listData[platform][country][city][recordDate][carId] ['carPhotos'] = -1



                                            listData[platform][country][city][recordDate][carId] ['allowedMiles'] = -1



                                            listData[platform][country][city][recordDate][carId] ['bookingPeriod'] = '1 day'



                                            listData[platform][country][city][recordDate][carId] ['seats'] = -1

                                            listData[platform][country][city][recordDate][carId] ['FuelType'] = -1

                                            listData[platform][country][city][recordDate][carId] ['vehicleCategory'] = -1

                                            totalCars[carId] = 1

                                        rankOfCar += 1
                                        # print(metaKey, recordDate, len(keyContent))
                                        # time.sleep(10000)

                filesChecked += 1
                # if filesChecked == len(filenames)-2:
                #     break


    writeCityRecords(currentCity,listData)
    listData[platform] = {}
