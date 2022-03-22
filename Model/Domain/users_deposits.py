from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class UsersDeposits():
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    currenty = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)