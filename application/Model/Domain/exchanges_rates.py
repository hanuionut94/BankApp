from sqlalchemy import Column, Integer, Float, CHAR
from datetime import datetime

from Utils.utils import Base


class ExchangeRates(Base):

    __tablename__ = 'exchangerates'

    id = Column(Integer, primary_key=True)
    currency = Column(CHAR(3), nullable=False)
    date_time = Column(CHAR(20), nullable=False)
    rate = Column(Float, nullable=False)

