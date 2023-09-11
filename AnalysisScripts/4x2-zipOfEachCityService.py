from basicImports import *
import requests
import random
import string
from os import walk
import requests # request img from web
import shutil # save img locally

import urllib.request


studiedApps = {}
studiedApps['Turo'] = 1
studiedApps['GerAroundEurope'] = 1
studiedApps['GetAround'] = 1

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'


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

import shutil
import tarfile
import glob


for platform in studiedApps:
    imagesPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/carImages/'+platform+'/'
    targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/carImages/temp/'
    filenames = next(walk(imagesPath), (None, None, []))[2]  # [] if no file
    filenames.sort()
    # print(platform, len(filenames))
    carCount = 0
    copied = 0
    tar = None
    for city in cities:
        copied = 0
        for fileName in filenames: 
            fileCity = fileName.split('~')[0]
            if city == fileCity:
                # shutil.copy(imagesPath+fileName, targetFolder+fileName)
                copied += 1
                # print(platform, city, copied)
                if copied == 1:
                    tar = tarfile.open('/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/carImagesTemp/'+platform+'~'+city+'.tar.gz', 'w:gz')
                if copied > 0:
                    tar.add(imagesPath+fileName)
        print(platform, city, copied)
        if copied > 0:
            print(platform, city, copied)
            tar.close()
            #delete temp
            # files = glob.glob(targetFolder)
            # for f in files:
            #     os.remove(f)
            # #create temp
            # os.mkdir(targetFolder)
    #         break
    # if copied > 0:
    #     break
    

        
