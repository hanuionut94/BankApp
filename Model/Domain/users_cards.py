from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import DateTime

from Utils.utils import Base

class UserCards(Base):

    __tablename__ = 'usercards'

    user_id = Column(String(13), foreign_key=ForeignKey('users.user_id', ondelete='CASCADE'))
    card_number = Column(String(16), primary_key=True)
    pin_hash = Column(String(256), nullable=False)
    cvv_hash = Column(String(256), nullable=False)
    expiration_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f'{self.user_id},{self.card_number}, {self.expiration_date}'