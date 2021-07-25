import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn import *


with open('../models/finalmodelDT.sav','rb') as f:
    DT = pickle.load(f)

with open('../models/finalmodelLR.sav','rb') as f:
    LR = pickle.load(f)

with open('../models/finalmodelGBC.sav','rb') as f:
    GBC = pickle.load(f)

with open('../models/finalmodelRF.sav','rb') as f:
    RFC = pickle.load(f)

def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"

def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt) 
    new_x_test = new_def_test["text"]
    vectorization = pickle.load(open('vectorization.pickle', 'rb'))
    #vectorization = TfidfVectorizer()
    new_xv_test = vectorization.transform(new_x_test)
    pred_LR = LR.predict(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_GBC = GBC.predict(new_xv_test)
    pred_RFC = RFC.predict(new_xv_test)
    fw = open("results.txt","w")

    if(pred_DT[0] == 0 and pred_RFC[0] == 0 and pred_GBC[0] == 0 and pred_LR[0] == 0):
        fw.write("Fake News")
    else:
        fw.write("Not a Fake News")
'''print("\n\nLR Prediction: {} \nDT Prediction: {} \nGBC Prediction: {} \nRFC Prediction: {}".format(output_lable(pred_LR[0]),                                                                                                       output_lable(pred_DT[0]), 
                                                                                                              output_lable(pred_GBC[0]), 
                                                                                                              output_lable(pred_RFC[0])))'''

with open("news.txt") as f:
    news = f.read()

#news = "watchu doin broasdcfiosa;docmspomdcposma['pocmposmdcpoam?asdasdasdsada"
manual_testing(news)



