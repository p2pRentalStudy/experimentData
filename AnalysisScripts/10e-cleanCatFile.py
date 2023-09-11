from basicImports import *
import requests
import random
import string
import ast


# READ CATEGORIES FROM HERE https://stylesatlife.com/articles/types-of-cars/
# MAKE A DICTIONARY OF CAR NAMES AND THEN ASSIGN CATEGORIES

totalCategories = ['Minivans, wagons, & SUVs', 'Sports cars & performance SUVs', 'SUVs, crossovers, & AWD options', 'High-end luxury & performance', 'Drop tops & hard tops', 'Luxury cars & SUVs']


fx = open('carCat.txt', 'r')
content = fx.read()
fx.close()

carCategories = {}


# fx = open('carCatCleaned.txt', 'r')
# carCategories = json.loads(fx.read())
# fx.close()


# print(len(content), content[0])
content = content.split('\n')

# print(len(content))
# time.sleep(1000)
i = 0
for contentPart in content:
    if contentPart != '':
        contentPart = json.loads(contentPart)
        for i in range(0, len(contentPart)):
            currentItem = contentPart[i]
            currentItem = ast.literal_eval(currentItem)
            # print(type(currentItem), len(currentItem))
            for carObj in currentItem:
                # print(carObj)
                # time.sleep(1000)
                # if 1:
                try:
                    carObj['model']  = carObj['model'].lower()
                    carObj['make']  = carObj['make'].lower()

                    ctype = carObj['type']
                    if isinstance(ctype, str):
                        if ',' in ctype:
                            totalTypes = ctype.split(', ')
                            # print(totalTypes)
                            carObj['type'] = []
                            for type in totalTypes:
                                type = type.lower()
                                carObj['type'].append(type)
                        elif '/' in ctype:
                            totalTypes = ctype.split('/')
                            # print(totalTypes)
                            carObj['type'] = []
                            for type in totalTypes:
                                type = type.lower()
                                carObj['type'].append(type)
                        else:
                            carObj['type'] = [ctype]

                    carCategories[carObj['model']+'~'+carObj['make']]= carObj
                    # carCategories[carObj['model']][carObj['make']] = 
                    i += 1
                    # print(carCategories)
                    # time.sleep(1000)
                # else:
                except Exception as e:
                    if 'message' not in carObj:
                        # print(e)
                        print(i, carObj)
                        time.sleep(10000000)
                        time.sleep(0.1)


print(len(carCategories.keys()))


fx = open('carCatCleaned.txt','w')
fx.write(json.dumps(carCategories))
fx.close()