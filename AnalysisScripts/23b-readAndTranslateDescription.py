from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
import pycld2 as cld2
from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/vehicleCat-output/'
fx = open(loadPath + 'vehicleCategories.txt','r')
carIdToCat = json.loads(fx.read())
fx.close()

carCats = ['truck', 'coupe', 'hatchback', 'wagon', 'van/minivan', 'sedan', 'SUV']



totalMeta = {'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}, 'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}}

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'
analyzedData = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


import numpy as np
import matplotlib.pyplot as plt


loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/vehicleDesctiption.txt'
fx = open(loadPath,'r')
analyzedData = json.loads(fx.read())
fx.close()


totalCars = 0
otherLang = 0
normal = 0
translatedDescriptionDict = {}
carCount = 0
translated = 0
for platform in analyzedData:
    translatedDescriptionDict[platform] = {}
    print(platform)
    for city in analyzedData[platform]:
        print('\t', city)
        translatedDescriptionDict[platform][city] = {}
        totalCars += len(analyzedData[platform][city])
        for carId in analyzedData[platform][city]:
            carCount += 1
            description = analyzedData[platform][city][carId]
            detected_language = ()
            try:
                _, _, _, detected_language = cld2.detect(description,  returnVectors=True)
                # print(type(description), description, detected_language)
            except:
                ijk = 10
            add = 0
            detected_language = list(detected_language)
            if len(detected_language) > 0:
                for k in range(len(detected_language)):
                    detected_language[k] = list(detected_language[k])
                    detected_language[k].append(detected_language[k][1]-detected_language[k][0])
                detected_language.sort(key=lambda x:x[-1], reverse = True)
                if detected_language[0][3]!='en' and detected_language[0][3]!='un':
                    # print(carId, description)
                    # print('\t', detected_language)
                    # time.sleep(1000)
                    translatedText = ''
                    try:
                        otherLang += 1
                        translatedText = GoogleTranslator(source='auto', target='en').translate(description)
                        
                        # print(translatedText)
                        analyzedData[platform][city][carId] = translatedText
                        

                        translated +=1 
                        savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/'         
                        fx = open(savePath+'vehicleDesctiption.txt','w')
                        fx.write(json.dumps(analyzedData))
                        fx.close()
                        add = 1
                        print('\t\t', carCount, translated)
                        # print('\t saving ownerTrips dict')
                        # time.sleep(1000)
                    except:
                        ijk = 10
                    # print(translatedText)
                    # time.sleep(1000)
            # elif len(detected_language) > 0:
                else:
                    translatedText = description
                    normal += 1
                    add = 1
                if add == 1:
                    translatedDescriptionDict[platform][city][carId] = translatedText



print(totalCars, otherLang+normal,  otherLang, normal)

# time.sleep(1000)

savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/'         
fx = open(savePath+'translatedDescription.txt','w')
fx.write(json.dumps(translatedDescriptionDict))
fx.close()
print('\t saving ownerTrips dict')

