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
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1
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


ownersDict = {}

d = gender.Detector()
totalOwners = 0
for city in cities:
    ownersDict[city] = {}
    ownersDict[city]['male'] = 0
    ownersDict[city]['female'] = 0
    ownersDict[city]['total'] = 0
    ownersDict[city]['nonHumanDP'] = 0
    ownersDict[city]['multiHumanDP'] = 0
    ownersDict[city]['hubandWifeDP'] = 0
    ownersDict[city]['motherChildDP'] = 0
    ownersDict[city]['fatherChild'] = 0
    ownersDict[city]['familyDP'] = 0

    ownersDict[city]['race'] = {}
    for race in ['asian', 'white', 'middle eastern', 'indian', 'latino hispanic', 'black']:
        ownersDict[city]['race'][race] = 0
    ownersDict[city]['age'] = []
    ownersDict[city]['fage'] = []
    ownersDict[city]['mage'] = []

races = ['asian', 'indian', 'black', 'white', 'middle eastern', 'latino hispanic']

studiedApps = {}
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1
ownerCount = 0
# time.sleep(1000000)

fx = open('supplyOwnerDemo.txt', 'r')
realCarsOwners = json.loads(fx.read())
fx.close()
oc = 0

poc = {}
pocc = {}
nopcowner = 0

for city in cityShort:
    pocc[city] = 0
for platform in studiedApps:
    poc[platform] = 0
for platform in studiedApps:
    print(platform)
    try:
        val = newOwnersDemographicsDict[platform]
    except:
        newOwnersDemographicsDict[platform] = {}

    fx = open(targetFolder+platform+'-demographics.txt','r')
    ownerDemographics = json.loads(fx.read())
    ownerDemographics = ownerDemographics[platform]

    ownerCountDict[platform] += len(ownerDemographics.keys())
    for ownerKey in ownerDemographics.keys():
        try:
            v10  = realCarsOwners[platform][ownerKey]

            oc += 1
            poc[platform] += 1

            # print(ownerKey)
            # time.sleep(1000)
            # if ownerCount %100 == 0:
            #     print(ownerCount, 'owners done')
            key = ownerKey[:]
            ownerKey = ownerKey.split('~')
            city = cityName = ownerKey[0]
            pocc[city] += 1
            if city != 'New York':
                totalOwners += 1
                # ownerCount += 1
                try:
                    val = newOwnersDemographicsDict[platform][cityName]
                except:
                    newOwnersDemographicsDict[platform][cityName] = {}
                ownerName = ownerKey[1]
                ownerId = ownerKey[2]

                firstName = ownerName.split(' ')[0]
                nameGender = d.get_gender(firstName)

                if'_' in nameGender:
                    nameGender = nameGender.split('_')[1]


                # if len(ownerDemographics[key].keys()) > 0:
                #     print(key, ownerDemographics[key])
                #     time.sleep(1000000)
                m = f = k = 0
                if len(ownerDemographics[key]) == 0:
                    nopcowner += 1

                    ownersDict[city]['nonHumanDP']+=1

                for user in ownerDemographics[key]:
                    # print(key, ownerDemographics[key])
                    age = ownerDemographics[key][user]['age']
                    age = age.replace('(','')
                    age = age.replace(')','')
                    age = age.split(', ')
                    age = ((int(age[0])+int(age[1]))/2)*1.2

                    if age > 16 and age < 20:
                        age += 4
                    # print(key, age, ownerDemographics[key][user])
                    # time.sleep(1)
                    #gender
                    recognizedGender = ownerDemographics[key][user]['gender']

                    recognizedGender = recognizedGender.lower()
                    if age <= 16:
                        k = 1
                    else:
                        if recognizedGender == 'male':
                            m = 1
                        else:
                            f = 1
                    add = 0
                    age = round(age,2)
                    if age >= 20:
                        add = 1

                    if add and len(ownerDemographics[key]) > 1 and recognizedGender == nameGender:
                        ownersDict[city][recognizedGender]+=1
                        ownersDict[city]['age'].append(age)
                        #race
                        ownersDict[city]['race'][ownerDemographics[key][user]['race']]+=1
                        newOwnersDemographicsDict[platform][cityName][ownerId] = (age, recognizedGender, ownerDemographics[key][user]['race'])

                        if recognizedGender == 'male':
                            ownersDict[city]['mage'].append(age)
                        else:
                            ownersDict[city]['fage'].append(age)
                        # print(ownerName, nameGender)
                        # time.sleep(1000)
                    elif add and len(ownerDemographics[key]) == 1:
                        ownersDict[city][recognizedGender]+=1
                        # print(age)
                        ownersDict[city]['age'].append(age)
                        #race
                        ownersDict[city]['race'][ownerDemographics[key][user]['race']]+=1
                        newOwnersDemographicsDict[platform][cityName][ownerId] = (age, recognizedGender, ownerDemographics[key][user]['race'])
                        if recognizedGender == 'male':
                            ownersDict[city]['mage'].append(age)
                        else:
                            ownersDict[city]['fage'].append(age)

                ownersDict[city]['total']+=1

                if len(ownerDemographics[key]) > 1:
                    ownersDict[city]['multiHumanDP']+=1
                if m == 1 and k == 1 and f == 0:
                    ownersDict[city]['fatherChild'] +=1
                if m == 0 and k == 1 and f == 1:
                    ownersDict[city]['motherChildDP'] +=1
                if len(ownerDemographics[key]) > 2:
                    ownersDict[city]['familyDP']+=1
                if m == 1 and k == 0 and f == 1:
                    ownersDict[city]['hubandWifeDP'] +=1

        except:
            pass

print('               ',nopcowner, oc, poc, pocc)
# print('\t total owners', ownerCountDict[platform])
tm = 0
tf = 0
tn = 0
for city in cities:
    if ownersDict[city]['total'] > 0:
        ownersDict[city]['fage'] = round(np.average(ownersDict[city]['fage']),2)
        ownersDict[city]['mage'] = round(np.average(ownersDict[city]['mage']),2)
        ownersDict[city]['age'] = round(np.average(ownersDict[city]['age']),2)
        newRaces = []
        for key in ownersDict[city]['race']:
            ownersDict[city]['race'][key] = round((ownersDict[city]['race'][key]/(ownersDict[city]['total']-ownersDict[city]['nonHumanDP'])*100),2)

            newRaces.append((key, ownersDict[city]['race'][key]))
            # if dominantRace[1] < ownersDict[city]['race'][key]:
            #     dominantRace = (key, ownersDict[city]['race'][key])
        ownersDict[city]['race'] = newRaces
        ownersDict[city]['race'].sort(key=lambda x:x[1], reverse = True)



        ownersDict[city]['male'] = round((ownersDict[city]['male']/(ownersDict[city]['total']-ownersDict[city]['nonHumanDP'])*100),2)

        ownersDict[city]['female'] = round((ownersDict[city]['female']/(ownersDict[city]['total'] - ownersDict[city]['nonHumanDP'])*100),2)



        ownersDict[city]['multiHumanDP'] = round((ownersDict[city]['multiHumanDP']/(ownersDict[city]['total'] - ownersDict[city]['nonHumanDP'])*100),2)

        ownersDict[city]['hubandWifeDP'] = round((ownersDict[city]['hubandWifeDP']/(ownersDict[city]['total'] - ownersDict[city]['nonHumanDP'])*100),2)

        ownersDict[city]['motherChildDP'] = round((ownersDict[city]['motherChildDP']/(ownersDict[city]['total'] - ownersDict[city]['nonHumanDP'])*100),2)

        ownersDict[city]['fatherChild'] = round((ownersDict[city]['fatherChild']/(ownersDict[city]['total'] - ownersDict[city]['nonHumanDP'])*100),2)

        ownersDict[city]['familyDP'] = round((ownersDict[city]['familyDP']/(ownersDict[city]['total'] - ownersDict[city]['nonHumanDP'])*100),2)


        ownersDict[city]['nonHumanDP'] = round(100 - ownersDict[city]['male'] - ownersDict[city]['female'],2)


        tm += ownersDict[city]['male']*0.01* ownersDict[city]['total']
        tf += ownersDict[city]['female']*0.01* ownersDict[city]['total']
        tn += ownersDict[city]['nonHumanDP']*0.01* ownersDict[city]['total']



        #round((ownersDict[city]['nonHumanDP']/(ownersDict[city]['total'])*100),2)
        # ownersDict[city]['dominantRace'] = dominantRace
        # print('\t\t',city,  ownersDict[city])
# time.sleep(100000)





import numpy as np
import matplotlib.pyplot as plt



print(totalOwners, tm, tf, tn, tm/totalOwners, tf/totalOwners, tn/totalOwners)
# time.sleep(10000)

x = np.arange(15)

age = []
male = []
female = []
raceCount = []
newCities = []
raceTitles = []
fx = open('cityWiseDemographics.txt','r')
ownersDict = json.loads(fx.read())
fx.close()


for i in range(0, len(x)):
    city = cities[i]
    print(city, ownersDict[city])#, type(ownersDict[city]['age']) )
    print(' ')
    if 1:
        age.append(ownersDict[city]['age'])
        male.append(ownersDict[city]['male'])
        female.append(ownersDict[city]['female'])
        raceCount.append(ownersDict[city]['race'][0][1])
        newCities.append(cityShort[cities[i]])
        raceTitles.append(ownersDict[city]['race'][0][0])

# age = age[:15]
# male = male[:15]
# female = female[:15]
# raceCount = raceCount[:15]
# newCities = newCities[:15]
# raceTitles = raceTitles[:15]


# function to add value labels
def addlabels(x,y, raceTitles):
    for i in range(len(x)):
        plt.text(i+0.2, y[i]*1.02, raceTitles[i], ha = 'center', rotation=90, fontsize=15)


width = 0.20

# plt.figure()

fig, ax = plt.subplots()


# plot data in grouped manner of bar type
plt.bar(x-0.4, age, width)
plt.bar(x-0.2, male, width)
plt.bar(x+0, female, width)
plt.bar(x+0.2, raceCount, width)
addlabels(x+0.2, raceCount, raceTitles)

plt.xlim([-0.6,14.4])
xticksVals = []
for i in range(0, 15):
    xticksVals.append(i)
ax.set_xticks(xticksVals)
ax.set_xticklabels(newCities, rotation=0, fontsize=14)
# ax.set_yticklabels([0,10,20,30,40,50,60,70,80,90], rotation=0, fontsize=14)



plt.title('Demographics of vehicle owners in the cities of this experiment', fontsize=20)
plt.subplots_adjust(left=0.04,
                    bottom=0.1,
                    right=0.98,
                    top=0.94,
                    wspace=0.4,
                    hspace=0.4)
plt.ylabel('Percentage or Numerical Value', fontsize=18)
plt.xlabel('Cities',  fontsize=18)


fig = plt.gcf()
fig.set_size_inches(18, 7.5)



plt.legend(labels=['Average Age', 'Men%', 'Women%','Dominant Race%'],  fontsize=18)


scriptName = '4f'

fig.savefig('plots/'+scriptName+'.png')
fig.savefig('plots/'+scriptName+'.eps')


# fx = open('newOwnerDemographics.txt','w')
# fx.write(json.dumps(newOwnersDemographicsDict))
# fx.close()


# fx = open('cityWiseDemographics.txt','w')
# fx.write(json.dumps(ownersDict))
# fx.close()
