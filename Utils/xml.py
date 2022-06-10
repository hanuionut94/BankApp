import re
from datetime import datetime
from bs4 import BeautifulSoup
from urllib import request
import requests


def get_link():
    response = requests.get('https://bnr.ro/Cursurile-pietei-valutare-in-format-XML-3424-Mobile.aspx')
    soup = BeautifulSoup(response.text, 'lxml')
    categories = soup.findAll(attrs={'href': re.compile("xrates.xml$")})
    list1 = []

    for i in categories:
        list1.append(i.text)

    xml_link = list1[0]

    link = request.urlopen(xml_link)
    soup = BeautifulSoup(link, 'lxml-xml')
    return soup


def rates():
    soup = get_link()
    multi = soup.find_all('Rate')
    rates = {}
    for item in multi:
        if item.attrs.get('multiplier') == '100':
            multiplier = (float(item.text) / 100)
            rates[item.attrs.get('currency')] = multiplier.__format__(".5f")

        else:
            rates[item.attrs.get('currency')] = float(item.text)
    return rates


def rates_data():
    soup = get_link()
    rates_date = soup.PublishingDate.string
    rates_date = datetime.strptime(rates_date, '%Y-%m-%d').date()
    return rates_date
