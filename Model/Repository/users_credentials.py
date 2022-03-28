from Model.Domain.users_credentials import UsersCredentials
from Utils.utils import engine
from sqlalchemy.orm import sessionmaker


class DBUsersCredentialsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    # CREATE
    def add_credentials(self, user_id, username, user_password_hash):
        credentials = UsersCredentials(
            user_id=user_id,
            username=username,
            user_password_hash=user_password_hash
        )
        # TODO -- Password Hash

        self.session.add(credentials)
        self.session.commit()

    # READ
    def get_credentials(self, user_id):
        return self.session.query(UsersCredentials).filter_by(
            user_id=user_id).first()  # TODO - exclud user_password_hash from output

    # UPDATE
    def update_password(self, user_id, user_password_hash):
        self.session.query(UsersCredentials).filter_by(user_id=user_id).update(
            {'user_password_hash': user_password_hash})
