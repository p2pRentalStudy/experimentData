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


studiedApps = {}
# studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/3-output/APPNAME/'


totalTranslatedReviews = {}
carPrices = {}

# import cld2
# from polyglot.detect import Detector

for platform in studiedApps:
    
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14m-output/'


    ttr = 0
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName)
        cars = {}
        reviews = {}
        fc = 0
        if fc > -1:
        # try:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            reviewsDict = {}
            
            for carID in content.keys():
                cars[carID] = 1
                reviewsDict[carID] = {}
                for date in content[carID].keys():
                    reviewsObj = content[carID][date][carID]
                    
                    for review in reviewsObj:
                        reviewText = review['reviewContent']
                        reviewID = str(review['autorId'])+'~'+str(review['reviewDate'])

                        try:
                            val = reviewsDict[carID][reviewID]
                        except:
                            if reviewText != '' and len(reviewText) > 10 and len(reviewText) < 10000:
                                translatedText = 'N/A'
                                doTranslate = 1
                                
                                if doTranslate == 1:
                                    try:
                                        translatedText = GoogleTranslator(source='auto', target='en').translate(reviewText)
                                    except:
                                        ijk = 10
                                else:
                                    translatedText = reviewText
                                review['translatedText'] = translatedText
                                ttr+= 1
                                if ttr % 1000 == 1:
                                    print('\t Translated ',ttr, 'reviews')
                            reviewsDict[carID][reviewID] = review

            print('\t', len(cars.keys()),  len(reviews.keys()),  len(reviews.keys())/len(cars.keys()))
            fx = open(savePath + platform+'-'+cityName+'.txt','w')
            fx.write(json.dumps(reviewsDict))
            fx.close()
        fc += 1


print(ttr)
            
