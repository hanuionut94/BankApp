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

    # READ WITH NAME
    def get_deposit_by_name(self, user_id, name):
        return self.session.query(UsersDeposits).filter_by(user_id=user_id, name=name).first()

    def get_deposit_currency_name(self, user_id, currency, name):
        return self.session.query(UsersDeposits).filter_by(user_id=user_id, currency=currency, name=name).first()

    # READ ALL
    def get_all_deposits(self, user_id):
        return self.session.query(UsersDeposits).filter_by(user_id=user_id).all()

    # UPDATE
    def update_deposit(self, user_id, currency, name, amount):
        if amount:
            self.session.query(UsersDeposits).filter_by(user_id=user_id, currency=currency, name=name).update(
                {'amount': amount})
            self.session.commit()

    # DELETE
    def delete_deposit(self, user_id, currency, name):
        self.session.query(UsersDeposits).filter_by(user_id=user_id, currency=currency, name=name).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = DBUsersDepositsRepository()

