from sqlalchemy import Column, Integer, CHAR, ForeignKey, Boolean, TEXT
from datetime import datetime

from Utils.utils import Base


class Messages(Base):

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(CHAR(13), ForeignKey('users.users_id', ondelete='CASCADE'))
    message = Column(TEXT, nullable=False)
    date = Column(datetime, nullable=False)
    state = Column(Boolean, nullable=False)
