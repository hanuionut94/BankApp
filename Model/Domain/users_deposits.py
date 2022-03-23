from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class UsersDeposits(Base):
    __tablename__ = 'usersdeposits'
    user_id = Column(Integer, primary_key=True)
    currency = Column(String, nullable=False)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)

    def __repr__(self):
        return f'user id = {self.user_id}, currency = {self.currency}, name = {self.name}, amount = {self.amount}, description = {self.description}'
