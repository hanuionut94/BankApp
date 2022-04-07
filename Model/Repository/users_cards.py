from datetime import datetime

from Model.Domain.users_cards import UserCards
from sqlalchemy.orm import sessionmaker
from random import randint

from Utils.utils import Base, engine
import hashlib


class DBUsersCardsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def add_card(self, user_id, card_number, pin_hash, cvv_hash, expiration_date):

        def card():
            # 1 mastercard start with 5, 2-6 bank, 7-15 unique personal identifiers, 16 check digit
            number = str(card_number)
            card1 = 512345+ int(number[4:]) + randint(0, 9)

            return card1

        def hash_cod(pin):
            hash_pin = hashlib.sha256(str(pin).encode('utf-8')).hexdigest()

            return hash_pin

        new_card = UserCards(
            user_id=user_id,
            card_number=card(),
            pin_hash=hash_cod(pin_hash),
            cvv_hash= hash_cod(cvv_hash),
            expiration_date=expiration_date
        )
        self.session.add(new_card)
        self.session.commit()
            #TODO -- 1 card for 1 amount
    # Read
    def get_card(self, card_number):
        return self.session.query(UserCards).filter_by(card_number=card_number).all()

    # READ ALL
    def get_card_all(self, user_id):
        return self.session.query(UserCards).filter_by(user_id=user_id).all()

    # DELETE
    def remove_card(self, card_number):
        self.session.query(UserCards).filter_by(card_number=card_number).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    users_cards_repo = DBUsersCardsRepository()

    # users_cards_repo.add_card(
    #     user_id=123,
    #     card_number=1234567912345,
    #     pin_hash='abcd',
    #     cvv_hash=123,
    #     expiration_date=datetime.today()
    # )
    print(users_cards_repo.get_card_all(123))