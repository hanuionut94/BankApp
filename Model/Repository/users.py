from Model.Domain.users import Users
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

from Utils.utils import Base, engine


class DBUsersRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    # Create new user
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

    # Read
    def get_user(self, user_id):
        return self.session.query(Users).filter_by(user_id=user_id).first()

    # Read all
    def get_all_users(self):
        return self.session.query(Users).all()

    # Read email
    def get_email(self, user_id):
        return self.session.query(Users).filter_by(user_id=user_id).first()

    def update_user(self, user_id, **kwargs):
        if kwargs:
            self.session.query(Users).filter_by(user_id=user_id).update({**kwargs})
            self.session.commit()

    # Delete user
    def delete_user(self, user_id):
        self.session.query(Users).filter_by(user_id=user_id).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    user_repo = DBUsersRepository()

    # user_repo.add_user(
    #     user_id='1234',
    #     first_name='Ionescu',
    #     last_name='Ion',
    #     email_name='ion.ionescu',
    #     address='adresa1',
    #     phone_number=721461432,
    #     date_of_birth='2002-02-10',
    #     join_date=date.today()
    # )

    user_repo.add_user(123, 'Popescu', 'Eusebiu', 'popescu.eusebiu', 'Braila', 751115123, '1998-09-01', join_date=date.today())