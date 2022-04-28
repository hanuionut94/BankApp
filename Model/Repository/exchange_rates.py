import requests
from sqlalchemy.orm import sessionmaker
from Utils.utils import engine, Base
import re
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
import urllib.request

import xmltodict



class DBExchangeRatesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)

    #READ
    def get_exhange(self, from_currency, to_currency):
        return self.session.query(DBExchangeRatesRepository).filter_by(from_currency=from_currency,to_currency=to_currency).first()

    #READ ALL
    def get_all_exchanges(self):
        return self.session.query(DBExchangeRatesRepository)


    def get_curs(self):
        url = "https://bnr.ro/Cursurile-pietei-valutare-in-format-XML-3424-Mobile.aspx"
        html_page = requests.get(url).text
        soup = BeautifulSoup(html_page, 'html.parser')
        a = [link.get('href') for link in soup.findAll('a', attrs={'href': re.compile("xrates.xml$")})][0]
        # val_tag = soup.find_all('')
        tree = ET.parse(a)
        root = tree.getroot()

        print(tree)

        for child in root:
            # print(child.tag, child.attrib)
            print(child.attrib['Cube'])



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    exchannge_rates_repo = DBExchangeRatesRepository()

    print(exchannge_rates_repo.get_curs())

