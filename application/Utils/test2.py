# Python code to illustrate parsing of XML files
# importing the required modules
import csv
import re

import requests
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from datetime import datetime, date


def parseXML():
    url = "https://bnr.ro/Cursurile-pietei-valutare-in-format-XML-3424-Mobile.aspx"
    html_page = requests.get(url).text
    soup = BeautifulSoup(html_page, 'html.parser')
    a = [link.get('href') for link in soup.findAll('a', attrs={'href': re.compile("xrates.xml$")})][0]
    resp = requests.get(a)
    with open('exchange.xml', 'wb') as f:
        f.write(resp.content)
    tree = ET.parse('exchange.xml')
    root = tree.getroot()

    dict1 = {}
    a = [x.attrib['currency'] for x in root[1][2] for key in x.attrib.keys() if key == 'multiplier']
    for x in root[1][2]:
        if x.attrib.get('currency') in a:
            b = float(x.text) / 100
            dict1[x.attrib.get('currency')] = b
        else:
            dict1[x.attrib.get('currency')] = float(x.text)
    print(dict1.values())
    print(date.today())
    c = datetime.strptime(root[0][1].text, '%Y-%m-%d').date()
    print(c)
    print(type(root[0][1].text))


print(parseXML())
