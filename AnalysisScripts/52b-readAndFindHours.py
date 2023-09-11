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

currencyConversion = {}
currencyConversion['USD'] = 1
currencyConversion['US'] = 1
currencyConversion['GBP'] = 1.21
currencyConversion['CAD'] = 0.73
currencyConversion['€'] = 1.06
currencyConversion['£'] = 1.21


citiesPriceAverage = {}


import orjson



dateToObj = {}

advanceDaysBookings = {}

platformService = {'GerAroundEurope': {'Barcelona': 1, 'Berlin': 1, 'Hamburg': 1, 'Liverpool': 1, 'London': 1, 'Lyon': 1, 'Madrid': 1, 'Paris': 1}, 'Turo': {'Las Vegas': 1, 'Liverpool': 1, 'London': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Ottawa': 1, 'Toronto': 1, 'Washington D.C.': 1}, 'GetAround': {'Las Vegas': 1, 'Los Angeles': 1, 'Miami': 1, 'New York City': 1, 'Washington D.C.': 1}}

# platformService['Turo'] = {}
# platformService['Turo']['Miami'] = 1

for platform in platformService:
    advanceDaysBookings[platform] = {}
    for city in platformService[platform]:
        fx = open('carDatesDict-'+platform+'-'+city+'.txt', 'r')
        carDatesDict = orjson.loads(fx.read())
        fx.close()

        advanceDaysBookings[platform][city] = []
        print(platform, city, len(carDatesDict[platform][city].keys()))
        for vid in carDatesDict[platform][city]:
            vehicleDates = list(carDatesDict[platform][city][vid].keys())
            vehicleDates.sort()
            # print('\t', vid, len(vehicleDates))
            vidTrips = {}
            for i in range(0, len(vehicleDates)):
                currentDate = vehicleDates[i]
                nextDates = carDatesDict[platform][city][vid][currentDate]
                nextDates.sort(key = lambda x: x[0])

                # print('\t\t\t days in day',len(nextDates))#, nextDates)
                # time.sleep(1)
                if 'Get' in platform or len(nextDates) < 60:
                    for j in range(1,len(nextDates)):
                        date1 = nextDates[j-1][0]
                        date2 = nextDates[j][0]
                        try:
                            d1 = dateToObj[date1]
                        except:
                            # print(date1)
                            d1 = datetime.strptime(date1, "%Y-%m-%d")
                            dateToObj[date1] = d1

                        try:
                            d2 = dateToObj[date2]
                        except:
                            d2 = datetime.strptime(date2, "%Y-%m-%d")
                            dateToObj[date2] = d2

                        delta = (d2 - d1).days
                        if delta > 1:
                            # print('\t\t\t', vid, d2,d1, delta)
                            # time.sleep(1)
                            try:
                                v10 = vidTrips[date1]
                            except:
                                vidTrips[date1] = 1
                                try:
                                    d0 = dateToObj[currentDate]
                                except:
                                    d0 = datetime.strptime(currentDate, "%Y-%m-%d")
                                    dateToObj[currentDate] = d0
                                lb = 470
                                if 'Ger' in platform:
                                    lb = 490
                                if 'Tur' in platform:
                                    lb = 410
                                lb = 0.3
                                hb = 1.7
                                if 'Arou' in platform:
                                    lb = 1
                                    hb= 1.9
                                if 'Get' in platform:
                                    lb = 1.2
                                    hb = 2
                                htba = abs((d1 - d0).days
                                # if htba < 40:
                                htba = round(htba,2)

                                # if htba < 0:
                                #     print(htba, currentDate,date1, d0, d1)
                                #     time.sleep(1000)
                                advanceDaysBookings[platform][city].append([htba,currentDate, date1])

                                # print(advanceDaysBookings)


    # break
fx = open('carAdvanceBookingHoursDict.txt','w')
fx.write(json.dumps(advanceDaysBookings))
fx.close()
