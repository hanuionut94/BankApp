from Model.Domain.users import Users
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from Utils.utils import Base, engine


class DBUsersRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    #Create new user
    def add_user(self, user_id, first_name, last_name, email_name, phone_number, address, date_of_birth, join_date):
        new_user = Users(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email_name=email_name,
            address=address,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            join_date=join_date
        )

        self.session.add(new_user)
        self.session.commit()

    #Read
    def get_user(self, user_id):
        return self.session.query(Users).filter_by(user_id=user_id).first()

     #Read all
    def get_all_users(self):
        return self.session.query(Users).all()

    #Read email
    def get_email(self, user_id):
       return self.session.query(Users).filter_by(user_id=user_id).first()

    #Delete user
    def delete_user(self, user_id):
        with self.engine.connect() as conn:
            conn.execute(text(f'DELETE FROM users WHERE user_id = "{user_id}"'))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    user_repo = DBUsersRepository()

    user_repo.add_user(
        user_id='1234567890123',
        first_name='Hanu',
        last_name='Ionut',
        email_name='i_hanu',
        address='adresa',
        phone_number=757271432,
        date_of_birth='2000-22-10',
        join_date = datetime.now()
    )
