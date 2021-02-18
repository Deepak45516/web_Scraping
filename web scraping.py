#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system(' pip install beautifulsoup4')


# In[3]:


get_ipython().system(' pip install requests')


# In[4]:


import sys


# In[5]:


import time


# In[6]:


from bs4 import BeautifulSoup


# In[7]:


import requests


# In[65]:


try:
    page=requests.get('https://www.indiafreestuff.in/oraimo-firefly-2s-12w-fast-wall-charger')
except Exception as e:
    error_type, error_obj, error_info=sys.exc_info()
    print('error for link:',url)
    print(error_type, 'Line:', error_info.tb_lineno)
    
time.sleep(2)
soup=BeautifulSoup(page.text, 'html.parser')
links=soup.find_all('div')


# In[67]:


page


# In[60]:


soup


# In[63]:


links


# In[68]:


for i in links:
    print(i.text)
    print("\n")


# In[ ]:




