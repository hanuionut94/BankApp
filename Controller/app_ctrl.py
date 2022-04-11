from Controller.currencies_ctrl import CurrenciesController
from Controller.users import UsersController
from Controller.users_accounts import UsersAccountsController
from Controller.users_cards import UsersCardsController
from Controller.users_deposits_ctrl import UsersDepositsController
from Controller.users_transactions import UsersTransactionsController
from Model.Repository.currencies import DBCurrenciesRepository
from Model.Repository.users import DBUsersRepository
from Model.Repository.users_accounts import DBUsersAccountsRepository
from Model.Repository.users_cards import DBUsersCardsRepository
from Model.Repository.users_deposits import DBUsersDepositsRepository
from Model.Repository.users_transactions import DBUsersTransactionsRepository


class AppController:
    def __init__(self, users_ctrl, users_accounts_ctrl, users_transactions_ctrl, currencies_ctrl, users_deposits_ctrl, users_cards_ctrl):
        self.users_ctrl = users_ctrl
        self.users_accounts_ctrl = users_accounts_ctrl
        self.users_transactions_ctrl = users_transactions_ctrl
        self.currencies_ctrl = currencies_ctrl
        self.users_deposits_ctrl = users_deposits_ctrl
        self.users_cards_ctrl = users_cards_ctrl

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

    def create_account(self, user_id, currency):
        if self.currencies_ctrl.check_currency(currency) and not self.users_accounts_ctrl.check_currency(user_id,
                                                                                                         currency):
            self.users_accounts_ctrl.create_account(user_id, currency)
            return True
        return False

    def pay_user(self, my_user_id, currency, amount, other_user_id):  # TODO -- .amount?
        if self.users_accounts_ctrl.check_balance(my_user_id, amount, currency):
            self.users_accounts_ctrl.remove_amount(my_user_id, amount, currency)
            self.users_accounts_ctrl.add_amount(other_user_id, amount, currency)
            return True
        return False

    def update_user(self, user_id, **kwargs):
        a = list(kwargs.keys())
        if app_ctrl.users_ctrl.verify_user(user_id):
            if a[0] in ['first_name', 'last_name', 'email_name', 'phone_number', 'address', 'date_of_birth']:
                self.users_ctrl.update_user(user_id, **kwargs)
                return True
            return False

    def create_deposit(self, user_id, currency, name, description):
        if self.currencies_ctrl.check_currency(currency):
            self.users_deposits_ctrl.add_deposits(user_id, currency, name, description)
            return True
        return False

    def add_amount_deposit(self, user_id, currency, name, amount):
        if self.users_deposits_ctrl.check_deposit(user_id, currency, name) and self.users_accounts_ctrl.check_balance(
                user_id, amount, currency):
            self.users_accounts_ctrl.remove_amount(user_id, amount, currency)
            self.users_deposits_ctrl.update_deposit(user_id, currency, name, amount)
            print('Succesfull')
        else:
            print('Error!')

    def withdraw_amount_deposit(self, user_id, currency, name, amount):
        if self.users_deposits_ctrl.check_deposit(user_id, currency, name) and self.users_deposits_ctrl.check_balance_deposit(user_id, currency, name, amount):
            self.users_deposits_ctrl.remove_money(user_id, currency, name, amount)
            self.users_accounts_ctrl.update_amount(user_id, currency, amount)
            print('The operation was created successfully!')
        else:
            print('Error')

    def delete_deposit(self, user_id, currency, name):
        if self.users_deposits_ctrl.check_deposit(user_id, currency, name):
            res = self.users_deposits_ctrl.get_amount(user_id, currency, name)
            self.users_deposits_ctrl.remove_money(user_id, currency, name, res)
            self.users_accounts_ctrl.update_amount(user_id, currency, res)
            self.users_deposits_ctrl.delete_deposit(user_id, currency, name)

    def change_card_pin(self, user_id, card_number, old_pin,new_pin):
        if self.users_ctrl.verify_user(user_id):
            self.users_cards_ctrl.change_pin(user_id, card_number, old_pin, new_pin)

    def change_user_credentials(self, user_id, old_password, new_password):
        if self.users_ctrl.verify_user(user_id):
            self.users_ctrl.change_pin(user_id, old_password, new_password)

    def ge_user_info(self, user_id):
        user_info = self.users_ctrl.get_user(user_id)
        user_info_account = self.users_accounts_ctrl.get_user_accounts(user_id)
        return user_info, f'open_accounts": list of accounts {user_info_account}'


if __name__ == '__main__':
    users_repo = DBUsersRepository()
    users_account_repo = DBUsersAccountsRepository()
    users_transactions_repo = DBUsersTransactionsRepository()
    currencies_repo = DBCurrenciesRepository()
    users_deposits_repo = DBUsersDepositsRepository()
    users_cards_repo = DBUsersCardsRepository()

    users_ctrl = UsersController(users_repo)
    users_accounts_ctrl = UsersAccountsController(users_account_repo)
    users_transactions_ctrl = UsersTransactionsController(users_transactions_repo)
    currencies_ctrl = CurrenciesController(currencies_repo)
    users_deposits_ctrl = UsersDepositsController(users_deposits_repo)
    users_cards_ctrl = UsersCardsController(users_cards_repo)

    app_ctrl = AppController(users_ctrl, users_accounts_ctrl, users_transactions_ctrl, currencies_ctrl, users_deposits_ctrl, users_cards_ctrl)

    print(app_ctrl.ge_user_info(1234))