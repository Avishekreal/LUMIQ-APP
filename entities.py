class Policyholder:
    def __init__(self, policyholder_id, name, address, contact_details):
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

class Policy:
    def __init__(self, policy_id, policyholder_id, policy_type, start_date, end_date, premium_amount, coverage_details):
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
