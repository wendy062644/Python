#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import requests
def main():
    global url_input, text, infor
    wh=[]
    root = Tk()
    root.title('疫情即時訊息')
    root.geometry('1080x720+400+100')
    infor = requests.get('https://covid19dashboard.cdc.gov.tw/dash3')
    
    Label(root, text='台灣疫情即時訊息:', font=("華文行楷", 30), fg='black').grid()
    
    text = Listbox(root, font=('微軟雅黑', 20), width=50, height=10).grid(row=1, columnspan=1)
    
    mainloop()
    
main()


# In[2]:


import requests
import json
res = requests.get('https://covid19dashboard.cdc.gov.tw/dash3')
s = json.loads(res.text)
s


# In[ ]:




