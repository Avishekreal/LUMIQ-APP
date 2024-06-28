import re

class Policyholder:
    def __init__(self, policyholder_id, name, address, contact_details):
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid name")
        if not isinstance(address, str) or not address:
            raise ValueError("Invalid address")
        if not isinstance(contact_details, dict) or "phone" not in contact_details or "email" not in contact_details:
            raise ValueError("Invalid contact details")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", contact_details["email"]):
            raise ValueError("Invalid email address")
        if not re.match(r"^\d{10}$", contact_details["phone"]):
            raise ValueError("Invalid phone number")

        self.policyholder_id = policyholder_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    @staticmethod
    def from_row(row):
        return Policyholder(
            policyholder_id=row[0],
            name=row[1],
            address=row[2],
            contact_details={"phone": row[3], "email": row[4]}
        )
from datetime import datetime

class Policy:
    def __init__(self, policy_id, policyholder_id, policy_type, start_date, end_date, premium_amount, coverage_details):
        if not isinstance(policyholder_id, int) or policyholder_id <= 0:
            raise ValueError("Invalid policyholder ID")
        if not isinstance(policy_type, str) or not policy_type:
            raise ValueError("Invalid policy type")
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        if not isinstance(premium_amount, (int, float)) or premium_amount <= 0:
            raise ValueError("Invalid premium amount")
        if not isinstance(coverage_details, dict):
            raise ValueError("Invalid coverage details")

        self.policy_id = policy_id
        self.policyholder_id = policyholder_id
        self.policy_type = policy_type
        self.start_date = start_date
        self.end_date = end_date
        self.premium_amount = premium_amount
        self.coverage_details = coverage_details

    @staticmethod
    def from_row(row):
        return Policy(
            policy_id=row[0],
            policyholder_id=row[1],
            policy_type=row[2],
            start_date=row[3],
            end_date=row[4],
            premium_amount=row[5],
            coverage_details=row[6]
        )
class Claim:
    def __init__(self, claim_id, policy_id, claim_date, claim_amount, claim_status, description, documents):
        if not isinstance(policy_id, int) or policy_id <= 0:
            raise ValueError("Invalid policy ID")
        try:
            datetime.strptime(claim_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        if not isinstance(claim_amount, (int, float)) or claim_amount <= 0:
            raise ValueError("Invalid claim amount")
        if claim_status not in ["Open", "Approved", "Rejected"]:
            raise ValueError("Invalid claim status")
        if not isinstance(description, str) or not description:
            raise ValueError("Invalid description")
        if not isinstance(documents, dict):
            raise ValueError("Invalid documents")

        self.claim_id = claim_id
        self.policy_id = policy_id
        self.claim_date = claim_date
        self.claim_amount = claim_amount
        self.claim_status = claim_status
        self.description = description
        self.documents = documents

    @staticmethod
    def from_row(row):
        return Claim(
            claim_id=row[0],
            policy_id=row[1],
            claim_date=row[2],
            claim_amount=row[3],
            claim_status=row[4],
            description=row[5],
            documents=row[6]
        )
    