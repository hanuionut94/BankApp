from Model.Domain.users_deposits import UsersDeposits
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker



class DBUsersDepositsRepository():
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root@localhost:3306/BankApp')
        self.session = sessionmaker(bind=self.engine)()

    #CREATE Deposits
    def add_deposit(self,user_id, currency, name, amount, description):
        new_deposit = UsersDeposits(
            user_id = user_id,
            currency = currency,
            name = name,
            amount = amount,
            description = description
        )

        self.session.add(new_deposit)
        self.session.commit()

    #READ
    def get_deposit(self, user_id):

        with self.engine.connect() as conn:
            query = conn.execute(text(f'SELECT * FROM usersdeposits WHERE user_id = "{user_id}"'))
            result = query.fetchall()[0]

            user = UsersDeposits(
                user_id = user_id,
                currency = result[1],
                name = result[2],
                amount = result[3],
                description = result[4]
            )

            return user

    #UPDATE
    def update_deposit(self, user_id, **kwargs):
        # TODO: currency exachange
        with self.engine.connect() as conn:
            # conn.execute(text(f'UPDATE usersdeposits SET name = "{name}", amount = "{amount}", description = "{description}" WHERE user_id = "{user_id}"'))
            conn.execute(text(f'UPDATE usersdeposits SET name = "{kwargs}" WHERE user_id = "{user_id}"'))

    #DELETE
    def delete_deposit(self, user_id):
        with self.engine.connect() as conn:
            conn.execute(text(f'DELETE FROM usersdeposits WHERE user_id = "{user_id}"'))

if __name__ == '__main__':
    repo = DBUsersDepositsRepository()

    # repo.add_deposit(
    #     user_id=413,
    #     currency='dol',
    #     name='depozit2',
    #     amount=14423.45,
    #     description='al 2 lea depozit'
    # )
    #
    # repo.add_deposit(
    #     user_id=112,
    #     currency='eur',
    #     name='depozit1',
    #     amount=423.45,
    #     description='primul depozit'
    # )
    #
    # print(repo.get_deposit(413))
    #
    repo.update_deposit(123, name='depozit2', description='al 2 lea depozit')

    # repo.delete_deposit(413)
