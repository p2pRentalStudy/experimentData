from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date

import ast


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES


fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

print('totalVehicleModels', len(catDict.keys()))




dictKeys = list(catDict.keys())
dictKeys.sort()

for key in dictKeys:
    if len(catDict[key]['type']) == 0:
        del catDict[key]


cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/18-output/APPNAME/'


catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
notFound = {}
totalTypes = {}


totalModels = {}

moreThanOne = {}
totalVehicles = {}


possibleCats = ['sedan', 'SUV', 'hatchback', 'van/minivan', 'coupe', 'truck', 'wagon']
priceDict = {}
currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21
vehiclePrices = {}

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

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))

cancellationRateDict = {}
cancelledDict = {}

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

for platform in studiedApps:
    cancellationRateDict[platform] = []
    print(platform)
    # time.sleep(100000)
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    cancelledDict[platform] = {}
    # print(filenames, tempFolder)
    # time.sle/ep(100000)
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        
        # if 'Liver' in cityName:
        if 1:
            print('\t', cityName)
            fx = open(tempFolder+fileName,'r')
            bookingDict = json.loads(fx.read())
            fx.close()
            # print('\t\tloaded')
            # # bookingDict = ast.literal_eval(bookingDict)
            # time.sleep(100000)
            # for cityName in bookingDict:
            if 1: 
                cancelledDict[platform][cityName] = {}
                cancelledDict[platform][cityName]['cancelledTrips'] = []
                cancelledDict[platform][cityName]['totalTrips'] = []

                content = bookingDict
                ccount = 0
                for vehicleId in content:
                    ccount+=1 
                    if ccount % 100 == 0:
                        print(ccount, 'done')
                    bookingDates = list(content[vehicleId].keys())
                    bookingDates.sort()
                    minTrips = 10000000
                    maxTrips = 0

                    # dcDatesCollecton = {}
                    # for key in bookingDates:
                    #     for d2 in content[vehicleId][key]:


                    cancelCount = 0
                    for i in range(10, len(bookingDates)):
                        
                        
                        currentBookingDate = bookingDates[i]

                        availabilityDates = content[vehicleId][currentBookingDate]
                        # availabilityDates.sort()
                        

                        # if len(availabilityDates) > 40:
                        #     print(vehicleId, currentBookingDate, availabilityDates)
                            
                        #     time.sleep(100000)
                        # print(vehicleId, len(availabilityDates), currentBookingDate)
                        # time.sleep(100000)

                        # availabilityDates = (set(availabilityDates))
                        # print('\t', len(availabilityDates))
                        availabilityDates.sort(key=lambda x:x[1])
                        for j in range(1,len(availabilityDates)):
                            # print(currentBookingDate, availabilityDates[j], availabilityDates[j-1])
                            minTrips = min(minTrips,availabilityDates[j][1],minTrips)
                            minTrips = min(minTrips,availabilityDates[j-1][1],minTrips)

                            maxTrips = max(maxTrips,availabilityDates[j][1],minTrips)
                            maxTrips = max(maxTrips,availabilityDates[j-1][1],minTrips)

                            d0 = datetime.strptime(availabilityDates[j-1][0], '%Y-%m-%d')
                            d1 = datetime.strptime(availabilityDates[j][0], '%Y-%m-%d')

                            dayDifference = d1-d0
                            dayDifference = str(dayDifference)
                            dayDifference = dayDifference.split(' ')[0]

                            if dayDifference != '1' and ':' not in dayDifference:
                                # print(dayDifference, vehicleId, currentBookingDate, availabilityDates)
                                if dayDifference < '3':
                                    cancelledDict[platform][cityName]['cancelledTrips'].append((cityName, dayDifference, vehicleId, currentBookingDate, availabilityDates))
                                    # time.sleep(100000)
                                # cancelCount > 10:
                                # break
                    vehicleTotalTrips = maxTrips - minTrips
                    if vehicleTotalTrips>-1:
                        cancelledDict[platform][cityName]['totalTrips'].append(vehicleTotalTrips)
                
                # print('\t', len(cancelledDict[platform][cityName]['totalTrips']), len(cancelledDict[platform][cityName]['cancelledTrips'])/100, sum(cancelledDict[platform][cityName]['totalTrips']))
                # time.sleep(1000)
                
                ttrips = len(cancelledDict[platform][cityName]['totalTrips'])

                ctrips = len(cancelledDict[platform][cityName]['cancelledTrips'])/100

                cratio = round((ctrips/ttrips)*100,2)
                cancellationRateDict[platform].append((cityShort[cityName], ttrips, cratio))



# for platforms in cancellationRateDict:
#     print(platform)
    paverage = []
    cancellationRateDict[platform].sort(key=lambda x:x[2])
    for item in cancellationRateDict[platform]:
        print('\t &', item[0], '&', item[1], '&', str(item[2])+'\\%')
        paverage.append(item[2])
    # for i in range(0, len(cancellationRateDict[platform])):
    #     cancellationRateDict[platform][i].append(np.average(paverage))
    
    print('\t', np.average(paverage))

savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/18-output/'         
fx = open(savePath+'cancellationDict.txt','w')
fx.write(json.dumps(cancellationRateDict))
fx.close()
print('\t saving cancellation dict for', platform)