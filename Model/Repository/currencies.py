from sqlalchemy.orm import sessionmaker
from Model.Domain.currencies import Currencies
from Utils.utils import Base, engine


class DBCurrenciesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    # READ
    def get_all_currency(self):
        return self.session.query(Currencies).all()

    def get_currency(self, currency):
        return self.session.query(Currencies).filter_by(currency=currency).first()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = DBCurrenciesRepository()

    print(repo.get_currency('EUR'))