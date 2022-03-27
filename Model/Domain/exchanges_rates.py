from sqlalchemy import Column, Integer, Float, String
from datetime import datetime

from Utils.utils import Base


class ExchangeRates(Base):

    __tablename__ = 'exchangerates'

    id = Column(Integer, primary_key=True)
    from_currency = Column(String(3), nullable=False)
    to_currency = Column(String(3), nullable=False)
    date_time = Column(datetime, nullable=False)
    rate = Column(Float, nullable=False)

