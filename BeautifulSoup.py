import requests
from bs4 import BeautifulSoup

data= requests.get('http://www.mg-cc.org/club-information/club-contacts')

soup= BeautifulSoup(data.text, 'html.parser')

for span in soup.findAll('span'):
    for b in span.findAll('b'):
        for br in span.findAll('br'):
            print (b.text)