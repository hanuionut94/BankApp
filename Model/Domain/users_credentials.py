from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base

class UsersCredentials(Base):

    __tablename__ = 'userscredentials'

    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey('users.user_id', ondelete='CASCADE'))
    username = Column(String(30), nullable=False)
    user_password_hash = Column(String(25), nullable=False)

    def __repr__(self):
        return f'{self.user_id}, {self.username}, {self.user_password_hash} '