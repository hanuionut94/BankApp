from Model.Domain.users_cards import UserCards
from sqlalchemy.orm import sessionmaker
from random import randint

from Utils.utils import Base, engine


class DBUsersCards:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def add_card(self, card_number):
        # 1 mastercard start with 5, 2-6 bank, 7-15 unique personal identifiers, 16 check digit
        def card():
            card1 = '5' + '12345' + str(card_number[4:]) + str(randint(0, 9))

            return card1
            # new_card = UserCards(
            #     user_id = user_id,
            #     card_number = card_number(),
            #     pin_hash =
            # )
            pass
        # TODO - HASH

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
