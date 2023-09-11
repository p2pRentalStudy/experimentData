from basicImports import *
import requests
import random
import string
from os import walk
import requests # request img from web
import shutil # save img locally

import urllib.request


studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'

def readCars(content, platform):
    carsDict = {}
    # content = content[platform]
    # for country in content.keys():
    #     for city in content[country].keys():
    for date in content:
        for id in content[date]:
            try:
                val = content[date][id]['ownerPic']

                car = content[date][id]
                carsDict[id] = car
            except:
                pass
    return carsDict

totalOwnersDict = {}


fx = open('platformCarCat.txt', 'r')
catDict = json.loads(fx.read())
fx.close()

loadPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/44a-output/'  

cars = 0

for platform in studiedApps:
    listData = {}
    fx = open(loadPath +platform+'-trips.txt', 'r')
    analyzedData = json.loads(fx.read())
    fx.close()

    totalOwnersDict[platform] = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    tempFolder2 = targetFolder.replace('APPNAME',platform)
    tempFolder2 = tempFolder2.replace('1-','0-')



    saveImagePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/ownerImages/APPNAME/'

    saveImagePath = saveImagePath.replace('APPNAME',platform)

    

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    # print(len(filenames))
    # time.s
    
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        # if 1:
        if cityName != 'New York':
            totalOwnersDict[platform][cityName] = {}
            print(platform, cityName)
            # 
            totalIDsPics = {}

            # try:
            if 1:
            # if 'Paris' in cityName:
                fx = open(tempFolder+fileName,'r')
                content = json.loads(fx.read())
                fx.close()
                carsDict = {}
                if 'Europe' in platform:
                    fx = open(tempFolder2+fileName,'r')
                    content2 = json.loads(fx.read())
                    fx.close()
                    
                    carsDict = readCars(content2, platform)
                # print('Sleeping', len(carsDict.keys()))
                # time.sleep(1000)
                ownerCount = 0
                # for country in content.keys():
                #     for city in content[country].keys():
                # print(len(content.keys()))
                for id in analyzedData[platform][cityName]:
                    if 1:
                        cars += 1
                    # try:
                        # v10 = analyzedData[platform][cityName][id]
                        # print(id, v10)
                        # time.sleep(1000)
                        # print(id, content[id])
                        dates = list(content[id].keys())
                        dates.sort()
                        date = dates[0]
                        car = content[id][date]

                        ownerId = car['ownerID']

                        ownerName = car['ownerName']
                    
                        try:
                            val = totalOwnersDict[platform][cityName][ownerId]
                        except:
                            totalOwnersDict[platform][cityName][ownerId] = {}
                            totalOwnersDict[platform][cityName][ownerId]['name'] = ownerName
                            totalOwnersDict[platform][cityName][ownerId]['vehicles'] = {}

                        try:
                            totalOwnersDict[platform][cityName][ownerId]['vehicles'][id] = catDict[platform][cityName][id]
                        except:
                            totalOwnersDict[platform][cityName][ownerId]['vehicles'][id]=  'sedan'
                        # print(totalOwnersDict)
                        # time.sleep(100000)
                    
                    # except:
                    #     pass


fx = open('multiplicityDict.txt','w')
fx.write(json.dumps(totalOwnersDict))
fx.close()
print('Came here', cars)





# from basicImports import *
# import requests
# import random
# import string
# import ast
# from os import walk
# import requests # request img from web
# import shutil # save img locally


# # READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# # MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

# totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


# fx = open('carCatCleaned.txt', 'r')
# catDict = json.loads(fx.read())
# fx.close()

# print(len(catDict.keys()))

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

# totalModels = {}

# moreThanOne = {}
# totalVehicles = {}
# studiedApps = {}
# studiedApps['Turo'] = 1
# studiedApps['GetAround'] = 1
# studiedApps['GerAroundEurope'] = 1

# ownerVehicles = {}
# for city in cities:
#     ownerVehicles[city] = {}
#     for service in studiedApps.keys():
#         ownerVehicles[city][service] = {}



# for platform in studiedApps:
#     listData = {}
#     tempFolder = targetFolder.replace('APPNAME',platform)
#     filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
#     filenames.sort()
#     nf = 0

#     for fileName in filenames:
#         cityName = fileName.split('-')[0]
#         if cityName != 'New York':
#             # try:
#             #     var = ownerVehicles[cityName][platform]
#             # except:
#             #     ownerVehicles[cityName][platform] = {}
#             print(platform, cityName)
#             # 
#             totalIDsPics = {}
#             if 1:
#             # try:
#                 fx = open(tempFolder+fileName,'r')
#                 content = json.loads(fx.read())
#                 fx.close()
#                 carCount = 0
#                 for id in content:
#                     # print(content[id])
#                     # time.sleep(1000000)
#                     for date in content[id]:
#                         car = content[id][date]
#                         ownerID = content[id][date]['ownerID']
#                         # print(car['make'], car['model'])
#                         totalVehicles[platform+id] = 1
#                         toBeSearchedKey = car['model'].lower()+'~'+car['make'].lower()
#                         totalModels[toBeSearchedKey] = 1

#                         try:
#                             var = ownerVehicles[cityName][platform][ownerID]
#                         except:
#                             ownerVehicles[cityName][platform][ownerID] = {}
                            
#                         ownerVehicles[cityName][platform][ownerID][toBeSearchedKey] = 1

#                         try:
#                             var = catDict[toBeSearchedKey]
#                             # found[toBeSearchedKey] = catDict[toBeSearchedKey]
#                             types = catDict[toBeSearchedKey]['type']

#                             if len(types) > 1:
#                                 moreThanOne[platform+id] = 1

#                             for type in types:
#                                 type = type.lower()
#                                 totalTypes[type] = 1
#                             # print(catDict[toBeSearchedKey])
#                             # time.sleep(1000)
#                         except Exception as e:
#                             # print('\t NOT FOUND',toBeSearchedKey, len(catDict.keys()), catDict['sportage~kia'], e)
#                             # time.sleep(1000)
#                             # time.sleep(0.1)
#                             if 'Turo' in platform or 'GetAround' in platform:
#                                 ctype = car['type']
#                                 ctype = ctype.lower()
#                                 if ctype == 'truck':
#                                     ctype  = 'pickup'
#                                 elif ctype == 'suv':
#                                     ctype  = 'SUV'
#                                 elif ctype == 'car':
#                                     ctype  = 'sedan'
#                                 elif ctype == 'convertible_':
#                                     ctype  = 'convertible'
#                                 catDict[toBeSearchedKey] = {'make':car['make'],'model':car['model'],'type':[ctype]}
#                                 totalTypes[ctype] = 1
#                             else:
#                                 try:
#                                     catDict[toBeSearchedKey] = {'make':car['make'],'model':car['model'],'type':tempDict[toBeSearchedKey]}
#                                     # totalTypes[tempDict[toBeSearchedKey]] = 1
#                                     types = tempDict[toBeSearchedKey]

#                                     if len(types) > 1:
#                                         moreThanOne[platform+id] = 1

#                                     for type in types:
#                                         type = type.lower()
#                                         totalTypes[type] = 1
#                                 except Exception as e:
#                                     print('\t NOT FOUND',nf, toBeSearchedKey, e)
#                                     # notFound[toBeSearchedKey] = 1
#                                     # found[toBeSearchedKey] = 1
#                                     nf += 1
#                                     catDict[toBeSearchedKey] = {'make':car['make'],'model':car['model'],'type':['TBR']}
#                                     # time.sleep(0.1)

#                         cat = catDict[toBeSearchedKey]['type']
#                         cat = cat[0]
#                         cat = cat.lower()
#                         if cat == 'minivan':
#                             cat = 'van/minivan'
#                         elif cat == 'pickup':
#                             cat = 'truck'
#                         elif cat == 'convertible':
#                             cat = 'coupe'
#                         elif cat == 'van':
#                             cat = 'van/minivan'
                        
                        
#                         if cityName != 'New York':
#                             citiesAndServices[cityName][platform][cat][id] = 1

#                         # print(cat)
#                         # time.sleep(1000)
#                         # 
#             # except Exception as e:
#             #     print(e)

# print(len(catDict.keys()),len(totalVehicles.keys()), len(moreThanOne.keys()))
# print(len(totalTypes), totalTypes.keys())
# # time.sleep(1000)
# f = 0

# catsCount = {}
# for cat in catCats:
#     catsCount[cat] = 0

# cityShort = {}
# cityShort['Barcelona'] = 'BAR'
# cityShort['Berlin'] = 'BER'
# cityShort['Hamburg'] = 'HAM'
# cityShort['Los Angeles'] = 'LAX'
# cityShort['London'] = 'LDN'
# cityShort['Liverpool'] = 'LPL'
# cityShort['Las Vegas'] = 'LVX'
# cityShort['Lyon'] = 'LYN'
# cityShort['Madrid'] = 'MAD'
# cityShort['Miami'] = 'MIA'
# cityShort['New York City'] = 'NYC'
# cityShort['Ottawa'] = 'OTW'
# cityShort['Paris'] = 'PAR'
# cityShort['Toronto'] = 'TRT'
# cityShort['Washington D.C.'] = 'WDC'

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


# totalMultiplicityDict = {}
# totalMultiplicityDict['1'] = []
# totalMultiplicityDict['2'] = []
# totalMultiplicityDict['3'] = []
# totalMultiplicityDict['4'] = []
# totalMultiplicityDict['5'] = []
# totalMultiplicityDict['6'] = []

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
#     'Washington D.C.' 
#     ]

# averageCars = []
# totalAboveOwners = 0
# totalOwnersExperiment = 0
# totalAboveVehicles = []

# aboveCarCategories = {}
# suchVehicles = 0
# for i in range(0,len(cities)):
#     city = cities[i]
#     cityMultiplicityDict = {}
#     cityMultiplicityDict['1'] = 0
#     cityMultiplicityDict['2'] = 0
#     cityMultiplicityDict['3'] = 0
#     cityMultiplicityDict['4'] = 0
#     cityMultiplicityDict['5'] = 0
#     cityMultiplicityDict['6'] = 0
#     maxCount = 0
#     totalOwners = 0
#     totalVehicles = 0
#     for platform in ownerVehicles[city]:
#         try:
#             for ownerID in ownerVehicles[city][platform]:
#                 totalOwners += 1
#                 totalOwnersExperiment += 1
#                 carCount = len(ownerVehicles[city][platform][ownerID])
#                 maxCount = max(maxCount, carCount)
#                 totalVehicles += len(ownerVehicles[city][platform][ownerID])
#                 cats = {}
#                 if carCount > 1:
#                     for vehicleID in ownerVehicles[city][platform][ownerID].keys():
#                         cat = catDict[vehicleID]['type']
#                         cat = cat[0]
#                         cat = cat.lower()
#                         if cat == 'minivan':
#                             cat = 'van/minivan'
#                         elif cat == 'pickup':
#                             cat = 'truck'
#                         elif cat == 'convertible':
#                             cat = 'coupe'
#                         elif cat == 'van':
#                             cat = 'van/minivan'

#                         cats[cat] = 1
                        
#                     cats = list(cats.keys())
#                     cats.sort()
#                     strOfCats = str(cats)
#                     try:
#                         val = aboveCarCategories[strOfCats]
#                     except:
#                         aboveCarCategories[strOfCats] = 0
#                     aboveCarCategories[strOfCats] += 1
#                     suchVehicles += 1
                    
                    

#                 if carCount < 3:
#                     totalAboveOwners += 1
#                     totalAboveVehicles.append(carCount)

#                 carCount = min(carCount,6)

#                 cityMultiplicityDict[str(carCount)] += 1
#                 # print(city, platform, ownerID, carCount)

#                 # time.sleep(1000)
#         except:
#             pass
#     totalOwners = max(1, totalOwners)
#     print(city,totalVehicles/totalOwners)
#     if totalVehicles/totalOwners > 0:
#         averageCars.append(totalVehicles/totalOwners)
#     if 0:
    
#     # if round(cityMultiplicityDict['1']/totalOwners*100,2) > 89 or round(cityMultiplicityDict['1']/totalOwners*100,2) < 80:
#         print(cityShort[city], '&', round(cityMultiplicityDict['1']/totalOwners*100,2), '&', round(cityMultiplicityDict['2']/totalOwners*100,2),'&', round(cityMultiplicityDict['3']/totalOwners*100,2),'&', round(cityMultiplicityDict['4']/totalOwners*100,2),'&', round(cityMultiplicityDict['5']/totalOwners*100,2),'&', round(cityMultiplicityDict['6']/totalOwners*100,2),'&', maxCount,'\\\\')
#         print('\\hline')
#         # cityMultiplicityDict
#     for carCt in cityMultiplicityDict:
#         totalMultiplicityDict[carCt].append(round(cityMultiplicityDict[carCt]/totalOwners*100,2))

# print(totalOwnersExperiment, totalAboveOwners/totalOwnersExperiment, sum(totalAboveVehicles)/totalAboveOwners)
# print('average cars: ', np.average(averageCars))
# for carCt in totalMultiplicityDict:
#     # print(carCt, (totalMultiplicityDict[carCt]))

#     print(carCt, np.average(totalMultiplicityDict[carCt]))

# sortedDict = {k: v for k, v in sorted(aboveCarCategories.items(), key=lambda item: item[1])}
# # sorted(aboveCarCategories)

# for cat in sortedDict:
#     counter = cat.count(',')
#     # if 1:
#     if counter >3:
#         print(cat, aboveCarCategories[cat],  round(aboveCarCategories[cat]/suchVehicles*100,2))
# time.sleep(1000)

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
#     counter = cat.count(',')
#     # if 1:
#     if counter >3:
#         print(cat, round(catsCount[cat]/len(totalVehicles)*100,2))
       
       
       
       
       
#         # nf = 0

#         # for key in found:
#         #     try:
#         #         if found[key] == -1:
#         #             nf += 1
#         #         else:
#         #             f += 1
#         #     except:
#         #         f += 1
#         # # print(nf+f, f/(nf+f), nf/(nf+f))
#         # fx = open('carCatCleaned.txt','w')
#         # fx.write(json.dumps(catDict))
#         # fx.close()
#         # print('Came here')
#         # break


        








# # tempDict = {}
# # tempDict['ibiza~seat'] = ['Hatchback']
# # tempDict['c-elysée~citroen'] = ['Sedan']
# # tempDict['208~peugeot'] = ['Hatchback']
# # tempDict['formentor~cupra'] = ['Sedan']
# # tempDict['formentor~cupra'] = ['SUV','Coupe']
# # tempDict['c3~citroen'] = ['SUV']
# # tempDict['cee\'d~kia'] = ['Hatchback']
# # tempDict['aygo~toyota'] = ['Hatchback']
# # tempDict['corsa-e~opel'] = ['Hatchback']
# # tempDict['corsa~opel'] = ['Hatchback']
# # tempDict['micra~nissan'] = ['Hatchback']
# # tempDict['2~mazda'] = ['Hatchback']
# # tempDict['berlingo~citroen'] = ['SUV']
# # tempDict['clio~renault'] = ['Hatchback']
# # tempDict['punto~fiat'] = ['Hatchback']
# # tempDict['auris~toyota'] = ['Hatchback']
# # tempDict['kangoo~renault'] = ['Van/Minivan']
# # tempDict['1007~peugeot'] = ['Hatchback']
# # tempDict['4~renault'] = ['Hatchback']
# # tempDict['mii~seat'] = ['Hatchback']
# # tempDict['panda~fiat'] = ['Hatchback']
# # tempDict['207~peugeot'] = ['Hatchback']
# # tempDict['207+~peugeot'] = ['Hatchback']
# # tempDict['carens~kia'] = ['SUV']
# # tempDict['c4~citroen'] = ['SUV']
# # tempDict['insignia~opel'] = ['Hatchback']
# # tempDict['fabia~skoda'] = ['Hatchback']
# # tempDict['corsa~vauxhall'] = ['Hatchback']
# # tempDict['forfour~smart'] = ['Hatchback']
# # tempDict['zafira~opel'] = ['Van/Minivan']
# # tempDict['clase~mercedes'] = ['Sedan']
# # tempDict['ateca~seat'] = ['SUV']
# # tempDict['zoe~renault'] = ['Hatchback']
# # tempDict['508~peugeot'] = ['Sedan']
# # tempDict['asx~mitsubishi'] = ['SUV']
# # tempDict['ë-c4~citroen'] = ['SUV']
# # tempDict['crz~honda'] = ['Hatchback']
# # tempDict['iq~toyota'] = ['Hatchback']
# # tempDict['jazz~honda'] = ['Hatchback']
# # tempDict['caddy~volkswagen'] = ['Van/Minivan']
# # tempDict['ioniq~hyundai'] = ['Sedan']
# # tempDict['touran~volkswagen'] = ['Van/Minivan']
# # tempDict['c-klasse~mercedes'] = ['Hatchback']
# # tempDict['rekord~opel'] = ['Sedan']
# # tempDict['mondeo~ford'] = ['Hatchback']
# # tempDict['talisman~renault'] = ['Sedan']
# # tempDict['3er~bmw'] = ['Sedan']
# # tempDict['e-klasse~mercedes'] = ['Sedan']
# # tempDict['9-3~saab'] = ['Convertible', 'Sedan']
# # tempDict['octavia~skoda'] = ['Sedan']
# # tempDict['1er~bmw'] = ['Hatchback']
# # tempDict['a-klasse~mercedes'] = ['Hatchback']
# # tempDict['delta~oldsmobile'] = ['Sedan']
# # tempDict['up!~volkswagen'] = ['Hatchback']
# # tempDict['w123~mercedes'] = ['Sedan']
# # tempDict['ix35~hyundai'] = ['Hatchback']
# # tempDict['cla-klasse~mercedes'] = ['Sedan']
# # tempDict['5er~bmw'] = ['Sedan']
# # tempDict['sl-klasse~mercedes'] = ['Convertible', 'Sedan']
# # tempDict['2er~bmw'] = ['Sedan']
# # tempDict['b-klasse~mercedes'] = ['Van/Minivan']
# # tempDict['roomster~skoda'] = ['Van/Minivan']
# # tempDict['807~peugeot'] = ['Wagon']
# # tempDict['modus~renault'] = ['Hatchback']
# # tempDict['one~mini'] = ['Hatchback']
# # tempDict['t-cross~volkswagen'] = ['SUV']
# # tempDict['captiva~chevrolet'] = ['SUV']
# # tempDict['e-up~volkswagen'] = ['Hatchback']
# # tempDict['grand~ford'] = ['SUV']
# # tempDict['new~volkswagen'] = ['Hatchback']
# # tempDict['defender~land-rover'] = ['SUV']
# # tempDict['q30~infiniti'] = ['Hatchback']
# # tempDict['alhambra~seat'] = ['Van/Minivan']
# # tempDict['5008~peugeot'] = ['SUV']
# # tempDict['4er~bmw'] = ['Sedan']
# # tempDict['crossland~opel'] = ['Hatchback']
# # tempDict['sharan~volkswagen'] = ['Wagon']
# # tempDict['slk-klasse~mercedes'] = ['Convertible', 'Coupe']
# # tempDict['3~bmw'] = ['Sedan']
# # tempDict['c-class~mercedes'] = ['Sedan']
# # tempDict['e-class~mercedes'] = ['Sedan']
# # tempDict['kuga~ford'] = ['SUV']
# # tempDict['partner~peugeot'] = ['Van/Minivan']
# # tempDict['407~peugeot'] = ['Hatchback']
# # tempDict['série~bmw'] = ['Hatchback']
# # tempDict['3008~peugeot'] = ['SUV']
# # tempDict['e-208~peugeot'] = ['Hatchback']
# # tempDict['s-max~ford'] = ['Wagon']
# # tempDict['e-niro~kia'] = ['SUV']
# # tempDict['classe~mercedes'] = ['Sedan']
# # tempDict['espace~renault'] = ['Wagon']
# # tempDict['c8~citroen'] = ['Wagon']
# # tempDict['taigo~volkswagen'] = ['SUV']
# # tempDict['exeo~seat'] = ['Hatchback']
# # tempDict['qashqai+2~nissan'] = ['SUV']
# # tempDict['cx~citroen'] = ['Hatchback']
# # tempDict['2cv~citroen'] = ['Hatchback']
# # tempDict['107~peugeot'] = ['Hatchback']
# # tempDict['freemont~fiat'] = ['SUV']
# # tempDict['301~peugeot'] = ['SUV']
# # tempDict['c2~citroen'] = ['Hatchback']
# # tempDict['bluecar~bolloré'] = ['Hatchback']
# # tempDict['model~tesla'] = ['Sedan']
# # tempDict['altea~seat'] = ['Hatchback']
# # tempDict['c-max~ford'] = ['SUV']
# # tempDict['giulietta~alfa-romeo'] = ['Hatchback']
# # tempDict['grande~fiat'] = ['Hatchback']
# # tempDict['grande~fiat'] = ['Hatchback']
# # tempDict['transporter~volkswagen'] = ['Van/Minivan']
# # tempDict['4007~peugeot'] = ['SUV']
# # tempDict['307~peugeot'] = ['Hatchback']
# # tempDict['rcz~peugeot'] = ['Sedan']
# # tempDict['xceed~kia'] = ['SUV']
# # tempDict['rifter~peugeot'] = ['Wagon']
# # tempDict['alto~suzuki'] = ['Hatchback']
# # tempDict['tipo~fiat'] = ['Hatchback']
# # tempDict['austin~mini'] = ['Hatchback']
# # tempDict['"huevito"~fiat'] = ['Hatchback']
# # tempDict['bravo~fiat'] = ['Hatchback']
# # tempDict['santa~hyundai'] = ['SUV']
# # tempDict['kallista~panther'] = ['Convertible','Coupe']
# # tempDict['lacetti~chevrolet'] = ['Sedan']
# # tempDict['i40~hyundai'] = ['Hatchback']
# # tempDict['ix20~hyundai'] = ['Hatchback']
# # tempDict['rexton~ssangyong'] = ['SUV']
# # tempDict['ypsilon~lancia'] = ['Hatchback']
# # tempDict['transit~ford'] = ['Wagon']
# # tempDict['ka+~ford'] = ['Hatchback']
# # tempDict['fluence~renault'] = ['Hatchback']
# # tempDict['mito~alfa-romeo'] = ['Hatchback']
# # tempDict['600~seat'] = ['Hatchback']
# # tempDict['epica~chevrolet'] = ['Sedan']
# # tempDict['motors~tata'] = ['Hatchback']
# # tempDict['c-zero~citroen'] = ['Hatchback']
# # tempDict['adam~opel'] = ['Hatchback']
# # tempDict['tourneo~ford'] = ['Wagon']
# # tempDict['pixo~nissan'] = ['Hatchback']
# # tempDict['c5~citroen'] = ['SUV']
# # tempDict['jogger~dacia'] = ['SUV']
# # tempDict['206~peugeot'] = ['Hatchback']
# # tempDict['laguna~renault'] = ['Sedan']
# # tempDict['trafic~renault'] = ['Wagon']
# # tempDict['ds5~citroen'] = ['Hatchback']
# # tempDict['coccinelle~volkswagen'] = ['Convertible', 'Sedan']
# # tempDict['t-roc~volkswagen'] = ['SUV']
# # tempDict['e-2008~peugeot'] = ['SUV']
# # tempDict['147~alfa-romeo'] = ['Hatchback']
# # tempDict['scirocco~volkswagen'] = ['Hatchback']
# # tempDict['scirocco~volkswagen'] = ['Hatchback']
# # tempDict['chr~toyota'] = ['SUV']
# # tempDict['multipla~fiat'] = ['Van/Minivan']
# # tempDict['b-max~ford'] = ['Hatchback']
# # tempDict['id~citroen'] = ['Hatchback']
# # tempDict['traction~citroen'] = ['Sedan']
# # tempDict['koleos~renault'] = ['SUV']
# # tempDict['agila~opel'] = ['Hatchback']
# # tempDict['bipper~peugeot'] = ['Van/Minivan']
# # tempDict['e~honda'] = ['Hatchback']
# # tempDict['124~fiat'] = ['Convertible', 'Coupe']
# # tempDict['wind~renault'] = ['Convertible', 'Hatchback']
# # tempDict['spring~dacia'] = ['SUV']
# # tempDict['cuore~daihatsu'] = ['Hatchback']
# # tempDict['xsara~citroen'] = ['Sedan']
# # tempDict['arkana~renault'] = ['SUV', 'Hatchback']
# # tempDict['grand~renault'] = ['Van','Minivan']
# # tempDict['i20~hyundai'] = ['Hatchback']
# # tempDict['polo~volkswagen'] = ['Hatchback']
# # tempDict['sandero~dacia'] = ['SUV']
# # tempDict['serie~bmw'] = ['Sedan']
# # tempDict['picanto~kia'] = ['Hatchback']
# # tempDict['cabriolet~mini'] = ['Convertible', 'Hatchback']
# # tempDict['a1~audi'] = ['Hatchback']
# # tempDict['logan~dacia'] = ['Sedan']
# # tempDict['qashqai~nissan'] = ['SUV']
# # tempDict['superb~skoda'] = ['Sedan']
# # tempDict['scénic~renault'] = ['Hatchback']
# # tempDict['mx-5~mazda'] = ['Coupe']
# # tempDict['arona~seat'] = ['SUV']
# # tempDict['&~lynk'] = ['SUV']
# # tempDict['leon~seat'] = ['Hatchback']
# # tempDict['twingo~renault'] = ['Hatchback']
# # tempDict['2008~peugeot'] = ['SUV']
# # tempDict['ka~ford'] = ['Hatchback']
# # tempDict['meriva~opel'] = ['Hatchback']
# # tempDict['308~peugeot'] = ['SUV']
# # tempDict['spider~alfa-romeo'] = ['Convertible', 'Coupe']
# # tempDict['note~nissan'] = ['Hatchback']
# # tempDict['captur~renault'] = ['SUV']
# # tempDict['doblo~fiat'] = ['Hatchback']
# # tempDict['tivoli~ssangyong'] = ['SUV']
# # tempDict['mégane~renault'] = ['SUV']
# # tempDict['ignis~suzuki'] = ['Hatchback']
# # tempDict['karl~opel'] = ['Hatchback']
# # tempDict['astra~opel'] = ['Hatchback']
# # tempDict['citigo~skoda'] = ['Hatchback']
# # tempDict['3~mazda'] = ['Sedan']
# # tempDict['verso~toyota'] = ['Hatchback']
# # tempDict['stonic~kia'] = ['Hatchback']
# # tempDict['korando~ssangyong'] = ['SUV']
# # tempDict['land~toyota'] = ['SUV']
# # tempDict['c1~citroen'] = ['Hatchback']
# # tempDict['206+~peugeot'] = ['Hatchback']
# # tempDict['i30~hyundai'] = ['Hatchback']
# # tempDict['108~peugeot'] = ['Hatchback']
# # tempDict['pt~chrysler'] = ['Hatchback']
# # tempDict['dokker~dacia'] = ['Wagon']
# # tempDict['tarraco~seat'] = ['SUV']
# # tempDict['5~mazda'] = ['SUV']
# # tempDict['ds4~citroen'] = ['Hatchback']
# # tempDict['duster~dacia'] = ['SUV']
# # tempDict['rav~toyota'] = ['SUV']
# # tempDict['i10~hyundai'] = ['Hatchback']
# # tempDict['mokka~opel'] = ['SUV']
# # tempDict['kadjar~renault'] = ['SUV']
# # tempDict['lodgy~dacia'] = ['Van/Minivan']
# # tempDict['zafira~vauxhall'] = ['Hatchback']
# # tempDict['astra~vauxhall'] = ['Hatchback']
# # tempDict['grand~citroen'] = ['Wagon']
# # tempDict['4~bmw'] = ['Sedan']
# # tempDict['ds3~citroen'] = ['Hatchback']
# # tempDict['a-class~mercedes'] = ['Sedan']
# # tempDict['1~bmw'] = ['Hatchback']
# # tempDict['adam~vauxhall'] = ['Hatchback']
# # tempDict['kodiaq~skoda'] = ['SUV']
# # tempDict['gl-class~mercedes'] = ['SUV']
# # tempDict['discovery~land-rover'] = ['SUV']
# # tempDict['pulsar~nissan'] = ['Sedan']
# # tempDict['spider~abarth'] = ['Convertible', 'Coupe']
# # tempDict['range~land-rover'] = ['SUV']
# # tempDict['galaxy~ford'] = ['Hatchback']
# # tempDict['5~bmw'] = ['Sedan']
# # tempDict['rapid~skoda'] = ['Sedan']
# # tempDict['2~bmw'] = ['Sedan']
# # tempDict['595~abarth'] = ['Hatchback']
# # tempDict['q2~audi'] = ['SUV']
# # tempDict['mokka~vauxhall'] = ['Hatchback']
# # tempDict['id.3~volkswagen'] = ['Hatchback']
# # tempDict['cla-class~mercedes'] = ['Sedan']
# # tempDict['grandland~vauxhall'] = ['SUV']
# # tempDict['pro~kia'] = ['Sedan']
# # tempDict['giulia~alfa-romeo'] = ['Sedan']
# # tempDict['stelvio~alfa-romeo'] = ['SUV']
# # tempDict['6~mazda'] = ['Sedan']
# # tempDict['12~renault'] = ['Sedan']
# # tempDict['18~renault'] = ['Sedan']
# # tempDict['mini~rover'] = ['Hatchback']
# # tempDict['c-crosser~citroen'] = ['SUV']




# # dictKeys = list(catDict.keys())
# # dictKeys.sort()

# # for key in dictKeys:
# #     if len(catDict[key]['type']) == 0:
# #         del catDict[key]
# # studiedApps = {}
# # studiedApps['Turo'] = 1
# # studiedApps['GetAround'] = 1
# # studiedApps['GerAroundEurope'] = 1


# # cities = ['Barcelona', 'Berlin', 'Hamburg', 'Los Angeles','London', 'Liverpool', 'Las Vegas', 'Lyon', 'Madrid','Miami', 'New York City', 'Ottawa',  'Paris',  'Toronto','Washington D.C.' ]
# # # cities = {'Barcelona', 'Berlin', 'Hamburg', 'Liverpool', 'London', 'Lyon', 'Madrid', 'Paris', 'Las Vegas', 'Los Angeles', 'Miami','New York City', 'Ottawa', 'Toronto','Washington D.C.' }
# # targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'


# # catCats = ['sedan', 'hatchback', 'coupe', 'truck', 'suv', 'wagon',  'van/minivan']
# # found = {}
# # notFound = {}
# # totalTypes = {}

# # citiesAndServices = {}
# # for city in cities:
# #     citiesAndServices[city] = {}
# #     for service in studiedApps.keys():
# #         citiesAndServices[city][service] = {}
# #         for cat in catCats:
# #             citiesAndServices[city][service][cat] = {}


# # for key in catDict.keys():
# #     # print(catDict[key])
# #     types = catDict[key]['type']
# #     for i in range(0,len(types)):
# #         ctype = types[i]
# #         if ctype != 'SUV':
# #             ctype = ctype.lower()
# #         if ctype == 'car':
# #             ctype = 'sedan'
# #         if '_' in ctype:
# #             ctype = ctype[:-1]
# #         catDict[key]['type'][i] = ctype
