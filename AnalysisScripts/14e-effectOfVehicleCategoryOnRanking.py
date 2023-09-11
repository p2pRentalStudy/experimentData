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
loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/vehicleCat-output/'
fx = open(loadPath + 'vehicleCategories.txt','r')
carIdToCat = json.loads(fx.read())
fx.close()

# carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']
carCats = ['sedan', 'van/minivan', 'hatchback', 'wagon', 'truck', 'SUV', 'coupe']
import itertools
newCats = list(itertools.permutations(carCats))


import random

def checkCategories(newCats, index):
    for carCats in newCats:
        carCatsDict = {}
        for i in range(0, len(carCats)):
            carCatsDict[carCats[i]] = i

        totalTranslatedReviews = {}
        carPrices = {}
        attribute = 'vehicleCategory'
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
                            values = []
                            try:
                                cityCorrelation.append(pearsonr(rankings,ratings)[0])
                                break
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

                        for id in content[date]:
                            carObj = content[date][id]
                            try:
                                carCategory = carIdToCat[platform+'~'+id]
                                carCategory = carCatsDict[carCategory[0]]
        
                                ratings.append(carCategory)
                                rankings.append(carObj['carRankInSearch'])
                            except Exception as e:
                                # print(e)
                                pass

                    print('\t', np.average(cityCorrelation))
                    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14-output/'+platform+'/'
                    fx = open(savePath + platform+'-'+cityName+'-'+attribute+'-'+str(index)+'.txt','w')
                    fx.write(json.dumps(cityCorrelation))
                    fx.close()
                    index += 1
                    # time.sleep(1000)

carCats = []
for i in range(0, len(newCats)):
    if i%250 == 0:
        carCats.append(newCats[i])
newCats = carCats

print(len(newCats))

threads = []
for t in range(20):
    ll = int((t*5/100)*len(newCats))
    ul = int((((t+1)*5)/100)*len(newCats))
    subArray = newCats[ll : ul]
    print(ll, ul)
    thread = Thread(target = checkCategories, args = (subArray, ll,))
    threads.append(thread)
    

for m in range(0, len(threads)):
    threads[m].start()

for m in range(0, len(threads)):
    threads[m].join()
    
