from application.Model.Repository.users_transactions import DBUsersTransactionsRepository


class UsersTransactionsController:
    def __init__(self, users_transactions_repo):
        self.users_transactions_repo = users_transactions_repo

    def add_transaction(self, user_id, amount, currency, vendor):
        self.users_transactions_repo.create_transaction(user_id, amount, currency, vendor)

if __name__ == '__main__':
    user_transactions_repo = DBUsersTransactionsRepository()

    user_transactions_ctrl = UsersTransactionsController(user_transactions_repo)