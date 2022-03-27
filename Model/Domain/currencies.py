from sqlalchemy import Column, String
from Utils.utils import Base


class Currencies(Base):
    __tablename__ = 'currencies'

    currency = Column(String(3), primary_key=True)
