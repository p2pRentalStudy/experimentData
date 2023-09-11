from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from datetime import date


fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

print(len(catDict.keys()))
dictKeys = list(catDict.keys())
dictKeys.sort()


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/23-output/vehicleTrips.txt'
fx = open(loadPath,'r')
tripsDict = json.loads(fx.read())
fx.close()


catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
totalTypes = []
from collections import Counter
maxCars = 5

myvehicles = []
vehicleCats = {}
modelUtil = {}
exptotalReviews = []


cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
countyAgainstCity = {}
countyAgainstCity['Barcelona'] = 'Spain'
countyAgainstCity['Berlin'] = 'Germany'
countyAgainstCity['Hamburg'] = 'Germany'
countyAgainstCity['Los Angeles'] = 'US'
countyAgainstCity['London'] = 'UK'
countyAgainstCity['Liverpool'] = 'UK'
countyAgainstCity['Las Vegas'] = 'US'
countyAgainstCity['Lyon'] = 'France'
countyAgainstCity['Madrid'] = 'Spain'
countyAgainstCity['Miami'] = 'US'
countyAgainstCity['New York City'] = 'US'
countyAgainstCity['Ottawa'] = 'Canada'
countyAgainstCity['Paris'] = 'France'
countyAgainstCity['Toronto'] = 'Canada'
countyAgainstCity['Washington D.C.'] = 'US'

# countriesHolidaysList = {'France': [('2022-01-01', "Jour de l'an"), ('2022-05-01', 'Fête du Travail'), ('2022-05-08', 'Armistice 1945'), ('2022-07-14', 'Fête nationale'), ('2022-11-11', 'Armistice 1918'), ('2022-04-18', 'Lundi de Pâques'), ('2022-06-06', 'Lundi de Pentecôte'), ('2022-05-26', 'Ascension'), ('2022-08-15', 'Assomption'), ('2022-11-01', 'Toussaint'), ('2022-12-25', 'Noël'), ('2023-01-01', "Jour de l'an"), ('2023-05-01', 'Fête du Travail'), ('2023-05-08', 'Armistice 1945'), ('2023-07-14', 'Fête nationale'), ('2023-11-11', 'Armistice 1918'), ('2023-04-10', 'Lundi de Pâques'), ('2023-05-29', 'Lundi de Pentecôte'), ('2023-05-18', 'Ascension'), ('2023-08-15', 'Assomption'), ('2023-11-01', 'Toussaint'), ('2023-12-25', 'Noël')], 'Germany': [('2022-01-01', 'Neujahr'), ('2022-04-15', 'Karfreitag'), ('2022-04-18', 'Ostermontag'), ('2022-05-01', 'Erster Mai'), ('2022-05-26', 'Christi Himmelfahrt'), ('2022-06-06', 'Pfingstmontag'), ('2022-10-03', 'Tag der Deutschen Einheit'), ('2022-12-25', 'Erster Weihnachtstag'), ('2022-12-26', 'Zweiter Weihnachtstag'), ('2023-01-01', 'Neujahr'), ('2023-04-07', 'Karfreitag'), ('2023-04-10', 'Ostermontag'), ('2023-05-01', 'Erster Mai'), ('2023-05-18', 'Christi Himmelfahrt'), ('2023-05-29', 'Pfingstmontag'), ('2023-10-03', 'Tag der Deutschen Einheit'), ('2023-12-25', 'Erster Weihnachtstag'), ('2023-12-26', 'Zweiter Weihnachtstag')], 'Spain': [('2022-01-01', 'Año nuevo'), ('2022-01-06', 'Epifanía del Señor'), ('2022-04-15', 'Viernes Santo'), ('2022-08-15', 'Asunción de la Virgen'), ('2022-10-12', 'Día de la Hispanidad'), ('2022-11-01', 'Todos los Santos'), ('2022-12-06', 'Día de la Constitución Española'), ('2022-12-08', 'La Inmaculada Concepción'), ('2022-12-26', 'Navidad (Trasladado)'), ('2023-01-02', 'Año nuevo (Trasladado)'), ('2023-01-06', 'Epifanía del Señor'), ('2023-04-06', 'Jueves Santo'), ('2023-04-07', 'Viernes Santo'), ('2023-05-01', 'Día del Trabajador'), ('2023-08-15', 'Asunción de la Virgen'), ('2023-10-12', 'Día de la Hispanidad'), ('2023-11-01', 'Todos los Santos'), ('2023-12-06', 'Día de la Constitución Española'), ('2023-12-08', 'La Inmaculada Concepción'), ('2023-12-25', 'Navidad')], 'US': [('2022-01-01', "New Year's Day"), ('2022-01-17', 'Martin Luther King Jr. Day'), ('2022-02-21', "Washington's Birthday"), ('2022-05-30', 'Memorial Day'), ('2022-06-19', 'Juneteenth National Independence Day'), ('2022-06-20', 'Juneteenth National Independence Day (Observed)'), ('2022-07-04', 'Independence Day'), ('2022-09-05', 'Labor Day'), ('2022-10-10', 'Columbus Day'), ('2022-11-11', 'Veterans Day'), ('2022-11-24', 'Thanksgiving'), ('2022-12-25', 'Christmas Day'), ('2022-12-26', 'Christmas Day (Observed)'), ('2023-01-01', "New Year's Day"), ('2023-01-02', "New Year's Day (Observed)"), ('2023-01-16', 'Martin Luther King Jr. Day'), ('2023-02-20', "Washington's Birthday"), ('2023-05-29', 'Memorial Day'), ('2023-06-19', 'Juneteenth National Independence Day'), ('2023-07-04', 'Independence Day'), ('2023-09-04', 'Labor Day'), ('2023-10-09', 'Columbus Day'), ('2023-11-11', 'Veterans Day'), ('2023-11-10', 'Veterans Day (Observed)'), ('2023-11-23', 'Thanksgiving'), ('2023-12-25', 'Christmas Day')], 'Canada': [('2022-01-01', "New Year's Day"), ('2022-01-03', "New Year's Day (Observed)"), ('2022-02-21', 'Family Day'), ('2022-04-15', 'Good Friday'), ('2022-04-18', 'Easter Monday'), ('2022-05-23', 'Victoria Day'), ('2022-07-01', 'Canada Day'), ('2022-08-01', 'Civic Holiday'), ('2022-09-05', 'Labour Day'), ('2022-10-10', 'Thanksgiving'), ('2022-12-25', 'Christmas Day'), ('2022-12-27', 'Christmas Day (Observed)'), ('2022-12-26', 'Boxing Day'), ('2023-01-01', "New Year's Day"), ('2023-01-02', "New Year's Day (Observed)"), ('2023-02-20', 'Family Day'), ('2023-04-07', 'Good Friday'), ('2023-04-10', 'Easter Monday'), ('2023-05-22', 'Victoria Day'), ('2023-07-01', 'Canada Day'), ('2023-07-03', 'Canada Day (Observed)'), ('2023-08-07', 'Civic Holiday'), ('2023-09-04', 'Labour Day'), ('2023-10-09', 'Thanksgiving'), ('2023-12-25', 'Christmas Day'), ('2023-12-26', 'Boxing Day')], 'UK': [('2022-06-03', 'Platinum Jubilee of Elizabeth II'), ('2022-09-19', 'State Funeral of Queen Elizabeth II'), ('2022-01-01', "New Year's Day"), ('2022-01-03', "New Year's Day (Observed)"), ('2022-01-02', 'New Year Holiday [Scotland]'), ('2022-01-04', 'New Year Holiday [Scotland] (Observed)'), ('2022-03-17', "St. Patrick's Day [Northern Ireland]"), ('2022-07-12', 'Battle of the Boyne [Northern Ireland]'), ('2022-08-01', 'Summer Bank Holiday [Scotland]'), ('2022-11-30', "St. Andrew's Day [Scotland]"), ('2022-12-25', 'Christmas Day'), ('2022-12-27', 'Christmas Day (Observed)'), ('2022-04-15', 'Good Friday'), ('2022-04-18', 'Easter Monday [England/Wales/Northern Ireland]'), ('2022-05-02', 'May Day'), ('2022-06-02', 'Spring Bank Holiday'), ('2022-08-29', 'Late Summer Bank Holiday [England/Wales/Northern Ireland]'), ('2022-12-26', 'Boxing Day'), ('2023-05-08', 'Coronation of Charles III'), ('2023-01-01', "New Year's Day"), ('2023-01-02', "New Year Holiday [Scotland], New Year's Day (Observed)"), ('2023-01-03', 'New Year Holiday [Scotland] (Observed)'), ('2023-03-17', "St. Patrick's Day [Northern Ireland]"), ('2023-07-12', 'Battle of the Boyne [Northern Ireland]'), ('2023-08-07', 'Summer Bank Holiday [Scotland]'), ('2023-11-30', "St. Andrew's Day [Scotland]"), ('2023-12-25', 'Christmas Day'), ('2023-04-07', 'Good Friday'), ('2023-04-10', 'Easter Monday [England/Wales/Northern Ireland]'), ('2023-05-01', 'May Day'), ('2023-05-29', 'Spring Bank Holiday'), ('2023-08-28', 'Late Summer Bank Holiday [England/Wales/Northern Ireland]'), ('2023-12-26', 'Boxing Day')]}

countriesHolidaysList = {
  'France': [
    ('2022-11-11',
    'Armistice 1918'),
    ('2022-11-01',
    'Toussaint'),
    ('2022-12-25',
    'Noël'),
    ('2023-01-01',
    "Jour de l'an"),
    ('2023-04-10',
    'Lundi de Pâques')
  ],
  'Germany': [
    ('2022-10-03',
    'Tag der Deutschen Einheit'),
    ('2022-12-25',
    'Erster Weihnachtstag'),
    ('2022-12-26',
    'Zweiter Weihnachtstag'),
    ('2023-01-01',
    "New Year's Day"),
    ('2023-01-02',
    "New Year's Day (Observed)"),
    ('2023-01-01',
    'Neujahr'),
    ('2023-04-07',
    'Karfreitag'),
    ('2023-04-10',
    'Ostermontag')
  ],
  'Spain': [
    ('2022-10-12',
    'Día de la Hispanidad'),
    ('2022-11-01',
    'Todos los Santos'),
    ('2022-12-06',
    'Día de la Constitución Española'),
    ('2022-12-08',
    'La Inmaculada Concepción'),
    ('2022-12-26',
    'Navidad (Trasladado)'),
    ('2023-01-01',
    "New Year's Day"),
    ('2023-01-02',
    "New Year's Day (Observed)"),
    ('2023-01-02',
    'Año nuevo (Trasladado)'),
    ('2023-01-06',
    'Epifanía del Señor'),
    ('2023-04-06',
    'Jueves Santo'),
    ('2023-04-07',
    'Viernes Santo')
  ],
  'US': [
    ('2022-10-10',
    'Columbus Day'),
    ('2022-11-11',
    'Veterans Day'),
    ('2022-11-24',
    'Thanksgiving'),
    ('2022-12-25',
    'Christmas Day'),
    ('2022-12-26',
    'Christmas Day (Observed)'),
    ('2023-01-01',
    "New Year's Day"),
    ('2023-01-02',
    "New Year's Day (Observed)"),
    ('2023-01-16',
    'Martin Luther King Jr. Day'),
    ('2023-02-20',
    "Washington's Birthday")
  ],
  'Canada': [
    ('2022-10-10',
    'Thanksgiving'),
    ('2022-12-25',
    'Christmas Day'),
    ('2022-12-27',
    'Christmas Day (Observed)'),
    ('2022-12-26',
    'Boxing Day'),
    ('2023-01-01',
    "New Year's Day"),
    ('2023-01-02',
    "New Year's Day (Observed)"),
    ('2023-02-20',
    'Family Day'),
    ('2023-04-07',
    'Good Friday'),
    ('2023-04-10',
    'Easter Monday')
  ],
  'UK': [
    ('2022-11-30',
    "St. Andrew's Day [Scotland]"),
    ('2022-12-25',
    'Christmas Day'),
    ('2022-12-27',
    'Christmas Day (Observed)'),
    ('2022-12-26',
    'Boxing Day'),
    ('2023-01-01',
    "New Year's Day"),
    ('2023-01-02',
    "New Year Holiday [Scotland], New Year's Day (Observed)"),
    ('2023-01-03',
    'New Year Holiday [Scotland] (Observed)'),
    ('2023-03-17',
    "St. Patrick's Day [Northern Ireland]"),
    ('2023-04-07',
    'Good Friday'),
    ('2023-04-10',
    'Easter Monday [England/Wales/Northern Ireland]')
  ]
}

def trimHolidays():
    minDate = '2022-09-28'
    maxDate = '2023-04-28'
    for city in cities:
        country = countyAgainstCity[city]
        holidays = countriesHolidaysList[country]
        newHolidays = []
        for item in holidays:
            if item[0] >= minDate and item[0] <= maxDate:
                newHolidays.append(item)
        countriesHolidaysList[country] = newHolidays

trimHolidays()

import copy
# print(countriesHolidaysList)
# time.sleep(1000)


studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

reviewRation = []
daysDelta = 14

totalBefore = []
totalAfter = []
for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    nf = 0


    print(platform)
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        if cityName != 'New York':
            cityBefore = []
            cityAfter = []
            print('\t', cityName)
            if 1:
                fx = open(tempFolder+fileName,'r')
                content = json.loads(fx.read())
                fx.close()
                cityList = []
                cityModelUtil = {}
                cityTotalReview = []
                for holiday in countriesHolidaysList[countyAgainstCity[cityName]]:
                    holidayBefore = []
                    holidayAfter = []
                    holidayDate = holiday[0]
                    holidayDate = datetime.strptime(holidayDate, "%Y-%m-%d")
                    for id in content:
                        vehicleid = platform+'~'+id
                        dates = list(content[id].keys())
                        dates.sort()
                        dates2 = dates[:]
                        for i in range(0,len(dates)):
                            dates[i] = dates[i].replace(' (2)', '')
                            dates[i] = datetime.strptime(dates[i], "%Y-%m-%d")
                        
                        #closestPrev
                        d1 = holidayDate+timedelta(days=-3)
                        #farthest prev
                        d2 = holidayDate+timedelta(days=-daysDelta-3)

                        #closestNext
                        d3 = copy.copy(holidayDate)
                        #farthest next
                        d4 = holidayDate+timedelta(days=daysDelta)
                        # print(id, d1,d2,d3,d4)
                        toBeCheckedDatesRange = [d1,d2,d3,d4]
                        # print(toBeCheckedDatesRange)
                        for i in range(0, len(toBeCheckedDatesRange)):
                            cloz_dict = {
                                abs(toBeCheckedDatesRange[i].timestamp() - date.timestamp()) : date
                                for date in dates}
                                # extracting minimum key using min()
                            toBeCheckedDatesRange[i] = cloz_dict[min(cloz_dict.keys())].date()


                        # holidayDate2 = holidayDate.date()

                        if  toBeCheckedDatesRange[0] != toBeCheckedDatesRange[1] and toBeCheckedDatesRange[0] < toBeCheckedDatesRange[2] and toBeCheckedDatesRange[1] < toBeCheckedDatesRange[2] and toBeCheckedDatesRange[3] > toBeCheckedDatesRange[2]:
                            car = content[id]

                            tripsBefore = car[str(toBeCheckedDatesRange[0])]['numberOfTrips'] - car[str(toBeCheckedDatesRange[1])]['numberOfTrips']

                            beforeDays = (toBeCheckedDatesRange[0] - toBeCheckedDatesRange[1]).days

                            tripsAfter = car[str(toBeCheckedDatesRange[3])]['numberOfTrips'] - car[str(toBeCheckedDatesRange[2])]['numberOfTrips']

                            afterDays = (toBeCheckedDatesRange[3] - toBeCheckedDatesRange[2]).days
                            holidayBefore.append(tripsBefore/beforeDays)
                            holidayAfter.append(tripsAfter/afterDays)
                            # if tripsBefore/beforeDays < tripsAfter/afterDays:
                            #     print('\t', id, holiday, tripsBefore/beforeDays, tripsAfter/afterDays) 
                    if len(holidayBefore) > 0 and len(holidayAfter) > 0:
                        print('\t\t\t', holiday, round(np.average(holidayBefore),3), round(np.average(holidayAfter),3))
                        cityBefore += holidayBefore
                        cityAfter += holidayAfter
            print('\t\t', round(np.average(cityBefore),3), round(np.average(cityAfter),3))
            totalBefore += cityBefore
            totalAfter += cityAfter

print('OVERALL')
print('\t', round(np.average(totalBefore),3), round(np.average(totalAfter),3))