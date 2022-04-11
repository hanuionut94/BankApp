from Model.Repository.users_deposits import DBUsersDepositsRepository


class UsersDepositsController:
    def __init__(self, users_deposits_ctrl):
        self.users_deposits_ctrl = users_deposits_ctrl

    def add_deposits(self, user_id, currency, name, description):
        amount = 0
        if self.users_deposits_ctrl.add_deposit(user_id, currency, name, amount, description):
            return True
        return False

    def check_deposit(self, user_id, currency, name):
        if self.users_deposits_ctrl.get_deposit_currency_name(user_id, currency, name):
            return True
        return False

    def check_balance_deposit(self, user_id, currency, name, amount):
        user_deposit = self.users_deposits_ctrl.get_deposit_currency_name(user_id, currency, name)
        if user_deposit and user_deposit.amount > amount:
            return True
        return False

    def update_deposit(self, user_id, currency, name, amount):
        total_amount = self.users_deposits_ctrl.get_deposit_currency_name(user_id, currency, name).amount
        res = total_amount + amount
        self.users_deposits_ctrl.update_deposit(user_id, currency, name, res)

    def remove_money(self, user_id, currency, name, amount):
        total_amount = self.users_deposits_ctrl.get_deposit_currency_name(user_id, currency, name).amount
        self.users_deposits_ctrl.update_deposit(user_id, currency, name, total_amount - amount)

    def delete_deposit(self, user_id, currency, name):
        if self.users_deposits_ctrl.delete_deposit(user_id, currency, name):
            return True
        return False

    def get_amount(self, user_id, currency, name):
        amount = self.users_deposits_ctrl.get_deposit_currency_name(user_id, currency, name).amount
        return amount


if __name__ == '__main__':
    users_deposits_repo = DBUsersDepositsRepository()

    users_deposits_ctrl = UsersDepositsController(users_deposits_repo)

    # users_deposits_ctrl.check_deposit(
    #     user_id=123,
    #     currency='dol',
    #     name='depozit2'
    # )
    #
    # users_deposits_ctrl.check_deposit(
    #     user_id=1234567890123,
    #     currency='dol',
    #     name='depozit2'
    # )

    users_deposits_ctrl.update_deposit(
        user_id=123,
        currency='EUR',
        name='Primul depozit',
        amount=100
    )