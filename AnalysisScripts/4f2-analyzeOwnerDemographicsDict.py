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
import gender_guesser.detector as gender



studiedApps = {}
# studiedApps['GetAround'] = 1
# studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1


ownerCountDict = {}
ownerCountDict['GetAround'] = 0
ownerCountDict['GerAroundEurope'] = 0
ownerCountDict['Turo'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/4a2-output/'

cityShort = {}
cityShort['Barcelona'] = 'BAR'
cityShort['Berlin'] = 'BER'
cityShort['Hamburg'] = 'HAM'
cityShort['Los Angeles'] = 'LAX'
cityShort['London'] = 'LDN'
cityShort['Liverpool'] = 'LPL'
cityShort['Las Vegas'] = 'LVX'
cityShort['Lyon'] = 'LYN'
cityShort['Madrid'] = 'MAD'
cityShort['Miami'] = 'MIA'
cityShort['New York City'] = 'NYC'
cityShort['Ottawa'] = 'OTW'
cityShort['Paris'] = 'PAR'
cityShort['Toronto'] = 'TRT'
cityShort['Washington D.C.'] = 'WDC'


cities = [
    'Barcelona', 
    'Berlin', 
    'Hamburg', 
    'Los Angeles',
    'London', 
    'Liverpool', 
    'Las Vegas', 
    'Lyon', 
    'Madrid',
    'Miami', 
    'New York City', 
    'Ottawa',  
    'Paris',  
    'Toronto',
    'Washington D.C.' ]


totalTranslatedReviews = {}
carPrices = {}

newOwnersDemographicsDict = {}


fx = open('newOwnerDemographics.txt','r')
newOwnersDemographicsDict = json.loads(fx.read())
fx.close()


fx = open('cityWiseDemographics.txt','r')
ownersDict = json.loads(fx.read())
fx.close()


x = np.arange(15)

age = []
male = []
female = []
raceCount = []
newCities = []
raceTitles = []

fa = []
ma = []
rind = 5
races = []
for i in range(0, len(x)):
    city = cities[i]

    ownersDict[city]['race'].sort(key=lambda x:x[0])
    ownersDict[city]['race'] = [ownersDict[city]['race'][2]]#, ownersDict[city]['race'][3], ownersDict[city]['race'][4]]
    print(city, ownersDict[city])#, type(ownersDict[city]['age']) )
    print(' ')
    
#     fa.append(ownersDict[city]['female'])
#     ma.append(ownersDict[city]['male'])
    # fa.append(ownersDict[city]['race'][rind][1]*ownersDict[city]['total']*0.01)
    # ma.append(ownersDict[city]['total'])
    # races = ownersDict[city]['race']

# print(np.average(fa))
# print(np.average(ma))
# print(races[rind][0], sum(fa)/sum(ma))
# 
# print(np.average(fa))
# print(np.average(ma))
