from Model.Repository.users_accounts import DBUsersAccountsRepository


class UsersAccountsController:
    def __init__(self, users_accounts_repo):
        self.users_accounts_repo = users_accounts_repo

    def check_balance(self, user_id, amount, currency):
        users_accounts = self.users_accounts_repo.get_account(user_id, currency)
        if users_accounts and self.users_accounts_repo.get_account(user_id, currency).amount > amount:
            return True
        return False

    def transfer_amount(self, user_id, amount, currency): #vendor
        total_amount = self.users_accounts_repo.get_account(user_id, currency).amount
        self.users_accounts_repo.update_account(user_id, currency, total_amount - amount)

    def remove_amount(self, user_id, amount, currency):
        total_amount = self.users_accounts_repo.get_account(user_id, currency).amount
        self.users_accounts_repo.update_account(user_id, currency, total_amount - amount)

    def check_currency(self, user_id, currency):
        if self.users_accounts_repo.get_account(user_id, currency):
            return True
        return False

    def add_amount(self, user_id, amount, currency):
        total_amount = self.users_accounts_repo.get_account(user_id, currency).amount
        self.users_accounts_repo.update_account(user_id, currency, total_amount + amount)

    def create_account(self, user_id, currency):
        amount = 0
        self.users_accounts_repo.create_account(user_id, currency, amount)

if __name__ == '__main__':
    users_accounts_repo = DBUsersAccountsRepository()

    users_accounts_ctrl = UsersAccountsController(users_accounts_repo)

    # users_accounts_ctrl.add_amount(
    #     user_id=123,
    #     amount=100000,
    #     currency='USD'
    # )

    # users_accounts_ctrl.create_account(
    #     user_id=123,
    #     currency='EUR'
    # )

    users_accounts_ctrl.check_balance(
        user_id=123,
        amount=100,
        currency='EUR'
    )



