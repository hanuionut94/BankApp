import requests
from flask import Flask, request
from Controller.app_ctrl import AppController
from Controller.users import UsersController
from Controller.users_accounts import UsersAccountsController
from Controller.users_transactions import UsersTransactionsController
from Model.Repository.users import DBUsersRepository
from Model.Repository.users_accounts import DBUsersAccountsRepository
from Model.Repository.users_transactions import DBUsersTransactionsRepository

app = Flask('BankApp')


@app.route('/api/v1')
def homepage():
    return f'Welcome!'


@app.route('/api/v1/create_transaction', methods=['POST'])
def create_transactions():
    print(request.get_json())

    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    currency = data.get('currency')
    vendor = data.get('vendor')  # TODO -- to add category

    app_ctrl.create_transactions(user_id, amount, currency, vendor)

    return {'message': 'Transaction created successfully!'}, 200


@app.route('/api/v1/get_user_info', methods=['GET, POST'])
def get_user_info(): #TODO --- GET?
    if request.method == 'POST':
        data = request.get_json()
        user_id = data.get('user_id')
        users_ctrl.get_user(user_id)


@app.route('/api/v1/add_money', methods=['POST'])
def add_money(): #todo -- error message?
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    currency = data.get('currency')

    app_ctrl.add_money(user_id, amount, currency)

    return {'message': 'The money was successfully added'}, 200

@app.route('/api/v1/create_account', methos=['POST'])
def create_account():
    pass


if __name__ == '__main__':
    users_rep = DBUsersRepository()
    users_account_repo = DBUsersAccountsRepository()
    users_transactions_repo = DBUsersTransactionsRepository()

    users_ctrl = UsersController(users_rep)
    users_account_ctrl = UsersAccountsController(users_account_repo)
    users_transactions_ctrl = UsersTransactionsController(users_transactions_repo)

    app_ctrl = AppController(users_ctrl, users_account_ctrl, users_transactions_ctrl)
    app.run(debug=True)
