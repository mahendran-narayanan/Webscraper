from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import os
import re
import requests
"""
   The url here is the google image search url which can be copied after searching for a particular image
"""
url='https://www.google.co.in/search?q=cars&rlz=1C1CHZL_enIN742IN742&source=lnms&tbm=isch&sa=X&ved=0ahUKEwikn5e06vjUAhWKto8KHcOTBnsQ_AUICigB&biw=1366&bih=638'
response=requests.get(url)
page=response.content
soup=BeautifulSoup(page)
"""
This program can scrap only first 12 - 13 images beacuse of the string limit in naming it
"""
co='a';
for i in soup.findAll("img",src=True):
    urllib.urlretrieve(i['src'],"a"+co+".png")
    co=co+'1'
    
