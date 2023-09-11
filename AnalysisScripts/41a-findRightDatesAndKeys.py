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


studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/APPNAME/'


totalTranslatedReviews = {}
carPrices = {}


citiesAndServices = {}
# citiesAndServices['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
# citiesAndServices['Turo'] = ['Liverpool', 'Las Vegas', 'London', 'Los Angeles','New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']
# citiesAndServices['GerAroundEurope'] = ['Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris', 'London']


citiesAndServices['GerAroundEurope'] = ['Paris']
citiesAndServices['GetAround'] = ['New York City']
citiesAndServices['Turo'] = ['Los Angeles']

bestKeys= {}
bestKeys['GerAroundEurope'] = ['Paris']
bestKeys['GetAround'] = ['New York City']
bestKeys['Turo'] = ['Los Angeles']
#rating, rating count, trip count, reviews count, +ve review, -ve reviews, allowed miles, pictures, 


attribute = 'averageRating'

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'

attributeAndRankingDict = {}
datesDict = {}
for platform in citiesAndServices:
    
    totalCars = {}
    for city in citiesAndServices[platform]:
        attributeAndRankingDict[platform] = {}
        filePath = targetFolder+platform+'/'+city+'-content.txt'
        
        cityName = city
        print(platform, cityName)
        cityCorrelation = []

        if 1:
            fx = open(filePath,'r')
            content = json.loads(fx.read())
            fx.close()
            ratings=[]
            rankings=[]

            totalDates = list(content.keys())
            totalDates.sort()
            prevDate  = ''
            # print(len(totalDates))
            # time.sleep(1000000000)
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

                # dayDifference = d1-d0
                # dayDifference = dayDifference.days

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
                try:
                    val = attributeAndRankingDict[platform][rankingKey]
                except:
                    attributeAndRankingDict[platform][rankingKey] = {}
                try:
                    val = attributeAndRankingDict[platform][rankingKey][key2]
                except:
                    attributeAndRankingDict[platform][rankingKey][key2] = {}

                # print(rankingKey, key2)
                # time.sleep(1000000000)
                for id in content[myDate]:
                    carObj = content[myDate][id]
                    attributeAndRankingDict[platform][rankingKey][key2][id] = {}
                    totalCars[id] = 1
                
        mk1 = ''
        mk2 = ''
        mc = 0
        for key1 in attributeAndRankingDict[platform]:
            for key2 in attributeAndRankingDict[platform][key1]:
                count = len(attributeAndRankingDict[platform][key1][key2].keys())
                # print('\t', count, key1, key2)
                if mc < count:
                    mc = count
                    mk1 = key1
                    mk2 = key2
                    
        print('\t', mk1,mk2,mc, len(totalCars.keys()))
        # break


