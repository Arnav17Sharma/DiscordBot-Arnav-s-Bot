from bs4 import BeautifulSoup
import requests


def wiki(query):
    source = requests.get(f'https://en.wikipedia.org/wiki/{query}').text

    soup = BeautifulSoup(source, 'lxml')
    body = soup.find('table', class_='infobox')
    l = body.find_all('tr')

    d={}
    for tr in l:
        try:
            th = tr.find('th')
            td = tr.find('td')
            if th.text=="":th.text="NA"
            if td.text=="":td.text="NA"
            d[th.text] = td.text
        except:pass
    return d