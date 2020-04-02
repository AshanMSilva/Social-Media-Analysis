import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd 
from datetime import datetime

#sentiment
import time 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import nltk 
import io 
import operator
import unicodedata 
import numpy as np 
import re 
import string 
from numpy import linalg 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.corpus import webtext 
from nltk.stem.porter import PorterStemmer 
from nltk.stem.wordnet import WordNetLemmatizer 

# open models
app = Flask(__name__)

# instaModel = pickle.load(open('instamodel.pkl', 'rb')) 
fbLikeModel = pickle.load(open('fbLikeModel.pkl', 'rb'))
# fbAdsModel =pickle.load(open('fbAdsModel.pkl', 'rb')) 

@app.route('/')
def home():
    return render_template('facebook_index.html')

@app.route('/sentimentAnalyser')
def sentimentAnalyser():
    return render_template('sentiment.html')
@app.route('/sentiment', methods=['POST'])
def sentiment():
        text=request.form['txt']
        tt=text
        sent_tokenizer = PunktSentenceTokenizer(text) 
        sents = sent_tokenizer.tokenize(text) 
        porter_stemmer = PorterStemmer()
        
        nltk_tokens = nltk.word_tokenize(text) 
        wordnet_lemmatizer = WordNetLemmatizer() 
        nltk_tokens = nltk.word_tokenize(text) 

        text = nltk.word_tokenize(text)
        sid = SentimentIntensityAnalyzer() 
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

        for word in tt.split("\n"): 
                print(word)
                scores = sid.polarity_scores(word)
                c= scores['compound']
                del scores['compound']
                res=max(scores, key=scores.get)


                #res= max(scores.iteritems(), key=operator.itemgetter(1))[0]
        return render_template('sentiment.html', prediction_text='The comment is {}'.format(res), msg=c)

@app.route('/fbLikePredict',methods=['POST'])
def fbLikePredict():
    birthday=request.form["birthday"]
    gender=request.form["gender"]
    friendcount =request.form["friendcount"]
    birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
    year = birthday.year
    month = birthday.month
    day = birthday.day
    if(gender=='Male'):
        gender=1
    if(gender=='Female'):
        gender=0
    year=int(year)
    day=int(day)
    month= int(month)
    gender=int(gender)
    friendcount=int(friendcount)
    final={'dob_day':[day] ,'dob_year':[year] ,'dob_month':[month] ,'gender':[gender] ,'friend_count':[friendcount] }
    final_features=pd.DataFrame.from_dict(final)
    prediction = fbLikeModel.predict(final_features)
    output=int(prediction[0])
    
    # output = round(prediction[0], 2)

    return render_template('facebookLike.html', prediction_text='Likes should be {}'.format(output))

@app.route('/fblikes')
def fblikes():
    return render_template('facebookLike.html')

if __name__ == "__main__":
    app.run(debug=True)