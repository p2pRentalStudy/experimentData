import requests
import json 
import time

url = "https://car-data.p.rapidapi.com/cars"

carCats = []
for i in range(0,1000):
    querystring = {"limit":"50","page":str(i)}

    headers = {
        'X-RapidAPI-Key': 'd9b53161aemshcdab736e389db5ap129b4fjsn5b12ec2e7063',
        "X-RapidAPI-Host": "car-data.p.rapidapi.com"
    }

    try:

        response = requests.request("GET", url, headers=headers, params=querystring)

        # print(response.text)
        carCats.append(response.text)
        print(i)
        time.sleep(5)

    except Exception as e:
        print(i, e)
        time.sleep(5)

fx = open('carCat.txt', 'a')
fx.write('\n'+json.dumps(carCats))
fx.close()
