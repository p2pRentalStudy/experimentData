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
studiedApps['GerAroundEurope'] = 1

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/3-output/APPNAME/'

def readCars(content, platform):
    carsDict = {}
    content = content[platform]
    # for country in content.keys():
    #     for city in content[country].keys():
    for date in content:
        for id in content[date]:
            car = content[date][id]
            carsDict[id] = car

    return carsDict

totalReview = {}
for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    tempFolder2 = targetFolder.replace('APPNAME',platform)
    tempFolder2 = tempFolder2.replace('1-','0-')



    saveImagePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/reviewerImages/APPNAME/'

    saveImagePath = saveImagePath.replace('APPNAME',platform)


    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()


    print('Total Files', len(filenames))
    # time.sleep(1000)
    # print(filenames)
    totalIDsPics = {}
    
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName)
        # try:
        if 1:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            
            carCount = 0
            # content = content[platform]
            # for country in content.keys():
            #     for city in content[country].keys():
            for id in content:
                for date in content[id]:
                    # print(content[id].keys())
                    # time.sleep(10000)
                    carData = content[id][date]
                    if 1:#'Ger' in platform:
                        carData = carData[id]
                    for author in carData:
                        # print(carData)
                        # print(author)
                        carId = date
                        totalReview[str(author['reviewDate'])] = 1
                        authorID = author['autorId']
                        authorPicUrl= author['authorImage']
                        authorName = author['authorName']
                        if authorPicUrl is None or len(authorPicUrl) < 7:
                            authorPicUrl = 'https://cdn.pixabay.com/photo/2017/11/10/05/48/user-2935527_960_720.png 1x, https://cdn.pixabay.com/photo/2017/11/10/05/48/user-2935527_1280.png'
                        # if carCount > 7:
                        #     print(cityName, carId, authorPicUrl, authorName)
                        #     print('Sleeping')
                        #     time.sleep(1000)
                        try:
                        # if 1:=
                            imgURL = authorPicUrl
                            carId =  cityName+'~'+authorName+'~'+str(authorID)
                            try:
                                val = totalIDsPics[carId]
                                # print('coming here')
                            except:
                            # if 1:
                                totalIDsPics[carId] = 1
                                
                                if ':' in imgURL:
                                    # ijk = 1
                                    img_data = requests.get(imgURL).content
                                    # carId += '~'+cityName
                                    with open(saveImagePath+carId+'.jpg', 'wb') as handler:
                                        handler.write(img_data)
                                    carCount += 1
                                if carCount % 100 == 1:
                                    print('\t', platform, carCount)
                                # carCount += 1
                                # time.sleep(0.1)
                        except Exception as e:
                            # pass
                            print(2, e)
                            # time.sleep(1000)

print('\t total auhtors',len(totalIDsPics.keys()))
print(len(totalReview.keys()))
# except Exception as e:
#     print(e)
