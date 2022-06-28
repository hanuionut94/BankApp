from application.Model.Repository.users_accounts import DBUsersAccountsRepository


class UsersAccountsController:
    def __init__(self, users_accounts_repo):
        self.users_accounts_repo = users_accounts_repo

    def check_balance(self, user_id, amount, currency):
        users_accounts = self.users_accounts_repo.get_account(user_id, currency)
        if users_accounts and users_accounts.amount > amount: #self.users_accounts_repo.get_account(user_id, currency).amount > amount:
            return True
        return False

    def transfer_amount(self, user_id, amount, currency): #vendor
        total_amount = self.users_accounts_repo.get_account(user_id, currency).amount
        self.users_accounts_repo.update_account(user_id, currency, total_amount - amount)

    def remove_amount(self, user_id, amount, currency):
        total_amount = self.users_accounts_repo.get_account(user_id, currency).amount
        self.users_accounts_repo.update_account(user_id, currency, total_amount - amount)

    def update_amount(self, user_id, currency, amount):
        total_amount = self.users_accounts_repo.get_account(user_id, currency).amount
        self.users_accounts_repo.update_account(user_id, currency, total_amount + amount)

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

    def get_user_accounts(self, user_id):
        users_accounts = self.users_accounts_repo.get_all_accounts(user_id)
        list_account = []
        accounts = {}
        for x in users_accounts:
            accounts[x.currency] = x.account_number
            # list_account.append(accounts)

        return accounts

    def get_info_accounts(self, user_id):
        user_info = self.users_accounts_repo.get_all_accounts(user_id)
        currencies = [x.currency for x in user_info]
        accounts = {}
        for x in user_info:
            accounts[x.currency]={'account_number': x.account_number, 'amount': x.amount}

        return accounts

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

    # users_accounts_ctrl.check_balance(
    #     user_id=123,
    #     amount=100,
    #     currency='EUR'
    # )

    print(users_accounts_ctrl.get_info_accounts(123))


