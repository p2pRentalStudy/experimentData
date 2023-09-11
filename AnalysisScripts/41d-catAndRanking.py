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
# citiesAndServices['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
# citiesAndServices['Turo'] = ['Liverpool', 'Las Vegas', 'London', 'Los Angeles','New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']
# citiesAndServices['GerAroundEurope'] = ['Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris', 'London']


# citiesAndServices['GerAroundEurope'] = ['Paris']
# citiesAndServices['GetAround'] = ['New York City']
citiesAndServices['Turo'] = ['Los Angeles']

bestKeys= {}
bestKeys['GerAroundEurope'] = ['PAGES', '2022-10-03~2022-10-04', 1189, 3217]
bestKeys['GetAround'] = ['PAGES', '2022-12-15~2023-02-11~16:00', 953, 1938]
bestKeys['Turo'] = ['100:105', '2022-10-13~2022-10-20', 360, 19684]
#rating, rating count, trip count, reviews count, +ve review, -ve reviews, allowed miles, pictures, 
#unique reviews, rating count, time listed

attribute = 'averageRating'

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'

datesDict = {}
attributeAndRankingDict = {}
possibleCats = ['sedan', 'suv', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
weight = 0.1
for platform in citiesAndServices:
    
    for city in citiesAndServices[platform]:
        attributeAndRankingDict[platform] = {}

        totalCats = {}
        for cat in possibleCats:
            totalCats[cat] = 1
        filePath = targetFolder+platform+'/'+city+'-content.txt'
        
        cityName = city
        
        cityCorrelation = []
        if 1:
            fx = open(filePath,'r')
            content = json.loads(fx.read())
            fx.close()
            ratings=[]
            rankings=[]
            weight = 0.95
            while weight < 1:
                print(platform, cityName)
                attributeAndRankingDict[platform] = {}
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

                        # print(rankingKey, key2)
                        # time.sleep(1000000000)
                        vc = 0
                        
                        for id in content[myDate]:
                            vc += 1
                            carObj = content[myDate][id]
                            try:
                                cat = platformCat[platform][city][id]
                                attributeAndRankingDict[platform][rankingKey][key2][id] = {}
                                attributeAndRankingDict[platform][rankingKey][key2][id]['rating'] = cat[0]
                                
                                attributeAndRankingDict[platform][rankingKey][key2][id]['rank'] = carObj['carRankInSearch']

                                totalCats[cat[0]] += 1

                                # print(carID, carObj['carRankInSearch'], cat)
                            except Exception as e:
                                pass
                                # print(e)
                            

                        
                            
                myData = []
                for i in range(0,10):
                    myData.append([])
                for key1 in attributeAndRankingDict[platform]:
                    for key2 in attributeAndRankingDict[platform][key1]:
                        # totalLength = len(attributeAndRankingDict[platform][key1][key2].keys())
                        totalLength = 0
                        cc = 0
                        for id in attributeAndRankingDict[platform][key1][key2]:
                            totalLength = max(totalLength, attributeAndRankingDict[platform][key1][key2][id]['rank'])
                        totalLength +=1
                        # print(totalLength)
                        for id in attributeAndRankingDict[platform][key1][key2]:
                            cc += 1
                            carObj = attributeAndRankingDict[platform][key1][key2][id]
                            rowNumber = int(carObj['rank']/totalLength * 100)
                            rowNumber = rowNumber  - rowNumber%10
                            rowNumber = int(rowNumber/10)
                            if 1:#carObj['rating'] >-1:
                                myData[rowNumber].append(carObj['rating'])

                for i in range(0,10):
                    
                    print('\t',  i)
                    if len(myData[i]) > 0:
                        for j in range(0, len(possibleCats)):
                            cat = possibleCats[j]
                            # print('\t', cat, myData[i].count(cat), round(myData[i].count(cat)/totalCats[cat] ,2))
                            print('\t\t', cat, myData[i].count(cat), round(myData[i].count(cat)/len(myData[i]) ,2))
            
                weight += 0.1
    break
            

