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
        return self.session.query(UsersCredentials).filter_by(
            user_id=user_id).first()

    # UPDATE
    def update_password(self, user_id, user_password_hash): 
        self.session.query(UsersCredentials).filter_by(user_id=user_id).update({'user_password_hash': user_password_hash})
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    users_repo = DBUsersCredentialsRepository()

    users_repo.add_credentials(
        user_id=123,
        username='ionut',
        user_password_hash='12345'
    )