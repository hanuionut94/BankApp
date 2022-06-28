from sqlalchemy.orm import sessionmaker
from application.Model.Domain.users_transactions import UsersTransactions

from application.Utils.utils import Base, engine


class DBUsersTransactionsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    # CREATE
    def create_transactions(self, transaction_id, user_id, currency, amount, vendor, date_time):
        new_transaction = UsersTransactions(
            transaction_id=transaction_id,
            user_id=user_id,
            currency=currency,
            amount=amount,
            vendor=vendor,
            date_time=date_time
        )

        self.session.add(new_transaction)
        self.session.commit()

    # READ
    def get_transaction(self, user_id, **kwargs):
        self.session.query(UsersTransactions).filter_by(user_id=user_id, **kwargs).all()

    # READ ALL
    def get_all_transactions(self, user_id):
        return self.session.query(UsersTransactions).filter_by(user_id=user_id).all()

    # DELETE
    def delete_transaction(self, user_id, transaction_id): #TODO -- try with kwargs
        self.session.query(UsersTransactions).filter_by(user_id, transaction_id)
        self.session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    depo_repo = DBUsersTransactionsRepository()

