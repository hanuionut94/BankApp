import hashlib

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('mysql+pymysql://root@localhost:3306/BankApp')


def hash_pin(pin):
    hash_pin = hashlib.sha256(str(pin).encode('utf-8')).hexdigest()

    return hash_pin

