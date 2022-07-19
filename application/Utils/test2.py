# import csv
# import re

# import requests
# import xml.etree.ElementTree as ET

# from bs4 import BeautifulSoup
# from datetime import datetime, date


# def parseXML():
#     url = "https://bnr.ro/Cursurile-pietei-valutare-in-format-XML-3424-Mobile.aspx"
#     html_page = requests.get(url).text
#     soup = BeautifulSoup(html_page, 'html.parser')
#     a = [link.get('href') for link in soup.findAll('a', attrs={'href': re.compile("xrates.xml$")})][0]
#     resp = requests.get(a)
#     with open('exchange.xml', 'wb') as f:
#         f.write(resp.content)
#     tree = ET.parse('exchange.xml')
#     root = tree.getroot()

#     dict1 = {}
#     a = [x.attrib['currency'] for x in root[1][2] for key in x.attrib.keys() if key == 'multiplier']
#     for x in root[1][2]:
#         if x.attrib.get('currency') in a:
#             b = float(x.text) / 100
#             dict1[x.attrib.get('currency')] = b
#         else:
#             dict1[x.attrib.get('currency')] = float(x.text)
#     print(dict1.values())
#     print(date.today())
#     c = datetime.strptime(root[0][1].text, '%Y-%m-%d').date()
#     print(c)
#     print(type(root[0][1].text))


def decompose(n):
    a = n**2
    l = []
    for x in reversed(range(0, n)):
        if a - x**2 > 0:
            l.append(x)
            a -= x**2
        elif   x == 1:
            l.append(x)
        else:
            continue

    return l.reverse()

print(decompose(11))
a = 5
print(a**2.5)