from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


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

# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


fx = open('platformCarCat.txt','r')
platformCat = json.loads(fx.read())
fx.close()




studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

from basicImports import *
import requests
import random
import string
import fileinput


citiesAndServices = {}
# citiesAndServices['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
# citiesAndServices['Turo'] = ['Liverpool', 'Las Vegas', 'London', 'Los Angeles','New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']
citiesAndServices['GerAroundEurope'] = ['Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris', 'London']

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'


# for platform in citiesAndServices:
#     cities = citiesAndServices[platform]
#     for city in cities:
#         try:
#             var = rankDict[city]
#         except:
#             rankDict[city] = {}
#         try:
#             var = rankDict
#         except:
#             rankDict = {}


for platform in citiesAndServices:
    cities = citiesAndServices[platform]
    for city in cities:#cityShort.keys():
        rankDict = {}

        # try:
        if 1:
            totalCars = {}
            f1Content = {}
            
            filePath = targetFolder+platform+'/'+city+'-content.txt'
           
            fx = open(filePath)
            f1Content = json.loads(fx.read())
            fx.close()

            datesKeys = {}
            myKeys = list(f1Content.keys())
            myKeys.sort()
            print(platform, city)
            # print(filePath)
            print(len(f1Content.keys()))
            dc = 0
            # print(myKeys)
            # time.sleep(100000)
            for myDate in myKeys:
                dc += 1
                

                recordDate = myDate

                recordDate = recordDate.split(')')[0]
                startDate = recordDate.split(' (')[0]
                d0 = datetime.strptime(startDate, '%Y-%m-%d')
                aheadDates = recordDate.split(' (')[1]
                aheadDates = aheadDates.split(' - - ')
                aheadDates[0] = aheadDates[0].split(' ')[0]
                aheadDates[1] = aheadDates[1].split(' ')[0]

                if platform == 'Turo':
                    d1 = datetime.strptime(aheadDates[0], '%m-%d-%Y')
                else:
                    d1 = datetime.strptime(aheadDates[0], '%Y-%m-%d')

                dayDifference = d1-d0
                dayDifference = dayDifference.days

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

                key2 = date1+'~'+date2+'~'+str(dayDifference)

                if platform == 'GetAround': 
                    key2 = key2+'~'+rankingKey
                    rankingKey = 'PAGES'
                if platform == 'GerAroundEurope': 
                    # key2 = key2+'~'+rankingKey
                    rankingKey = 'PAGES'
                try:
                    val = rankDict[rankingKey]
                except:
                    rankDict[rankingKey] = {}
                try:
                    val = rankDict[rankingKey][key2]
                except:
                    rankDict[rankingKey][key2] = []

                for carID in f1Content[myDate].keys():
                    carObj = f1Content[myDate][carID]
                    try:
                        cat = platformCat[platform][city][carID]
                        # print(carID, carObj['carRankInSearch'], cat)
                    except:
                        cat = ['sedan', 'NDA']
                    rankDict[rankingKey][key2].append((carID, carObj['carRankInSearch'], myDate))
                    # time.sleep(1)

                # print(date1,date2, dayDifference, rankingKey)
                # turo price, getaround time, ga europe page number
                # time.sleep(1000)
                # for carID in f1Content[myDate].keys():
        
            if 1 or city == 'London':
                print('\t\t', dc)
        # except Exception as e:
        #     if 'such file or di' not in str(e):
        #         print('\t Exception!', e)
        #     # time.sleep(10000)
        #     pass
        fx = open('/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/40a-output/'+platform+'~'+city+'.txt','w')
        fx.write(json.dumps(rankDict))
        fx.close()
        # print('Came here')