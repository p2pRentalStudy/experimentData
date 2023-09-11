from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

print(len(catDict.keys()))




dictKeys = list(catDict.keys())
dictKeys.sort()

for key in dictKeys:
    if len(catDict[key]['type']) == 0:
        del catDict[key]
studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1


cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
# cities = {'Barcelona', 'Berlin', 'Hamburg', 'Liverpool', 'London', 'Lyon', 'Madrid', 'Paris', 'Las Vegas', 'Los Angeles', 'Miami','New York City', 'Ottawa', 'Toronto','Washington D.C.' }
# targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData//13-output/'+platform+'/'



catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
notFound = {}
totalTypes = {}


cityAverage = {}
for city in cities:
    cityAverage[city] = {}
    for cat in catCats:
        cityAverage[city][cat] = []

totalModels = {}

moreThanOne = {}
totalVehicles = {}


ownerVehicles = {}
for city in cities:
    ownerVehicles[city] = {}
    for service in studiedApps.keys():
        ownerVehicles[city][service] = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1
possibleCats = ['sedan', 'SUV', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
priceDict = {}

catDict = {}
for cat in catCats:
    catDict[cat] = []
currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


citiesPriceAverage = {}
platformAverage = {}

for platform in studiedApps:
    platformAverage[platform] = []
for city in cities:
    citiesPriceAverage[city] = []

totalPriceCDF = []

fx = open('platformCarCat.txt', 'r')
cityServiceCat = json.loads(fx.read())
fx.close()

# fx = open('carPricesDict.txt', 'r')
# carPricingDict = json.loads(fx.read())
# fx.close()
# print('calculating averages')

values = []



carPrices = {}

dateValues = {}

totalReqs = 0 
combos = {}
# for i in range(0,200):
#     for x in range(0, 24):
#         for j in range(i,min(i+30,200)):
#             for k in range(0,24):
#                 try:
#                     val = combos[str(j)+str(k)]
#                 except:
#                     combos[str(j)+str(k)] = 0
#                 combos[str(j)+str(k)] += 1
#                 totalReqs += 1
# avrgTotal = []
# for key in combos:
#     avrgTotal.append(combos[key])
# print(totalReqs*0.67, np.average(avrgTotal)*0.67)

# time.sleep(100000)
pricingDict = {}
from statistics import mode

#pre vehicle records 3209.094352423133, claimed = 2M
# per time stamp 28.770424924304738, claimed = 446

triploadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'  

for platform in studiedApps:
    npd = {}
    npd['dp'] = {}
    npd['ndp'] = {}
    for cat in catCats:
        npd['dp'][cat] = []
        npd['ndp'][cat] = []

    pricingDict[platform] = []
# if 1:
    tempFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/13c-output/'+platform+'/'
    listData = {}
    fx = open(triploadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()
    # tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    nfn = []
    for item in filenames:
        if platform in item:
            nfn.append(item)
    filenames = nfn
    totalCarTrips = {}
    diffPricesMain = []
    # print(filenames)
    for fileName in filenames:
        cityName = fileName.split('-')[1]
        cityName = cityName.replace('.txt', '')
        platform = fileName.split('-')[0]
        
        fx = open(tempFolder+fileName,'r')
        carPricingDict = json.loads(fx.read())
        # print(platform, cityName, len(analyzedData[platform][cityName].keys()))
        fx.close()
        # print()
        
        differingPrices2 = 0
        maxUpdate = 0
        for vehicleId in carPricingDict:
            vid = vehicleId.replace(platform,'')
            vid = vid.replace(cityName,'')
            vid = vid.replace('~','')

            vehiclePrice = carPricingDict[vehicleId]

            # print(vehicleId, vid)
            # time.sleep(1000)

        # for vehicleId in analyzedData[platform][cityName]:
           # vid = vehicleId
           # vehiclePrice = carPricingDict[cityName+'~'+platform+'~'+vehicleId]
            try:
            # if 1:
                x10 = analyzedData[platform][cityName][vid]
                differingPrices = []
                
                differingPrices = 0

                for i in range(1, len(vehiclePrice)):
                    if vehiclePrice[i-1]   != vehiclePrice[i] : 
                        differingPrices+=1
                # diffPricesMain.append(len(differingPrices)/len(carPricingDict[vehicle]))
                cat = 'sedan'
                tba = differingPrices*24
                try:
                    cat= cityServiceCat[platform][cityName][vid][0]
                except:
                    pass

                tbaCat = 'ndp'
                if tba > 200:# len(vehiclePrice)*0.01:
                    tbaCat = 'dp'
                if len(vehiclePrice) > 0:
                    npd[tbaCat][cat].append(np.average(vehiclePrice))
                
            except:
                pass
    selectedCats =  ['sedan', 'suv', 'hatchback']
    print(platform)
    for cati in range(0, len(selectedCats)):  
        cat = selectedCats[cati]
        for dpType in ['dp','ndp']: 
            totalCars = len(npd['ndp'][cat]) + len(npd['dp'][cat])
            print('\t', int(np.average(npd[dpType][cat])), '&', len(npd[dpType][cat])/totalCars,end=' &')
    print('\\\\')
