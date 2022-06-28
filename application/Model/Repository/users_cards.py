from datetime import datetime
from application.Model.Domain.users_cards import UsersCards
from sqlalchemy.orm import sessionmaker
from random import randint

from application.Utils.utils import Base, engine, hash_pin


class DBUsersCardsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def add_card(self, user_id, card_number, pin_hash, cvv_hash, expiration_date):
        def card():
            number = str(card_number)
            card1 = 512345 + int(number[4:]) + randint(0, 9)

            return card1

        new_card = UsersCards(
            user_id=user_id,
            card_number=card(),
            pin_hash=hash_pin(pin_hash),
            cvv_hash=hash_pin(cvv_hash),
            expiration_date=expiration_date  # +3 years
        )
        self.session.add(new_card)
        self.session.commit()

    # Read
    def get_card(self, user_id, card_number):
        return self.session.query(UsersCards).filter_by(user_id=user_id, card_number=card_number).first()

    # READ ALL
    def get_card_all(self, user_id):
        return self.session.query(UsersCards).filter_by(user_id=user_id).all()

    # UPDATE
    def update_card(self, user_id, card_number, pin_hash):
        self.session.query(UsersCards).filter_by(user_id=user_id, card_number=card_number).update({"pin_hash":pin_hash})

    # DELETE
    def remove_card(self, card_number):
        self.session.query(UsersCards).filter_by(card_number=card_number).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    users_cards_repo = DBUsersCardsRepository()


