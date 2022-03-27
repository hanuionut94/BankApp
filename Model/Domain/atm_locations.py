from sqlalchemy import Column, String, Integer
from Utils.utils import Base


class ATMLocations(Base):
    __tablename__ = 'atmlocantions'

    atm_id = Column(String(9), primary_key=True)
    address = Column(String(200), nullable=False)
    lat = Column(String(9), nullable=False)
    lng = Column(String(9), nullable=False)
    numbers_atm = Column(Integer, nullable=False)
