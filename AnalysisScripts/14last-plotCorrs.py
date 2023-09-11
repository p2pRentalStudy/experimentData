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


studiedApps = {}
# studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1


targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/14-output/data/APPNAME/'


totalTranslatedReviews = {}
carPrices = {}




for platform in studiedApps:
    
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        attribute = 'average rating'
        print(platform, cityName, attribute)
        cityCorrelation = []

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
e = [0.5, 1., 1.5, 2.]
plt.errorbar(x, y, yerr=e, fmt='o')
plt.title('Heatmap of averave booking of vehicles (price/day in USD)')
plt.subplots_adjust(left=0.08,
                    bottom=0.13,
                    right=1.03,
                    top=0.95,
                    wspace=0.4,
                    hspace=0.4)

fig = plt.gcf()
fig.set_size_inches(7, 7.5)

scriptName = '13d'
fig.savefig('plots/'+scriptName+'-heatmapPrice.png') 
fig.savefig('plots/'+scriptName+'-heatmapPrice.eps') 