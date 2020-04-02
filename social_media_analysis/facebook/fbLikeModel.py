import pandas as pd
from sklearn import preprocessing
import numpy as np
from datetime import datetime
import dateutil
import matplotlib.pyplot as plt
import pip
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pickle

full=pd.read_csv('facebooklike.csv', sep=',', na_values='NaN')

toDrop = ['userid','tenure', 'age','friendships_initiated','likes_received','mobile_likes','mobile_likes_received','www_likes','www_likes_received']
processed = full.drop(toDrop,axis=1)

#convert gender into male=1 & female=0
processed['gender']=(processed['gender']=='male').astype(int)

modified=processed

# test=modified[0:0]
# train=modified[0:0]

# for i in range(len(modified)):
#     if((i%100)==0):
#         test = pd.concat([test, modified[i:i+1]], axis=0)
#     else:
#         train = pd.concat([train, modified[i:i+1]], axis=0)

# X_train = train
# X_test = test
# y_train = train['likes']
# y_test = test['likes']

# X_train = X_train.reset_index(drop=True)
# X_test = X_test.reset_index(drop=True)

# y_train = X_train['likes']
# X_train = X_train.drop(['likes'],axis=1)

# y_test = X_test['likes']
# X_test = X_test.drop(['likes'],axis=1)

y_train=modified['likes']
X_train=modified.drop(['likes'],axis=1)

model_xgb = xgb.XGBRegressor(max_depth=6, learning_rate=0.01, n_estimators=2000)
model_xgb.fit(X_train, y_train)


pickle.dump(model_xgb, open('fbLikeModel.pkl','wb'))
 