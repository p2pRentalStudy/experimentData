from curses import keyname
from basicImports import *
import requests
import random


full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

requestToken = ''
requestHeader = {}
requestURL = ''
requestBody = ''



allThreadsDone = 1

countriesList = {'United States': {}}
countriesList['United States']['Washington D.C.'] = [38.912430, -77.032006]
countriesList['United States']['New York City'] = [40.713448, -73.962365]
countriesList['United States']['Miami'] = [25.775357, -80.195057]
countriesList['United States']['Los Angeles'] = [34.051182, -118.244274]
countriesList['United States']['Las Vegas'] = [36.169099, -115.146391]

dateFormat = "%Y-%m-%d %H:%M:%S"

app = 'GetAround'

maxSleep = 6

#get new bearer token
def getNewToken():
    global requestToken

	#no token needed
    requestToken = ''

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
        tempVals = line.split(': ')
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


    listHeaders = ''

    latitude = coordinates[0]
    longitude =  coordinates[1]

    currentURL = requestURL[:]
    currentURL = currentURL.replace('LATITUDE', str(latitude))
    currentURL = currentURL.replace('LONGITUDE', str(longitude))



    now = datetime.now()
    startDate = now + timedelta(hours=1)


    maxDays = 60
    payload = {}
    bookingHours = 8
    dataDict = {}
    for statDayDelta in range(0, maxDays):
        # for startHourDelta in range(0, 24):
        hoursToBeAdded =  24 * statDayDelta

        tempStart = startDate + timedelta(hours=hoursToBeAdded)

        tempEnd = tempStart + timedelta(hours=bookingHours)

        t1 = str(tempStart).split(' ')[0] + 'T' + str(tempStart).split(' ')[1].split('.')[0]
        t1 = t1.replace(':', '%3A')
        t1 = t1.split('%3A')[0]
        t1 = t1 + '%3A00%3A00Z'
        listVehicleUrl = currentURL.replace('TB1', t1)


        t2 = str(tempEnd).split(' ')[0] + 'T' + str(tempEnd).split(' ')[1].split('.')[0]
        t2 = t2.replace(':', '%3A')
        t2 = t2.split('%3A')[0]
        t2 = t2 + '%3A00%3A00Z'
        listVehicleUrl = listVehicleUrl.replace('TB2', t2)


        response = requests.request("GET", listVehicleUrl, headers = requestHeader, data = payload)

        # print(len(response.text.encode()))
        # time.sleep(1000)
        if response.status_code == 200:
            content = json.loads(response.text.encode())
            # print(content.keys())
            t1 = t1.replace('%3A00%3A00Z', '')
            t2 = t2.replace('%3A00%3A00Z', '')

            keyName =  country + '~' + city + '~' + app + '~' + t1 + '~' + t2
            dataDict[keyName] = content 
            dataDict['startTime'] = t1
            dataDict['endTime'] = t2
            if statDayDelta % 20 == 0 and statDayDelta != 0: 
                print('\t\t',country, city, statDayDelta)  
                # time.sleep(1000)
        else:
            print('\t\tFailed req:', country, city, response.status_code)
            

        waitTime = random.uniform(0.5, 1.5)
        time.sleep(waitTime) 
    
    reqContent[city] = dataDict
    d[city] = 200

    # time.sleep(1000)
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
            d = manager.dict()
            reqContent = manager.dict()
            numberOfThreads = len(countriesList[country])
            i = 0
            for city in countriesList[country]:
                # worker(i, reqContent, d, country, city, countriesList[country][city])
                p = Process(target=worker, args=(i, reqContent, d, country, city, countriesList[country][city],))
                procs.append(p)
                i += 1
            
            print('\tStarting iet', ietNumber,'for', country)
            for i in range(numberOfThreads):
                procs[i].start()

            for i in range(numberOfThreads):
                procs[i].join()

            responseIndex = 0

            totalSize = 0
            for k in (d.keys()):
                content = json.dumps(reqContent[k])
                totalSize += len(content)
                print('\t',k, totalSize)
                saveResponse(k, country, content)

            print(ietNumber,'--'+country+'-- Started at:',nowf.strftime('%I:%M %p'),'-In Time M:', int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)/60),'-S:', int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)%60), ' Total Size:', totalSize/1000,'KB')
            ietNumber += 1

            time.sleep(300)

        if ietNumber % 20 == 0 and ietNumber != 0:
            getNewToken() 


        print('SLEEPING AFTER COMPLETING THE COUNTRIES')
        #6 hrs sleep
        time.sleep(15000)

    



if __name__ == "__main__":
	mainProc()