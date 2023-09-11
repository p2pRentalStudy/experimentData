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







targetFolder =  '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/ownerImages/APPNAME/'

# https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
FACE_PROTO = "weights/deploy.prototxt.txt"
# https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20180205_fp16/res10_300x300_ssd_iter_140000_fp16.caffemodel
FACE_MODEL = "weights/res10_300x300_ssd_iter_140000_fp16.caffemodel"
# The gender model architecture
# https://drive.google.com/open?id=1W_moLzMlGiELyPxWiYQJ9KFaXroQ_NFQ
GENDER_MODEL = 'weights/deploy_gender.prototxt'
# The gender model pre-trained weights
# https://drive.google.com/open?id=1AW3WduLk1haTVAxHOkVS_BEzel1WXQHP
GENDER_PROTO = 'weights/gender_net.caffemodel'
# Each Caffe Model impose the shape of the input image also image preprocessing is required like mean
# substraction to eliminate the effect of illunination changes
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
# Represent the gender classes
GENDER_LIST = ['Male', 'Female']
# The model architecture
# download from: https://drive.google.com/open?id=1kiusFljZc9QfcIYdU2s7xrtWHTraHwmW
AGE_MODEL = 'weights/deploy_age.prototxt'
# The model pre-trained weights
# download from: https://drive.google.com/open?id=1kWv0AjxGSN0g31OeJa02eBGM0R_jcjIl
AGE_PROTO = 'weights/age_net.caffemodel'
# Represent the 8 age classes of this CNN probability layer
AGE_INTERVALS = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)',
                 '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']



# Initialize frame size
frame_width = 1280
frame_height = 720
# load face Caffe model
face_net = cv2.dnn.readNetFromCaffe(FACE_PROTO, FACE_MODEL)
# Load age prediction model
age_net = cv2.dnn.readNetFromCaffe(AGE_MODEL, AGE_PROTO)
# Load gender prediction model
gender_net = cv2.dnn.readNetFromCaffe(GENDER_MODEL, GENDER_PROTO)




def get_faces(frame, confidence_threshold=0.5):
    # convert the frame into a blob to be ready for NN input
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104, 177.0, 123.0))
    # set the image as input to the NN
    face_net.setInput(blob)
    # perform inference and get predictions
    output = np.squeeze(face_net.forward())
    # initialize the result list
    faces = []
    # Loop over the faces detected
    for i in range(output.shape[0]):
        confidence = output[i, 2]
        if confidence > confidence_threshold:
            box = output[i, 3:7] * \
                np.array([frame.shape[1], frame.shape[0],
                         frame.shape[1], frame.shape[0]])
            # convert to integers
            start_x, start_y, end_x, end_y = box.astype(int)
            # widen the box a little
            start_x, start_y, end_x, end_y = start_x - \
                10, start_y - 10, end_x + 10, end_y + 10
            start_x = 0 if start_x < 0 else start_x
            start_y = 0 if start_y < 0 else start_y
            end_x = 0 if end_x < 0 else end_x
            end_y = 0 if end_y < 0 else end_y
            # append to our list
            faces.append((start_x, start_y, end_x, end_y))
    return faces


def display_img(title, img):
    """Displays an image on screen and maintains the output until the user presses a key"""
    # Display Image on screen
    cv2.imshow(title, img)
    # Mantain output until user presses a key
    cv2.waitKey(0)
    # Destroy windows when user presses a key
    cv2.destroyAllWindows()


# from: https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]
    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image
    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    # resize the image
    return cv2.resize(image, dim, interpolation = inter)


def get_gender_predictions(face_img):
    blob = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=MODEL_MEAN_VALUES, swapRB=False, crop=False
    )
    gender_net.setInput(blob)
    return gender_net.forward()


def get_age_predictions(face_img):
    blob = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=MODEL_MEAN_VALUES, swapRB=False
    )
    age_net.setInput(blob)
    return age_net.forward()



def predict_age_and_gender(input_path: str):
    """Predict the gender of the faces showing in the image"""
    # Initialize frame size
    # frame_width = 1280
    # frame_height = 720
    # Read Input Image
    totalFace = []
    img = cv2.imread(input_path)
    # resize the image, uncomment if you want to resize the image
    # img = cv2.resize(img, (frame_width, frame_height))
    # Take a copy of the initial image and resize it
    try:
        frame = img.copy()

        if frame.shape[1] > frame_width:
            frame = image_resize(frame, width=frame_width)
        # predict the faces
        faces = get_faces(frame)
        # Loop over the faces detected
        # for idx, face in enumerate(faces):
        
        for i, (start_x, start_y, end_x, end_y) in enumerate(faces):
            face_img = frame[start_y: end_y, start_x: end_x]
            age_preds = get_age_predictions(face_img)
            gender_preds = get_gender_predictions(face_img)
            i = gender_preds[0].argmax()
            gender = GENDER_LIST[i]
            gender_confidence_score = gender_preds[0][i]
            i = age_preds[0].argmax()
            age = AGE_INTERVALS[i]
            age_confidence_score = age_preds[0][i]
            # Draw the box
            label = f"{gender}-{gender_confidence_score*100:.1f}%, {age}-{age_confidence_score*100:.1f}%"

            totalFace.append((gender, age))
            # label = "{}-{:.2f}%".format(gender, gender_confidence_score*100)
            # print(label)
    except:
        ijk = 10

    return totalFace

import os
import shutil

totalDemographicsOwners = {}

target = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/tempImages/'
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import tensorflow as tf
import logging


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)

from functools import wraps
from deepface.commons import functions
import sys
import io

import sys
import subprocess
from timeit import default_timer as timer


# {'race': {'asian': 0.5138802342116833, 'indian': 2.023613825440407, 'black': 1.213485561311245, 'white': 67.81983971595764, 'middle eastern': 15.573060512542725, 'latino hispanic': 12.856124341487885}, 'dominant_race': 'white'}

studiedApps = {}
# studiedApps['GerAroundEurope'] = 1
# studiedApps['GetAround'] = 1
studiedApps['Turo'] = 1

ownerCount = 0
noPicOwnerCount = 0
multiusersInDP = 0
for platform in studiedApps:
    print(platform)
    totalDemographicsOwners[platform] = {}
    listData = {}
    tempFolder = targetFolder.replace('APPNAME',platform)

    filenames = next(walk(tempFolder), (None, None, []))[2]  # [] if no file
    filenames.sort()

    print(len(filenames))
    # time.sleep(10000)
    start = timer()
    for fileName in filenames:
        

        ownerCount += 1
        ownerId = fileName
        picPath = tempFolder+fileName
        # print(ownerId,picPath)
        # time.sleep(1000)
        totalFace = predict_age_and_gender(picPath)

        shutil.copy(picPath, target+'temp.jpg')

        cmd  = subprocess.run([sys.executable, "4a3-deepFaceCall.py", picPath], capture_output=True)
        s2_out = cmd.stdout.decode()  # bytes => str

        # print(s2_out)
        # time.sleep(10000)
        drace = 'white'
        try:
            drace = s2_out.split(" 'dominant_race': '")[1]
            drace = drace.split("'")[0]
            end = timer()
            # print('\t\t',ownerCount, drace, end - start)
            start = timer()
        except:
            drace = 'white'
        # print(drace)

        # time.sleep(1000)
        totalDemographicsOwners[platform][ownerId] = {}
        if len(totalFace) > 1:
            multiusersInDP += 1
        if len(totalFace) > 0:
            for i in range(0, len(totalFace)):
                totalDemographicsOwners[platform][ownerId]['user'+str(i+1)] = {}
                totalDemographicsOwners[platform][ownerId]['user'+str(i+1)]['gender'] = totalFace[i][0]
                totalDemographicsOwners[platform][ownerId]['user'+str(i+1)]['age'] = totalFace[i][1]
                totalDemographicsOwners[platform][ownerId]['user'+str(i+1)]['race'] = drace
        else:
            noPicOwnerCount += 1
        

        if ownerCount%1000 ==0:
            print('\t', ownerCount, ' owners done')
        # time.sleep(2)
savePath = '/home/hakhan/Google Drive/p2pCarRentalProject/AnalysisScripts/IntermediateData/4a2-output/'
fx = open(savePath+platform+'-demographics.txt','w')
fx.write(json.dumps(totalDemographicsOwners))
fx.close()
print('saved demographics dictionary', ownerCount, noPicOwnerCount, multiusersInDP)



