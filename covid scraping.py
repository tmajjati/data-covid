#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


# In[24]:


page = requests.get("https://www.worldometers.info/coronavirus")


# In[25]:


page.status_code


# In[26]:


page.content


# In[27]:



soup = BeautifulSoup(page.content, 'lxml')


# In[28]:


print(soup.prettify())


# In[29]:



table = soup.find('table', attrs={'id': 'main_table_countries_today'})


# In[30]:


table


# In[31]:


rows = table.find_all("tr", attrs={"style": ""})


# In[32]:


data = []
for i,item in enumerate(rows):
    
    if i == 0:
        
        data.append(item.text.strip().split("\n")[:13])
        
    else:
        data.append(item.text.strip().split("\n")[:12])


# In[33]:


data


# In[34]:



import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import dask.dataframe as dd

dt = pd.DataFrame(data)
dt = pd.DataFrame(data[1:], columns=data[0][:12]) 
df = dd.from_pandas(dt,npartitions=1)


# In[35]:


df.head()


# In[36]:


df.to_csv('../Extracted_data/data-*.csv')


# In[ ]:




