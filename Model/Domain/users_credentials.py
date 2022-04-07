from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UsersCredentials(Base):
    __tablename__ = 'userscredentials'

    user_id = Column(String(13), ForeignKey("users.user_id"), primary_key=True)
    username = Column(String(30), nullable=False)
    user_password_hash = Column(String(25), nullable=False)

    # users = relationship('Users', back_populates='users_credentials')

    def __repr__(self):
        return f'{self.user_id}, {self.username}, {self.user_password_hash} '
