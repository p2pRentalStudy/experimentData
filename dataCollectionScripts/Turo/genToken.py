import http.client
import time
import json
from datetime import datetime


while 1:
    conn = http.client.HTTPSConnection("api.turo.com")
    payload = ''
    headers = {
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M)Turo/22.25.0',
    'accept-encoding': 'text',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'accept-language': 'en-US',
    'authorization': 'Basic YW5kcm9pZC1uYXRpdmU6U3MvK2hRUUZmMjEwcVczcFROQTlleUVRcy8vbk5acFFtL1QyNEhuTXNJQkZSRzlN',
    'Content-Length': '0',
    }
    conn.request("POST", "/oauth/token?grant_type=client_credentials&expires_in=50000", payload, headers)
    res = conn.getresponse()
    waitTime = 20000

    fx = open('oauthToken.txt','r')
    prevToken = fx.read()
    fx.close()

    try:
        data = res.read()
        retObject = data.decode("utf-8")
        retObject = json.loads(retObject)
        print(retObject)
        fx = open('oauthToken.txt','w')
        fx.write('Bearer '+retObject['access_token'])
        fx.close()

    except:
        fx = open('oauthToken.txt','w')
        fx.write(prevToken)
        fx.close()

        waitTime = 100

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print('Sleeping for ',waitTime,' second at', current_time)
    time.sleep(waitTime)
