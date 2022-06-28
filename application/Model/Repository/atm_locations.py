from sqlalchemy.orm import sessionmaker
from Model.Domain.atm_locations import ATMLocations
from Utils.utils import engine


class DBATMLocationsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)

    # READ
    def get_atm_location(self, atm_id):
        return self.session.query(ATMLocations).filter_by(atm_id=atm_id).first()

    # READ ALL
    def get_all_locations(self):
        return self.session.query(ATMLocations).all()
