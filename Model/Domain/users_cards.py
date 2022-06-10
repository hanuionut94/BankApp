from sqlalchemy import Column, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date, DateTime

from Utils.utils import Base


class UsersCards(Base):
    __tablename__ = 'userscards'

    user_id = Column(CHAR(13))
    card_number = Column(CHAR(16),primary_key=True)
    pin_hash = Column(CHAR(256), nullable=False)
    cvv_hash = Column(CHAR(256), nullable=False)
    expiration_date = Column(DateTime, nullable=False)

    # users = relationship('Users', back_populates='users_cards')

    def __repr__(self):
        return f'user_id = {self.user_id},card_number = {self.card_number}, expiration_date = {self.expiration_date}'
