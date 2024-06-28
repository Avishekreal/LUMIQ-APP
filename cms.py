from database import Database
from entities import Policyholder, Policy, Claim

class ClaimsManagementSystem:
    def __init__(self, db_name="cms.db"):
        self.db = Database(db_name)

    def create_policyholder(self, policyholder):
        self.db.create_policyholder(policyholder)

    def read_policyholder(self, policyholder_id):
        row = self.db.read_policyholder(policyholder_id)
        return Policyholder.from_row(row) if row else None

    def update_policyholder(self, policyholder):
        self.db.update_policyholder(policyholder)

    

  
