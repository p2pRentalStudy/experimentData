from basicImports import *
import requests
import random
import string
import fileinput


citiesAndServices = {}
citiesAndServices['Turo'] = ['Las Vegas']#, 'Liverpool', 'London', 'Los Angeles','New York City', 'Miami', 'Ottowa', 'Toronto', 'Washinton D.C']
# citiesAndServices['GetAround'] = ['Las Vegas']#, 'Los Angeles', 'Miami','New York City', 'Washinton D.C']
# citiesAndServices['GerAroundEurope'] = ['Barcelona']#, 'Berlin', 'Hamburg', 'Liverpool','Lyon', 'Madrid', 'Paris']

targetFolder = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/0-output/data/'


carNumberDict = {}
for platform in citiesAndServices:
    cities = citiesAndServices[platform]
    for city in cities:
        try:
            var = carNumberDict[city]
        except:
            carNumberDict[city] = {}
        try:
            var = carNumberDict[city][platform]
        except:
            carNumberDict[city][platform] = 0

def readLargeFile(filePath):
    start = time.time()
 
    #keeps a track of number of lines in the file
    count = 0
    content = ''
    for lines in fileinput.input([filePath]):
        content += lines
        count = count + 1
        
    #time at the end of program execution is noted
    end = time.time()
    
    #total time taken to print the file
    print("Execution time in seconds: ",(end - start))
    print("No. of lines printed: ",count)
    return content

for platform in citiesAndServices:
    cities = citiesAndServices[platform]
    for city in cities:
        totalCars = {}
        f1Content = {}
        print('loading ', platform, city)
        filePath = targetFolder+platform+'/'+city+'-content.txt'
        print(filePath)
        fx = open(filePath)
        f1Content = json.loads(fx.read())
        fx.close()

        # f1Content = json.loads(readLargeFile(filePath))
        # f1Content = f1Content[platform]
        # for country in f1Content.keys():
        #     # print(country)
        #     f1Content = f1Content[country]
        #     break
        # f1Content = f1Content[city]
        datesKeys = {}

        myKeys = list(f1Content.keys())
        # myKeys.sort()
        totalCatsDict = {}
        print(len(f1Content.keys()))
        for date in myKeys:
            dateObj = date.split(' ')[0]
            try:
                var = datesKeys[dateObj]
            except:
                datesKeys[dateObj] = 1
                print(date)
            for carID in f1Content[date].keys():

                totalCars[carID] = 1
                # print(f1Content[date][carID])
                # time.sleep(100000)
                try:
                    totalCatsDict[f1Content[date][carID]['vehicleCategory']] = 1
                except:
                    pass


        # for date in 
        
        carNumberDict[city][platform] = len(totalCars.keys())
        
        f1Content = {}
        # time.sleep(1000)

print(carNumberDict)
print(totalCatsDict.keys())
