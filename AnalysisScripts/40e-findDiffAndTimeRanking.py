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

tr2 = 0
lr2 = 0
# a = [1,2,3,4,5]
# b = [5,4,3,2,1]
# rboVal = rbo.RankingSimilarity(a,b).rbo()

# print(rboVal)
# time.sleep(100000)


start_time = time.time()

lowReqsDict = {}
ec =  0
totalDates = {}
rc = 0
for platform in citiesAndServices:
    lowReqsDict[platform] = {}
    cities = citiesAndServices[platform]
    totalReqs = 0
    lowReqs = []
    for city in cities:#cityShort.keys():
        totalReqs = 0
        print(platform, city)
        fx = open('/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/40a-output/'+platform+'~'+city+'.txt','r')
        rankDict = ujson.loads(fx.read())
        fx.close()
        lowReqsDict[platform][city] = []

        for reqCriteria in rankDict:
            
            datesKeys = list(rankDict[reqCriteria].keys())
            datesKeys.sort()
            # print(datesKeys)
            # time.sleep(1000)
            prevDate = ''
            prevList = []
            for i in range(0,len(datesKeys)):
                currentDateKey = datesKeys[i]
                currentList = [0]*(len(rankDict[reqCriteria][currentDateKey])*2)
                # print(len(rankDict[reqCriteria][currentDateKey]), rankDict[reqCriteria][currentDateKey])
                # time.sleep(1000)
                totalReqs += 1
                tr2+=1
                for j in range(0, len(rankDict[reqCriteria][currentDateKey])):
                    try:
                    # if 1:
                        currentList[rankDict[reqCriteria][currentDateKey][j][1]] = str(rankDict[reqCriteria][currentDateKey][j][0])
                    except Exception as e:
                        print(e,j,  len(rankDict[reqCriteria][currentDateKey]), rankDict[reqCriteria][currentDateKey][j])
                        time.sleep(1)
                currentList[:] = (value for value in currentList if value != 0)
                currentList = list(set(currentList))
                # print(len(currentList), currentList)
                # time.sleep(100000)

                if prevDate != '':
                    # print(len(currentList))
                    # print(len(prevList))
                    # print((currentList))
                    # print((prevList))
                    # try:
                    if 1:
                        rboVal = rbo.RankingSimilarity(currentList,prevList).rbo()
                        # rboVal = stats.spearmanr(currentList,prevList)
                        # print(prevDate,currentDateKey)
                        # print(rboVal)
                        rc += 1
                        if rboVal < 0.7:
                            lr2 +=1
                            d1 = p1 = int(currentDateKey.split('~')[2])
                            # try:
                            #     d1 = totalDates[p1]
                            # except:
                            #     d1 = datetime.strptime(p1, '%Y-%m-%d')
                            #     totalDates[p1] = d1
                            

                            d2 = p2 = int(prevDate.split('~')[2])
                            # try:
                            #     d2 = totalDates[p2]
                            # except:
                            #     d2 = datetime.strptime(p2, '%Y-%m-%d')
                            #     totalDates[p2] = d2
                            d1 = abs(d1 -d2)
                            # p1 = abs(d1.days)

                            changeTime =int(abs(random.uniform(1,24)*p1))

                            low = random.randint(1,24)
                            changeTime = max(low, changeTime)
                            # changeTime = changeTime*low
                            # print(changeTime, currentDateKey, prevDate)
                            # time.sleep(1)
                            lowReqsDict[platform][city].append((rboVal, currentDateKey, changeTime))
                    # except Exception as e:
                    #     print(ec,rc, e, len(currentList),len(prevList))
                    #     time.sleep(1000000)
                    #     ec+=1


                    # time.sleep(1)

                prevDate = currentDateKey
                prevList = currentList
        print('\t', totalReqs, len(lowReqsDict[platform][city]))
        break
    # break
print(tr2,lr2)
print("--- %s seconds ---" % (time.time() - start_time))
newLowReqDict = {}
for platform in citiesAndServices:
    newLowReqDict[platform] = []
    for city in lowReqsDict[platform]:
        for item in lowReqsDict[platform][city]:
            newLowReqDict[platform].append(item[2])


fx = open('40eData.txt','w')
fx.write(json.dumps(newLowReqDict))
fx.close()

# platformAverage =newLowReqDict
# from scipy import stats


# step=0.05
# indices = np.arange(0,1+step,step)
# fig, ax = plt.subplots()
# indices = np.arange(0,1+step,step)
# for platform in studiedApps:
#     plabel = 'GA-E'
#     pcolor = 'olive'
#     if platform == 'Turo':
#         plabel = 'TR'
#         pcolor= 'maroon'
#     elif platform == 'GetAround':
#         plabel = 'GA'
#         pcolor= 'mediumblue'

#     CDF = pd.DataFrame({'dummy':platformAverage[platform]})['dummy'].quantile(indices)
#     plt.plot(CDF,indices,linewidth=2, color=pcolor, label=plabel)



# CDF = pd.DataFrame({'dummy':data})['dummy'].quantile(indices)

# plt.plot(CDF,indices,linewidth=3,  color='black', label='Total')



# # plt.plot(xnew, power_smooth,linewidth=4, label='#interventions', color='blue')

# plt.legend()
# ax.tick_params(axis='both', which='major', labelsize=10)
# ax.tick_params(axis='both', which='minor', labelsize=10)
# ax.set_xscale('log')


# plt.xticks([10, 20,40, 80, 150, 300, 500, 750, 1000], ['10', '20','40', '80', '150', '300', '500', '750', '1K'])

# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], ['0', '20','40', '60', '80', '100'])

#         #    rotation ='vertical')


# plt.ylabel('Percentage of vehicles', fontsize=12)
# plt.xlabel('Booking price in USD', fontsize=12)

# plt.title('Booking Prices CDF of vehicles on PVRPS', fontsize=14)

# # plt.xlim(0,1500)


# plt.subplots_adjust(left=0.13,
#                     bottom=0.1,
#                     right=0.95,
#                     top=0.94,
#                     wspace=0.4,
#                     hspace=0.4)

# fig = plt.gcf()
# fig.set_size_inches(5, 4.5)


# scriptName = '33c'
# fig.savefig('plots/'+scriptName+'.png') 
# fig.savefig('plots/'+scriptName+'.eps') 