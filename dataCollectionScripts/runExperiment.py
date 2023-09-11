import time
import os

import psutil
import datetime

def killxtermProcs():
    PROCNAME1 = "xterm"
    count = 0
    for proc in psutil.process_iter():
        try:
            if PROCNAME1 in proc.name():
                count +=1
                proc.kill()
        except Exception as e:
            time.sleep(2)
            print(e)


full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'

hcount = 0
killWait = 86400

while 1:
    try:
        datetime.datetime.now()
        hcount = hcount+1
        print(hcount, 'Starting Procs: ',datetime.datetime.now().time())

        os.system("xterm -e \"python3 "+dpath+"GetAround/vehicleList.py\" &")
        #sleep
        time.sleep(killWait)

        killxtermProcs()
        datetime.datetime.now()
        # print('Stopping Procs: ',datetime.datetime.now().time())
        time.sleep(60)

    except Exception as e:
        time.sleep(60)
        print(e)