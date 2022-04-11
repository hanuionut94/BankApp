from Utils.utils import hash_pin


class UsersCredentialsController:
    def __init__(self, users_credentials_ctrl):
        self.users_credentials.ctrl = users_credentials_ctrl

    def change_pin(self, user_id, old_password, new_password):
        password = self.users_repo.get_user(user_id).user_password_hash
        old_password = hash_pin(old_password)
        if password == old_password:
            self.users_credentials.update_password(user_id, new_password)
            print('Pin changed successfully!')
            return True
        else:
            print('Error')
