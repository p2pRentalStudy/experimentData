from curses import keyname
from basicImports import *
import requests
import random
import string

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)



apps = [
    'GerAroundEurope', 
    'GetAround', 
    'Turo'
    ]


def getCarDetails(app, carIds, reqContent):
    
    myProxies = ['154.53.91.92:8800', '196.51.59.224:8800', '154.53.88.150:8800', '154.26.168.91:8800', '154.26.168.58:8800', '154.53.91.45:8800', '196.51.56.78:8800', '154.26.168.45:8800', '154.26.168.81:8800', '196.51.56.1:8800', '154.53.91.119:8800', '196.51.59.214:8800', '154.53.88.59:8800', '196.51.56.239:8800', '154.53.88.152:8800', '196.51.56.149:8800', '194.55.82.215:8800', '196.51.59.117:8800', '154.53.88.3:8800', '194.55.82.81:8800', '154.26.168.50:8800', '154.53.91.5:8800', '194.55.82.35:8800', '196.51.59.150:8800', '194.55.82.188:8800', '179.43.135.60:8800', '193.37.55.95:8800', '185.218.148.223:8800', '185.218.148.255:8800', '179.43.135.68:8800', '185.218.148.63:8800', '185.218.148.129:8800' ,'193.37.52.30:8800', '193.37.52.167:8800', '193.37.55.98:8800']
    
    proxyIndex = 0
    # reqContent[app] = {}

    headers = {
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M)',
    'accept-encoding': 'gzip'
    }
    requestURL = ''
    appConn = ''
    if 'Turo' in app:
        #request to be added 
        appConn = "api.turo.com"
        headers['user-agent'] = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC)Turo/22.25.0'
        headers['accept-language'] = 'en-US'
        requestURL = 'https://api.turo.com/api/vehicle/detail?vehicleId='
            
    elif 'Europe' in app:
        appConn = "api-eu.getaround.com"
 
        identifierTemplate = '96795b08-0deb-4d88-ac33-f4bcdeffd58f'
        
        randInt = random.randint(0, len(identifierTemplate)-3)
        if identifierTemplate[randInt] == '-':
            randInt += 1
        identifier = identifierTemplate[:randInt]+ random.choice(string.ascii_letters)+identifierTemplate[randInt+1:]

        headers['x_vl_authorization']= 'cf4d2f5591763483bf1f258c5820e411'
        headers['drivy-user-identifier']= identifier

        requestURL = 'https://api-eu.getaround.com/api/v1/cars/'
    else:
        appConn = "getaround3.appspot.com"

        headers['user-agent'] = 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M) Getaround-Android/433 gzip'
        requestURL = 'https://getaround3.appspot.com/_ah/api/mobile/v2/cars/'
    

    idcount = 0
    for carId in carIds:
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
                conn = http.client.HTTPSConnection(appConn)
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
                    print('\t\t Failed Req: ',idcount, app, carId, response.status_code )#
                    # print('\t\t\t',headers)
                    print('\t\t\t',thisRequestURL)
                    # time.sleep(0.5)
                
            except:
                print('\t\t Exception in executing requests of ', app)
                time.sleep(100)
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
    
        
        print('\tSleeping after completing total cars as: ',totalCars,', at ',currentDate)
        time.sleep(3000)




if __name__ == "__main__":
	mainProc()