import tempfile
from basicImports import *
from os import walk


full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)


while 1:
    carsIDsDict = {}
    carsIDsDict['apps'] = {}
    carsIDsDict['apps']['GerAroundEurope'] = {}
    carsIDsDict['apps']['GerAroundEurope']['lastReadDate'] = ''
    carsIDsDict['apps']['GerAroundEurope']['carIDs'] = {}

    carsIDsDict['apps']['GetAround'] = {}
    carsIDsDict['apps']['GetAround']['lastReadDate'] = ''
    carsIDsDict['apps']['GetAround']['carIDs'] = {}

    carsIDsDict['apps']['Turo'] = {}
    carsIDsDict['apps']['Turo']['lastReadDate'] = ''
    carsIDsDict['apps']['Turo']['carIDs'] = {}





    apps = [
        'GerAroundEurope', 
        'GetAround', 
        'Turo'
        ]

    now = datetime.now()
    currentDate = now + timedelta(hours=1)
    currentDate = str(currentDate).split(' ')[0]
    # print(currentDate)
    # time.sleep(1000)
    ownersIDs = {}
    ownersIDs['Turo'] = {}
    ownersIDs['GetAround'] = {}


    for app in apps:
        print(app)
        newAdress = dpath+'/../'+app+'/vehiclesList'
        # filenames = next(walk(newAdress), (None, None, []))[2]  # [] if no file
        filenames = os.listdir(newAdress)
        # print('\t', newAdress)
        filenames.sort()
        for fileName in filenames:
            if '.txt' in fileName:
                tempFn = fileName[:]
                # print('\t', fileName)
                fileName = fileName.split('oded-')[1]
                fileName = fileName.replace('.txt', '')
                if fileName < currentDate:# and fileName > carsIDsDict['apps'][app]['lastReadDate']:
                    print('\t\t',tempFn)
                    fx = open(newAdress+'/'+tempFn,'rb')
                    data = b''
                    data = fx.read()
                    fx.close()
                    myRecords = data.split(b'0x0A')


                    #read exisiting dictionary
                    # fx = open('readIDS.txt','r')
                    # data = fx.read()
                    # fx.close()

                    # if len(json.dumps(data)) < len(json.dumps(carsIDsDict)):
                    #     fx = open('readIDS.txt','w')
                    #     fx.write(json.dumps(carsIDsDict))
                    #     fx.close()
                    # else:
                    #     carsIDsDict = json.loads(data)
                    success = 0
                    
                    for currentRecord in myRecords:
                        # if 1:
                        try:
                            str_object2 = zlib.decompress(currentRecord)
                            mystr = str_object2.decode()
                            requestData = mystr.replace('\\\\"',' ')
                            requestData = json.loads(requestData)
                            success += 1
                            # print(requestData.keys())
                            # time.sleep()
                            for key in requestData:
                                if '~' in key:
                                    item = requestData[key]
                                    # print('\n\n', key, item)
                                    # print(item.keys())

                                    carKey = ''
                                    if app == 'GerAroundEurope':
                                        carKey = 'cars'
                                    elif app == 'GetAround':
                                        carKey = 'cars'
                                    elif app == 'Turo':
                                        carKey = 'list'
                                    totalCars = item[carKey]
                                    keyItems = key.replace('%2F','-')
                                    keyItems = keyItems.split('~')
                                    # print(keyItems)
                                    keyStructureDict = {}
                                    keyStructureDict['collectionDate'] = fileName
                                    keyStructureDict['country'] = keyItems[0]
                                    keyStructureDict['city'] = keyItems[1]
                                    keyStructureDict['startDate'] = keyItems[3]
                                    keyStructureDict['endDate'] = keyItems[4]
                                    keyStructureDict['page'] = '1'
                                    keyStructureDict['priceMin'] = '-1'
                                    keyStructureDict['priceMax'] = '-1'

                                    if 'Europe' in app:
                                        keyStructureDict['page'] = keyItems[5]
                                    elif 'Turo' in app:
                                        keyStructureDict['priceMin'] = keyItems[5]
                                        keyStructureDict['priceMax'] = keyItems[6]

                                    # print(keyStructureDict, len(totalCars))
                                    # print(' \n\n')
                                    for car in totalCars:
                                        # print(car)
                                        # time.sleep(300)
                                        vehicleID = keyStructureDict['city']+'#'
                                        if 'Turo' in app:
                                            ownersIDs[app][vehicleID+str(car['owner']['id'])] = 1
                                            vehicleID += str(car['vehicle']['id'])
                                            

                                        elif 'Europe' in app:
                                            vehicleID += str(car['id'])
                                            abc = 1
                                        else:
                                            ownersIDs[app][vehicleID+str(car['owner_id'])] = 1
                                            vehicleID += str(car['car_id'])
                                            
                                        carsIDsDict['apps'][app]['carIDs'][vehicleID] = car
                                        # print(vehicleID, car.keys())
                                        
                                        # time.sleep(10000)
                        except Exception as e:
                            e = str(e)
                            if 'stream' not in e:
                                print('\tEXCEPTION!!',success, e)  
                        
                        # carsIDsDict['apps'][app]['lastReadDate'] = fileName
                        # fx = open('readIDS.txt','w')
                        # fx.write(json.dumps(carsIDsDict))
                        # fx.close()
            # break
    # print(carsIDsDict)
    for app in carsIDsDict.keys():
        print(app, len(carsIDsDict[app].keys()))
    fx = open('readIDS.txt','w')
    fx.write(json.dumps(carsIDsDict))
    fx.close()


    fx = open('ownerIDs-TuroAndGetAround.txt','w')
    fx.write(json.dumps(ownersIDs))
    fx.close()
    print('Sleeping after reading ids\n\n')
    time.sleep(10000)