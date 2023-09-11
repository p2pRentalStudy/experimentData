from basicImports import *
import requests
import random
import string
from os import walk


studiedApps = {}
# studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
# studiedApps['GerAroundEurope'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/getCarDetails/carDetails/'

totalFiles = []
for root, dirs, files in os.walk(targetFolder):
     for file in files:
        totalFiles.append(os.path.join(root, file))
# print(len(totalFiles))
listData = {}

def writeCityRecords(currentCity, listData):

    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/'+platform+'/'

    fx = open(savePath+currentCity+'-content.txt','w')
    fx.write(json.dumps(listData[platform][currentCity]))
    fx.close()

    return 0

currentCity = ''
for platform in studiedApps:
    listData[platform] = {}
    res = [i for i in totalFiles if platform+'#' in i]

    newRes = {}
    for fn in res:
        if platform in fn:
            fn1 = fn.split('/')
            
            fn1 = fn1[7:]
            # print(fn1)
            for part in fn1:
                if '.txt' in part:
                    newRes[part] = fn
            # newRes.append(fn)
    
    res=list(newRes.keys())
    res.sort()

    #carDetailsTuro#Washington D.C.#997074#2022-10-04.txt
    #2022-10-10Turo#Las Vegas#1118438#2022-10-10.txt

    print(platform, len(res), 'files')

    # for item in res:
    #     print(item)
    filesChecked = 0
    # time.sleep(1000)
    # time.sleep(1000)
    for file in res:
        file = newRes[file]
        if '.txt' in file:

            filesChecked += 1

            if filesChecked %1000 == 0:
                print('\t',filesChecked, 'checked', file)
            
            fileContent = open(file, 'rb').read()


            fileContent = zlib.decompress(fileContent)
            # print(item)
            try:
                fileContent = json.loads(fileContent)

                partsOfKey = file.split('/')[-1]
                partsOfKey = partsOfKey.split('#')

                city = partsOfKey[1]
                carID = partsOfKey[2]
                recordDate = partsOfKey[3]
                recordDate = recordDate.replace('.txt', '')
                # print(recordDate)
                # time.sleep(100000)
                if 1:
                # if 'Around' in platform and recordDate <  '2023-04-17':
                    # print(recordDate)
                    # time.sleep(100000)
                    recordCity = city
                    if recordCity != currentCity:
                        if currentCity != '':
                            print('saving for', currentCity)
                            writeCityRecords(currentCity,listData)
                            listData[platform] = {}
                        currentCity = recordCity

                    try:
                        v1 = listData[platform][city]
                    except: 
                        listData[platform][city] = {}

                    try:
                        v1 = listData[platform][city][carID]
                    except: 
                        listData[platform][city][carID] = {}

                    try:
                        v1 = listData[platform][city][carID][recordDate]
                    except: 
                        listData[platform][city][carID][recordDate] = {}


                    carData = {}
                    
                    # if fileContent['number_of_ratings'] > 0:
                    # fx = open('temp.txt','w')
                    # fx.write(json.dumps(fileContent))
                    # fx.close()
                    # print('Sleeping')
                    # time.sleep(10000)

                    if 'Turo' in platform:

                        carData['id'] = fileContent['vehicle']['id']
                        carData['guidelines'] = fileContent['guidelines']
                        carData['numberOfImages'] = len(fileContent['images'])

                        carData['avrgFuelEconomy'] = fileContent['basicCarDetails']['averageFuelEconomy']
                        carData['avrgCityFuelEconomy'] = fileContent['basicCarDetails']['cityFuelEconomy']
                        carData['avrgHighwayFuelEconomy'] = fileContent['basicCarDetails']['highwayFuelEconomy']
                        try:
                            carData['fuelType'] = fileContent['basicCarDetails']['fuelType']['value']
                        except:
                            carData['fuelType'] = 'NA'
                        carData['numberOfSeats'] = fileContent['basicCarDetails']['numberOfSeats']
                        carData['numberOfDoors'] = fileContent['basicCarDetails']['numberOfDoors']


                        carData['description'] = fileContent['description']

                        
                        carData['protectionPlan'] = fileContent['currentVehicleProtection']['displayName']

                        carData['image'] = fileContent['images'][0]['originalImageUrl']

                        carData['features'] = fileContent['badges']
                        carData['activeListing'] = fileContent['listingDeleted']

                        carData['ownerName'] = fileContent['owner']['name']
                        carData['ownerID'] = fileContent['owner']['id']
                        carData['ownerPic'] = fileContent['owner']['image']['originalImageUrl']
                        carData['ownerProfile'] = fileContent['owner']['url']


                        carData['madeFavoriteByHowMany'] = fileContent['numberOfFavorites']
                        carData['numberOfTrips'] = fileContent['numberOfRentals']
                        carData['numberOfTrips2'] = fileContent['tripCount']
                        carData['numberOfReviewes'] = fileContent['numberOfReviews']


                        carData['dailyPrice'] = str(fileContent['rate']['averageDailyPriceWithCurrency']['amount'])+fileContent['rate']['averageDailyPriceWithCurrency']['currencyCode']


                        carData['allowedDistance'] = fileContent['rate']['dailyDistance']['scalar']
                        carData['allowedMonthlyDistance'] = fileContent['rate']['monthlyDistance']['scalar']
                        carData['allowedWeeklyDistance'] = fileContent['rate']['weeklyDistance']['scalar']


                        carData['weeklyBookingDiscount'] = fileContent['rate']['weeklyDiscountPercentage']
                        carData['monthlyBookingDiscount'] = fileContent['rate']['monthlyDiscountPercentage']
                        
                        carData['overallRating'] = fileContent['ratings']['ratingToHundredth']
                        carData['cleanlinessRating'] = fileContent['ratings']['histogram']['buckets'][0]['averageRating']
                        carData['maintenanceRating'] = fileContent['ratings']['histogram']['buckets'][1]['averageRating']
                        carData['convenienceRating'] = fileContent['ratings']['histogram']['buckets'][3]['averageRating']
                        carData['communicationRating'] = fileContent['ratings']['histogram']['buckets'][2]['averageRating']
                        carData['accuracyRating'] = fileContent['ratings']['histogram']['buckets'][4]['averageRating']


                        carData['auotmaticTransmission'] = fileContent['vehicle']['automaticTransmission']
                        carData['color'] = fileContent['color']

                        carData['make'] = fileContent['vehicle']['make']
                        carData['model'] = fileContent['vehicle']['model']
                        carData['makeCountry'] = fileContent['vehicle']['marketCountry']
        
                        carData['listingCreated'] = fileContent['vehicle']['listingCreatedTime']
                        carData['numberPlate'] = fileContent['vehicle']['registration']['licensePlate']
                        carData['numberPlateRegistrationState'] = fileContent['vehicle']['registration']['state']
                        carData['vin'] = fileContent['vehicle']['vin']
                        carData['year'] = fileContent['vehicle']['year']
                        carData['type'] = fileContent['vehicle']['type']


                    elif 'GetAround' in platform:
                        # print('sleeping')
                        # time.sleep(1000)
                        carData['id'] = fileContent['car_id']
                        carData['guidelines'] = ''
                        if '-icon-pets-no' in json.dumps(fileContent):
                            carData['guidelines'] = 'no pet'
                        if 'No smoking i' in json.dumps(fileContent):
                            carData['guidelines'] += ', no smoking'
                        
                            
                        
                        carData['numberOfImages'] = len(fileContent['cdn_photo_urls'].split('http'))

                        try:
                            carData['bookingSchedule'] = fileContent['schedule']
                        except:
                            carData['bookingSchedule'] =  {}

                        carData['avrgFuelEconomy'] = -1
                        carData['avrgCityFuelEconomy'] = -1
                        carData['avrgHighwayFuelEconomy'] = -1


                        carData['fuelType'] = fileContent['fuel']

                        carData['numberOfSeats'] = -1
                        carData['numberOfDoors'] = -1
                        carData['isAlsoAnUberCar'] = fileContent['is_uber_car']

                        try:
                            carData['description'] = fileContent['information']
                        except:
                            carData['description'] = 'NA'
                        carData['features'] = fileContent['features']
                        carData['protectionPlan'] = -1

                        carData['image'] = fileContent['cdn_photo_url']


                        carData['activeListing'] = fileContent['status']

                        carData['ownerName'] = fileContent['owner_name']
                        carData['ownerID'] = fileContent['owner_id']
                        carData['ownerPic'] = fileContent['cdn_owner_photo']
                        carData['ownerProfile'] = -1
                        carData['ownerResponseTime'] = fileContent['response_time']
                        carData['ownerResponseRate'] = fileContent['response_rate']


                        carData['carPolicies'] = fileContent['policies']

                        carData['madeFavoriteByHowMany'] = -1
                        carData['numberOfTrips'] = fileContent['number_of_rentals']
                        carData['numberOfTrips2'] = fileContent['number_of_rentals']
                        carData['numberOfReviewes'] = fileContent['number_of_ratings']
                        # print(fileContent)
                        # time.sleep(1000)

                        carData['dailyPrice'] = str(round(float(fileContent['price_hourly'])*8,2))
                        # print(carData['dailyPrice'])
                        # time.sleep(1)

                        carData['allowedDistance'] = -1
                        carData['allowedMonthlyDistance'] = -1
                        carData['allowedWeeklyDistance'] = -1


                        carData['weeklyBookingDiscount'] = -1
                        carData['monthlyBookingDiscount'] = -1
                        
                        carData['overallRating'] = -1
                        carData['cleanlinessRating'] = -1
                        carData['maintenanceRating'] = -1
                        carData['convenienceRating'] = -1
                        carData['communicationRating'] = -1
                        carData['accuracyRating'] = -1

                        carData['auotmaticTransmission'] = fileContent['transmission']
                        carData['color'] = -1

                        carData['make'] = fileContent['make']
                        carData['model'] = fileContent['model']
                        carData['makeCountry'] = -1
        
                        carData['listingCreated'] = -1
                        carData['numberPlate'] = fileContent['license_plate']
                        carData['numberPlateRegistrationState'] = -1
                        carData['vin'] = -1
                        carData['year'] = fileContent['year']
                        carData['type'] = fileContent['type']

                    elif 'Europe' in platform:
                        # print('sleeping')
                        # time.sleep(1000)
                        carData['id'] = fileContent['data']['id']

                        carData['avrgFuelEconomy'] = -1
                        carData['avrgCityFuelEconomy'] = -1
                        carData['avrgHighwayFuelEconomy'] = -1

                        sectionNumber = -1
                        for i1 in range(1,len(fileContent['sections'])):
                            if fileContent['sections'][i1]['header'] == 'Technical features':
                                sectionNumber = i1 
                                break
                        if sectionNumber != -1:
                            carData['fuelType'] = fileContent['sections'][sectionNumber]['items'][3]['detail_text']

                            carData['numberOfSeats'] = fileContent['sections'][sectionNumber]['items'][1]['detail_text']
                            carData['Mileage'] = fileContent['sections'][sectionNumber]['items'][2]['detail_text']
                            carData['numberOfDoors'] = -1

                            carData['auotmaticTransmission'] = fileContent['sections'][sectionNumber]['items'][4]['detail_text']

                            carData['year'] = fileContent['sections'][sectionNumber]['items'][0]['detail_text']
                            
                            try:
                                carData['isAlsoAnUberCar'] = fileContent['is_uber_car']
                            except:
                                carData['isAlsoAnUberCar'] = 'NA'
                        sectionNumber = -1
                        for i1 in range(1,len(fileContent['sections'])):
                            if fileContent['sections'][i1]['header'] == 'Car description':
                                sectionNumber = i1 
                                break
                        if sectionNumber != -1:
                            # print(sectionNumber)
                            carData['description'] = fileContent['sections'][sectionNumber]['items'][0]['text']
                        
                        sectionNumber = -1
                        for i1 in range(1,len(fileContent['sections'])):
                            if fileContent['sections'][i1]['header'] == 'Options':
                                sectionNumber = i1 
                                break
                        if sectionNumber != -1:
                            carData['features'] = fileContent['sections'][sectionNumber]['items']
                        
                        sectionNumber = -1
                        for i1 in range(1,len(fileContent['sections'])):
                            if fileContent['sections'][i1]['header'] == "Insurance & assistance":
                                sectionNumber = i1 
                                break
                        if sectionNumber != -1:
                            carData['protectionPlan'] = fileContent['sections'][sectionNumber]['items'][0]['title']


                        try:
                            carData['image'] = fileContent['sections'][0]['items'][0]['photos'][0]['url']
                        except:
                            carData['image'] = 'NA'

                        try:
                            carData['activeListing'] = fileContent['status']
                        except:
                            carData['activeListing'] = 'NA'

                        sectionNumber = -1
                        for i1 in range(1,len(fileContent['sections'])):
                            if fileContent['sections'][i1]['header'] == "Owner":
                                sectionNumber = i1 
                                break
                        if sectionNumber != -1:
                            carData['ownerName'] = fileContent['sections'][sectionNumber]['items'][0]['public_name']
                            carData['ownerID'] = fileContent['sections'][sectionNumber]['items'][0]['id']
                            carData['ownerPic'] = fileContent['sections'][sectionNumber]['items'][0]['avatar']['thumb_url']
                            carData['ownerProfileCreatedAt'] = fileContent['sections'][sectionNumber]['items'][0]['created_at']

                        carData['ownerProfile'] = -1
                        try:
                            carData['ownerResponseTime'] = fileContent['sections'][0]['items'][2]['alert']['message']
                        except:
                            carData['ownerResponseTime'] =  'NA'
                        # carData['ownerResponseRate'] = -1
                        sectionNumber = -1
                        for i1 in range(1,len(fileContent['sections'])):
                            if fileContent['sections'][i1]['header'] == "Owner guidelines":
                                sectionNumber = i1 
                                break
                        if sectionNumber != -1:
                            carData['carPolicies'] = fileContent['sections'][sectionNumber]['items'][0]['text']

                        carData['madeFavoriteByHowMany'] = -1
                        
                        carData['numberOfTrips'] = fileContent['sections'][0]['items'][1]['stats']['ended_rentals_count']
                        
                        carData['numberOfReviewes'] = fileContent['sections'][0]['items'][1]['stats']['ratings_count']

                        carData['dailyPrice'] = fileContent['sections'][0]['items'][1]['display_total_price']

                        carData['allowedDistance'] = -1
                        carData['allowedMonthlyDistance'] = -1
                        carData['allowedWeeklyDistance'] = -1


                        carData['weeklyBookingDiscount'] = -1
                        carData['monthlyBookingDiscount'] = -1
                        
                        carData['overallRating'] = fileContent['sections'][0]['items'][1]['stats']['ratings_average']

                        carData['cleanlinessRating'] = -1
                        carData['maintenanceRating'] = -1
                        carData['convenienceRating'] = -1
                        carData['communicationRating'] = -1
                        carData['accuracyRating'] = -1

            
                        carData['color'] = -1
                        try:
                            carData['make'] = fileContent['sections'][0]['items'][1]['title'].split(' ')[0]
                        except:
                            carData['make'] = fileContent['sections'][0]['items'][1]['title']

                        try:
                            carData['model'] = fileContent['sections'][0]['items'][1]['title'].split(' ')[1]
                        except:
                            carData['model'] = fileContent['sections'][0]['items'][1]['description']

                        # carData['make'] = fileContent['sections'][0]['items'][1]['title']
                        # carData['model'] = fileContent['sections'][0]['items'][1]['description']
                        try:
                            carData['year'] = fileContent['sections'][0]['items'][1]['description'].split(' ')[0]
                        except:
                            carData['year'] = -1
                        carData['makeCountry'] = -1
        
                        carData['listingCreated'] = carData['ownerProfileCreatedAt']
                        carData['numberPlate'] = -1
                        carData['numberPlateRegistrationState'] = -1
                        carData['vin'] = -1
                        
                        carData['type'] = fileContent['data']['type']


                    # print(carData)
                    # fx = open('temp.txt','w')
                    # fx.write(json.dumps(carData))
                    # fx.close()
                    # time.sleep(1000)

                    listData[platform][city][carID][recordDate] = carData

                    # print(json.dumps(carData))
                    # print('Sleeping')
                    # time.sleep(1000)

            except Exception as e:
                print(e)
                # fx = open('temp.txt','w')
                # fx.write(json.dumps(fileContent))
                # fx.close()
                # time.sleep(1000)
                pass
    # # 
    # 
    # print('cars',len(totalCars.keys()))
    
    # if filesChecked > 5:
    #     break


    writeCityRecords(currentCity,listData)
    listData[platform] = {}