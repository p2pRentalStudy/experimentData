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
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from PIL import Image

gauth = GoogleAuth()       
drive = GoogleDrive(gauth) 
 

for platform in studiedApps:
    imagesPath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/carImages/'+platform+'/'
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
        if fc>9600:
            basewidth = 300
            try:
                # if fc%100 == 0 or gauth.access_token_expired:
                #     # Refresh them if expired
                #     # printGoogle Drive Token Expired, Refreshing"
                #     gauth.Refresh()
                #     drive = GoogleDrive(gauth)  

                img = Image.open(filePath)
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                img.save(imagesPath+'resized_image.jpg')
                gfile = drive.CreateFile({'title': platform+'~'+fileName, 'parents': [{'id': '1ffOTa_fvCqi9SAfosqaxwUaOwqv69ItX'}]})
                # Read file and set it as the content of this instance.
                gfile.SetContentFile(imagesPath+'resized_image.jpg')
                gfile.Upload() # Upload the file.
            except Exception as e:
                print('\t', fc, e)
            # time.sleep(0.01)

        
        
