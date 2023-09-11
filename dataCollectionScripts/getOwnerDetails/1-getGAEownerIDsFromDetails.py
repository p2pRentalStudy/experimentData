from basicImports import *
import requests
import random
import string
from os import walk


#Read only ids from getAroundEurope files and add those ids in the readCarID owner dict, and save in this folder


readOwnersDict = {}
fx = open('/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/GerCarIDs/ownerIDs-TuroAndGetAround.txt','r')

readOwnersDict = json.loads(fx.read())

fx.close()

readOwnersDict['GerAroundEurope'] = {}

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/getCarDetails/carDetails/'

filenames = next(walk(targetFolder), (None, None, []))[2]  # [] if no file

filenames.sort()

newFileNames = []

# for id in readOwnersDict['Turo']:
#     print(id)
#     time.sleep(1000)


for fn in filenames:
    if 'GerAroundEurope#' in fn:
        newFileNames.append(fn)
print('GerAroundEurope files', len(newFileNames)) 


for fn in newFileNames:
    nfn = targetFolder+fn
    # print(nfn)
    fx = open(nfn,'rb')
    data = b''
    data = fx.read()
    fx.close()

    str_object2 = zlib.decompress(data)
    mystr = str_object2.decode()
    requestData = mystr.replace('\\\\"',' ')
    requestData = json.loads(requestData)
    requestData = requestData['sections']

    for item in requestData:
        try:
            if item['header'] == 'Owner':
                for item2 in item['items']:
                    try:
                        carId = str(item2['id'])
                        cityName = fn.split('#')[1]
                        carId = cityName+'#'+carId
                        # print(carId)
                        readOwnersDict['GerAroundEurope'][carId] = 1
                    except:
                        pass
            # requestData['header'][1]['items'][0]['id']
        except:
            pass


    # time.sleep(1000)
print(len(readOwnersDict['GerAroundEurope']))
fx = open('newOwnerIds.txt','w')
fx.write(json.dumps(readOwnersDict))
fx.close()