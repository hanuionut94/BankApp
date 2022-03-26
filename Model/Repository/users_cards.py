from Model.Domain.users_cards import UserCards
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from random import randrange,randint

class DBUsersCards():
    def __init__(self):
        self.engine = create_engine('mysql+pymsql://root@localhost:3306/BankApp')
        self.session = sessionmaker(bind=self.engine)()


    def add_card(self, user_id):

        #1 mastercard start with 5, 2-6 bank, 7-15 unique personal identifiers, 16 check digit
        def card_number():
            card = '5'+'12345'+str(user_id[4:])+str(randint(0,9))

            return card

        # new_card = UserCards(
        #     user_id = user_id,
        #     card_number = card_number(),
        #     pin_hash =
        # )

