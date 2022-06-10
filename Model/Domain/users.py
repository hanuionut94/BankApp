from sqlalchemy import Column, CHAR, VARCHAR
from sqlalchemy.types import Date, DateTime
from Utils.utils import Base


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(CHAR(13), primary_key=True)
    first_name = Column(VARCHAR(30), nullable=False)
    last_name = Column(VARCHAR(30), nullable=False)
    email_name = Column(VARCHAR(50), nullable=False)
    address = Column(VARCHAR(50), nullable=False)
    phone_number = Column(CHAR(10), nullable=False)
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
