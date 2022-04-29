from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker, relationship

from Utils.utils import Base, engine


class Currencies(Base):

    __tablename__ = 'currencies'

    currency = Column(String(3), primary_key=True)
    # users_transactions = relationship('UsersTransactions', back_populates='currencies')

    def __repr__(self):
        return f'{self.currency}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()

    new = Currencies(
        currency = 'USD'
    )


    session.add(new)
    session.commit()


