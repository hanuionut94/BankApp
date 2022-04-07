from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime
from Model.Domain.currencies import Currencies
from Utils.utils import Base


class UsersTransactions(Base):
    __tablename__ = 'userstransactions'

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(13)) #, ForeignKey("users.user_id"))
    currency = Column(String(3)) #, ForeignKey("currencies.currency"))
    amount = Column(Float(2), nullable=False)
    vendor = Column(String(100), nullable=False)
    date_time = Column(DateTime, nullable=False)

    # users = relationship('Users', back_populates='users_transactions')
    #
    # currencies = relationship('Currencies', back_populates='users_transactions')

    def __repr__(self):
        return f'{self.transactions_id}, {self.user_id}, {self.currency}, {self.amount}, {self.vendor}, {self.date_time}'
