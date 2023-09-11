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
races = {}
races['male'] = {}
races['female'] = {}
races['white'] = {}
races['asian'] = {}
races['latino hispanic'] = {}
races['middle eastern'] = {}
races['black'] = {}
races['indian'] = {}

ownersDict  = {}  
famowner = 0
mainOneFaceDp = 0
totalAges = []
m = 0
f = 0
w  = 0
b = 0
ind = 0
newData = []
for city in realCarsOwners:
    ownersDict[city] = {}
    ownersDict[city]['age'] = []
    ownersDict[city]['male'] = 0
    ownersDict[city]['female'] = 0
    ownersDict[city]['race'] = {}
    for race in races:
        ownersDict[city]['race'][race] = 0

    singleDP = 0
    # totalCity = 0
    for platform in realCarsOwners[city]:
        totalOwnersCity = len(realCarsOwners[city][platform].keys())
        for owner in realCarsOwners[city][platform]:
            ownerObj  = realCarsOwners[city][platform][owner]
            # print(ownerObj)
            
            if ownerObj['peopleInDp'] == 1: 
                mainOneFaceDp += 1
                gender = ownerObj['ownerGenders'][0][0].lower()
                ownersDict[city][gender] += 1
                if gender == 'male':
                    m += 1
                else:
                    f += 1
                age = ownerObj['ownerGenders'][0][1]
                age = age.replace('(', '')
                age = age.replace(',', '')
                age = age.replace(')', '')
                age = age.split(' ')
                age = round((int(age[0])+int(age[1]))/2 *1.5,2)
                totalAges.append(age)
                ownersDict[city]['age'].append(age)
                ownersDict[city]['race'][ownerObj['ownerGenders'][0][2]] += 1
                if ownerObj['ownerGenders'][0][2] == 'white':
                    w += 1
                if ownerObj['ownerGenders'][0][2] == 'black':
                    b += 1
                if ownerObj['ownerGenders'][0][2] == 'indian':
                    ind += 1
                singleDP += 1
            elif ownerObj['peopleInDp'] > 1:
                famowner += 1
            elif ownerObj['peopleInDp'] == 0:
                nopcowner += 1
            poc[platform] += 1
            pocc[city] += 1
            oc += 1

    ownersDict[city]['age'] =round(np.average(ownersDict[city]['age']),2)
    ownersDict[city]['male'] = round((ownersDict[city]['male']/singleDP)*100,2)
    ownersDict[city]['female'] = round((ownersDict[city]['female']/singleDP)*100,2)

    # newData.append([ownersDict[city]['male'], ])
    for race in races:
        ownersDict[city]['race'][race] = round((ownersDict[city]['race'][race]/singleDP)*100,2)
print(oc, nopcowner, famowner, m/mainOneFaceDp, f/mainOneFaceDp, w/mainOneFaceDp, b/mainOneFaceDp, ind/mainOneFaceDp)
# time.sleep(10000)
print(np.average(totalAges))
x = np.arange(15)

age = []
male = []
female = []
raceCount = []
newCities = []
raceTitles = []
# fx = open('cityWiseDemographics.txt','r')
# ownersDict = json.loads(fx.read())
# fx.close()

print()
for i in range(0, len(x)):
    city = cities[i]
    print(city, ownersDict[city])#, type(ownersDict[city]['age']) )
    print(' ')
    
    age.append(ownersDict[city]['age'])
    male.append(ownersDict[city]['male'])
    female.append(ownersDict[city]['female'])
    rc = max(ownersDict[city]['race'], key=ownersDict[city]['race'].get)
    # print(rc)
    # time.sleep(1000)
    raceCount.append(ownersDict[city]['race'][rc])
    newCities.append(cityShort[cities[i]])
    raceTitles.append(rc)


# age = age[:15]
# male = male[:15]
# female = female[:15]
# raceCount = raceCount[:15]
# newCities = newCities[:15]
# raceTitles = raceTitles[:15]
print(raceCount)

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
plt.ylim([10,100])

xticksVals = []
for i in range(0, 15):
    xticksVals.append(i)
ax.set_xticks(xticksVals)
ax.set_xticklabels(newCities, rotation=0, fontsize=18)
# ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=18)
ax.tick_params(axis='both', which='major', labelsize=18)



plt.title('Demographics of vehicle owners in the cities of this experiment', fontsize=20)
plt.subplots_adjust(left=0.07,
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


scriptName = '4f4'

fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 


# fx = open('newOwnerDemographics.txt','w')
# fx.write(json.dumps(newOwnersDemographicsDict))
# fx.close()


# fx = open('cityWiseDemographics.txt','w')
# fx.write(json.dumps(ownersDict))
# fx.close()

