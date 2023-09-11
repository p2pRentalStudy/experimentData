from curses import keyname
import re
from basicImports import *
import requests
import random


full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

requestToken = 'Bearer afa9d6fc-4a97-4e67-9693-160a01c1deeb'


requestHeader = {}
requestURL = ''
requestBody = ''



allThreadsDone = 1

countriesList = {}
countriesList['TC1'] = {}
# countriesList['Canada'] = {}
# countriesList['United States2'] = {}
# countriesList['United Kingdom'] = {}

countriesList['TC1']['Miami'] = [25.775357, -80.195057]

countriesList['TC1']['Ottawa'] = [45.405357, -75.712878]

countriesList['TC1']['New York City'] = [40.713448, -73.962365]

countriesList['TC1']['Toronto'] = [43.731397, -79.450457]

countriesList['TC1']['Washington D.C.'] = [38.912430, -77.032006]

countriesList['TC1']['London'] = [51.509283, -0.126682]

countriesList['TC1']['Los Angeles'] = [34.051182, -118.244274]

countriesList['TC1']['Liverpool'] = [53.407477, -2.990112]

countriesList['TC1']['Las Vegas'] = [36.169099, -115.146391]


vehicleType = [6, 9, 10, 12, 11]  # 6:Cars, 9:SUVs, 10:Minivans, 12:Vans, 11:Trucks

from proxy_requests import ProxyRequests


# vehicleTypes = ['FAMILY_FRIENDLY', 'SPORTY_SPINS', '']

dateFormat = "%Y-%m-%d %H:%M:%S"

app = 'Turo'

maxSleep = 6

#get new bearer token

myProxies = ['10.154.34.199:8888']
tokenProxyIndex = 0
def getNewToken():
    global requestToken
    global tokenProxyIndex

    # tokenProxyIndex += 1
    tokenProxyIndex = tokenProxyIndex% len(myProxies)

    proxy = myProxies[0]
    
    currentProxy = {"http": proxy, "https": proxy}
    
    url = "https://api.turo.com/oauth/token?grant_type=client_credentials"

    payload={}
    headers = {
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M)Turo/22.25.0',
    'accept-language': 'en-US',
    'accept-encoding': 'gzip',
    'authorization': 'Basic YW5kcm9pZC1uYXRpdmU6U3MvK2hRUUZmMjEwcVczcFROQTlleUVRcy8vbk5acFFtL1QyNEhuTXNJQkZSRzlN',
    }

    response = requests.post(url, headers=headers, data=payload, proxies=currentProxy)


    if response.status_code == 200:
        requestToken = 'Bearer '+json.loads(response.text)['access_token']
        print(requestToken)
        # time.sleep(10000)
    else:
        print('request for TOKEN failed ,', response.status_code)
        # print(url)
        print(headers)
        # time.sleep(1000)

def getRequestURL():
    global requestURL

    fx = open(dpath+"/requestURL.txt", "r")
    requestURL = fx.read()
    fx.close()

def getRequestHeaders():
    global requestHeader

    file = open(dpath+"/requestHeaders.txt", "r")
    i =0
    for line in file:
        line = line.replace('\n','')
        tempVals = line.split(':')
        requestHeader[tempVals[0]] = tempVals[1]
        # listHeaders = listHeaders + line
        i = 1+i
    #print ('Headers: 'headersDynamic)
    file.close()


def getRequestBody():
    global requestBody

    fx = open(dpath+"/requestBody.txt", "r")
    requestBody = fx.read()
    fx.close()



def worker(tid, reqContent, d, country, city, coordinates):
    global requestBody
    global requestURL
    global requestHeader
    global requestToken


    listHeaders = ''
    proxyIndex = 0

    latitude = coordinates[0]
    longitude =  coordinates[1]



    now = datetime.now()
    startDate = now + timedelta(hours=1)


    maxDays = 60
    payload = {}
    bookingHours = 8
    dataDict = {}
    # currentURL =  "https://api.turo.com/api/search?startDate=TB1&startTime=TB2&instantBook=false&endDate=TB3&endTime=TB4&latitude=TB5&page=1&itemsPerPage=200&longitude=TB6&deluxeClass=false&superDeluxeClass=false&delivery=false&country=US&allStarHost=false&sortType=RELEVANCE&minimumPrice=TB7&maximumPrice=TB8"

    currentURL = "https://api.turo.com/api/search?startDate=TB1&startTime=TB2&endDate=TB3&endTime=TB4&latitude=TB5&page=1&longitude=TB6&sortType=RELEVANCE&minimumPrice=TB7&maximumPrice=TB8"

    

    for startDayDelta in range(0, maxDays):
        # for startHourDelta in range(0, 24):
        hoursToBeAdded =  24 * (1+startDayDelta)

        tempStart = startDate + timedelta(hours=hoursToBeAdded)
        tempEnd = tempStart + timedelta(hours=24)
      
        listVehicleUrl = currentURL[:]
        date = str(tempStart).split(' ')[0]
        date = date.split('-')
        t1 = date[1] + "%2F" + date[2] + "%2F" + date[0]

        date2 = str(tempEnd).split(' ')[0]
        date2 = date2.split('-')
        t2 = date2[1] + "%2F" + date2[2] + "%2F" + date2[0]


        listVehicleUrl = listVehicleUrl.replace('TB1', t1)
        listVehicleUrl = listVehicleUrl.replace('TB3', t2)

        listVehicleUrl = listVehicleUrl.replace('TB2', '10%3A00')
        listVehicleUrl = listVehicleUrl.replace('TB4', '10%3A00')

        listVehicleUrl = listVehicleUrl.replace('TB5', str(latitude))
        listVehicleUrl = listVehicleUrl.replace('TB6', str(longitude))


        #take care of page number and PRICE RANGE
        minPrice = 10
        totalReqs = 0
        failWait = 40
        if startDayDelta % 1 == 0: #and statDayDelta != 0: 
            n1 = datetime.now()
            c1 = n1.strftime("%H:%M:%S")
            print('\t',country, city, 'day delta =', startDayDelta, 'Time = ', c1)  

        while minPrice <= 1500:
            maxPrice = minPrice+3
            
            if minPrice >= 1000:
                maxPrice = minPrice+100
            elif minPrice >= 350:
                maxPrice = minPrice+70
            elif minPrice >= 200:
                maxPrice = minPrice+50

            else:
                maxPrice = minPrice+5

            #make request 
            thisRequestURL = listVehicleUrl[:]
            thisRequestURL = thisRequestURL.replace('TB7', str(minPrice))
            thisRequestURL = thisRequestURL.replace('TB8', str(maxPrice))

            # print(headers)
            # time.sleep(1000)
            # waitTime = random.uniform(0.5, )
            # time.sleep(waitTime) 

            # requestToken = 'Bearer afa9d6fc-4a97-4e67-9693-160a01c1deeb'
            headers = {
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC)Turo/22.25.0',
            'accept-language': 'en-US',
            'authorization': ''+requestToken,
            'accept-encoding': 'gzip'
            }


            myProxies = ['179.43.135.60:8800', '193.37.55.95:8800', '185.218.148.223:8800', '185.218.148.255:8800', '179.43.135.68:8800', '185.218.148.63:8800', '185.218.148.129:8800' ,'193.37.52.30:8800', '193.37.52.167:8800', '193.37.55.98:8800']


            try:
                proxyIndex += 1
                proxyIndex = proxyIndex% (len(myProxies)+1)

                response = None
                waitTime =  1 #random.uniform(1.5, 2.5)
                time.sleep(waitTime) 

                if proxyIndex == len(myProxies):
                    response = requests.get(thisRequestURL, headers=headers)
                else:
                    proxy = myProxies[proxyIndex]
                    currentProxy = {"http": proxy, "https": proxy}
                    response = requests.get(thisRequestURL, headers=headers, proxies=currentProxy)

                # print(response.text[:1000])
                # print(headers)
                # # print(len(response.text), thisRequestURL, headers)
                # time.sleep(10000)

                if response.status_code == 200:
                    totalReqs += 1
                    content = json.loads(response.text.encode())
                    if totalReqs %10 == 0:
                        print('\t\t',startDayDelta, totalReqs, city, t1, t2, maxPrice, len(content['list']))
                    t1 = t1.replace('%3A00%3A00Z', '')
                    t2 = t2.replace('%3A00%3A00Z', '')

                    keyName =  country + '~' + city + '~' + app + '~' + t1 + '~' + t2+ '~' + str(minPrice) + '~' + str(maxPrice)
                    dataDict[keyName] = content 
                    minPrice = maxPrice+1
                    failWait = 40
                else:
                    n1 = datetime.now()
                    c1 = n1.strftime("%H:%M:%S")
                    
                    print('\t\t!!!!FAILED req:', totalReqs, country, city, response.status_code, minPrice, maxPrice, c1)

                    print('\t\t Waiting for', failWait,' second to take action')
                    time.sleep(failWait)
                    failWait = failWait*1.2
                    
                    # if 1:
                    if response.status_code == 429:
                        n1 = datetime.now()
                        c1 = n1.strftime("%H:%M:%S")
                        print('\t\t\t Sleeping', c1)
                        time.sleep(100)
                        n1 = datetime.now()
                        c1 = n1.strftime("%H:%M:%S")
                        print('\t\t\t Generating new token', c1)
                        getNewToken()
                        n1 = datetime.now()
                        c1 = n1.strftime("%H:%M:%S")
                        print('\t\t\t Generated new token', c1)
                        time.sleep(10)
                    elif response.status_code == 400:
                        print('\t\t\t', thisRequestURL, response.text)
                        # print('\t\t\t', headers)
                        getNewToken()
                        time.sleep(10)
                        n1 = datetime.now()
                        c1 = n1.strftime("%H:%M:%S")
                        # print('\t\t\t Generated new token', c1)
                        time.sleep(10)
                    else:
                        minPrice = maxPrice+1
            except Exception as e:
                print('Exception !!!' , e)

    reqContent[city] = dataDict
    d[city] = 200

    return 0



def saveResponse(city, country, response):
    zCompressed = zlib.compress(response.encode())
    nowf2 = datetime.now()
    filenm = dpath+'/vehiclesList/'+country+'-'+city+'-responseEncoded-'+nowf2.strftime("%Y-%m-%d")+'.txt'
    logFile = open(filenm, "ab")
    logFile.write(zCompressed)
    logFile.write(b'0x0A')
    logFile.close()


def mainProc():
    
    getRequestURL()  
    getRequestHeaders()
    getRequestBody()


    current_milli_timeLife = int(round(time.time() * 1000))
    ietNumber = 0
    manager = Manager()
    nowf = datetime.now()
    while 1:
        procs = []
        for country in countriesList.keys():
            
            procs = []
            
            numberOfThreads = len(countriesList[country])
            i = 0
            for city in countriesList[country]:
                getNewToken() 
                d = manager.dict()
                reqContent = manager.dict()
                worker(i, reqContent, d, country, city, countriesList[country][city])

                totalSize = 0
                for k in (d.keys()):
                    content = json.dumps(reqContent[k])
                    totalSize += len(content)
                    print('\t',k, totalSize)
                    saveResponse(k, city, content)

                # print(ietNumber,'--'+country+'-- Started at:',nowf.strftime('%I:%M %p'),'-In Time M:', int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)/60),'-S:', int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)%60), ' Total Size:', totalSize/1000,'KB')
                # ietNumber += 1
                time.sleep(30)

        print('SLEEPING AFTER COMPLETING THE COUNTRIES')
        #6 hrs sleep
        time.sleep(100)

    



if __name__ == "__main__":
	mainProc()