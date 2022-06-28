from sqlalchemy import Column, CHAR, VARCHAR
from application.Utils.utils import Base


class UsersCredentials(Base):
    __tablename__ = 'userscredentials'

    user_id = Column(CHAR(13), primary_key=True)  # ForeignKey("users.user_id"),
    username = Column(VARCHAR(30), nullable=False)
    user_password_hash = Column(VARCHAR(500), nullable=False)

    # users = relationship('Users', back_populates='users_credentials')

    def __repr__(self):
        return f'{self.user_id}, {self.username}, {self.user_password_hash} '
