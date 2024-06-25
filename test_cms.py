import os
import unittest
from cms import ClaimsManagementSystem
from entities import Policyholder, Policy, Claim

class TestDatabaseIntegration(unittest.TestCase):
    db_name = 'test_cms.db'

    def setUp(self):
        # Ensure the database file is not left over from previous tests
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
        self.cms = ClaimsManagementSystem(self.db_name)

    def tearDown(self):
        # Close the CMS to ensure the database connection is properly closed
        self.cms.db.connection.close()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_create_and_read_policyholder(self):
        policyholder = Policyholder(
            policyholder_id=1,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        retrieved_policyholder = self.cms.read_policyholder(1)
        self.assertEqual(retrieved_policyholder.name, "Avishek Gope")

    def test_update_policyholder(self):
        policyholder = Policyholder(
            policyholder_id=2,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policyholder.name = "Avishek Gope"
        self.cms.update_policyholder(policyholder)
        retrieved_policyholder = self.cms.read_policyholder(2)
        self.assertEqual(retrieved_policyholder.name, "Avishek Gope")

    def test_delete_policyholder(self):
        policyholder = Policyholder(
            policyholder_id=3,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        self.cms.delete_policyholder(3)
        retrieved_policyholder = self.cms.read_policyholder(3)
        self.assertIsNone(retrieved_policyholder)

    def test_create_and_read_policy(self):
        policyholder = Policyholder(
            policyholder_id=4,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=1,
            policyholder_id=4,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        retrieved_policy = self.cms.read_policy(1)
        self.assertEqual(retrieved_policy.policy_type, "Health")

    def test_update_policy(self):
        policyholder = Policyholder(
            policyholder_id=5,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=2,
            policyholder_id=5,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        policy.policy_type = "Life"
        self.cms.update_policy(policy)
        retrieved_policy = self.cms.read_policy(2)
        self.assertEqual(retrieved_policy.policy_type, "Life")

    def test_delete_policy(self):
        policyholder = Policyholder(
            policyholder_id=6,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=3,
            policyholder_id=6,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        self.cms.delete_policy(3)
        retrieved_policy = self.cms.read_policy(3)
        self.assertIsNone(retrieved_policy)

    def test_create_and_read_claim(self):
        policyholder = Policyholder(
            policyholder_id=7,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=4,
            policyholder_id=7,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        claim = Claim(
            claim_id=1,
            policy_id=4,
            claim_date="2024-06-01",
            claim_amount=500.0,
            claim_status="Pending",
            description="Medical expenses",
            documents="doc1, doc2"
        )
        self.cms.create_claim(claim)
        retrieved_claim = self.cms.read_claim(1)
        self.assertEqual(retrieved_claim.claim_amount, 500.0)

    def test_update_claim(self):
        policyholder = Policyholder(
            policyholder_id=8,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=5,
            policyholder_id=8,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        claim = Claim(
            claim_id=2,
            policy_id=5,
            claim_date="2024-06-01",
            claim_amount=500.0,
            claim_status="Pending",
            description="Medical expenses",
            documents="doc1, doc2"
        )
        self.cms.create_claim(claim)
        claim.claim_status = "Approved"
        self.cms.update_claim(claim)
        retrieved_claim = self.cms.read_claim(2)
        self.assertEqual(retrieved_claim.claim_status, "Approved")

    def test_delete_claim(self):
        policyholder = Policyholder(
            policyholder_id=9,
            name="Avishek Gope",
            address="Raj pearl pg,Noda sector 62, Springfield",
            contact_details={"phone": "9264270247", "email": "avishe06500@gmal.com"}
        )
        self.cms.create_policyholder(policyholder)
        policy = Policy(
            policy_id=6,
            policyholder_id=9,
            policy_type="Health",
            start_date="2024-01-01",
            end_date="2025-01-01",
            premium_amount=1000.0,
            coverage_details="Basic health coverage"
        )
        self.cms.create_policy(policy)
        claim = Claim(
            claim_id=3,
            policy_id=6,
            claim_date="2024-06-01",
            claim_amount=500.0,
            claim_status="Pending",
            description="Medical expenses",
            documents="doc1, doc2"
        )
        self.cms.create_claim(claim)
        self.cms.delete_claim(3)
        retrieved_claim = self.cms.read_claim(3)
        self.assertIsNone(retrieved_claim)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
