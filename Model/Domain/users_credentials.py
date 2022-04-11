from sqlalchemy import Column, String
from Utils.utils import Base


class UsersCredentials(Base):
    __tablename__ = 'userscredentials'

    user_id = Column(String(13), primary_key=True)  # ForeignKey("users.user_id"),
    username = Column(String(30), nullable=False)
    user_password_hash = Column(String(256), nullable=False)

    # users = relationship('Users', back_populates='users_credentials')

    def __repr__(self):
        return f'{self.user_id}, {self.username}, {self.user_password_hash} '
