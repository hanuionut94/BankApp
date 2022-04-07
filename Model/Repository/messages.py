from sqlalchemy.orm import sessionmaker
from Model.Domain.messages import Messages
from Utils.utils import engine


class DBMessagesRepository:
    def __init__(self):
        self.session = sessionmaker(engine)

    # READ ALL
    def get_messages(self, user_id):
        return self.session.query(Messages).all()
