from sqlalchemy import Column, String
from sqlalchemy.types import Date, DateTime
from sqlalchemy.orm import relationship
from Model.Domain.users_credentials import UsersCredentials
from Model.Domain.users_deposits import UsersDeposits
from Model.Domain.users_cards import UsersCards
from Model.Domain.users_transactions import UsersTransactions

from Model.Domain.currencies import Currencies


from Utils.utils import Base


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(String(13), primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email_name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    phone_number = Column(String(10), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    join_date = Column(DateTime, nullable=False)
    # users_deposits = relationship('UsersDeposits', back_populates='users')
    # users_transactions = relationship('UsersTransactions', back_populates='users')
    # users_accounts = relationship('UsersAccounts', back_populates='users')
    # users_credentials = relationship('UsersCredentials', back_populates='users')
    # users_cards = relationship('UsersCards', back_populates='users')


    def __repr__(self):
        return f'user id = {self.user_id}\n' \
               f'first name = {self.first_name}\n' \
               f'last name = {self.last_name}\n' \
               f'email = {self.email_name}\n' \
               f'phone = {self.phone_number}\n' \
               f'date of birth = {self.date_of_birth}\n' \
               f'join date = {self.join_date}'
