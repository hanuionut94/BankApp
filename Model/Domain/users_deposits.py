from sqlalchemy import Column, String, Float, ForeignKey, Constraint
from sqlalchemy.orm import relationship
from Utils.utils import Base


class UsersDeposits(Base):

    __tablename__ = 'usersdeposits'

    user_id = Column(String(13),ForeignKey("users.user_id"), primary_key=True)
    currency = Column(String(3), nullable=False)
    name = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(200), nullable=False)
    # users = relationship('Users', back_populates='users_deposits')

    def __repr__(self):
        return f'user id = {self.user_id}, currency = {self.currency}, name = {self.name}, amount = {self.amount}, description = {self.description}'
