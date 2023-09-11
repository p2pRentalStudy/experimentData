from basicImports import *
import requests
import random
import string
from os import walk
import requests # request img from web
import shutil # save img locally

import urllib.request
# Import Libraries
import cv2
import numpy as np

from deepface import DeepFace


import sys
n = len(sys.argv)

picPath = sys.argv[1]
print("\nimage path:", sys.argv[1])


objs = DeepFace.analyze(img_path = picPath, 
        actions = ['race']
, enforce_detection=False)

print(objs)