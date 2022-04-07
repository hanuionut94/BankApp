from Model.Repository.users import DBUsersRepository


class UsersController:
    def __init__(self, users_repo):
        self.users_repo = users_repo

    def get_user(self, user_id):
        self.users_repo.get_user(user_id)

if __name__ == '__main__':
    users_repo = DBUsersRepository()

    users_ctrl = UsersController(users_repo)