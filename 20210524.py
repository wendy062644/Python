#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
res = requests.get('https://covid19dashboard.cdc.gov.tw/dash3')
res.encoding = 'utf-8'
s = json.loads(res.text)
s


