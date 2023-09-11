from basicImports import *
import requests
import random
import string
from os import walk
import requests # request img from web
import shutil # save img locally

import urllib.request


studiedApps = {}
# studiedApps['Turo'] = 1
# studiedApps['GerAroundEurope'] = 1
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
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from PIL import Image


for platform in studiedApps:
    imagesPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/carImages/'+platform+'/'
    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/carImagesSmall/'
    filenames = next(walk(imagesPath), (None, None, []))[2]  # [] if no file
    filenames.sort()
    print(platform, len(filenames))
    fc = 0
    for fileName in filenames: 
        fc += 1
        if fc%200 == 0:
            print('\t\t', fc, 'files uplaoded')
            # print('sleeping here')
            # time.sleep(1000)
        filePath = imagesPath+fileName
        if fc>-1:
            basewidth = 300
            try:
                img = Image.open(filePath)
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                img.save(savePath+platform+'~'+fileName+'.jpg')
                
            except Exception as e:
                print('\t', fc, e)
            # time.sleep(0.01)

        
        
