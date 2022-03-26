from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, ForeignKey

Base = declarative_base()


class UsersDeposits(Base):

    __tablename__ = 'usersdeposits'

    user_id = Column(String(13), primary_key=True,foreign_key=ForeignKey('users.user_id', ondelete='CASCADE'))
    currency = Column(String(3), nullable=False)
    name = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(200), nullable=False)

    def __repr__(self):
        return f'user id = {self.user_id}, currency = {self.currency}, name = {self.name}, amount = {self.amount}, description = {self.description}'
