from sqlalchemy import Column, String, Float, ForeignKey
from Utils.utils import Base


class UsersAccounts(Base):
    __tablename__ = 'usersaccounts'

    user_id = Column(String(13), foreign_key=ForeignKey('users.users_id', ondelete='CASCADE'))
    account_number = Column(String(24), nullable=False)
    currency = Column(String(3), foreign_key=ForeignKey('currencies.currency', ondelete='CASCADE'))
    amount = Column(Float(2), nullable=False)
