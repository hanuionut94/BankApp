from sqlalchemy import Column, VARCHAR, Integer, CHAR
from Utils.utils import Base


class ATMLocations(Base):
    __tablename__ = 'atmlocantions'

    atm_id = Column(VARCHAR(9), primary_key=True)
    address = Column(VARCHAR(200), nullable=False)
    lat = Column(CHAR(9), nullable=False)
    lng = Column(CHAR(9), nullable=False)
    numbers_atm = Column(Integer, nullable=False)
