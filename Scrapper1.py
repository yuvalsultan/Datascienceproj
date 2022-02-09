
# coding: utf-8

# In[8]:


#importing the libraries
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import json, csv
from time import sleep
import time
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import json, csv
from time import sleep
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import re
import os
driver = webdriver.Chrome(ChromeDriverManager().install())


# In[9]:


list_of_urls = [
    'https://www.amazon.com/s?k=earphones&ref=nb_sb_noss_2'
    'https://www.amazon.com/s?k=headphones&ref=nb_sb_noss_2'
    'https://www.amazon.com/s?k=watches&ref=nb_sb_noss_2'
    'https://www.amazon.com/s?k=shirts&ref=nb_sb_noss_2'
 ]

import requests
headers = {
  'authority': 'www.amazon.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'rtt': '50',
  'downlink': '10',
  'ect': '4g',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
}


def getDescription(url) :
    page = requests.get(url, headers=headers)
    results = soup.find(id='productOverview_feature_div')
    return results.text

def getResults(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results=(soup.find_all('div', {'data-component-type' : 's-search-result'}))
    return results
if(not os.path.exists("dataFinal.csv")):
    results_list = []
    for url in list_of_urls:
        results_list.append(getResults(url))

for link in list_of_urls:
    resp = requests.get(link)
    buffer = int(time.time() % 100)
    if (resp.status_code == 200):
        def createCSV(resultslist) :
            for results in resultslist:
                for item in results:
                        atag = item.h2.a
                        name = atag.text.strip()
                        url = 'http://www.amazon.com' + atag.get('href')
                        try:
                            offer_price = int(item.find('span','a-price').find('span','a-offscreen').text[1:])
                        except:
                            prioffer_pricece = np.nan
                        try:
                            img_link = int(item.find('span','a-image').find('span','a-offscreen').text[1:])
                        except:
                            img_link = np.nan
                        try:
                            mrp = int(item.find('span','a-image').find('span','a-offscreen-mrp-segment32').text[1:])
                        except:
                            mrp = np.nan
                        try: 
                            rating = item.i.text
                        except:
                            rating = ''
                        try:
                            no_of_reviews = item.find('span', {'class': 'a-size-base','dir' : 'auto'}).text
                        except:
                            no_of_reviews = ''
                        try:
                            title = item.find('span', {'class': 'a-size-desc','dir' : 'auto'}).text
                        except:
                            title = ''
                        try:
                            bseller = item.find('span', {'class': 'a-size-base-BestSeller','dir' : 'auto'})
                        except:
                            bseller = np.nan
                        try:
                            curr = item.find('span', {'class': 'a-product-country-currency','dir' : 'auto'})
                        except:
                            curr = np.nan
                        try:
                            cat = item.find('span', {'class': 'cl-category-list-option','dir' : 'auto'})
                        except:
                            cat = np.nan
                        try:
                            sponsered = item.find('span', {'class': 'a-product-spon','dir' : 'auto'})
                        except:
                            sponsered = np.nan
                        description = getDescription(url)
                        l = [item,img_link,sponsered,title,offer_price,curr,rating,cat,mrp,bseller]
                        data.append(l)
            return pd.DataFrame(data, columns = ["product_link","image_link","sponsered","title","offer_price","currency","rating","category","mrp","isBestSeller"])

    else:
        link = "dataFinal.csv"
        data = pd.read_csv(link)
        data = data[buffer:]
        for index, rows in data.iterrows():
            print(rows)
            sleep(4)
        pass


# In[ ]:





# In[ ]:




