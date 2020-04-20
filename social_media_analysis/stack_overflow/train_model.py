#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
get_ipython().run_line_magic('matplotlib', 'inline')

# In[24]:

df=pd.read_csv('training_data.csv')
df.head()

# In[25]:

df.shape

# In[26]:

X=df[['tag_count','is_answered','is_closed','view_count','answer_count','last_edit_date','score']].values
y=df['percentage'].values

# In[27]:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# In[28]:

regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# In[29]:
y_pred = regressor.predict(X_test)

# In[30]:

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)

# In[31]:

df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

# In[22]:

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# In[32]:

filename = 'finalized_model.sav'
pickle.dump(regressor, open(filename, 'wb'))

# In[ ]:




