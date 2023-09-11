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
import pandas as pd

fx = open('platformCarCat.txt','r')
platformCat = json.loads(fx.read())
fx.close()


studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/APPNAME/'


totalTranslatedReviews = {}
carPrices = {}


citiesAndServices = {}
citiesAndServices['GerAroundEurope'] = ['Paris']
# citiesAndServices['GetAround'] = ['New York City']
# citiesAndServices['Turo'] = ['Los Angeles']

bestKeys= {}
bestKeys['GerAroundEurope'] = ['PAGES', '2022-10-03~2022-10-04', 1189, 3217]
bestKeys['GetAround'] = ['PAGES', '2022-12-15~2023-02-11~16:00', 953, 1938]
bestKeys['Turo'] = ['100:105', '2022-10-13~2022-10-20', 360, 19684]
#rating, rating count, trip count, reviews count, +ve review, -ve reviews, allowed miles, pictures, 
#unique reviews, rating count, time listed


genderPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14n-output/'

attribute = 'averageRating'

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'

detailsFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/'

datesDict = {}
attributeAndRankingDict = {}
possibleCats = ['Positive', 'Negative']
weight = 0.1

def readCars(content, platform):
    carsDict = {}
    # content = content[platform]
    # for country in content.keys():
    #     for city in content[country].keys():
    for date in content:
        for id in content[date]:
            try:
                val = content[date][id]['ownerPic']

                car = content[date][id]
                carsDict[id] = car
            except:
                pass
    return carsDict


df = pd.DataFrame()

carDataSample = {
    'tripsNumber':0,
    'averageRating':0,
    'ratingCount':0,
    'reviewCount':0,
    'posReviews':0,
    'negReviews':0,
    'male-female-Owner':0,
    'picturesCount':0,
    'category':0,
    'milage':0,
    'descWordCount':0,
    'pets':0,
    'smoking':0,
    'uniqueReviewers':0,
    'ownerTotalCars':0,
    'ownerTotalRating':0,
    'FuelType':0,
    'makeYear':0,
    'responseTime':0,
    'responseRate':0,
    'ownerTotalTrips':0,
    'favoriteCount':0,
    'allowedMiles':0,
    'listedSince':0,
    'ownerMemberSince':0,
    'featuresCount':0,
    'rank':0,
}
import ujson
import copy 



citiesAndServices = {}
citiesAndServices['GerAroundEurope'] = ['Paris']
# citiesAndServices['GetAround'] = ['New York City']
# citiesAndServices['Turo'] = ['Los Angeles']

for platform in citiesAndServices:
    totalRows = []
    
    mileageToIntDict = {}
    mileageCode = 1
    for city in citiesAndServices[platform]:
        cityName = city
        print(platform, cityName)
        attributeAndRankingDict[platform] = {}

        totalCats = {}
        for cat in possibleCats:
            totalCats[cat] = 1
        filePath = targetFolder+platform+'/'+city+'-content.txt'
        
        cityName = city
        
        cityCorrelation = []

        fx = open(filePath,'r')
        content = json.loads(fx.read())
        fx.close()


        genderPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/4a2-output/'


        fx = open(genderPath+platform+'-demographics.txt','r')
        ownerDemographics = ujson.loads(fx.read())
        ownerDemographics = ownerDemographics[platform]
        fx.close()
        reviewsDict = {}
        if 'GetAr' not in platform:
            genderPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14n-output/'
            fx = open(genderPath + platform+'-'+cityName+'.txt','r')
            reviewsDict = json.loads(fx.read())
            fx.close()

        fx =  open(detailsFolder+platform+'/'+city+'-content.txt','r')
        content2 = ujson.loads(fx.read())
        fx.close()

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

        if 1:
            
            attributeAndRankingDict[platform] = {}
            totalDates = list(content.keys())
            totalDates.sort()
            prevDate  = ''
            # print(len(totalDates))
            # time.sleep(1000000000)
            print('\tCame Here')
            for i in range(0, len(totalDates)):
                myDate = totalDates[i]
                recordDate = myDate

                recordDate = recordDate.split(')')[0]
                startDate = recordDate.split(' (')[0]
                try:
                    d0 = datesDict[startDate]
                except:
                    d0 = datetime.strptime(startDate, '%Y-%m-%d')
                    datesDict[startDate] = d0

                # d0 = datetime.strptime(startDate, '%Y-%m-%d')
                aheadDates = recordDate.split(' (')[1]
                aheadDates = aheadDates.split(' - - ')
                aheadDates[0] = aheadDates[0].split(' ')[0]
                aheadDates[1] = aheadDates[1].split(' ')[0]

                if platform == 'Turo':
                    try:
                        d1 = datesDict[aheadDates[0]]
                    except:
                        d1 = datetime.strptime(aheadDates[0], '%m-%d-%Y')
                        datesDict[aheadDates[0]] = d1
                else:
                    try:
                        d1 = datesDict[aheadDates[0]]
                    except:
                        d1 = datetime.strptime(aheadDates[0], '%Y-%m-%d')
                        datesDict[aheadDates[0]] = d1

                rankingKey = ':'
                if platform == 'Turo': 
                    rankingKey = myDate.split(' ')[5]+':'+myDate.split(' ')[6]
                elif platform == 'GetAround': 
                    rankingKey = myDate.split(' ')[2]+':'+myDate.split(' ')[6]
                elif platform == 'GerAroundEurope': 
                    rankingKey = myDate.split(' ')[5]+':'+myDate.split(' ')[5]

                rankingKey = rankingKey.replace('PriceHigh=','')
                rankingKey = rankingKey.replace('PriceLow=','')
                rankingKey = rankingKey.replace(')','')
                rankingKey = rankingKey.replace('PaheNumber=','')

                date1= str(d0).split(' ')[0]
                date2= str(d1).split(' ')[0]

                key2 = date1+'~'+date2

                if platform == 'GetAround': 
                    key2 = key2+'~'+rankingKey
                    rankingKey = 'PAGES'
                if platform == 'GerAroundEurope': 
                    # key2 = key2+'~'+rankingKey
                    rankingKey = 'PAGES'
                if rankingKey == bestKeys[platform][0] and key2 == bestKeys[platform][1]:
                    try:
                        val = attributeAndRankingDict[platform][rankingKey]
                    except:
                        attributeAndRankingDict[platform][rankingKey] = {}
                    try:
                        val = attributeAndRankingDict[platform][rankingKey][key2]
                    except:
                        attributeAndRankingDict[platform][rankingKey][key2] = {}
                    vc = 0
                    prevRank = -1
                    for id in content[myDate]:
                        carDataSampleTemp = copy.deepcopy(carDataSample)
                        try:
                            carObj = content[myDate][id]
                            dates = list(content2[id].keys())
                            dates.sort()
                            ind = int(len(dates)*0.15)
                            date2 = dates[ind]
                            date = dates[0]
                            
                            try:
                                carDataSampleTemp['tripCount'] = carObj['trips']
                            except:
                                ijk = 10
                            try:
                                carDataSampleTemp['averageRating'] = carObj['averageRating']
                            except:
                                ijk = 10
                            try:
                                carDataSampleTemp['ratingCount'] = carObj['ratingCount']
                            except:
                                ijk = 10
                            
                            try:
                                
                                carNew = content2[id][date2]
                                carDataSampleTemp['reviewCount'] = carNew['numberOfReviewes']
                            except:
                                ijk = 10

                            try:
                                positiveReviews = 1
                                negativeReviews = 0
                                carReviews = reviewsDict[id]
                                for reviewID in carReviews:
                                    review = carReviews[reviewID]
                                    if abs(review['polarity']['neg']) > 0:
                                        negativeReviews += 1
                                    else:
                                        positiveReviews += 1
                                carDataSampleTemp['posReviews'] = positiveReviews
                                carDataSampleTemp['negReviews'] = negativeReviews
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                ownerId = carNew['ownerID']
                                ownerName = carNew['ownerName']
                                ownerId = cityName+'~'+ownerName+'~'+str(ownerId)+'.jpg'
                                ownerId = ownerId.replace('/',' ')
                                userId = list(ownerDemographics[ownerId].keys())[0]
                                gender = ownerDemographics[ownerId][userId]['gender']
                                codeArr = ['Male', 'Female']
                                gender = codeArr.index(gender)+1
                                carDataSampleTemp['male-female-Owner'] = gender
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                carDataSampleTemp['picturesCount'] = carNew['numberOfImages']
                            except:
                                ijk = 10

                            try:
                                possibleCats = ['sedan', 'suv', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
                                cat = platformCat[platform][city][id][0]
                                picNumber = possibleCats.index(cat)
                                carDataSampleTemp['category'] = picNumber
                            except:
                                ijk = 10
                                
                            try:
                                carNew = content2[id][date]
                                mval = carNew['Mileage']
                                if type(mval) == str:
                                    
                                    try:
                                        val = mileageToIntDict[mval]
                                    except:
                                        mileageToIntDict[mval] = mileageCode
                                        mileageCode += 1
                                    mval = mileageToIntDict[mval]
                                carDataSampleTemp['milage'] = mval
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                picNumber = len(carNew['description'].split(' '))
                                carDataSampleTemp['descWordCount'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                picNumber = carNew['madeFavoriteByHowMany']
                                carDataSampleTemp['favoriteCount'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carReviews = reviewsDict[id]
                                totalReviewers = {}
                                for reviewID in carReviews:
                                    reviewerId = carReviews[reviewID]['autorId']
                                    totalReviewers[reviewerId] = 1
                                
                                picNumber = len(carReviews.keys()) - len(totalReviewers.keys())
                                carDataSampleTemp['uniqueReviewers'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carReviews = reviewsDict[id]
                                ownerID = carNew['ownerID']
                                ownerCars = len(content3[platform][city][str(ownerID)]['vehicles'].keys())
                                if ownerCars > 12:
                                    ownerCars  = 5
                                picNumber = ownerCars
                                carDataSampleTemp['ownerTotalCars'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carReviews = reviewsDict[id]
                                ownerId = str(carNew['ownerID'])
                                ownerObj = content4[ownerId]
                                dates = list(ownerObj.keys())
                                dates.sort()
                                date3 = dates[0]
                                listingCreated = ownerObj[date3]['averageRating']
                                picNumber = float(listingCreated)
                                carDataSampleTemp['ownerTotalRating'] = picNumber
                            except:
                                ijk = 10

                            try:
                                fuelDict = {}
                                fuelDict['pertrol'] = 2
                                fuelDict['diesel'] = 3
                                fuelDict['hybrid'] = 1
                                fuelDict['unleaded 95'] = 2
                                fuelDict['unleaded 98'] = 2
                                fuelDict['electric'] = 0
                                fuelDict['other'] = 3
                                fuelDict['lpg'] = 4
                                fuelDict['gasoline'] = 1
                                fuelDict['na'] = 5
                                fuelDict['regular'] = 2
                                fuelDict['premium'] = 1

                                carNew = content2[id][date]
                                features = carNew['fuelType']
                                features = features.lower()
                                picNumber = fuelDict[features]
                                carDataSampleTemp['FuelType'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carReviews = reviewsDict[id]
                                carNew = content2[id][date]
                                picNumber = int(carNew['year'])
                                carDataSampleTemp['makeYear'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                ownerId = str(carNew['ownerID'])
                                ownerObj = content4[ownerId]
                                dates = list(ownerObj.keys())
                                dates.sort()
                                date4 = dates[0]
                                picNumber = int(ownerObj[date4]['responseTime'])
                                carDataSampleTemp['responseTime'] = picNumber
                            except:
                                ijk = 10

                            try:
                                ownerId = str(carNew['ownerID'])
                                ownerObj = content4[ownerId]
                                dates = list(ownerObj.keys())
                                dates.sort()
                                date4 = dates[0]
                                picNumber = int(ownerObj[date4]['responseRate'])
                                carDataSampleTemp['responseRate'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                ownerId = str(carNew['ownerID'])
                                ownerObj = content4[ownerId]
                                dates = list(ownerObj.keys())
                                dates.sort()
                                date = dates[0]
                                listingCreated = ownerObj[date]['totalTrips']
                                if 'GerA' in platform:
                                    listingCreated  = listingCreated.replace('rentals', '')
                                picNumber = int(listingCreated)
                                carDataSampleTemp['ownerTotalTrips'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                features = carNew['guidelines']
                                features = features.lower()
                                # print(features)
                                # time.sleep(1000)
                                if 'pet' in features:
                                    picNumber = 0
                                else:
                                    picNumber  = 1
                                carDataSampleTemp['pets'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                features = carNew['guidelines']
                                features = features.lower()
                                # print(features)
                                # time.sleep(1000)
                                if 'smok' in features:
                                    picNumber = 0
                                else:
                                    picNumber  = 1
                                carDataSampleTemp['smoking'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                picNumber = int(carNew['allowedDistance'])
                                carDataSampleTemp['smoking'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                listingCreated = carNew['listingCreated']
                                # print(listingCreated)
                                if 'GerA' in platform:
                                    listingCreated = listingCreated.split('T')[0]
                                    d1 = datetime.strptime(listingCreated, '%Y-%m-%d')
                                elif 'Turo' in platform:
                                    listingCreated = int(str(listingCreated)[:10])
                                    d1=datetime.fromtimestamp(listingCreated)
                                d2 = datetime.strptime('2023/04/21', "%Y/%m/%d")
                                delta = d2 - d1
                                picNumber = delta.days
                                carDataSampleTemp['listedSince'] = picNumber
                            except:
                                ijk = 10


                            try:
                                carNew = content2[id][date]
                                ownerId = str(carNew['ownerID'])
                                ownerObj = content4[ownerId]
                                dates = list(ownerObj.keys())
                                dates.sort()
                                date = dates[0]
                                listingCreated = ownerObj[date]['listingsStarted']
                                if 'GerA' in platform:
                                    listingCreated = listingCreated.split('T')[0]
                                    d1 = datetime.strptime(listingCreated, '%m/%d/%Y')
                                elif 'Turo' in platform: 
                                    d1= datetime.strptime(listingCreated, "%m-%d-%Y")
                                d2 = datetime.strptime('2023/04/21', "%Y/%m/%d")
                                delta = d2 - d1
                                picNumber = delta.days
                                carDataSampleTemp['ownerMemberSince'] = picNumber
                            except:
                                ijk = 10

                            try:
                                carNew = content2[id][date]
                                features = carNew['features']
                                if 'Turo' in platform:
                                    features = len(features)
                                elif 'Get' in platform:
                                    features = len(features.split(','))
                                else:
                                    features = len(features)
                                picNumber = features
                                carDataSampleTemp['featuresCount'] = picNumber
                            except:
                                ijk = 10

                            carDataSampleTemp['rank'] = int((carObj['carRankInSearch']/(bestKeys[platform][2]*1))*100)
                            
                            rankVal = int(carDataSampleTemp['rank']/10)
                            carDataSampleTemp.pop('rank')
                            
                            carDataSampleTemp['rank'] = rankVal
                            # prevRank = carDataSampleTemp['rank']
                            totalRows.append(carDataSampleTemp)
                            # time.sleep(0.1)
                            # print(carDataSampleTemp)
                            # time.sleep(1000)
                            # print(carDataSampleTemp)
                            # if carDataSampleTemp['rank'] != prevRank:
                                # print(carDataSampleTemp['rank'], carObj['carRankInSearch'])
                        except:
                            pass

    break
print(len(totalRows[0].keys()))
df =  pd.DataFrame(totalRows)
totalRow = len(df.index)
df  = df.iloc[1: totalRow]
df.to_csv(platform+'totalData.csv')  
df.to_pickle(platform+'totalData.pkl')  # where to save it, usually as a .pkl

# df = pd.read_pickle(file_name)

import pandas as pd
  
# Initialize data to lists.
# data = [{'a': 1, 'b': 2, 'c': 3},
#         {'a': 10, 'b': 20, 'c': 30}]
  
# # Creates DataFrame.
# df = pd.DataFrame(data)
