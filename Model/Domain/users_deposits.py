from sqlalchemy import Column, Float, ForeignKey, Constraint, CHAR, VARCHAR
from sqlalchemy.orm import relationship
from Utils.utils import Base


class UsersDeposits(Base):

    __tablename__ = 'usersdeposits'

    user_id = Column(CHAR(13),ForeignKey("users.user_id"), primary_key=True)
    currency = Column(CHAR(3), nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(VARCHAR(200), nullable=False)
    # users = relationship('Users', back_populates='users_deposits')

    def __repr__(self):
        return f'user id = {self.user_id}, currency = {self.currency}, name = {self.name}, amount = {self.amount}, description = {self.description}'
