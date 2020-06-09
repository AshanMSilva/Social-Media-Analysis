import pandas as pd
     
training_data = (pd.read_csv('links.csv'))

links = training_data.iloc[:,0].values
#features =training_data.iloc[:,1:-1].values
ids=[]
for link in links:
    id = link[32:43]
    ids.append(id)
print(ids)

df = pd.DataFrame({'ChannelID':ids}).to_csv('ids.csv')