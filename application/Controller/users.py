from application.Model.Repository.users import DBUsersRepository


class UsersController:
    def __init__(self, users_repo):
        self.users_repo = users_repo

    def verify_user(self, user_id):
        if self.users_repo.get_user(user_id):
            return True
        return False

    def get_user(self, user_id):
        return self.users_repo.get_user(user_id)

    def update_user(self, user_id, **kwargs):
        self.users_repo.update_user(user_id, **kwargs)



if __name__ == '__main__':
    users_repo = DBUsersRepository()

    users_ctrl = UsersController(users_repo)

    print(users_ctrl.get_user(1234567890123))
