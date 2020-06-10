import pandas as pd
from sklearn import preprocessing
import numpy as np
from datetime import datetime
import dateutil
# from hyperopt import hp
import matplotlib.pyplot as plt
import pip
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pickle


full=pd.read_csv('facebookAds.csv', sep=',', na_values='NaN')

toDrop=['AdID','LandingPage','Location','Placements','AdSpendCurrency','SourceFile','SourceZip','pages']

modified = full.drop(toDrop,axis=1)
pd.options.display.float_format = '{:.2f}'.format

copy=modified["CreationDate"].copy()
starts=modified['Age'].copy()
ends=modified['Age'].copy()
count=modified['AdText'].copy()
clicks_copy=modified['Clicks'].copy()
impre_copy=modified['Impressions'].copy()
spend_copy=modified['AdSpend'].copy()

for i in range(len(modified)):  
    
    d=modified["CreationDate"][i]
    try:
        date_str=d[:8]
        dt=datetime.strptime(date_str, '%m/%d/%y').weekday()
    except:
        dt=dt
    copy[i] = dt
    
    a=modified["Age"][i]
    try:
        txtCount=len(modified['AdText'][i])
        if('-' in a):
            start=a.split('-')[0]
            end=a.split('-')[1][:3]
        else:
            start=start
            end=end
    except:
        txtCount=txtCount
        start=start
        end=end
    count[i]=txtCount
    starts[i] = start
    ends[i]=end
    
    try:
        clicks=int(modified["Clicks"][i])
        impressions=int(modified["Impressions"][i])
        spends=int(modified["AdSpend"][i])
    except:
        clicks=clicks
        impressions=impressions
        spends=spends
        
    clicks_copy[i]=clicks
    impre_copy[i]=impressions
    spend_copy[i]=spends
modified["date"]=copy.astype(np.int64)
modified['mon']=(modified['date']==0).astype(int)
modified['tue']=(modified['date']==1).astype(int)
modified['wed']=(modified['date']==2).astype(int)
modified['thu']=(modified['date']==3).astype(int)
modified['fri']=(modified['date']==4).astype(int)
modified['sat']=(modified['date']==5).astype(int)
modified['sun']=(modified['date']==6).astype(int)

modified['male']=((modified['Gender']=="Male")).astype(int)
modified['female']=((modified['Gender']=="Female")).astype(int)
modified['all']=((modified['Gender']=="All")).astype(int)

modified['AdTextRes']= count.astype(np.int64)
modified["startAge"]=starts.astype(np.int64)
modified["endAge"]=ends.astype(np.int64)

modified['AdClicks']= clicks_copy.astype(np.int64)
modified["AdImpressions"]=impre_copy.astype(np.int64)
modified["AdSpends"]=spend_copy.astype(np.int64)


modified = modified.drop(['AdText','date','EndDate','CreationDate','Gender','Age'], axis=1)
modified = modified.drop(['Clicks','Impressions','AdSpend'],axis=1)

X_train = modified
y_train = X_train['AdClicks'] 
X_train = X_train.drop(['AdClicks'],axis=1)

y_train_impre=modified['AdImpressions']
X_train_impre=modified.drop(['AdImpressions','AdClicks'],axis=1)


model_xgb= xgb.XGBRegressor(max_depth=6, learning_rate=0.01, n_estimators=2000)
model_xgb_impre= xgb.XGBRegressor(max_depth=6, learning_rate=0.01, n_estimators=2000)
model_xgb.fit(X_train, y_train)
model_xgb_impre.fit(X_train_impre, y_train_impre)

pickle.dump(model_xgb, open('fbAdsModel.sav','wb'))
pickle.dump(model_xgb_impre, open('fbAdsImpreModel.sav','wb'))
