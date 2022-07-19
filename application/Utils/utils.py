import hashlib
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine



Base = declarative_base()

engine = create_engine('mysql+pymysql://root@localhost:3306/BankApp')


class HashPin:

    def hash_pin(self, pin):
        return hashlib.sha256(str(pin).encode('utf-8')).hexdigest()



