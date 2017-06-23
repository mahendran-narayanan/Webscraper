import requests
from BeautifulSoup import BeautifulSoup 
url = 'http://www.contextures.com/xlSampleData01.html'
#url='https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
response = requests.get(url)
html=response.content
soup= BeautifulSoup(html)
table=soup.find('table')
index=0
for row in table.findAll('tr'):
    col=row.findAll('td')
    for c in col:
        res= c.find('p').extract()
        print res.getText()
'''
tablebody=soup.find('table')
row= tablebody.find_all('tr')
for r in row:
    data=[]
    col=r.find_all('td')
    for td in col:
        data.append(td)
    print data
'''
