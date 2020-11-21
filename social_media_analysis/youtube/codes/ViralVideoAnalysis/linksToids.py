import pandas as pd

training_data = (pd.read_csv('links.csv'))

links = training_data.iloc[:,0].values

ids=[]
for link in links:
    id = link[32:43]
    ids.append(id)


df = pd.DataFrame({'ChannelID':ids}).to_csv('ids.csv')
print("done")
