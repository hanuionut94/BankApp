from Controller.currencies_ctrl import CurrenciesController
from Controller.users import UsersController
from Controller.users_accounts import UsersAccountsController
from Controller.users_deposits_ctrl import UsersDepositsController
from Controller.users_transactions import UsersTransactionsController
from Model.Repository.currencies import DBCurrenciesRepository
from Model.Repository.users import DBUsersRepository
from Model.Repository.users_accounts import DBUsersAccountsRepository
from Model.Repository.users_deposits import DBUsersDepositsRepository
from Model.Repository.users_transactions import DBUsersTransactionsRepository


class AppController:
    def __init__(self, users_ctrl, users_accounts_ctrl, users_transactions_ctrl, currencies_ctrl, users_deposits_ctrl):
        self.users_ctrl = users_ctrl
        self.users_accounts_ctrl = users_accounts_ctrl
        self.users_transactions_ctrl = users_transactions_ctrl
        self.currencies_ctrl = currencies_ctrl
        self.users_deposits_ctrl = users_deposits_ctrl

    def create_transactions(self, user_id, amount, currency, vendor):
        if self.users_accounts_ctrl.check_balance(self, user_id, amount):
            self.users_accounts_ctrl.transfer_amount(user_id, amount, currency)
            self.users_transactions_ctrl.add_transaction(user_id, amount, currency, vendor)
            return True
        return False

    def add_money(self, user_id, amount, currency):
        if self.users_accounts_ctrl.check_currency(user_id, currency):
            self.users_accounts_ctrl.add_amount(user_id, amount, currency)
            print('The money was successfully added')
        else:
            print('Currency not exist!')

    def create_deposit(self, user_id, currency, name, description):
        if self.currencies_ctrl.check_currency(currency):
            self.users_deposits_ctrl.add_deposits(user_id, currency, name, description)
            return True
        return False

    def create_account(self, user_id, currency):
        if self.currencies_ctrl.check_currency(currency) and not self.users_accounts_ctrl.check_currency(user_id,
                                                                                                         currency):
            self.users_accounts_ctrl.create_account(user_id, currency)
            return True
        return False

    def pay_user(self, my_user_id, currency, amount, other_user_id): #TODO -- .amount?
        if self.users_accounts_ctrl.check_balance(my_user_id, amount, currency):
            self.users_accounts_ctrl.remove_amount(my_user_id, amount, currency)
            self.users_accounts_ctrl.add_amount(other_user_id, amount, currency)
            return True
        return False

    def add_amount_deposit(self, user_id, currency, name, amount):
        if self.users_deposits_ctrl.check_deposit(user_id, currency, name) and self.users_accounts_ctrl.check_balance(user_id, amount, currency):
            self.users_accounts_ctrl.remove_amount(user_id, amount, currency)
            self.users_deposits_ctrl.update_deposit(user_id, currency, name, amount)
            print('Succesfull')
        else:
            print('Error!')

if __name__ == '__main__':
    users_repo = DBUsersRepository()
    users_account_repo = DBUsersAccountsRepository()
    users_transactions_repo = DBUsersTransactionsRepository()
    currencies_repo = DBCurrenciesRepository()
    users_deposits_repo = DBUsersDepositsRepository()

    users_ctrl = UsersController(users_repo)
    users_accounts_ctrl = UsersAccountsController(users_account_repo)
    users_transactions_ctrl = UsersTransactionsController(users_transactions_repo)
    currencies_ctrl = CurrenciesController(currencies_repo)
    users_deposits_ctrl = UsersDepositsController(users_deposits_repo)

    app_ctrl = AppController(users_ctrl, users_accounts_ctrl, users_transactions_ctrl, currencies_ctrl, users_deposits_ctrl)

    app_ctrl.pay_user(
        my_user_id=123,
        currency='EUR',
        amount=300,
        other_user_id=1234
    )