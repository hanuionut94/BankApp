from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.types import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class UsersTransactions(Base):

    __tablename__ = 'userstransactions'

    transactions_id = Column(Integer, primary_key=True)
    user_id = Column(String(13), foreign_key=ForeignKey('users.user_id', ondelete='CASCADE'))
    currency = Column(String(3), foreign_key=ForeignKey('currencies.currencies', ondelete='CASCADE'))
    amount = Column(Float(2), nullable=False)
    vendor = Column(String(100), nullable=False)
    date_time = Column(DateTime, nullable=False)

    def __repr__(self):
        f'{self.transactions_id}, {self.user_id}, {self.currency}, {self.amount}, {self.vendor}, {self.date_time}'