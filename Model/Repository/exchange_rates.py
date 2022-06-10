from urllib import request

import requests
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from Model.Domain.exchanges_rates import ExchangeRates
from Utils.utils import engine, Base
from datetime import date

from Utils.xml import rates_data, rates


class DBExchangeRatesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    # READ
    def get_exhange(self, currency):
        return self.session.query(DBExchangeRatesRepository).filter_by(currency=currency).first()

    def delete_exchange(self):
        self.session.query(ExchangeRates).delete()
        self.session.commit()

    # READ ALL
    def get_all_exchanges(self):
        return self.session.query(DBExchangeRatesRepository)

    def get_curs(self):
        def add_exchange():
            for keys, values in rates().items():
                exchange_rates = ExchangeRates(
                    currency=keys,
                    date_time=rates_data(),
                    rate=values
                )

                self.session.add(exchange_rates)
            self.session.commit()

        today = date.today()

        result = self.session.query(func.count()).select_from(ExchangeRates).first()
        print(result[0])
        if result[0] == 0:
            add_exchange()
        if today != rates_data():
            self.delete_exchange()
            add_exchange()

    def from_currency_to(self, from_currency, amount, to_currency):
        from_currency = self.session.query(ExchangeRates).filter_by(currency=from_currency).first().rate
        to_currency = self.session.query(ExchangeRates).filter_by(currency=to_currency).first().rate
        return ((from_currency * amount) / to_currency).__format__(".4f")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    exchannge_rates_repo = DBExchangeRatesRepository()

    print(exchannge_rates_repo.get_curs())
    # print(exchannge_rates_repo.from_currency_to('EUR', 10, 'USD'))
    # exchannge_rates_repo.delete_exchange()