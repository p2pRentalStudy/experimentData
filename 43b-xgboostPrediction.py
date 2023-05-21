from basicImports import *
import requests
import random
import string
import ast
from os import walk
import requests # request img from web
import shutil # save img locally
from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator
from scipy.stats import pearsonr   
import pandas as pd

fx = open('platformCarCat.txt','r')
platformCat = json.loads(fx.read())
fx.close()


studiedApps = {}
studiedApps['GerAroundEurope'] = 1
studiedApps['Turo'] = 1


totalTranslatedReviews = {}
carPrices = {}


citiesAndServices = {}
citiesAndServices['GerAroundEurope'] = ['Paris']
citiesAndServices['GetAround'] = ['New York City']
citiesAndServices['Turo'] = ['Los Angeles']


import pickle

datesDict = {}
attributeAndRankingDict = {}

from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


for platform in citiesAndServices:
    dataset = loadtxt(platform+'totalData.csv', delimiter=",")

    # print(len(dataset[0]))
    # time.sleep(10000)

    X = dataset[:,0:28]
    Y = dataset[:,28]

    
    seed = 7
    test_size = 0.33
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
    # fit model no training data


    model = XGBClassifier()
    model.fit(X_train, y_train)
    # make predictions for test data
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]
    # evaluate predictions
    accuracy = accuracy_score(y_test, predictions)
    print(platform, "Accuracy: %.2f%%" % (accuracy * 100.0))

    file_name = platform+"_xgb.pkl"

    # save
    pickle.dump(model, open(file_name, "wb"))

    # # load
    # xgb_model_loaded = pickle.load(open(file_name, "rb"))

    # # test
    # ind = 1
    # test = X_val[ind]
    # xgb_model_loaded.predict(test)[0] == xgb_model.predict(test)[0]