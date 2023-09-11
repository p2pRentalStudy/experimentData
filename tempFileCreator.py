import os

# folder path
dir_path = r'/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/getCarReviews/carReviews'

import shutil
import time 

# list to store files
res = []
dest = '/home/hakhan/Google Drive/p2pCarRentalProject/dataCollectionScripts/t3/'
# Iterate directory

fn = 0
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        # print(dir_path, path)
        # time.sleep(1000)
        if 'GerA' in os.path.join(dir_path, path):
            res.append(path)
            sp = os.path.join(dir_path, path)
            dp = dest+path
            shutil.copy(sp, dp)
            if fn %1000 == 0:
                print(fn,'file copied')
            fn += 1
print(len(res))
