#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import requests
from time import sleep
browser = webdriver.Chrome()
browser.get('https://coinmarketcap.com/ja/currencies/bitcoin/')
coin_price=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span")
#ニュース一覧を上から順に繰り返します/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span")


# In[7]:


coin_text="ビットコイン(BTC) "


# In[8]:


coin_text=coin_text+coin_price.text


# In[39]:


WEBHOOK_URL = "https://discordapp.com/api/webhooks/1003301610069426296/T4AoR7IJlspRulYO4ZuXw8_Ke2vVz68jDjajF99UUTeZ4veQfSsaPH0EPCMEGNhl3gjg?wait=true"
payload = {
    "username"      : "Market Price",
    "content"       : str(coin_text),
    "avatar_url"    : "https://www.pngfind.com/pngs/m/56-568764_message-png-message-icon-png-white-transparent-png.png",
}

### メッセージだけ
res = requests.post( WEBHOOK_URL, json=payload )
print( res.status_code )
print( json.dumps( json.loads(res.content), indent=4, ensure_ascii=False ) )


# In[41]:


get_ipython().run_line_magic('run', 'C:\\Users\\jun19\\Downloads/bitcoin.py')


# In[ ]:




