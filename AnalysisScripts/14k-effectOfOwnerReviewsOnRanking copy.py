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
# studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1

currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/APPNAME/'

targetFolder2 = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'

targetFolder3 = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/2-output/APPNAME/'

totalTranslatedReviews = {}
carPrices = {}
import datetime  


attribute = 'numberOfMakeYear'

for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    tempFolder2 = targetFolder2.replace('APPNAME',platform)
    tempFolder3 = targetFolder3.replace('APPNAME',platform)
    

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName, attribute)
        
        cityCorrelation = []
        if 1:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()

            fx = open(tempFolder3+fileName,'r')
            content3 = json.loads(fx.read())
            content3 = content3[platform][cityName]
            fx.close()
            ownerDict = {}
            # print(content3.keys())
            # time.sleep(10000)
            for id in content3:
                try:
                    val = ownerDict[id]
                except:
                    ownerDict[id] = {}
                for date in content3[id]:
                    # print(id, content3[id][date].keys())
                    ownerDict[id] = content3[id][date]['averageRating']
                    # time.sleep(10000)
                    # break
                # ownerDict[ownerID][id] = 1

            content3 = {}
            fx = open(tempFolder2+fileName,'r')
            content2 = json.loads(fx.read())
            fx.close()

            ratings=[]
            rankings=[]

            totalDates = list(content.keys())
            totalDates.sort()
            prevDate  = ''
            for i in range(0, len(totalDates)):
                
                date = totalDates[i]
                firstDate = date.split(' ')[0]
                
                d1 = datetime.datetime.strptime(firstDate, '%Y-%m-%d').date()
                if prevDate == '':
                    prevDate = firstDate
                elif prevDate!=firstDate:
                    # print(date, len(rankings))
                    try:
                        cityCorrelation.append(pearsonr(rankings,ratings)[0])
                    except Exception as e:
                        print('exception',e, len(rankings))
                        fx = open('temp.txt','w')
                        fx.write(json.dumps(ratings))
                        fx.close()
                        print('sleeping')
                        time.sleep(10000)
                    rankings = []
                    ratings = []
                    prevDate = firstDate
                    if i > 5:
                        break

                for id in content[date]:
                    carObj = content[date][id]
                    checkKey = 'ownerID'

                   
                    try:
                        nextKeys = list(content2[id].keys())
                        carObj2 = content2[id][nextKeys[0]]

                        ownerId = str(carObj2[checkKey])
                        
                        # print(ownerId, ownerDict[ownerId])#, )
                        # time.sleep(1000)
                        bookingPrice = float(ownerDict[ownerId])#len(ownerDict[carObj2[checkKey]].keys())
                    
                        # print(id, bookingPrice)
                        # time.sleep(10000)
                        ratings.append(bookingPrice)
                        rankings.append(carObj['carRankInSearch'])
                    except Exception as e:
                        # print(e)
                        pass


            print('\t', np.average(cityCorrelation))
            savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14-output/'+platform+'/'
            fx = open(savePath + platform+'-'+cityName+'-'+attribute+'.txt','w')
            fx.write(json.dumps(cityCorrelation))
            fx.close()
            # time.sleep(1000)