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



attribute = 'averageRating'

for platform in studiedApps:
    
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
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
            ratings=[]
            rankings=[]

            totalDates = list(content.keys())
            totalDates.sort()
            prevDate  = ''
            for i in range(0, len(totalDates)):
                date = totalDates[i]
                firstDate = date.split(' ')[0]
                if prevDate == '':
                    prevDate = firstDate
                elif prevDate!=firstDate:
                    # print(date, len(rankings))
                    try:
                        cityCorrelation.append(pearsonr(rankings,ratings)[0])
                    except:
                        print('exception',len(rankings))
                        fx = open('temp.txt','w')
                        fx.write(json.dumps(ratings))
                        fx.close()
                        print('sleeping')
                        time.sleep(10000)
                    rankings = []
                    ratings = []
                    prevDate = firstDate

                for id in content[date]:
                    carObj = content[date][id]
                    if carObj['averageRating'] is not None:
                    # if str(carObj['averageRating']) != 'null':
                        # print(carObj['averageRating'])
                        ratings.append(carObj['averageRating'])
                        rankings.append(carObj['carRankInSearch'])
            print('\t', np.average(cityCorrelation))
            savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14-output/'+platform+'/'
            fx = open(savePath + platform+'-'+cityName+'-'+attribute+'.txt','w')
            fx.write(json.dumps(cityCorrelation))
            fx.close()
            # time.sleep(1000)