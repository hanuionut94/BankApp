from sqlalchemy.orm import sessionmaker
from Model.Domain.exchanges_rates import ExchangeRates
from Utils.utils import engine


class DBExchangeRatesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)

    #READ
    def get_exhange(self, from_currency, to_currency):
        return self.session.query(DBExchangeRatesRepository).filter_by(from_currency=from_currency,to_currency=to_currency).first()

    #READ ALL
    def get_all_exchanges(self):
        return self.session.query(DBExchangeRatesRepository)