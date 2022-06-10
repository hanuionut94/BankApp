import random
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from Model.Domain.users_accounts import UsersAccounts
from Utils.utils import engine, Base


class DBUsersAccountsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    #CREATE
    def create_account(self, user_id, currency, amount):

        def account(currency):
            card = 'RO'+ str(random.randint(10,99))+'RNCB' + currency +str(random.randint(1000000000000,9999999999999))
            return card

        new_account = UsersAccounts(
            user_id=user_id,
            account_number=account(currency),
            currency=currency,
            amount=amount
        )
        result = self.session.query(func.count()).select_from(UsersAccounts).filter_by(user_id=user_id, currency=currency).first()
        if result[0] < 1:
            self.session.add(new_account)
            self.session.commit()
        else:
            print('One account for each currency!!!')

   #READ
    def get_account(self, user_id, currency):
        return self.session.query(UsersAccounts).filter_by(user_id=user_id, currency=currency).first()

    #READ ALL
    def get_all_accounts(self, user_id):
        return self.session.query(UsersAccounts).filter_by(user_id=user_id).all()

    def update_account(self, user_id, currency, amount):
        if amount:
            self.session.query(UsersAccounts).filter_by(user_id=user_id, currency=currency).update({'amount': amount})
            self.session.commit()

    #DELETE ACOOUNT
    def delete_account(self, user_id, currency):
        self.session.query(UsersAccounts).filter_by(user_id=user_id, currency=currency).first()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = DBUsersAccountsRepository()
