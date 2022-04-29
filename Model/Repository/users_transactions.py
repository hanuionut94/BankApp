from sqlalchemy.orm import sessionmaker
from Model.Domain.users_transactions import UsersTransactions

from Utils.utils import Base, engine


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

    depo_repo.create_transactions(
        transaction_id=123,
        user_id='1234',
        currency='EUR',
        amount=100,
        vendor='Altex',
        date_time='2022-01-02'
    )
    depo_repo.create_transactions(
        transaction_id=124,
        user_id='1235',
        currency='EUR',
        amount= 50,
        vendor='EMAG',
        date_time='2022-04-02'
    )
    depo_repo.create_transactions(
        transaction_id=125,
        user_id='1234',
        currency='USD',
        amount=10,
        vendor='EMAG',
        date_time='2022-03-02'
    )
