from Model.Domain.users import Users
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from Utils.utils import Base, engine

class DBUsersRepository:
    def __init__(self):
        self.e
        self.session = sessionmaker(bind=self.engine)()

    #Create new user
    def add_user(self, user_id, first_name, last_name, email_name, phone_number, date_of_birth, join_date):
        new_user = Users(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email_name=email_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            join_date=join_date
        )

        self.session.add(new_user)
        self.session.commit()

    #Read
    def get_user(self, user_id):
        # return self.session.query(Users).filter_by(user_id=user_id).first()

        with self.engine.connect() as conn:
            query = conn.execute(text(f'SELECT * FROM users WHERE user_id = "{user_id}"'))
            res = query.fetchall()[0]

            users = Users(
                user_id=user_id,
                first_name=res[1],
                last_name=res[2],
                email_name=res[3],
                address = [4],
                phone_number=res[5],
                date_of_birth = res[6],
                join_date = res[7]
            )
            return users

     #Read all
    def get_all_users(self):
        return self.session.query(Users).all()

    #Read email
    def get_email(self, user_id):
       # return self.session.query(Users).filter_by(user_id=user_id).first()

        with self.engine.connect() as conn:
            query = conn.execute(text(f'SELECT email_name FROM users WHERE user_id = "{user_id}"'))

        res = query.fetchall()[0][0]
        return res



    #Delete user
    def delete_user(self, user_id):
        # return self.session.query(Users).filter_by(user_id=user_id).delete()
        with self.engine.connect() as conn:
            query = conn.execute(text(f'DELETE FROM users WHERE user_id = "{user_id}"'))

        return query


if __name__ == '__main__':
    user_repo = DBUsersRepository()

