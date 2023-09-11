from basicImports import *
import requests
import random
import string
from os import walk
import requests # request img from web
import shutil # save img locally
from difflib import SequenceMatcher

import urllib.request


studiedApps = {}
studiedApps['Turo'] = 1
# studiedApps['GerAroundEurope'] = 1
# studiedApps['GetAround'] = 1

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

citiesAndServices = {}
citiesAndServices['Turo'] = ['Las Vegas', 'Liverpool', 'London', 'Los Angeles','New York City', 'Miami', 'Ottowa', 'Toronto', 'Washinton D.C']

#'Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.', 'London', 'Liverpool'
# citiesAndServices['Turo'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.', 'London', 'Liverpool']

citiesAndServices['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
citiesAndServices['GerAroundEurope'] = ['London','Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris']


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/'
overlapaverage = []
overlapIDs = {}
for city1 in citiesAndServices['Turo']:
    overlaps = 0
    for service in ['GetAround', 'GerAroundEurope']:
        for city2 in citiesAndServices[service]:
            if city1 == city2:
                totalTuroCars = {}
                fx = open(targetFolder+'Turo/'+city1+'-content.txt','r')
                f1Content = json.loads(fx.read())
                # print(f1Content.keys())
                # f1Content = f1Content['Turo'][city1]
                fx.close()
                fx = open(targetFolder+service+'/'+city2+'-content.txt','r')
                f2Content = json.loads(fx.read())
                # print(f1Content.keys())
                # f1Content = f1Content['Turo'][city1]
                # f2Content = f2Content[service][city1]
                fx.close()
                print('loaded cars of', city1, 'Turo, service')
                
                cid = 0
                
                for id in f2Content:
                    cid += 1
                    if cid % 10000 == 1:
                        print('\t Turo', cid, 'done')
                    for date in f2Content[id]:
                        # print('Turo', id ,date)
                        car = f2Content[id][date]

                        car['ownerName'] = car['ownerName'].lower()
                        car['make'] = car['make'].lower()
                        car['model'] = car['model'].lower()
            
                        totalTuroCars[id] = 1
                        for id2 in f1Content:
                            breakit = 0
                            for date2 in f1Content[id2]:
                                car2 = f1Content[id2][date2]
                                if car2['ownerName'] != '':
                                    car2['ownerName'] = car2['ownerName'].lower()
                                    car2['make'] = car2['make'].lower()
                                    car2['model'] = car2['model'].lower()

                                    similarityRatio = round(similar(car['ownerName'].split(' ')[0],car2['ownerName'].split(' ')[0]),2)

                                    similarityRatio2 = round(similar(car['model'],car2['model']),2)
                                    if similarityRatio > 0.9 and  car['make'] ==  car2['make'] and similarityRatio2 > 0.7:
                                        # totalTuroCars[car['ownerName']] = 
                                        overlaps +=1
                                        # print('\t',overlaps, id, 'Turo: ', car['ownerName'], car['make'], car['model'],'   ', service, car2['ownerName'],  similarityRatio, car2['make'], car2['model'])
                                        # time.sleep(1)
                                        breakit = 1
                                        break
                                break
                            if breakit == 1:
                                break
                        break
                print(city1, overlaps, len(f1Content.keys()) + len(f2Content.keys()), 'turo', len(f1Content.keys()), service, len(f2Content.keys()))    
#                 overlapaverage.append(round(overlaps/len(f1Content.keys())*100,4))            

# print(np.average(overlapaverage))