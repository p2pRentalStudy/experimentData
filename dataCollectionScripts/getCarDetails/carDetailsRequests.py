from curses import keyname
from basicImports import *
import requests
import random
import string
from requests.auth import HTTPProxyAuth


full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)


#run seperately for Turo and Getaround in seperate terminal by commenting one and leaving one
apps = [
    'GetAround'
    #'Turo'
    ]


def getCarDetails(app, carIds, reqContent):
    # '10.36.25.252:8888','10.36.25.252:8888','10.36.25.252:8888',
    myProxies1 = ['193.37.55.98:8800', '185.218.148.255:8800', '193.37.52.30:8800', '185.218.148.63:8800', '185.218.148.223:8800', '179.43.135.60:8800', '193.37.55.95:8800', '193.37.52.167:8800', '185.218.148.129:8800', '179.43.135.68:8800']
    #'178.212.190.67:12323', '178.212.190.2:12323', 

    myProxies2 = [ '193.37.55.98:8800', '185.218.148.255:8800', '193.37.52.30:8800', '185.218.148.63:8800', '185.218.148.223:8800', '179.43.135.60:8800', '193.37.55.95:8800', '193.37.52.167:8800', '185.218.148.129:8800', '179.43.135.68:8800']

    if 'Europe' in app:
        myProxies = myProxies1
    else:
        myProxies = myProxies2
    proxyIndex = 0
    # reqContent[app] = {}

    headers = {
    'user-agent': 'Dalvik/2.1.0',
    'accept-encoding': 'gzip'
    }
    requestURL = ''
    if 'Turo' in app:
        #request to be added 
        headers['user-agent'] = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC)Turo/22.25.0'
        headers['accept-language'] = 'en-US'
        requestURL = 'https://api.turo.com/api/vehicle/detail?vehicleId='
            
    elif 'Europe' in app:
        identifierTemplate = '96795b08-0deb-4d88-ac33-f4bcdeffd58f'
        
        randInt = random.randint(0, len(identifierTemplate)-3)
        if identifierTemplate[randInt] == '-':
            randInt += 1
        identifier = identifierTemplate[:randInt]+ random.choice(string.ascii_letters)+identifierTemplate[randInt+1:]

        headers['x_vl_authorization']= 'cf4d2f5591763483bf1f258c5820e411'
        headers['drivy-user-identifier']= identifier

        requestURL = 'https://api-eu.getaround.com/api/v1/cars/'
    else:
        headers['user-agent'] = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M) Getaround-Android/433 gzip'
        requestURL = 'https://getaround3.appspot.com/_ah/api/mobile/v2/cars/'
    

    idcount = 0
    for carId in carIds:
        if 'Turo' in app and idcount%10 == 0:
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
            idcount += 1
            if idcount % 1000 == 0:
                print('\t\t\t', idcount,' vehicles of "',app, '" done')
            thisRequestURL = thisRequestURL+id
            # print(thisRequestURL)
            try:
            # if 1:
                if 'Europe1' in app or 'Turo' in app:
                    response = requests.get(thisRequestURL, headers=headers)
                else:
                    response = requests.get(thisRequestURL, headers=headers, proxies=currentProxy)
                # response = requests.get(thisRequestURL, headers=headers, proxies=currentProxy)
                if response.status_code == 200:
                        content = response.text.encode()
                        # print('\t\t', carId, len(json.dumps(content)))
                        if 1:
                        # try:
                            # print(app,carId, len(content))
                            # time.sleep(10000)
                            # reqContent[app+'#'+carId] = content
                            now = datetime.now()
                            currentDate = str(now)
                            # print(currentDate)
                            currentDate = currentDate.split(' ')[0]
                            currentDate = currentDate.replace(' ','~')

                            npath = dpath+'/carDetails/'+currentDate
                            isExist = os.path.exists(dpath+'/carDetails/'+currentDate)
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
                    print('\t\t Failed Req: ',idcount, app, carId, response.status_code , response.text, currentProxy)#
                    # print('\t\t\t',headers)
                    print('\t\t\t',thisRequestURL)
                    # time.sleep(0.5)
                
            except Exception as e:
                print('\t\t Exception in executing requests of ', app, e)
                time.sleep(100)
        if 'Europ' in app:
            time.sleep(10)
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
            # time.sleep(10000)
            totalCars += len(carsIDsDict['apps'][app]['carIDs'].keys())
            p = Process(target=getCarDetails, args=(app, carIds, reqContent))
            procs.append(p)
        
        for i in range(numberOfThreads):
                procs[i].start()

        for i in range(numberOfThreads):
            procs[i].join()

        
        print('\tSleeping after completing total cars as: ',totalCars,', at ',currentDate)
        time.sleep(3000)




if __name__ == "__main__":
	mainProc()