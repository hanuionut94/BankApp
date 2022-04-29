from Model.Domain.users_credentials import UsersCredentials
from Utils.utils import engine, hash_pin, Base
from sqlalchemy.orm import sessionmaker


class DBUsersCredentialsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    # CREATE
    def add_credentials(self, user_id, username, user_password_hash):
        credentials = UsersCredentials(
            user_id=user_id,
            username=username,
            user_password_hash=hash_pin(user_password_hash)
        )

        self.session.add(credentials)
        self.session.commit()

        #todo -- 1 account

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

    # UPDATE
    def update_password(self, user_id, user_password_hash): 
        self.session.query(UsersCredentials).filter_by(user_id=user_id).update({'user_password_hash': user_password_hash})
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    users_repo = DBUsersCredentialsRepository()

    users_repo.add_credentials(
        user_id=1234,
        username='ionut',
        user_password_hash='12345'
    )