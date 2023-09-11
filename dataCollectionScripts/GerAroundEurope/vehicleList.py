
from basicImports import *
from fp.fp import FreeProxy
from hidemypython.proxy_parser import generate_proxy
from hidemypython.utils import Dict
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException






full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

requestToken = ''
requestHeader = {}
requestURL = ''
requestBody = ''



allThreadsDone = 1

countriesList = {}
countriesList = {}
total_pages = 0
countriesList['France'] = {}
countriesList['Germany'] = {}
countriesList['Spain'] = {}
countriesList['UK'] = {}
# 2 most populous cities of each country

countriesList['France']['Paris'] = [48.854990, 2.349358]
countriesList['France']['Lyon'] = [45.763326, 4.835961]
countriesList['Germany']['Berlin'] = [52.522066, 13.403975]
countriesList['Germany']['Hamburg'] = [53.551025, 9.993733]
countriesList['Spain']['Madrid'] = [40.416426, -3.704094]
countriesList['Spain']['Barcelona'] = [41.386657, 2.169244]
countriesList['UK']['London'] = [51.507114, -0.127556]
countriesList['UK']['Liverpool'] = [53.407477, -2.990112]


vehicleType = [6, 9, 10, 12, 11]  # 6:Cars, 9:SUVs, 10:Minivans, 12:Vans, 11:Trucks

from proxy_requests import ProxyRequests


# vehicleTypes = ['FAMILY_FRIENDLY', 'SPORTY_SPINS', '']

dateFormat = "%Y-%m-%d %H:%M:%S"

app = 'GetAroundEurope'

maxSleep = 6

#get new bearer token
def getNewToken():
    global requestToken

    url = "https://api.turo.com/oauth/token?grant_type=client_credentials"

    payload='grant_type%3Dclient_credentials='

    headers = {
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M)Turo/22.25.0',
    'accept-language': 'en-US',
    'accept-encoding': 'gzip',
    'authorization': 'Basic YW5kcm9pZC1uYXRpdmU6U3MvK2hRUUZmMjEwcVczcFROQTlleUVRcy8vbk5acFFtL1QyNEhuTXNJQkZSRzlN',
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    
    if response.status_code == 200:
        requestToken = 'Bearer '+json.loads(response.text)['access_token']
    else:
        print('request for TOKEN failed ,', response.text)

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

    latitude = coordinates[0]
    longitude =  coordinates[1]



    now = datetime.now()
    startDate = now + timedelta(hours=1)


    maxDays = 45
    payload = {}
    bookingHours = 8
    dataDict = {}
    # currentURL =  "https://api.turo.com/api/search?startDate=TB1&startTime=TB2&instantBook=false&endDate=TB3&endTime=TB4&latitude=TB5&page=1&itemsPerPage=200&longitude=TB6&deluxeClass=false&superDeluxeClass=false&delivery=false&country=US&allStarHost=false&sortType=RELEVANCE&minimumPrice=TB7&maximumPrice=TB8"

    currentURL = 'https://api-eu.getaround.com/api/v1/order/picks?longitude=TB28&start_date=TB3&start_time=TB4&end_date=TB5&end_time=TB6&latitude=TB1&page=TB7'

    
    # scrapper = Scrapper(category='ALL' , print_err_trace=False)
    # data = scrapper.getProxies()
    myProxies = ['193.37.55.98:8800', '185.218.148.255:8800', '193.37.52.30:8800', '185.218.148.63:8800', '185.218.148.223:8800', '179.43.135.60:8800', '193.37.55.95:8800', '193.37.52.167:8800', '185.218.148.129:8800', '179.43.135.68:8800']
    
    # for item in data.proxies:
    #     # print(item.port)
    #     if item.port == '443':
    #         myProxies.append(item.ip+':'+item.port)

    # print(len(myProxies))      
    # time.sleep(1000000) 
    proxyIndex = 0

    for startDayDelta in range(0, maxDays):
        # for startHourDelta in range(0, 24):

        now = datetime.now()
        startDate = now + timedelta(hours=24)


        hoursToBeAdded =  24 * (1+startDayDelta)

        tempStart = startDate + timedelta(hours=hoursToBeAdded)
        tempEnd = tempStart + timedelta(hours=24)
      
        listVehicleUrl = currentURL[:]
        date = str(tempStart).split(' ')[0]
        # date = date.split('-')
        t1 = date #date[1] + "%2F" + date[2] + "%2F" + date[0]

        date2 = str(tempEnd).split(' ')[0]
        # date2 = date2.split('-')
        t2 = date2 #date2[1] + "%2F" + date2[2] + "%2F" + date2[0]


        listVehicleUrl = listVehicleUrl.replace('TB3', t1)
        listVehicleUrl = listVehicleUrl.replace('TB5', t2)

        listVehicleUrl = listVehicleUrl.replace('TB4', '10%3A00')
        listVehicleUrl = listVehicleUrl.replace('TB6', '10%3A00')

        listVehicleUrl = listVehicleUrl.replace('TB1', str(latitude))
        listVehicleUrl = listVehicleUrl.replace('TB2', str(longitude))


        #take care of page number and PRICE RANGE
        totalReqs = 0
        failWait = 100
        if startDayDelta % 1 == 0: #and statDayDelta != 0: 
            n1 = datetime.now()
            c1 = n1.strftime("%H:%M:%S")
            print('\t',country, city, 'day delta =', startDayDelta, 'Time = ', c1)  
        pageNumber = 1
        while pageNumber < 52:
        
            #make request 
            thisRequestURL = listVehicleUrl[:]
            thisRequestURL = thisRequestURL.replace('TB7', str(pageNumber))

           
            identifierTemplate = '96795b08-0deb-4d88-ac33-f4bcdeffd58f'
            
            randInt = random.randint(0, len(identifierTemplate)-3)
            if identifierTemplate[randInt] == '-':
                randInt += 1
            identifier = identifierTemplate[:randInt]+ random.choice(string.ascii_letters)+identifierTemplate[randInt+1:]

            headers = {
            'x_vl_authorization': 'cf4d2f5591763483bf1f258c5820e411',
            'drivy-user-identifier': identifier
             }


            # print(randInt, headers)
            # time.sleep(1000)
            # waitTime = random.uniform(0.5, )
            # time.sleep(waitTime) 

             # print(thisRequestURL)
            # print('\t\t\t\t\tSleeping before request')
            
            
            proxyIndex += 1
            proxyIndex = proxyIndex% (len(myProxies)+1)
            
            try:
                response = None
                waitTime =  1 #random.uniform(1.5, 2.5)
                time.sleep(waitTime) 

                if proxyIndex == len(myProxies):
                    response = requests.get(thisRequestURL, headers=headers)
                else:
                    proxy = myProxies[proxyIndex]
                    currentProxy = {"http": proxy, "https": proxy}
                    # if tempStart > 
                    response = requests.get(thisRequestURL, headers=headers, proxies=currentProxy)

                # print(response.text)
                # time.sleep(10000)
                if response.status_code == 200:
                    totalReqs += 1
                    content = json.loads(response.text.encode())
                    if totalReqs %20 == 0:
                        print('\t\t',startDayDelta, totalReqs, city, t1, t2, pageNumber, len(content['cars']))
                    keyName =  country + '~' + city + '~' + app + '~' + t1 + '~' + t2+ '~' + str(pageNumber)
                    dataDict[keyName] = content 
                    failWait = 600
                else:
                    n1 = datetime.now()
                    c1 = n1.strftime("%H:%M:%S")
                    
                    print('\t\t!!!!FAILED req:', totalReqs, country, city, response.status_code, pageNumber, c1)

                    print('\t\t Waiting for', failWait,' second to take action')
                    time.sleep(failWait)
                    failWait = failWait*1.5
                    if 1:
                    # if response.status_code == 429:
                        print('\t\t\t Woke up', c1)
                        time.sleep(2)      
                pageNumber = pageNumber+1
            except Exception as e:
                print(e)
                # time.sleep(100000)
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
    
    # getRequestURL()  
    # getRequestHeaders()
    # getRequestBody()


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
                # getNewToken() 
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
        time.sleep(7200)

    



if __name__ == "__main__":
	mainProc()