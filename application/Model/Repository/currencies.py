from sqlalchemy.orm import sessionmaker
from application.Model.Domain.currencies import Currencies
from application.Utils.utils import Base, engine
from application.Utils.xml import rates


class DBCurrenciesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    #ADD
    def add_currency(self):
        for key in rates().keys():
            currencies = Currencies(
                currency = key
            )
            self.session.add(currencies)
        self.session.commit()

    # READ
    def get_all_currency(self):
        return self.session.query(Currencies).all()

    def get_currency(self, currency):
        return self.session.query(Currencies).filter_by(currency=currency).first()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = DBCurrenciesRepository()

    print(repo.add_currency())