from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator
from scipy.stats import pearsonr   
import scipy.stats

studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1



targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/APPNAME/'


totalTranslatedReviews = {}
carPrices = {}


citiesAndServices = {}
# citiesAndServices['GerAroundEurope'] = ['Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris', 'London']
# citiesAndServices['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
# citiesAndServices['Turo'] = ['Liverpool', 'Las Vegas', 'London', 'Los Angeles','New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']


np.seterr(all="ignore")


attribute = 'averageRating'

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'

detailsFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/'


datesDict = {}
attributeAndRankingDict = {}
import math
import ujson 

def processID(id):
    carObj = content[myDate][id]
    try:
        contentAttribute = 'trips'
        # if carObj[contentAttribute] is not None:
        #     tempList.append((carObj['carRankInSearch'], carObj[contentAttribute]))


        #########################
        # contentAttribute = 'Description'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # picNumber = len(carNew['description'].split(' '))
        # tempList.append((carObj['carRankInSearch'], picNumber))
        #########################
        # contentAttribute = 'multiplicity'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerID = carNew['ownerID']
        # ownerCars = len(content3[platform][city][str(ownerID)]['vehicles'].keys())
        # if ownerCars > 12:
        #     ownerCars  = 5
        # picNumber = ownerCars
        # tempList.append((carObj['carRankInSearch'], picNumber))
        # #########################
        # contentAttribute = 'listedSince'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # listingCreated = carNew['listingCreated']
        # # print(listingCreated)
        # if 'GerA' in platform:
        #     listingCreated = listingCreated.split('T')[0]
        #     d1 = datetime.strptime(listingCreated, '%Y-%m-%d')
        # elif 'Turo' in platform:
        #     listingCreated = int(str(listingCreated)[:10])
        #     d1=datetime.fromtimestamp(listingCreated)
        # d2 = datetime.strptime('2023/04/21', "%Y/%m/%d")
        # # print(d1,d2)
        # delta = d2 - d1
        # picNumber = delta.days
        # tempList.append((carObj['carRankInSearch'], picNumber))
        #########################
        # contentAttribute = 'allowed miles'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # picNumber = int(carNew['allowedDistance'])
        # tempList.append((carObj['carRankInSearch'], picNumber))
        ##########################################
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # picNumber = int(carNew['year'])
        # print(picNumber)
        # time.sleep(10000)
        ###############################
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerId = carNew['ownerID']
        # ownerName = carNew['ownerName']
        # ownerId = cityName+'~'+ownerName+'~'+str(ownerId)+'.jpg'
        # ownerId = ownerId.replace('/',' ')
        # userId = list(ownerDemographics[ownerId].keys())[0]
        # gender = ownerDemographics[ownerId][userId]['gender']
        # codeArr = ['Male', 'Female']
        # picNumber = codeArr.index(gender)
        ######################
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # features = carNew['features']
        # if 'Turo' in platform:
        #     features = len(features)
        # elif 'Get' in platform:
        #     features = len(features.split(','))
        # else:
        #     features = len(features)
        # picNumber = features
        # tempList.append((carObj['carRankInSearch'], picNumber))
        ######################
        # contentAtrribute = 'pets'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # features = carNew['guidelines']
        # features = features.lower()
        # print(features)
        # time.sleep(1000)
        # if 'pet' in features:
        #     picNumber = 0
        # else:
        #     picNumber  = 1
        # tempList.append((carObj['carRankInSearch'], picNumber))
        ######################
        # contentAtrribute = 'smoking'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # features = carNew['guidelines']
        # features = features.lower()
        # if 'smok' in features:
        #     picNumber = 0
        # else:
        #     picNumber  = 1
        # tempList.append((carObj['carRankInSearch'], picNumber))
        ####################################
        # positiveReviews = 1
        # negativeReviews = 0
        # carReviews = reviewsDict[id]
        # for reviewID in carReviews:
        #     review = carReviews[reviewID]
        #     # print(review)
        #     # time.sleep(1000)
        #     if abs(review['polarity']['neg']) > 0:
        #         negativeReviews += 1
        #     else:
        #         positiveReviews += 1
        # picNumber = round(negativeReviews/positiveReviews,2)
        # tempList.append((carObj['carRankInSearch'], picNumber))
        ####################################
        # contentAtrribute = 'Repeated Reviewers'
        # carReviews = reviewsDict[id]
        # totalReviewers = {}
        # for reviewID in carReviews:
        #     reviewerId = carReviews[reviewID]['autorId']
        #     totalReviewers[reviewerId] = 1
        
        # picNumber = len(carReviews.keys()) - len(totalReviewers.keys())
        # tempList.append((carObj['carRankInSearch'], picNumber))
        #################################################
        # contentAttribute = 'Category'
        # possibleCats = ['sedan', 'suv', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
        # cat = platformCat[platform][city][id][0]
        # picNumber = possibleCats.index(cat)
        # tempList.append((carObj['carRankInSearch'], picNumber))
        #################################################
        # contentAttribute = 'Response Time'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerId = str(carNew['ownerID'])
        # ownerObj = content4[ownerId]
        # dates = list(ownerObj.keys())
        # dates.sort()
        # date = dates[0]
        # # print(ownerObj[date]['responseTime'])
        # # time.sleep(1000)
        # picNumber = int(ownerObj[date]['responseTime'])
        # if picNumber != -1:
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        # #################################################
        # contentAttribute = 'Response Rate'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerId = str(carNew['ownerID'])
        # ownerObj = content4[ownerId]
        # dates = list(ownerObj.keys())
        # dates.sort()
        # date = dates[0]
        # # print(ownerObj[date]['responseRate'])
        # # time.sleep(1000)
        # picNumber = int(ownerObj[date]['responseRate'])
        # if picNumber != -1:
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        # #################################################
        # contentAttribute = 'Verified Owner'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerId = str(carNew['ownerID'])
        # ownerObj = content4[ownerId]
        # dates = list(ownerObj.keys())
        # dates.sort()
        # date = dates[0]
        # # print(ownerObj[date]['responseRate'])
        # # time.sleep(1000)
        # picNumber = len(ownerObj[date]['verifications'])
        # if picNumber != -1:
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        # #################################################
        # contentAtrribute = 'Fuel Type'

        # fuelDict = {}
        # fuelDict['pertrol'] = 2
        # fuelDict['diesel'] = 3
        # fuelDict['hybrid'] = 1
        # fuelDict['unleaded 95'] = 2
        # fuelDict['unleaded 98'] = 2
        # fuelDict['electric'] = 0
        # fuelDict['other'] = 3
        # fuelDict['lpg'] = 4
        # fuelDict['gasoline'] = 1
        # fuelDict['na'] = 5
        # fuelDict['regular'] = 2
        # fuelDict['premium'] = 1

        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # features = carNew['fuelType']
        # features = features.lower()
        # picNumber = fuelDict[features]
        # tempList.append((carObj['carRankInSearch'], picNumber))
        ####################################
        # contentAttribute = 'Transmission Type'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # transmission = str(carNew['auotmaticTransmission'])
        
        # fuelDict = {}
        # fuelDict['transmission'] = 2
        # fuelDict['Manual'] = 2
        # fuelDict['Automatic'] = 1
        # fuelDict['automatic'] = 1
        # fuelDict['True'] = 1
        # fuelDict['manual'] = 2
        # fuelDict['False'] = 2
        # picNumber = int(fuelDict[transmission])
        # if picNumber != -1:
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        # #################################################
        # contentAttribute = 'Display Pic'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerId = carNew['ownerID']
        # ownerName = carNew['ownerName']
        # ownerId = cityName+'~'+ownerName+'~'+str(ownerId)+'.jpg'
        # ownerId = ownerId.replace('/',' ')
        # picNumber = len(ownerDemographics[ownerId].keys())
        # tempList.append((carObj['carRankInSearch'], picNumber))
        # ######################
        # contentAttribute = 'Car Colors'
        # fuelDict = {}
        # fuelDict['black'] = 1
        # fuelDict['white'] = 2
        # fuelDict['blue'] = 4
        # fuelDict['gray'] = 3
        # fuelDict['green'] = 5
        # fuelDict['yellow'] = 6
        # fuelDict['red'] = 7
        # fuelDict['cyan'] = 8
        # fuelDict['red'] = 7
        
        # picNumber = fuelDict[carColors[platform][city][id]]

        # tempList.append((carObj['carRankInSearch'], picNumber))
        ######################
        # contentAtrribute = 'fuel economy'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # picNumber = carNew['avrgFuelEconomy']
        # if picNumber is not None:
        #     picNumber = float(picNumber)
        #     # print(picNumber)
        #     # time.sleep(10000)
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        ####################################
        # contentAtrribute = 'favorite count'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # picNumber = carNew['madeFavoriteByHowMany']
        # if picNumber is not None:
        #     picNumber = int(picNumber)
        #     # print(picNumber)
        #     # time.sleep(10000)
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        # ####################################
        # contentAtrribute = 'Also Uber'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # picNumber = carNew['isAlsoAnUberCar']
        # if picNumber is not None:
        #     picNumber = int(picNumber)
        #     print(picNumber)
        #     time.sleep(1)
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        ####################################
        # contentAttribute = 'Owner Member Since'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerId = str(carNew['ownerID'])
        # ownerObj = content4[ownerId]
        # dates = list(ownerObj.keys())
        # dates.sort()
        # date = dates[0]
        # listingCreated = ownerObj[date]['listingsStarted']
        # if 'GerA' in platform:
        #     listingCreated = listingCreated.split('T')[0]
        #     d1 = datetime.strptime(listingCreated, '%m/%d/%Y')
        # elif 'Turo' in platform: 
        #     d1= datetime.strptime(listingCreated, "%m-%d-%Y")
        # d2 = datetime.strptime('2023/04/21', "%Y/%m/%d")
        # delta = d2 - d1
        # picNumber = delta.days
        # if picNumber != -1:
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        # #################################################
        # contentAttribute = 'Owner Average Rating '
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerId = str(carNew['ownerID'])
        # ownerObj = content4[ownerId]
        # dates = list(ownerObj.keys())
        # dates.sort()
        # date = dates[0]
        # # print(ownerObj[date]['responseRate'])
        # # time.sleep(1000)
        # listingCreated = ownerObj[date]['averageRating']
        # picNumber = float(listingCreated)
        # if picNumber != -1:
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        # #################################################
        # contentAttribute = 'Owner Total Trips'
        # dates = list(content2[id].keys())
        # dates.sort()
        # date = dates[0]
        # carNew = content2[id][date]
        # ownerId = str(carNew['ownerID'])
        # ownerObj = content4[ownerId]
        # dates = list(ownerObj.keys())
        # dates.sort()
        # date = dates[0]
        # listingCreated = ownerObj[date]['totalTrips']
        # if 'GerA' in platform:
        #     listingCreated  = listingCreated.replace('rentals', '')
        # picNumber = int(listingCreated)
        # if picNumber != -1:
        #     tempList.append((carObj['carRankInSearch'], picNumber))
        ################################################################
        contentAttribute = 'Owner Total Trips'
        dates = list(content2[id].keys())
        dates.sort()
        date = dates[0]
        carNew = content2[id][date]
        listingCreated = str(carNew['protectionPlan'])
        # print(listingCreated)
        picNumber = 2
        if 'Turo' in platform:
            listingCreated = listingCreated.replace('plan','')
        picNumber = int(listingCreated)
        if picNumber != -1:
            tempList.append((carObj['carRankInSearch'], picNumber))
        ################################################################
    except Exception as e:
        # if '1' not in str(e) and '2' not in str(e) and '3' not in str(e) and '4' not in str(e) and '5' not in str(e):
        #     print(e)
        #     time.sleep(1)
        pass

# citiesAndServices['GerAroundEurope'] = ['Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris', 'London']
# citiesAndServices['GetAround'] =  [ 'Miami', 'Las Vegas','New York City', 'Washington D.C.','Los Angeles']
citiesAndServices['Turo'] = ['Liverpool', 'Las Vegas', 'London', 'Los Angeles','New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']



fx = open('platformCarCat.txt','r')
platformCat = json.loads(fx.read())
fx.close()

# max cat combos

# import itertools
# possibleCats = ['sedan', 'suv', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
# print(list(itertools.permutations(possibleCats)))
# time.sleep(10000)

for platform in citiesAndServices:
    print(platform)
    cityCorrelation = []
    for city in citiesAndServices[platform]:
        cityCorrelation2 = []
        attributeAndRankingDict[platform] = {}

        filePath = targetFolder+platform+'/'+city+'-content.txt'
        
        cityName = city
        print('\t\t', cityName)

        fx = open(filePath,'r')
        content = ujson.loads(fx.read())
        fx.close()
        ratings=[]
        rankings=[]

        totalDates = list(content.keys())
        totalDates.sort()
        i = 0
        prevI = -1
        contentAttribute = 'averageRating'
        contentAttribute = 'ratingCount'
        contentAtrribute = 'numberOfReviewes'

        if contentAttribute == 'ratingCount' and 'Turo' in platform:
            contentAttribute = 'trips'

        fx =  open(detailsFolder+platform+'/'+city+'-content.txt','r')
        content2 = ujson.loads(fx.read())
        fx.close()

        genderPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/4a2-output/'


        fx = open(genderPath+platform+'-demographics.txt','r')
        ownerDemographics = ujson.loads(fx.read())
        ownerDemographics = ownerDemographics[platform]
        fx.close()
        reviewsDict = {}


        fx =  open('multiplicityDict.txt','r')
        content3 = json.loads(fx.read())
        fx.close()

        fx =  open('finalCarColors.txt','r')
        carColors = json.loads(fx.read())
        fx.close()

        content4 = {}
        if platform!= 'GetAround':
            fx =  open('/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/2-output/'+platform+'/'+city+'-content.txt','r')
            content4 = json.loads(fx.read())
            fx.close()
        
        if 'GetAr' not in platform:
            genderPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14n-output/'
            fx = open(genderPath + platform+'-'+cityName+'.txt','r')
            reviewsDict = json.loads(fx.read())
            fx.close()


        
        loopVar = len(totalDates)

        loopVar = 10000
        if 'GetAr' in platform:
            loopVar = 50000
        while i < loopVar:
            # print(i,len(totalDates))
            myDate = totalDates[i]
            f1p1 = myDate.split('PaheNumber=')[0]
            tempList = []
            if 'GerAr' in platform:
                for j in range(i, min(loopVar, i+300)):
                    myDate = totalDates[j]
                    f2p1 = myDate.split('PaheNumber=')[0]
                    
                    if f2p1 == f1p1:
                        # print(i, j, totalDates[i], totalDates[j], f1p1, f2p1)
                        # time.sleep(1)
                        for id in content[myDate]:
                            processID(id)
                    else:
                        break

                i = j 
                if i == prevI:
                    i += 1
                prevI = i
        
            else:
                # print( totalDates[i])
                # time.sleep(1)
                for id in content[myDate]:
                    processID(id)
                i+=1
            random.shuffle(tempList)
            attributeList = []
            rankList = []
            for k in range(0, len(tempList)):
                attributeList.append(tempList[k][1])
                rankList.append(tempList[k][0])
            pr = round(scipy.stats.spearmanr(attributeList, rankList)[0],2)
            # print('\n\n\n',i, pr)
            # time.sleep(1)
            if not math.isnan(pr):
                cityCorrelation.append(pr)
                cityCorrelation2.append(pr)
        print('\t\t\t', round(np.average(cityCorrelation),2))
        # break
    print('\t', contentAtrribute, round(np.average(cityCorrelation),2))
    # break
            

