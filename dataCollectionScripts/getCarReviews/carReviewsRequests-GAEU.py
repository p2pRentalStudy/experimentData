from basicImports import *
import requests
import random
import string

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)


apps = [
    'GerAroundEurope', 
    # 'GetAround', 
    # 'Turo'
]


def getCarDetails(app, carIds, reqContent):
    
    myProxies1 = ['51.81.45.244:8800', '31.40.225.36:8800', '193.168.180.43:8800', '212.115.61.44:8800', '212.115.61.178:8800', '193.168.180.26:8800', '51.81.45.158:8800', '51.81.45.227:8800', '142.214.182.9:8800', '193.168.180.144:8800', '212.115.61.29:8800', '192.126.252.65:8800', '31.40.225.32:8800', '142.214.182.48:8800', '192.126.252.26:8800', '31.40.225.35:8800', '142.214.182.28:8800']
    
    #'178.212.190.67:12323', '178.212.190.2:12323', 

    myProxies2 = [ '193.37.55.98:8800', '185.218.148.255:8800', '193.37.52.30:8800', '185.218.148.63:8800', '185.218.148.223:8800', '179.43.135.60:8800', '193.37.55.95:8800', '193.37.52.167:8800', '185.218.148.129:8800', '179.43.135.68:8800']

    if 'Europe' in app:
        myProxies = myProxies1
    else:
        myProxies = myProxies2
    
    proxyIndex = 0
    # reqContent[app] = {}

    headers = {
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M)',
    'accept-encoding': 'gzip'
    }

    requestURL = ''
    if 'Turo' in app:
        #request to be added 
        headers['user-agent'] = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC)Turo/22.25.0'
        headers['accept-language'] = 'en-US'
        requestURL = 'https://api.turo.com/api/vehicle/reviews?vehicleId=TBA1&page=TBA2'
            
    elif 'Europe' in app:
        identifierTemplate = '96795b08-0deb-4d88-ac33-f4bcdeffd58f'
        
        randInt = random.randint(0, len(identifierTemplate)-3)
        if identifierTemplate[randInt] == '-':
            randInt += 1
        identifier = identifierTemplate[:randInt]+ random.choice(string.ascii_letters)+identifierTemplate[randInt+1:]

        headers['x_vl_authorization']= 'cf4d2f5591763483bf1f258c5820e411'
        headers['drivy-user-identifier']= identifier

        requestURL = 'https://api-eu.getaround.com/api/v1/cars/TBA1/reviews'
                        

    idcount = 0
    for carId in carIds:
        pageNumber = 1
        if 'Turo' in app and idcount%1000 == 0:
            fx = open('/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/Turo/oauthToken.txt','r')
            requestToken = fx.read()
            fx.close
            # print(requestToken)
            # time.sleep(100)
            headers['authorization']= ''+requestToken

            # print(headers)
            # time.sleep(100)

        proxyIndex = (proxyIndex+1) % len(myProxies)
        proxy = myProxies[proxyIndex]
        if 'Europe1' in app: 
            currentProxy = {"http": 'https://14a6567036982:cde0271484@'+proxy, "https": 'https://14a6567036982:cde0271484@'+proxy}
        else:
            currentProxy = {"http": proxy, "https": proxy}
        

        city, id = carId.split('#')[0], carId.split('#')[1]
        thisRequestURL = requestURL

        #make request
        if thisRequestURL != '':
            thisRequestURL = requestURL
            idcount += 1

            if idcount % 1000 == 0:
                print('\t\t\t', idcount,' vehicles of "', app, '" done')
            
            thisRequestURL = thisRequestURL.replace('TBA1', id)

            if 'Turo' in app:
                thisRequestURL = thisRequestURL.replace('TBA2', str(pageNumber))
            # print(thisRequestURL)
            # time.sleep(1000)
            try:
            # if 1:
                if 'Europe1' in app:
                    response = requests.get(thisRequestURL, headers=headers)
                else:
                    response = requests.get(thisRequestURL, headers=headers, proxies=currentProxy)
                if response.status_code == 200:
                        content = response.text.encode()
                        # print('\t\t', carId, len(json.dumps(content)))
                        if 1:
                        # try:
                            # print(content)
                            # reqContent[app+'#'+carId] = content
                            now = datetime.now()
                            currentDate = str(now)
                            # print(currentDate)
                            currentDate = currentDate.split(' ')[0]
                            currentDate = currentDate.replace(' ','~')
                            
                            npath = dpath+'/carReviews/'+currentDate
                            isExist = os.path.exists(npath)
                            if not isExist:
                                os.makedirs(npath)
                                
                            zCompressed = zlib.compress(content)

                            fn = npath+'/'+app+'#'+carId+'#'+currentDate+'.txt'

                            fx = open(fn,'wb')
                            fx.write(zCompressed)
                            fx.close()
                            
                        # except Exception as e:
                        #     print('\t\t Exception 1: ',e) 
                else:
                    print('\t\t Failed Req: ',idcount, app, carId, response.status_code, currentProxy)#
                    # print('\t\t\t',headers)
                    print('\t\t\t',thisRequestURL)
                    # time.sleep(0.5)
                
            except Exception as e:
                print('\t\t Exception in executing requests of ', app, e)
                time.sleep(100)
        if 'Europ' in app:
            time.sleep(70)
        else:
            time.sleep(10)
        # time.sleep(132.5)
    # print(app, reqContent[app].keys())
    return 0


def mainProc():
    ietr = 0

    while 1:
        manager = Manager()
        reqContent = manager.dict()
        now = datetime.now()
        currentDate = now + timedelta(hours=1)
        currentDate = str(currentDate)
        ietr +=1
        print(ietr,'Starting Requests at:', currentDate)


        fx = open('/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/GerCarIDs/readIDS.txt','r')
        carsIDsDict = json.loads(fx.read())
        fx.close()
        totalCars = 0

        procs = []

        numberOfThreads = len(apps)
        
        print('\tRead IDS:')

        for app in apps:
            
            print('\t\t',app, len(carsIDsDict['apps'][app]['carIDs'].keys()))

            carIds = list(carsIDsDict['apps'][app]['carIDs'].keys())
            random.shuffle(carIds)
            # carIds = carIds[:3]
            # print(carIds)
            # time.sleep(10000)
            # getCarDetails(app, carIds, reqContent)
            totalCars += len(carsIDsDict['apps'][app]['carIDs'].keys())
            p = Process(target=getCarDetails, args=(app, carIds, reqContent))
            procs.append(p)
        
        for i in range(numberOfThreads):
                procs[i].start()

        for i in range(numberOfThreads):
            procs[i].join()

        # now = datetime.now()
        # currentDate = now + timedelta(hours=1)
        # currentDate = str(currentDate)

        # currentDate = currentDate.replace(' ','~')

        # print(reqContent.keys())

        # time.sleep(10000)
        # for app in apps:
        # print(reqContent.keys())
        # zCompressed = zlib.compress(json.dumps(reqContent.copy()).encode())
        # fn = 'carDetails/'+currentDate+'.txt'
        # fx = open(fn,'wb')
        # fx.write(zCompressed)
        # fx.close()
    
        
        print('\tSleeping after completing REVIEWS of total cars as: ',totalCars,', at ',currentDate)
        time.sleep(3000)




if __name__ == "__main__":
	mainProc()