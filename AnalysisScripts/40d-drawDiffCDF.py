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
citiesAndServices['GetAround'] = ['Las Vegas', 'Los Angeles', 'Miami','New York City', 'Washington D.C.']
citiesAndServices['Turo'] = ['Liverpool', 'Las Vegas', 'London', 'Los Angeles','New York City', 'Miami', 'Ottawa', 'Toronto', 'Washington D.C.']
citiesAndServices['GerAroundEurope'] = ['Barcelona', 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris', 'London']

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'



import ujson 
import rbo
from scipy import stats


# a = [1,2,3,4,5]
# b = [5,4,3,2,1]
# rboVal = rbo.RankingSimilarity(a,b).rbo()

# print(rboVal)
# time.sleep(100000)


start_time = time.time()

lowReqsDict = {}
fx = open('40bData.txt','r')
newLowReqDict = json.loads(fx.read())
fx.close()



platformAverage =newLowReqDict

from scipy import stats


step=0.05
indices = np.arange(0,1+step,step)
fig, ax = plt.subplots()
indices = np.arange(0,1+step,step)
totalVals = []

totalLen = 0
selectedLen = 0
for platform in studiedApps:
    print(platform)
    plabel = 'GA-E'
    pcolor = 'olive'
    if platform == 'Turo':
        plabel = 'TR'
        pcolor= 'maroon'
    elif platform == 'GetAround':
        plabel = 'GA'
        pcolor= 'mediumblue'


    x = platformAverage[platform]
    totalLen += len(x)
    x2 = [item for item in platformAverage[platform] if item <0.7]
    selectedLen += len(x2)
    y = list(range(0,len(x)))
    print('\t', np.average(x2), len(x2)/len(x))

    x = x2
    # print((x))

    sns.ecdfplot(data=x, color=pcolor, label=plabel)
    
    totalVals.append(np.average(x))

print(np.average(totalVals))
print(selectedLen/totalLen)
# CDF = pd.DataFrame({'dummy':data})['dummy'].quantile(indices)

# plt.plot(CDF,indices,linewidth=3,  color='black', label='Total')



# plt.plot(xnew, power_smooth,linewidth=4, label='#interventions', color='blue')

plt.legend(fontsize=13)
ax.tick_params(axis='both', which='major', labelsize=13)
# ax.set_xscale('log')


# plt.xticks([10, 20,40, 80, 150, 300, 500, 750, 1000], ['10', '20','40', '80', '150', '300', '500', '750', '1K'])

plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0', '20','40', '60', '80', '100'])
plt.xticks([0.1,0.2, 0.3,0.4,0.5,0.6,0.7], [0.1,0.2, 0.3,0.4,0.5,0.6,0.7])

        #    rotation ='vertical')


plt.ylabel('Lists Percentage', fontsize=14, labelpad=-6)
plt.xlabel('Change Percentage (RBO)',labelpad=4, fontsize=13)

plt.title('Change % in Ranked Vehicles Lists', fontsize=14)

plt.xlim(0,0.7)


plt.subplots_adjust(left=0.14,
                    bottom=0.16,
                    right=0.95,
                    top=0.92,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
fig.set_size_inches( 4, 3.5)


scriptName = '40d'
fig.savefig('plots/'+scriptName+'.png') 
fig.savefig('plots/'+scriptName+'.eps') 