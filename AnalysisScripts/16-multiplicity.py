from basicImports import *
import requests
import random
import string
from os import walk
import requests # request img from web
import shutil # save img locally
import urllib.request
import matplotlib as mpl
# mpl.style.use('v2.0')
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches


def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]

studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GetAround'] = 1
studiedApps['GerAroundEurope'] = 1

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'
def empirical_cdf(s: pd.Series, n_bins: int = 100):
    # Sort the data into `n_bins` evenly spaced bins:
    discretized = pd.cut(s, n_bins)
    # Count the number of datapoints in each bin:
    bin_counts = discretized.value_counts().sort_index().reset_index()
    # Calculate the locations of each bin as just the mean of the bin start and end:
    bin_counts["loc"] = (pd.IntervalIndex(bin_counts["index"]).left + pd.IntervalIndex(bin_counts["index"]).right) / 2
    # Compute the CDF with cumsum:
    return bin_counts.set_index("loc").iloc[:, -1].cumsum()

cityColors = {}
cityColors['Barcelona'] = 'black'
cityColors['Berlin'] = 'grey'
cityColors['Hamburg'] = 'rosybrown'
cityColors['Liverpool'] = 'maroon'
cityColors['London'] = 'tomato'
cityColors['Lyon'] = 'sandybrown'
cityColors['Madrid'] = 'darkorange'
cityColors['Paris'] = 'goldenrod'
cityColors['Las Vegas'] = 'khaki'
cityColors['Los Angeles'] = 'olive'
cityColors['Miami'] = 'darkseagreen'
cityColors['New York City'] = 'turquoise'
cityColors['Washington D.C.'] = 'teal'
cityColors['Ottawa'] = 'slateblue'
cityColors['Toronto'] = 'purple'

cityShort = {}
cityShort['Barcelona'] = 'BAR'
cityShort['Berlin'] = 'BER'
cityShort['Hamburg'] = 'HAM'
cityShort['Liverpool'] = 'LPL'
cityShort['London'] = 'LDN'
cityShort['Lyon'] = 'LYN'
cityShort['Madrid'] = 'MAD'
cityShort['Paris'] = 'PAR'
cityShort['Las Vegas'] = 'LAS'
cityShort['Los Angeles'] = 'LAX'
cityShort['Miami'] = 'MAI'
cityShort['New York City'] = 'NYC'
cityShort['Washington D.C.'] = 'WDC'
cityShort['Ottawa'] = 'OTW'
cityShort['Toronto'] = 'TRT'

platformLineStyle = {}
platformLineStyle['Turo'] = '.'
platformLineStyle['GetAround'] = 'v'
platformLineStyle['GerAroundEurope'] = 's'

platformShort = {}
platformShort['Turo'] = 'TR'
platformShort['GetAround'] = 'GA'
platformShort['GerAroundEurope'] = 'GE'

citiesCDF = []

alphaLevel = 0
for platform in studiedApps:
    alphaLevel += 0.1
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    # print(filenames)

    for fileName in filenames:
        cityName = fileName.split('-')[0]

        #
        totalIDsPics = {}
        if cityName != 'New York':
            print(platform, cityName)
            try:
                fx = open(tempFolder+fileName,'r')
                content = json.loads(fx.read())
                fx.close()

                carCount = 0
                cityCarOwnersDict = {}
                # for country in content.keys():
                #     for city in content[country].keys():
                for id in content:
                    dates = list(content[id])
                    dates.sort()
                    for date in dates:
                        car = content[id][date]

                        carId = car['id']
                        ownerID = car['ownerID']
                        try:
                            var = cityCarOwnersDict[ownerID]
                        except:
                            cityCarOwnersDict[ownerID] = {}

                        try:
                            cityCarOwnersDict[ownerID][carId] = int(car['numberOfTrips'])
                        except:
                            cityCarOwnersDict[ownerID][carId]  = 0
            #             print(ownerID, carId, cityCarOwnersDict[ownerID][carId])
            #             time.sleep(1000)
            except:
                pass
            singleOwner = []
            multiOwner = []
            totalOwnersCDF = []
            for owner in cityCarOwnersDict:
                totalTrips = 0
                totalCars = len(cityCarOwnersDict[owner])
                tripsPerCar = []
                totalOwnersCDF.append(totalCars)
                for car in cityCarOwnersDict[owner]:
                    totalTrips += cityCarOwnersDict[owner][car]
                    tripsPerCar.append(cityCarOwnersDict[owner][car])

                tripsPerCar = sum(tripsPerCar)/len(tripsPerCar)

                if totalCars > 1:
                    multiOwner.append(tripsPerCar*totalCars)
                else:
                    singleOwner.append(tripsPerCar)
            print('\t',np.average(singleOwner),sum(singleOwner),'    ',np.average(multiOwner), sum(multiOwner))


            #owned CDF
            totalOwnersCDF.sort()

            citiesCDF.append((platform, cityName, totalOwnersCDF, alphaLevel))

for item in citiesCDF:
    alphaLevel = item[3]
    totalOwnersCDF = item[2]
    cityName = item[1]
    platform = item[0]
    x, y = ecdf(totalOwnersCDF)
    x = np.insert(x, 0, x[0])
    y = np.insert(y, 0, 0.)
    plt.plot(x, y, drawstyle='steps-post', lw=2, marker = platformLineStyle[platform], color = cityColors[cityName], alpha=alphaLevel)
    plt.grid(True)
    # plt.savefig('ecdf.png')

    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/16-output/'

# handles, labels = plt.gca().get_legend_handles_labels()

newCityColorLines = []
for key in cityColors:
    line = Line2D([0], [0], label=cityShort[key], color=cityColors[key])
    newCityColorLines.append(line)

# handles.extend(newCityColorLines)
# plt.legend(handles=handles)


first_legend = plt.legend(handles=newCityColorLines, loc=4)
ax = plt.gca().add_artist(first_legend)

# Create another legend for the second line.

platformLines = []
for key in platformLineStyle:
    line = Line2D([0], [0], label=platformShort[key], color='purple', marker=platformLineStyle[key])
    platformLines.append(line)

# best'	0
# 'upper right'	1
# 'upper left'	2
# 'lower left'	3
# 'lower right'	4
# 'right'	5
# 'center left'	6
# 'center right'	7
# 'lower center'	8
# 'upper center'	9
# 'center'	10
plt.legend(handles=platformLines, loc=8)


xmax = 40
plt.ylim([0.6,1])
plt.xlim([0.5,xmax])
plt.xticks(np.arange(1, xmax, step=2))
# plt.xticks([1, 2,3,4,5,6,7,8,9,10,11,12,], ['January', 'February', 'March'],rotation=20)
# plt.savefig(savePath+platform+'-'+cityName+'.png')
plt.savefig(savePath+'totalOwnerCDF.png')
# plt.clf()
# break
