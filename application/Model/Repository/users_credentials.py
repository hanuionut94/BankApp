from application.Model.Domain.users_credentials import UsersCredentials
from application.Utils.utils import engine, Base, HashPin
from sqlalchemy.orm import sessionmaker


class DBUsersCredentialsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    # CREATE
    def add_credentials(self, user_id, username, user_password_hash):
        credentials = UsersCredentials(
            user_id=user_id,
            username=username,
            user_password_hash=HashPin.hash_pin(user_password_hash)
        )

        self.session.add(credentials)
        self.session.commit()

    # READ
    def get_credentials(self, user_id):
        return self.session.query(UsersCredentials).filter_by(user_id=user_id).first()

    def validate_user(self, username, password):
        response = self.session.query(UsersCredentials).filter_by(username=username, password=password).first()
        if response:
            return True
        return False

    def get_user_id(self, username,password):
        return self.session.query(UsersCredentials).filter_by(username=username, password=password).first().user_id

    def get_username(self, username):
        return self.session(UsersCredentials).filter_by(username=username).first()

    # UPDATE
    def update_password(self, user_id, user_password_hash): 
        self.session.query(UsersCredentials).filter_by(user_id=user_id).update({'user_password_hash': user_password_hash})
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    users_repo = DBUsersCredentialsRepository()
