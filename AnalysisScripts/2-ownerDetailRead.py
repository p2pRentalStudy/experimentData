from basicImports import *
import requests
import random
import string
from os import walk


studiedApps = {}
studiedApps['Turo'] = 1



targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/getOwnerDetails/ownerDetails'

def writeCityRecords(currentCity, listData):

    savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/2-output/'+platform+'/'

    fx = open(savePath+currentCity+'-content.txt','w')
    fx.write(json.dumps(listData[platform][currentCity]))
    fx.close()

    return 0

totalFiles = []
for root, dirs, files in os.walk(targetFolder):
     for file in files:
        totalFiles.append(os.path.join(root, file))
print('Total Files', len(totalFiles))
# time.sleep(1000)
listData = {}
currentCity = ''

def convert(obj):
    if type(obj) == list:
        for x in obj:
            convert(x)
    elif type(obj) == dict:
        for k, v in obj.items():
            if v is None:
                obj[k] = 5
            else:
                convert(v)

for platform in studiedApps:
    listData[platform] = {}
    res = [i for i in totalFiles if platform+'#' in i]
    newRes = {}
    for fn in res:
        if platform in fn:
            fn1 = fn.split('/')
            
            fn1 = fn1[5:]
            # print(fn1)
            for part in fn1:
                if '.txt' in part:
                    newRes[part] = fn
            # newRes.append(fn)
    
    res=list(newRes.keys())
    res.sort()

    print(platform, len(res), 'files')
    filesChecked = 0
    if 1: 
        for file in res:
            file = newRes[file]

            if '.txt' in file:
                
                fileContent = open(file, 'rb').read()


                fileContent = zlib.decompress(fileContent)
                # print(item)
                fileContent = json.loads(fileContent)

                partsOfKey = file.split('/')[-1]
                partsOfKey = partsOfKey.split('#')

                city = partsOfKey[1]
                ownerID = partsOfKey[2]
                recordDate = partsOfKey[3]
                recordDate = recordDate.replace('.txt', '')

                recordCity = city
                if recordCity != currentCity:
                    if currentCity != '':
                        print('saving for', currentCity)
                        writeCityRecords(currentCity,listData)
                        listData[platform] = {}
                    currentCity = recordCity

                try:
                    v1 = listData[platform][city]
                except: 
                    listData[platform][city] = {}

                try:
                    v1 = listData[platform][city][ownerID]
                except: 
                    listData[platform][city][ownerID] = {}

                try:
                    v1 = listData[platform][city][ownerID][recordDate]
                except: 
                    listData[platform][city][ownerID][recordDate] = {}


                ownerData = {}
                
                # fx = open('temp.txt','w')
                # fx.write(json.dumps(fileContent))
                # fx.close()
                if 'Turo' in platform:

                    ownerData['id'] = fileContent['driver']['id']

                    ownerData['alsoArententer'] = fileContent['approvedToDrive']
                   
                    ownerData['image'] = fileContent['driver']['image']['originalImageUrl']

                    ownerData['name'] = fileContent['driver']['name']

                    ownerData['ownerProfileLink'] = fileContent['driver']['url']
                    try:
                        ownerData['location'] = fileContent['locations'][0]['address']
                    except:
                        ownerData['location'] = 'NA'

                    ownerData['listingsStarted'] = str(fileContent['memberSince']['month'])+'-01-'+str(fileContent['memberSince']['year'])

                    
                    ownerData['totalTrips'] = fileContent['numberOfRentalsFromCarOwners']+fileContent['numberOfRentalsFromRenters']

                    ownerData['ratingCount'] = fileContent['numberOfRatingsFromRenters'] + fileContent['numberOfRatingsFromCarOwners']

                    # for keyItem in []
                    # if fileContent[keyItem] is None:
                    #     fileContent['] = 1
                    # convert(fileContent)
                    try:
                        ownerData['averageRating'] = (fileContent['ratingsFromRenters']['overall']*fileContent['numberOfRatingsFromRenters'])/(fileContent['numberOfRatingsFromRenters'] + fileContent['numberOfRatingsFromCarOwners']) + (fileContent['ratingsFromCarOwners']['overall']*fileContent['numberOfRatingsFromCarOwners'])/(fileContent['numberOfRatingsFromRenters'] + fileContent['numberOfRatingsFromCarOwners'])
                    except:
                        ownerData['averageRating'] = 'NA'

                    try:
                        ownerData['responseRate'] = fileContent['responseRate']
                    except:
                        ownerData['responseRate'] =  'NA'

                    try:
                        ownerData['responseTime'] = fileContent['responseTime']['value']
                    except:
                        ownerData['responseTime'] =  'NA'
                    ownerData['verifications'] = []

                    for verification in fileContent['verifications']:
                        ownerData['verifications'].append(verification['verificationType'])

                    ownerData['vehicles'] = []

                    ownerData['totalOfferedVehicles'] = len(fileContent['vehicles'])

                    for vehicle in fileContent['vehicles']:
                        tempVehicle = {}
                        tempVehicle['id'] = vehicle['id']
                        tempVehicle['automaticTransmission'] = vehicle['automaticTransmission']
                        tempVehicle['image'] = vehicle['image']['originalImageUrl']
                        tempVehicle['listingCreatedTime'] = vehicle['listingCreatedTime']
                        tempVehicle['make'] = vehicle['make']
                        tempVehicle['model'] = vehicle['model']
                        tempVehicle['numberPlate'] = vehicle['registration']['licensePlate']
                        tempVehicle['type'] = vehicle['type']
                        tempVehicle['year'] = vehicle['year']
                        ownerData['vehicles'].append(tempVehicle)

                elif 'Europe' in platform:
                    
                    # fx = open('temp.txt','w')
                    # fx.write(json.dumps(fileContent))
                    # fx.close()
                    # filesChecked += 1


                    # if filesChecked > 15:
                    #     print(filesChecked,'sleeping')
                    #     time.sleep(1000)
                    # else:
                    #     pass
                        
                    ownerData['id'] = fileContent['id']
                    ownerData['totalOfferedVehicles'] = fileContent['display_car_count']

                    ownerData['alsoArententer'] = -1
                   
                    ownerData['image'] = fileContent['avatar']['thumb_url']

                    ownerData['name'] = fileContent['display_name']

                    ownerData['ownerProfileLink'] = -1

                    ownerData['location'] = -1

                    ownerData['listingsStarted'] = fileContent['member_since_item']['detail_text']

                    ownerData['totalTrips'] = fileContent['display_rental_count']

                    ownerData['averageRating'] = fileContent['stats']['ratings_average']

                    ownerData['ratingCount'] = fileContent['stats']['ratings_count']

                    ownerData['responseRate'] = -1
                    ownerData['responseTime'] = -1

                    ownerData['verifications'] = []

                    ownerData['vehicles'] = []

                listData[platform][city][ownerID][recordDate] = ownerData


    writeCityRecords(currentCity,listData)
    listData[platform] = {}