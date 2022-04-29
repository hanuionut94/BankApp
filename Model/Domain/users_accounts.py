from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from Utils.utils import Base


class UsersAccounts(Base):
    __tablename__ = 'usersaccounts'

    user_id = Column(String(13)) #ForeignKey("users.user_id"))
    account_number = Column(String(24),  primary_key=True)
    currency = Column(String(3))
    amount = Column(Float(2), nullable=False)

    # users = relationship("Users", back_populates="users_accounts")

    def __repr__(self):
        return f'{self.user_id}, {self.account_number}, {self.currency}, {self.amount}'


