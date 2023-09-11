from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


fx = open('carCatCleaned.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

print(len(catDict.keys()))
tempDict = {}
tempDict['ibiza~seat'] = ['Hatchback']
tempDict['c-elysée~citroen'] = ['Sedan']
tempDict['208~peugeot'] = ['Hatchback']
tempDict['formentor~cupra'] = ['Sedan']
tempDict['formentor~cupra'] = ['SUV','Coupe']
tempDict['c3~citroen'] = ['SUV']
tempDict['cee\'d~kia'] = ['Hatchback']
tempDict['aygo~toyota'] = ['Hatchback']
tempDict['corsa-e~opel'] = ['Hatchback']
tempDict['corsa~opel'] = ['Hatchback']
tempDict['micra~nissan'] = ['Hatchback']
tempDict['2~mazda'] = ['Hatchback']
tempDict['berlingo~citroen'] = ['SUV']
tempDict['clio~renault'] = ['Hatchback']
tempDict['punto~fiat'] = ['Hatchback']
tempDict['auris~toyota'] = ['Hatchback']
tempDict['kangoo~renault'] = ['Van/Minivan']
tempDict['1007~peugeot'] = ['Hatchback']
tempDict['4~renault'] = ['Hatchback']
tempDict['mii~seat'] = ['Hatchback']
tempDict['panda~fiat'] = ['Hatchback']
tempDict['207~peugeot'] = ['Hatchback']
tempDict['207+~peugeot'] = ['Hatchback']
tempDict['carens~kia'] = ['SUV']
tempDict['c4~citroen'] = ['SUV']
tempDict['insignia~opel'] = ['Hatchback']
tempDict['fabia~skoda'] = ['Hatchback']
tempDict['corsa~vauxhall'] = ['Hatchback']
tempDict['forfour~smart'] = ['Hatchback']
tempDict['zafira~opel'] = ['Van/Minivan']
tempDict['clase~mercedes'] = ['Sedan']
tempDict['ateca~seat'] = ['SUV']
tempDict['zoe~renault'] = ['Hatchback']
tempDict['508~peugeot'] = ['Sedan']
tempDict['asx~mitsubishi'] = ['SUV']
tempDict['ë-c4~citroen'] = ['SUV']
tempDict['crz~honda'] = ['Hatchback']
tempDict['iq~toyota'] = ['Hatchback']
tempDict['jazz~honda'] = ['Hatchback']
tempDict['caddy~volkswagen'] = ['Van/Minivan']
tempDict['ioniq~hyundai'] = ['Sedan']
tempDict['touran~volkswagen'] = ['Van/Minivan']
tempDict['c-klasse~mercedes'] = ['Hatchback']
tempDict['rekord~opel'] = ['Sedan']
tempDict['mondeo~ford'] = ['Hatchback']
tempDict['talisman~renault'] = ['Sedan']
tempDict['3er~bmw'] = ['Sedan']
tempDict['e-klasse~mercedes'] = ['Sedan']
tempDict['9-3~saab'] = ['Convertible', 'Sedan']
tempDict['octavia~skoda'] = ['Sedan']
tempDict['1er~bmw'] = ['Hatchback']
tempDict['a-klasse~mercedes'] = ['Hatchback']
tempDict['delta~oldsmobile'] = ['Sedan']
tempDict['up!~volkswagen'] = ['Hatchback']
tempDict['w123~mercedes'] = ['Sedan']
tempDict['ix35~hyundai'] = ['Hatchback']
tempDict['cla-klasse~mercedes'] = ['Sedan']
tempDict['5er~bmw'] = ['Sedan']
tempDict['sl-klasse~mercedes'] = ['Convertible', 'Sedan']
tempDict['2er~bmw'] = ['Sedan']
tempDict['b-klasse~mercedes'] = ['Van/Minivan']
tempDict['roomster~skoda'] = ['Van/Minivan']
tempDict['807~peugeot'] = ['Wagon']
tempDict['modus~renault'] = ['Hatchback']
tempDict['one~mini'] = ['Hatchback']
tempDict['t-cross~volkswagen'] = ['SUV']
tempDict['captiva~chevrolet'] = ['SUV']
tempDict['e-up~volkswagen'] = ['Hatchback']
tempDict['grand~ford'] = ['SUV']
tempDict['new~volkswagen'] = ['Hatchback']
tempDict['defender~land-rover'] = ['SUV']
tempDict['q30~infiniti'] = ['Hatchback']
tempDict['alhambra~seat'] = ['Van/Minivan']
tempDict['5008~peugeot'] = ['SUV']
tempDict['4er~bmw'] = ['Sedan']
tempDict['crossland~opel'] = ['Hatchback']
tempDict['sharan~volkswagen'] = ['Wagon']
tempDict['slk-klasse~mercedes'] = ['Convertible', 'Coupe']
tempDict['3~bmw'] = ['Sedan']
tempDict['c-class~mercedes'] = ['Sedan']
tempDict['e-class~mercedes'] = ['Sedan']
tempDict['kuga~ford'] = ['SUV']
tempDict['partner~peugeot'] = ['Van/Minivan']
tempDict['407~peugeot'] = ['Hatchback']
tempDict['série~bmw'] = ['Hatchback']
tempDict['3008~peugeot'] = ['SUV']
tempDict['e-208~peugeot'] = ['Hatchback']
tempDict['s-max~ford'] = ['Wagon']
tempDict['e-niro~kia'] = ['SUV']
tempDict['classe~mercedes'] = ['Sedan']
tempDict['espace~renault'] = ['Wagon']
tempDict['c8~citroen'] = ['Wagon']
tempDict['taigo~volkswagen'] = ['SUV']
tempDict['exeo~seat'] = ['Hatchback']
tempDict['qashqai+2~nissan'] = ['SUV']
tempDict['cx~citroen'] = ['Hatchback']
tempDict['2cv~citroen'] = ['Hatchback']
tempDict['107~peugeot'] = ['Hatchback']
tempDict['freemont~fiat'] = ['SUV']
tempDict['301~peugeot'] = ['SUV']
tempDict['c2~citroen'] = ['Hatchback']
tempDict['bluecar~bolloré'] = ['Hatchback']
tempDict['model~tesla'] = ['Sedan']
tempDict['altea~seat'] = ['Hatchback']
tempDict['c-max~ford'] = ['SUV']
tempDict['giulietta~alfa-romeo'] = ['Hatchback']
tempDict['grande~fiat'] = ['Hatchback']
tempDict['grande~fiat'] = ['Hatchback']
tempDict['transporter~volkswagen'] = ['Van/Minivan']
tempDict['4007~peugeot'] = ['SUV']
tempDict['307~peugeot'] = ['Hatchback']
tempDict['rcz~peugeot'] = ['Sedan']
tempDict['xceed~kia'] = ['SUV']
tempDict['rifter~peugeot'] = ['Wagon']
tempDict['alto~suzuki'] = ['Hatchback']
tempDict['tipo~fiat'] = ['Hatchback']
tempDict['austin~mini'] = ['Hatchback']
tempDict['"huevito"~fiat'] = ['Hatchback']
tempDict['bravo~fiat'] = ['Hatchback']
tempDict['santa~hyundai'] = ['SUV']
tempDict['kallista~panther'] = ['Convertible','Coupe']
tempDict['lacetti~chevrolet'] = ['Sedan']
tempDict['i40~hyundai'] = ['Hatchback']
tempDict['ix20~hyundai'] = ['Hatchback']
tempDict['rexton~ssangyong'] = ['SUV']
tempDict['ypsilon~lancia'] = ['Hatchback']
tempDict['transit~ford'] = ['Wagon']
tempDict['ka+~ford'] = ['Hatchback']
tempDict['fluence~renault'] = ['Hatchback']
tempDict['mito~alfa-romeo'] = ['Hatchback']
tempDict['600~seat'] = ['Hatchback']
tempDict['epica~chevrolet'] = ['Sedan']
tempDict['motors~tata'] = ['Hatchback']
tempDict['c-zero~citroen'] = ['Hatchback']
tempDict['adam~opel'] = ['Hatchback']
tempDict['tourneo~ford'] = ['Wagon']
tempDict['pixo~nissan'] = ['Hatchback']
tempDict['c5~citroen'] = ['SUV']
tempDict['jogger~dacia'] = ['SUV']
tempDict['206~peugeot'] = ['Hatchback']
tempDict['laguna~renault'] = ['Sedan']
tempDict['trafic~renault'] = ['Wagon']
tempDict['ds5~citroen'] = ['Hatchback']
tempDict['coccinelle~volkswagen'] = ['Convertible', 'Sedan']
tempDict['t-roc~volkswagen'] = ['SUV']
tempDict['e-2008~peugeot'] = ['SUV']
tempDict['147~alfa-romeo'] = ['Hatchback']
tempDict['scirocco~volkswagen'] = ['Hatchback']
tempDict['scirocco~volkswagen'] = ['Hatchback']
tempDict['chr~toyota'] = ['SUV']
tempDict['multipla~fiat'] = ['Van/Minivan']
tempDict['b-max~ford'] = ['Hatchback']
tempDict['id~citroen'] = ['Hatchback']
tempDict['traction~citroen'] = ['Sedan']
tempDict['koleos~renault'] = ['SUV']
tempDict['agila~opel'] = ['Hatchback']
tempDict['bipper~peugeot'] = ['Van/Minivan']
tempDict['e~honda'] = ['Hatchback']
tempDict['124~fiat'] = ['Convertible', 'Coupe']
tempDict['wind~renault'] = ['Convertible', 'Hatchback']
tempDict['spring~dacia'] = ['SUV']
tempDict['cuore~daihatsu'] = ['Hatchback']
tempDict['xsara~citroen'] = ['Sedan']
tempDict['arkana~renault'] = ['SUV', 'Hatchback']
tempDict['grand~renault'] = ['Van','Minivan']
tempDict['i20~hyundai'] = ['Hatchback']
tempDict['polo~volkswagen'] = ['Hatchback']
tempDict['sandero~dacia'] = ['SUV']
tempDict['serie~bmw'] = ['Sedan']
tempDict['picanto~kia'] = ['Hatchback']
tempDict['cabriolet~mini'] = ['Convertible', 'Hatchback']
tempDict['a1~audi'] = ['Hatchback']
tempDict['logan~dacia'] = ['Sedan']
tempDict['qashqai~nissan'] = ['SUV']
tempDict['superb~skoda'] = ['Sedan']
tempDict['scénic~renault'] = ['Hatchback']
tempDict['mx-5~mazda'] = ['Coupe']
tempDict['arona~seat'] = ['SUV']
tempDict['&~lynk'] = ['SUV']
tempDict['leon~seat'] = ['Hatchback']
tempDict['twingo~renault'] = ['Hatchback']
tempDict['2008~peugeot'] = ['SUV']
tempDict['ka~ford'] = ['Hatchback']
tempDict['meriva~opel'] = ['Hatchback']
tempDict['308~peugeot'] = ['SUV']
tempDict['spider~alfa-romeo'] = ['Convertible', 'Coupe']
tempDict['note~nissan'] = ['Hatchback']
tempDict['captur~renault'] = ['SUV']
tempDict['doblo~fiat'] = ['Hatchback']
tempDict['tivoli~ssangyong'] = ['SUV']
tempDict['mégane~renault'] = ['SUV']
tempDict['ignis~suzuki'] = ['Hatchback']
tempDict['karl~opel'] = ['Hatchback']
tempDict['astra~opel'] = ['Hatchback']
tempDict['citigo~skoda'] = ['Hatchback']
tempDict['3~mazda'] = ['Sedan']
tempDict['verso~toyota'] = ['Hatchback']
tempDict['stonic~kia'] = ['Hatchback']
tempDict['korando~ssangyong'] = ['SUV']
tempDict['land~toyota'] = ['SUV']
tempDict['c1~citroen'] = ['Hatchback']
tempDict['206+~peugeot'] = ['Hatchback']
tempDict['i30~hyundai'] = ['Hatchback']
tempDict['108~peugeot'] = ['Hatchback']
tempDict['pt~chrysler'] = ['Hatchback']
tempDict['dokker~dacia'] = ['Wagon']
tempDict['tarraco~seat'] = ['SUV']
tempDict['5~mazda'] = ['SUV']
tempDict['ds4~citroen'] = ['Hatchback']
tempDict['duster~dacia'] = ['SUV']
tempDict['rav~toyota'] = ['SUV']
tempDict['i10~hyundai'] = ['Hatchback']
tempDict['mokka~opel'] = ['SUV']
tempDict['kadjar~renault'] = ['SUV']
tempDict['lodgy~dacia'] = ['Van/Minivan']
tempDict['zafira~vauxhall'] = ['Hatchback']
tempDict['astra~vauxhall'] = ['Hatchback']
tempDict['grand~citroen'] = ['Wagon']
tempDict['4~bmw'] = ['Sedan']
tempDict['ds3~citroen'] = ['Hatchback']
tempDict['a-class~mercedes'] = ['Sedan']
tempDict['1~bmw'] = ['Hatchback']
tempDict['adam~vauxhall'] = ['Hatchback']
tempDict['kodiaq~skoda'] = ['SUV']
tempDict['gl-class~mercedes'] = ['SUV']
tempDict['discovery~land-rover'] = ['SUV']
tempDict['pulsar~nissan'] = ['Sedan']
tempDict['spider~abarth'] = ['Convertible', 'Coupe']
tempDict['range~land-rover'] = ['SUV']
tempDict['galaxy~ford'] = ['Hatchback']
tempDict['5~bmw'] = ['Sedan']
tempDict['rapid~skoda'] = ['Sedan']
tempDict['2~bmw'] = ['Sedan']
tempDict['595~abarth'] = ['Hatchback']
tempDict['q2~audi'] = ['SUV']
tempDict['mokka~vauxhall'] = ['Hatchback']
tempDict['id.3~volkswagen'] = ['Hatchback']
tempDict['cla-class~mercedes'] = ['Sedan']
tempDict['grandland~vauxhall'] = ['SUV']
tempDict['pro~kia'] = ['Sedan']
tempDict['giulia~alfa-romeo'] = ['Sedan']
tempDict['stelvio~alfa-romeo'] = ['SUV']
tempDict['6~mazda'] = ['Sedan']
tempDict['12~renault'] = ['Sedan']
tempDict['18~renault'] = ['Sedan']
tempDict['mini~rover'] = ['Hatchback']
tempDict['c-crosser~citroen'] = ['SUV']
tempDict['antara~opel'] = ['SUV']

tempDict['9-3x~saab'] = ['Van/Minivan']
tempDict['i3s~bmw'] = ['Hatchback']
tempDict['velar~land-rover'] = ['SUV']
tempDict['crossland~vauxhall'] = ['SUV']
tempDict['5~renault'] = ['Hatchback']
tempDict['kamiq~skoda'] = ['SUV']
tempDict['puma~ford'] = ['Hatchback']
tempDict['grand~chrysler'] = ['Van/Minivan']
tempDict['7~ds'] = ['SUV']
tempDict['156~alfa-romeo'] = ['Sedan']
tempDict['3~ds'] = ['SUV']
tempDict['citan~mercedes'] = ['Van/Minivan']
tempDict['ds7~citroen'] = ['SUV']
tempDict['space~mitsubishi'] = ['Hatchback']


import random


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
targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'


catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
found = {}
notFound = {}
totalTypes = {}

citiesAndServices = {}
serviceCityCarCat = {}

for service in studiedApps.keys():
    serviceCityCarCat[service] = {}

for city in cities:
    citiesAndServices[city] = {}
    for service in studiedApps.keys():
        citiesAndServices[city][service] = {}
        for cat in catCats:
            citiesAndServices[city][service][cat] = {}


for key in catDict.keys():
    # print(catDict[key])
    types = catDict[key]['type']
    for i in range(0,1):
        ctype = types[i]
        # print(ctype)
        # if ctype != 'SUV':
        ctype = ctype.lower()
        if ctype == 'car':
            ctype = 'sedan'
        if ctype == 'pickup':
            ctype = 'truck'
        if ctype == 'van' or ctype == 'minivan':
            ctype = 'van/minivan'
        if '_' in ctype:
            # time.sleep(1000)
            ctype = ctype[:-1]
        catDict[key]['type'] = [ctype]


# for key in catDict.keys():
#     # print(catDict[key])
#     types = catDict[key]['type']
#     for i in range(0,1):
#         ctype = types[i]
#         print(ctype)

for key in tempDict.keys():
    # print(catDict[key])
    types = tempDict[key]
    for i in range(0,1):
        ctype = types[i]
        # print(ctype)
        # if ctype != 'SUV':
        ctype = ctype.lower()
        if ctype == 'car':
            ctype = 'sedan'
        if ctype == 'pickup':
            ctype = 'truck'
        if ctype == 'van' or ctype == 'minivan':
            ctype = 'van/minivan'
        if '_' in ctype:
            # time.sleep(1000)
            ctype = ctype[:-1]
        tempDict[key] = [ctype]



totalModels = {}

moreThanOne = {}
totalVehicles = {}
for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()


    # print(filenames)
    nf = 0



    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName)
        try:
            val = serviceCityCarCat[platform]
        except:
            serviceCityCarCat[platform] = {}
        try:
            val = serviceCityCarCat[platform][cityName]
        except:
            serviceCityCarCat[platform][cityName] = {}
        #
        totalIDsPics = {}
        if 1:
        # try:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()

            carCount = 0
            # for country in content.keys():
            #     for city in content[country].keys():
            for id in content:
                dates = list(content[id].keys())
                dates.sort()
                for dateI in range(0,len(dates)):
                    date = dates[dateI]
                    car = content[id][date]
                    fuelType = car['fuelType']
                    year = car['year']
                    # print(car['make'], car['model'])
                    totalVehicles[platform+id] = 1
                    toBeSearchedKey = car['model'].lower()+'~'+car['make'].lower()
                    totalModels[toBeSearchedKey] = 1
                    try:
                        var = catDict[toBeSearchedKey]
                        # found[toBeSearchedKey] = catDict[toBeSearchedKey]
                        types = catDict[toBeSearchedKey]['type']

                        if len(types) > 1:
                            moreThanOne[platform+id] = 1

                        for type in types:
                            type = type.lower()

                            totalTypes[type] = 1
                        # print(catDict[toBeSearchedKey])
                        # time.sleep(1000)
                    except Exception as e:
                        # print('\t NOT FOUND',toBeSearchedKey, len(catDict.keys()), catDict['sportage~kia'], e)
                        # time.sleep(1000)
                        # time.sleep(0.1)
                        if 'Turo' in platform or 'GetAround' in platform:
                            ctype = car['type']
                            ctype = ctype.lower()
                            if ctype == 'pickup':
                                ctype  = 'truck'
                            # elif ctype == 'suv':
                            #     ctype  = 'SUV'
                            elif ctype == 'van':
                                ctype  = 'van/minivan'
                            elif ctype == 'minivan':
                                ctype  = 'van/minivan'
                            elif ctype == 'car':
                                ctype  = 'sedan'
                            elif ctype == 'convertible_':
                                ctype  = 'convertible'
                            catDict[toBeSearchedKey] = {'make':car['make'],'model':car['model'],'type':[ctype]}
                            # if ctype ==
                            totalTypes[ctype] = 1
                        else:
                            try:
                                catDict[toBeSearchedKey] = {'make':car['make'],'model':car['model'],'type':tempDict[toBeSearchedKey]}
                                # totalTypes[tempDict[toBeSearchedKey]] = 1
                                types = tempDict[toBeSearchedKey]

                                if len(types) > 1:
                                    moreThanOne[platform+id] = 1

                                for type in types:
                                    type = type.lower()
                                    totalTypes[type] = 1
                            except Exception as e:
                                print('\t NOT FOUND',nf, toBeSearchedKey, e)
                                # notFound[toBeSearchedKey] = 1
                                # found[toBeSearchedKey] = 1
                                nf += 1
                                catDict[toBeSearchedKey] = {'make':car['make'],'model':car['model'],'type':['TBR']}
                                # time.sleep(0.1)

                    cat = catDict[toBeSearchedKey]['type']
                    cat = cat[0]
                    # cat = cat.lower()
                    # if cat == 'minivan':
                    #     cat = 'van/minivan'
                    # elif cat == 'pickup':
                    #     cat = 'truck'
                    # elif cat == 'convertible':
                    #     cat = 'coupe'
                    # elif cat == 'van':
                    #     cat = 'van/minivan'


                    if cityName != 'New York':
                        citiesAndServices[cityName][platform][cat][id] = [toBeSearchedKey, fuelType, year]
                        serviceCityCarCat[platform][cityName][id] = [cat, toBeSearchedKey]

                    # print(cat)
                    # time.sleep(1000)
                    #
        # except Exception as e:
        #     print(e)

print(len(catDict.keys()),len(totalVehicles.keys()), len(moreThanOne.keys()))
print(len(totalTypes), totalTypes.keys())
# time.sleep(1000)
f = 0

# catsCount = {}
# for cat in catCats:
#     catsCount[cat] = 0


# cities = [
#     'Barcelona',
#     'Berlin',
#     'Hamburg',
#     'Los Angeles',
#     'London',
#     'Liverpool',
#     'Las Vegas',
#     'Lyon',
#     'Madrid',
#     'Miami',
#     'New York City',
#     'Ottawa',
#     'Paris',
#     'Toronto',
#     'Washington D.C.' ]

# for i in range(0,len(cities)):
#     city = cities[i]
#     print(city)
#     cityCars = 0
#     for service in citiesAndServices[city]:
#         print('\t', service)
#         for cat in citiesAndServices[city][service]:
#             cityCars += len(citiesAndServices[city][service][cat])
#             catsCount[cat] += len(citiesAndServices[city][service][cat])
#             # if len(citiesAndServices[city][service][cat]) > 0:
#             # print('\t\t', cat, len(citiesAndServices[city][service][cat]))

#     print('\t', cityCars, (round(cityCars/len(totalVehicles)*100,2),'\%'))


# for cat in catsCount:
#     print(cat, round(catsCount[cat]/len(totalVehicles)*100,2))





# nf = 0

# for key in found:
#     try:
#         if found[key] == -1:
#             nf += 1
#         else:
#             f += 1
#     except:
#         f += 1
# print(nf+f, f/(nf+f), nf/(nf+f))




fx = open('carCatCleaned.txt','w')
fx.write(json.dumps(catDict))
fx.close()
print('Came here')

fx = open('citiesAndServicesCats.txt','w')
fx.write(json.dumps(citiesAndServices))
fx.close()
print('Came here')


fx = open('platformCarCat.txt','w')
fx.write(json.dumps(serviceCityCarCat))
fx.close()
print('Came here')

# # break
