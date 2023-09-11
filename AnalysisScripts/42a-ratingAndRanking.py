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
citiesAndServices['GerAroundEurope'] = ['Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris', 'London']
citiesAndServices['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
citiesAndServices['Turo'] = ['Liverpool', 'Las Vegas', 'London', 'Los Angeles','New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']


np.seterr(all="ignore")


attribute = 'averageRating'

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'

detailsFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/'


datesDict = {}
attributeAndRankingDict = {}
import math
import ujson 

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

        if contentAttribute == 'ratingCount' and 'Turo' in platform:
            contentAttribute = 'trips'

        fx =  open(detailsFolder+platform+'/'+city+'-content.txt','r')
        content2 = json.loads(fx.read())
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
                            carObj = content[myDate][id]
                            if carObj[contentAttribute] is not None:
                                tempList.append((carObj['carRankInSearch'], carObj[contentAttribute]))
                    else:
                        break
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

                i = j 
                if i == prevI:
                    i += 1
                prevI = i
        
            else:
                # print( totalDates[i])
                # time.sleep(1)
                for id in content[myDate]:
                    carObj = content[myDate][id]
                    if carObj[contentAttribute] is not None:
                        tempList.append((carObj['carRankInSearch'], carObj[contentAttribute]))

                random.shuffle(tempList)
                attributeList = []
                rankList = []
                for k in range(0, len(tempList)):
                    attributeList.append(tempList[k][1])
                    rankList.append(tempList[k][0])
                pr = round(scipy.stats.spearmanr(attributeList, rankList)[0],2)
                # if 'GetAro' in platform:
                #     print(attributeList)
                #     print(rankList)
                #     print(pr)
                #     time.sleep(100000)
                if not math.isnan(pr):
                    cityCorrelation.append(pr)
                    cityCorrelation2.append(pr)
                i+=1

        print('\t\t\t', round(np.average(cityCorrelation),2))
        # break
    print('\t', attribute, round(np.average(cityCorrelation),2))
    # break
            

