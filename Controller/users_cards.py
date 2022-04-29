from Model.Repository.users_cards import DBUsersCardsRepository
from Utils.utils import hash_pin


class UsersCardsController:
    def __init__(self, users_cards_ctrl):
        self.users_cards_ctrl = users_cards_ctrl

    def check_pin(self, user_id, card_number, old_pin, new_pin):
        pin = self.users_cards_ctrl.get_card(user_id, card_number).pin_hash
        old_pin = hash_pin(old_pin)
        if pin == old_pin:
            self.users_cards_ctrl.update_card(user_id, card_number, new_pin)
            print('Pin changed successfully!')
            return True
        else:
            print('Error')


if __name__ == '__main__':
    users_cards_repo = DBUsersCardsRepository()

    users_cards_ctrl = UsersCardsController(users_cards_repo)

    print(users_cards_ctrl.check_pin(1234, 568403582, 12345, 123456))
