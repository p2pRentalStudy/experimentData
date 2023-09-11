from basicImports import *
import requests
import random
import string
from os import walk


studiedApps = {}
studiedApps['Turo'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/getCarReviews/carReviews'

totalFiles = []
for root, dirs, files in os.walk(targetFolder):
     for file in files:
        totalFiles.append(os.path.join(root, file))

def writeCityRecords(currentCity, listData):

    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/3-output/'+platform+'/'

    fx = open(savePath+currentCity+'-content.txt','w')
    fx.write(json.dumps(listData[platform][currentCity]))
    fx.close()

    return 0


print('Total Files', len(totalFiles))
# time.sleep(1000)
listData = {}
currentCity = ''
for platform in studiedApps:
    listData[platform] = {}
    res = [i for i in totalFiles if platform+'#' in i]
    newRes = {}
    for fn in res:
        if platform in fn:
            fn1 = fn.split('/')
            # print(fn1)
            # time.sleep(10000)
            
            fn1 = fn1[5:]
            # print(fn1)
            for part in fn1:
                if '.txt' in part:
                    newRes[part] = fn
            # newRes.append(fn)
    
    res=list(newRes.keys())
    res.sort()

    print(platform, len(res), 'files')
    # time.sleep(1000)
    filesChecked = 0
    
    if 1: 
        for file in res:
            file = newRes[file]
            if '.txt' in file:
                fileContent = open(file, 'rb').read()
                fileContent = zlib.decompress(fileContent)
                # print(item)
                fileContent = json.loads(fileContent)

                partsOfKey = file.split('/')[-1]
                partsOfKey = partsOfKey.split('#')

                city = partsOfKey[1]
                carID = partsOfKey[2]
                recordDate = partsOfKey[3]
                recordDate = recordDate.replace('.txt', '')
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
                
                
                if 'Turo' in platform:
                    
                    carData[carID] = []
                    for review in fileContent['list']:
                        tempReview = {}
                        # print(review)
                        tempReview['autorId'] = review['author']['id']
                        tempReview['authorImage'] = review['author']['image']['originalImageUrl']
                        tempReview['authorName'] = review['author']['name']
                        tempReview['authorProfile'] = review['author']['url']

                        tempReview['reviewDate'] = review['date']['localDate'] + ' '+ review['date']['localTime']
                        
                        tempReview['reviewRating'] = review['feedbackReply']

                        tempReview['reviewContent'] = review['review']

                        carData[carID].append(tempReview)
                
                elif 'Europe' in platform:
                    carData[carID] = []

                    for review in fileContent['reviews']:
                        tempReview = {}
                        # print(review)
                        tempReview['autorId'] = review['source']['id']

                        tempReview['autorProfileCreatedAt'] = review['source']['created_at']
                        tempReview['authorImage'] = review['source']['avatar']['thumb_url']
                        tempReview['authorName'] = review['source']['public_name']
                        tempReview['authorProfile'] = -1
                        tempReview['authorGivenNumberOfReviews'] = review['source']['stats']['ratings_count']
                        tempReview['authorBookedRentalCount'] = review['source']['stats']['driver_ended_rentals_count']

                        tempReview['reviewDate'] = review['created_at']
                        
                        tempReview['reviewRating'] = review['rating']

                        tempReview['reviewContent'] = review['comment']

                        carData[carID].append(tempReview)


                listData[platform][city][carID][recordDate] = carData


    writeCityRecords(currentCity,listData)
    listData[platform] = {}