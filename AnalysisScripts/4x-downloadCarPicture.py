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
# studiedApps['GetAround'] = 1

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/1-output/data/APPNAME/'

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


for platform in studiedApps:
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)
    tempFolder2 = targetFolder.replace('APPNAME',platform)
    tempFolder2 = tempFolder2.replace('1-','0-')



    saveImagePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/carImages/APPNAME/'

    saveImagePath = saveImagePath.replace('APPNAME',platform)

    

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    # print(filenames)
    
    for fileName in filenames:
        cityName = fileName.split('-')[0]
        print(platform, cityName)
        # 
        totalIDsPics = {}

        try:
            fx = open(tempFolder+fileName,'r')
            content = json.loads(fx.read())
            fx.close()
            
            carCount = 0
            # for country in content.keys():
            #     for city in content[country].keys():
            for id in content:
                for date in content[id]:
                    car = content[id][date]
                    # print(country, city, id, car)
                    # print('Sleeping')
                    # time.sleep(1000)

                    carId = car['id']
                    carPicUrl= car['image']
                    carName = car['model']
                    # print(car.keys())
                    # # time.sleep(1000)
                    if carPicUrl is None or len(carPicUrl) < 7:
                        carPicUrl = 'https://cdn.pixabay.com/photo/2017/11/10/05/48/user-2935527_960_720.png 1x, https://cdn.pixabay.com/photo/2017/11/10/05/48/user-2935527_1280.png'
                    # if carCount > 7:
                    #     print(carId, carPicUrl, carName)
                    #     print('Sleeping')
                    #     time.sleep(1000)
                    try:
                        imgURL = carPicUrl
                        carId = cityName+'~'+carName+'~'+str(carId)
                        try:
                            val = totalIDsPics[carId]
                        except:
                            totalIDsPics[carId] = 1
                            
                            if ':' in imgURL:
                                img_data = requests.get(imgURL).content
                                with open(saveImagePath+carId+'.jpg', 'wb') as handler:
                                    handler.write(img_data)
                            if carCount % 10 == 1:
                                print('\t', platform, carCount)
                            carCount += 1
                            time.sleep(0.1)
                    except Exception as e:
                        pass
                        # print(e)
                        # time.sleep(1000)

                    break
            print('\t total cars',len(totalIDsPics.keys()))
        except Exception as e:
            print(e)
