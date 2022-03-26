from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.types import DateTime

Base = declarative_base()


class Users(Base):

    __tablename__ = 'users'

    user_id = Column(String(13), primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email_name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    phone_number = Column(String(10), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    join_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f'user id = {self.user_id}\n' \
               f'first name = {self.first_name}\n' \
               f'last name = {self.last_name}\n' \
               f'email = {self.email_name}\n' \
               f'phone = {self.phone_number}\n' \
               f'date of birth = {self.date_of_birth}\n' \
               f'join date = {self.join_date}'

