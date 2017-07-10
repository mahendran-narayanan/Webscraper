from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import os
import re
import requests
"""
    The url here is the google image search url which can be copied after searching for a particular image
"""
url=''  # Enter your url here
response=requests.get(url)
page=response.content
soup=BeautifulSoup(page)
count=1
n=int(raw_input("Enter the number of images to download (limit<20) :"))
for i in soup.findAll("img",src=True):
    if(count<=n):
        urllib.urlretrieve(i['src'],"image_"+str(count)+".png")
        count+=1
    else:
        break
