from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from datetime import datetime

from Utils.utils import Base


class Messages(Base):

    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(13), ForeignKey('users.users_id', ondelete='CASCADE'))
    message = Column(String, nullable=False)
    date = Column(datetime, nullable=False)
    state = Column(Boolean, nullable=False)
