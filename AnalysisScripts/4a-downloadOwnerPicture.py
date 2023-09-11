from basicImports import *
import requests
import random
import string
from os import walk
import requests # request img from web
import shutil # save img locally

import urllib.request


studiedApps = {}
# studiedApps['GerAroundEurope'] = 1
# studiedApps['GetAround'] = 1
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


for platform in studiedApps:
    listData = {}
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
            print(len(content.keys()))
            for id in content:
                # print(id, content[id])
                dates = list(content[id].keys())
                dates.sort()
                date = dates[0]
                car = content[id][date]

                ownerId = car['ownerID']
                if 'Europe' in platform:
                    # print(carsDict[str(id)])
                    try:
                        ownerPicUrl= carsDict[str(id)]['ownerPic']
                    except:
                        try:
                            ownerPicUrl= car['ownerPic']
                        except:
                        # print(ownerPicUrl)
                            ownerPicUrl = None
                else:
                    ownerPicUrl= car['ownerPic']

                ownerName = car['ownerName']
                if ownerPicUrl is None or len(ownerPicUrl) < 16:
                    ownerPicUrl = 'https://cdn.pixabay.com/photo/2017/11/10/05/48/user-2935527_960_720.png'
                
                if 1:
                # try:
                    imgURL = ownerPicUrl
                    ownerId = cityName+'~'+ownerName+'~'+str(ownerId)
                    # print(ownerId, imgURL)
                    ownerId = ownerId.replace('/',' ')
                    try:
                        val = totalIDsPics[ownerId]
                    except:
                        totalIDsPics[ownerId] = 1
                        
                        if ':' in imgURL:
                            try:
                                img_data = requests.get(imgURL).content
                                with open(saveImagePath+ownerId+'.jpg', 'wb') as handler:
                                    handler.write(img_data)
                            except:
                                print('Excetion', ownerCount)
                                time.sleep(1)
                                    
                            # print('Sleeping')
                            # time.sleep(1000)
                        if ownerCount % 100 == 1:
                            print('\t\t\t', platform, ownerCount)
                            # ownerIDs[ownerId] = 1
                        ownerCount += 1
                        time.sleep(0.1)
                # except Exception as e:
                #     pass
                    # print(e)
                    # time.sleep(1000)

            print('\t\t total owners',len(totalIDsPics.keys()))
            # time.sleep(100000)
            # if len(totalIDsPics.keys()) > 10:
            #     time.sleep(1000)
        # except Exception as e:
        #     print(e)
