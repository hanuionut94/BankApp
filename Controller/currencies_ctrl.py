from Model.Repository.currencies import DBCurrenciesRepository


class CurrenciesController:
    def __init__(self, currencies_repo):
        self.currencies_repo = currencies_repo

    def check_currency(self, currency):
        if self.currencies_repo.get_currency(currency):
            return True
        return False


if __name__ == '__main__':
    currency_repo = DBCurrenciesRepository()

    currency_ctrl = CurrenciesController(currency_repo)

    currency_ctrl.check_currency(
        currency='EUR'
    )