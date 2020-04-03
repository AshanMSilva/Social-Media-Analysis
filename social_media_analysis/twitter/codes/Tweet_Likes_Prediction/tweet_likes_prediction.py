# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:13:58 2020

@author: user
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class TweetLikesPrediction():
    def set_tokenizer(self,sentences):
        tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
        tokenizer.fit_on_texts(sentences)
        return tokenizer
    
    def texts_to_sequences(self, sentences, tokenizer):
        sequences=tokenizer.texts_to_sequences(sentences)
        return sequences
    
    def get_padded_sequeces(self, sequences):
        padded_sequences = pad_sequences(sequences)
        return padded_sequences

    def get_padded_sequeces_with_maxlength(self, sequences, maxlength):
        padded_sequences = pad_sequences(sequences, maxlen=maxlength)
        return padded_sequences
    
    def train_model(self, features, labels):
        X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=0.2, random_state=0)
        
        #print(training_data.duration)
        logReg =LogisticRegression()
        
        logReg.fit(features, labels)
        #prediction= logReg.predict(X_test)
        return logReg

# sentences =['I love my dog', 'I love my cat', 'You love my dog!', 'Do you think my dog is amazing?']

# tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
# tokenizer.fit_on_texts(sentences)
# word_index = tokenizer.word_index

# sequences = tokenizer.texts_to_sequences(sentences)

# padded = pad_sequences(sequences) #use maxlen=5 to give len size to array element and use padding='post' to pass zeros from begining to end 
