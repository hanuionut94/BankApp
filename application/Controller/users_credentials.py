from application.Model.Repository.users_credentials import DBUsersCredentialsRepository
from application.Utils.utils import HashPin


class UsersCredentialsController:
    def __init__(self, users_credentials_repo):
        self.users_credentials_repo = users_credentials_repo
    
    def add_user_credentials(self, username, password):
        self.add_credentials(username, password)

    # def change_pin(self, user_id, old_password, new_password):
    #     password = self.users_repo.get_user(user_id).user_password_hash
    #     old_password = hash_pin(old_password)
    #     if password == old_password:
    #         self.users_credentials.update_password(user_id, new_password)
    #         print('Pin changed successfully!')
    #         return True
    #     else:
    #         print('Error')
    #
    def check_users_crendetials(self, username, password):
        password = HashPin.hash_pin(password)
        if self.users_credentials_repo.validate_user(username, password):
            return self.users_credentials_repo.get_user_id(username,password)
        return None

    def get_username_by_id(self, user_id):
        return self.users_credentials_repo.get_credentials(user_id)

    def get_username(self, username):
        return self.users_credentials_repo.get_username(username)

users_credentials_repo = DBUsersCredentialsRepository()
user_credentials_ctrl = UsersCredentialsController(users_credentials_repo)