# claims_management_system.py

from database import Database
from entities import Policyholder, Policy, Claim

class ClaimsManagementSystem:
    def __init__(self, cms_db, postgres, password, host="localhost", port="5432"):
        self.db = Database("cms_db", "postgres", "password", "localhost", "5432")
        
    # Policyholder CRUD operations
    def create_policyholder(self, policyholder):
        self.db.create_policyholder(policyholder)

    def read_policyholder(self, policyholder_id):
        return self.db.read_policyholder(policyholder_id)

    def update_policyholder(self, policyholder):
        self.db.update_policyholder(policyholder)

    def delete_policyholder(self, policyholder_id):
        self.db.delete_policyholder(policyholder_id)

    # Policy CRUD operations
    def create_policy(self, policy):
        self.db.create_policy(policy)

    def read_policy(self, policy_id):
        return self.db.read_policy(policy_id)

    def update_policy(self, policy):
        self.db.update_policy(policy)

    def delete_policy(self, policy_id):
        self.db.delete_policy(policy_id)

    # Claim CRUD operations
    def create_claim(self, claim):
        self.db.create_claim(claim)

    def read_claim(self, claim_id):
        return self.db.read_claim(claim_id)

    def update_claim(self, claim):
        self.db.update_claim(claim)

    def delete_claim(self, claim_id):
        self.db.delete_claim(claim_id)
