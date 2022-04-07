from Model.Domain.users_deposits import UsersDeposits
from sqlalchemy.orm import sessionmaker

from Utils.utils import Base, engine


class DBUsersDepositsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    # CREATE Deposits
    def add_deposit(self, user_id, currency, name, amount, description):
        new_deposit = UsersDeposits(
            user_id=user_id,
            currency=currency,
            name=name,
            amount=amount,
            description=description
        )

        self.session.add(new_deposit)
        self.session.commit()

    # READ
    def get_deposit_by_currency(self, user_id, currency):
        return self.session.query(UsersDeposits).filter_by(user_id=user_id, currency=currency).first()

    #READ WITH NAME
    def get_deposit_by_name(self, user_id, name):
        return self.session.query(UsersDeposits).filter_by(user_id=user_id, name=name).first()

    def get_deposit_currency_name(self, user_id, currency, name):
        return self.session.query(UsersDeposits).filter_by(user_id=user_id, currency=currency, name=name).first()

    # READ ALL
    def get_all_deposits(self, user_id):
        return self.session.query(UsersDeposits).filter_by(user_id=user_id).all()


    #UPDATE
    def update_deposit(self, user_id, currency, name, amount):
        if amount:
            self.session.query(UsersDeposits).filter_by(user_id=user_id, currency=currency, name=name).update({'amount':amount})
            self.session.commit()


    # DELETE
    def delete_deposit(self, user_id):
        self.session.query(UsersDeposits).filter_by(user_id=user_id).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = DBUsersDepositsRepository()

    # repo.add_deposit(
    #     user_id=1234,
    #     currency='dol',
    #     name='depozit2',
    #     amount=14423.45,
    #     description='al 2 lea depozit'
    # )
    #
    # repo.add_deposit(
    #     user_id=123,
    #     currency='eur',
    #     name='depozit1',
    #     amount=423.45,
    #     description='primul depozit'
    # )

    print(repo.get_deposit('123'))

    repo.update_deposit(123, name='depozit3', description='al 3 lea depozit')
    #
    repo.delete_deposit('1234')
