from application.Controller.app_ctrl import AppController
from application.Controller.currencies_ctrl import CurrenciesController
from application.Controller.users import UsersController
from application.Controller.users_accounts import UsersAccountsController
from application.Controller.users_cards import UsersCardsController
from application.Controller.users_credentials import UsersCredentialsController
from application.Controller.users_deposits_ctrl import UsersDepositsController
from application.Controller.users_transactions import UsersTransactionsController
from application.Model.Repository.currencies import DBCurrenciesRepository
from application.Model.Repository.users import DBUsersRepository
from application.Model.Repository.users_accounts import DBUsersAccountsRepository
from application.Model.Repository.users_cards import DBUsersCardsRepository
from application.Model.Repository.users_credentials import DBUsersCredentialsRepository
from application.Model.Repository.users_deposits import DBUsersDepositsRepository
from application.Model.Repository.users_transactions import DBUsersTransactionsRepository
from application import app
from flask import render_template, request



@app.route('/api/v1')
@app.route('/')
def index():
    return render_template("index.html")


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


@app.route('/api/v1/add_money', methods=['POST'])
def add_money(): #todo -- error message?
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    currency = data.get('currency')

    app_ctrl.add_money(user_id, amount, currency)

    return {'message': 'The money was successfully added'}, 200


@app.route('/api/v1/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
    users_id = data.get('user_id')
    amount = data.get('amount')
    currency = data.get('currency')
    vendor = data.get('vendor')

    app_ctrl.create_account(users_id, amount, currency, vendor)

@app.route('/api/v1/pay_user', methods=['POST'])
def pay_user():
    data = request.get_json()
    my_user_id = data.get('my_user_id')
    currency = data.get('currency')
    amount = data.get('amount')
    other_user_id = data.get('other_user_id')

    app_ctrl.pay_user(my_user_id, currency, amount, other_user_id)

@app.route('/api/v1/create_deposit', methods=['POST'])
def create_deposit():
    data = request.json()
    user_id = data.get('user_id')
    currency = data.get('currency')
    name = data.get('name')
    description = data.get_json('description')

    app_ctrl.create_deposit(user_id, currency, name, description)

@app.route('/api/v1/update_user', methods=['POST'])
def update_user():
    data = request.get_json()
    user_id = data.get('user_id')
    kwargs = data.get('kwargs')

    app_ctrl.update_user(user_id, **kwargs)

@app.route('/api/v1/get_user_info', methods=['POST'])
def get_user_info():
    data = request.get_json()
    user_id = data.get('user_id')
    users_ctrl.get_user(user_id)

    info = app_ctrl.get_user_info(user_id)
    if info:
        return info, 200
    return {'Message': 'Info do not exist!'}, 403

@app.route('/api/v1/get_all_user_accounts', methods=['POST'])
def get_all_user_accounts():
    data = request.get_json()
    user_id = data.get('user_id')
    users_ctrl.get_user(user_id)

    info = app_ctrl.get_all_user_accounts(user_id)
    if info:
        return info, 200
    return {'Message':'Info do no exist!'}, 403

@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_id = app_ctrl.login_user(username, password)

    if user_id:
        return user_id, 200
    return {'Message':'Credentials do not match!'}, 403

if __name__ == '__main__':
    users_rep = DBUsersRepository()
    users_account_repo = DBUsersAccountsRepository()
    users_transactions_repo = DBUsersTransactionsRepository()
    currencies_repo = DBCurrenciesRepository()
    users_deposits_repo = DBUsersDepositsRepository()
    users_cards_repo = DBUsersCardsRepository()
    users_credentials_repo = DBUsersCredentialsRepository()

    users_ctrl = UsersController(users_rep)
    users_account_ctrl = UsersAccountsController(users_account_repo)
    users_transactions_ctrl = UsersTransactionsController(users_transactions_repo)
    currencies_ctrl = CurrenciesController(currencies_repo)
    users_deposits_ctrl = UsersDepositsController(users_deposits_repo)
    users_cards_ctrl = UsersCardsController(users_cards_repo)
    users_credentials_ctrl = UsersCredentialsController(users_credentials_repo)

    app_ctrl = AppController(users_ctrl, users_account_ctrl, users_transactions_ctrl,currencies_ctrl, users_deposits_ctrl, users_cards_ctrl, users_credentials_ctrl)
    app.run(debug=True)
