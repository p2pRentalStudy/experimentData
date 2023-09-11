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
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



studiedApps = {}
# studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1




totalTranslatedReviews = {}
carPrices = {}

sentiment = SentimentIntensityAnalyzer()
targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14m-output/'


citiesAndServices = {}
citiesAndServices['Turo'] = ['Los Angeles', 'Liverpool', 'Las Vegas', 'London', 'New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']
# citiesAndServices['GerAroundEurope'] = ['Paris', 'Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid',  'London']


savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14n-output/'

for platform in citiesAndServices:
    
    for city in citiesAndServices[platform]:
        cityName = city
        print(platform, city)
        fx = open(targetFolder + platform+'-'+cityName+'.txt','r')
        reviewsDict = json.loads(fx.read())
        fx.close()

        for carID in reviewsDict.keys():
            for reviewID in reviewsDict[carID].keys():
                review = reviewsDict[carID][reviewID]
                # print(review)
                try:
                    reviewTextEnglish = review['translatedText']
                except:
                    reviewTextEnglish = review['reviewContent']
                if reviewTextEnglish == 'N/A':
                    reviewTextEnglish = review['reviewContent']


                review['polarity'] = {}

                if reviewTextEnglish is not None and len(reviewTextEnglish) > 3:
                    try:
                        polarity = sentiment.polarity_scores(reviewTextEnglish)
                    except:
                        polarity = {}

                    # print(reviewTextEnglish, polarity)
                    # time.sleep(1)
                    review['polarity'] = polarity
                reviewsDict[carID][reviewID] = review


        fx = open(savePath + platform+'-'+cityName+'.txt','w')
        fx.write(json.dumps(reviewsDict))
        fx.close()

                
