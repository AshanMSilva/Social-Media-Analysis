import pandas as pd


files = ['JPvideos.csv','CAvideos.csv','DEvideos.csv','FRvideos.csv','GBvideos.csv','INvideos.csv','KRvideos.csv','MXvideos.csv','RUvideos.csv','USvideos.csv']
data=[]

for file in files:
    
    datafile = (pd.read_csv(file))
    data += list((datafile.iloc[:,0].values)[:10000])


df = pd.DataFrame({'VideoID':data}).to_csv('data.csv')

print(len(data))