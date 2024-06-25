import sqlite3

class Database:
    def __init__(self, db_name="cms.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS policyholders (
                    policyholder_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL
                )
                """
            )
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS policies (
                    policy_id INTEGER PRIMARY KEY,
                    policyholder_id INTEGER NOT NULL,
                    policy_type TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    premium_amount REAL NOT NULL,
                    coverage_details TEXT NOT NULL,
                    FOREIGN KEY (policyholder_id) REFERENCES policyholders (policyholder_id)
                )
                """
            )
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS claims (
                    claim_id INTEGER PRIMARY KEY,
                    policy_id INTEGER NOT NULL,
                    claim_date TEXT NOT NULL,
                    claim_amount REAL NOT NULL,
                    claim_status TEXT NOT NULL,
                    description TEXT NOT NULL,
                    documents TEXT NOT NULL,
                    FOREIGN KEY (policy_id) REFERENCES policies (policy_id)
                )
                """
            )

    # Policyholder methods
    def create_policyholder(self, policyholder):
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO policyholders (policyholder_id, name, address, phone, email)
                VALUES (?, ?, ?, ?, ?)
                """,
                (policyholder.policyholder_id, policyholder.name, policyholder.address, policyholder.contact_details["phone"], policyholder.contact_details["email"])
            )

    def read_policyholder(self, policyholder_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM policyholders WHERE policyholder_id = ?", (policyholder_id,))
        row = cursor.fetchone()
        return row

    def update_policyholder(self, policyholder):
        with self.connection:
            self.connection.execute(
                """
                UPDATE policyholders
                SET name = ?, address = ?, phone = ?, email = ?
                WHERE policyholder_id = ?
                """,
                (policyholder.name, policyholder.address, policyholder.contact_details["phone"], policyholder.contact_details["email"], policyholder.policyholder_id)
            )

    def delete_policyholder(self, policyholder_id):
        with self.connection:
            self.connection.execute("DELETE FROM policyholders WHERE policyholder_id = ?", (policyholder_id,))

    # Policy methods
    def create_policy(self, policy):
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO policies (policy_id, policyholder_id, policy_type, start_date, end_date, premium_amount, coverage_details)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (policy.policy_id, policy.policyholder_id, policy.policy_type, policy.start_date, policy.end_date, policy.premium_amount, policy.coverage_details)
            )

    def read_policy(self, policy_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM policies WHERE policy_id = ?", (policy_id,))
        row = cursor.fetchone()
        return row

    def update_policy(self, policy):
        with self.connection:
            self.connection.execute(
                """
                UPDATE policies
                SET policyholder_id = ?, policy_type = ?, start_date = ?, end_date = ?, premium_amount = ?, coverage_details = ?
                WHERE policy_id = ?
                """,
                (policy.policyholder_id, policy.policy_type, policy.start_date, policy.end_date, policy.premium_amount, policy.coverage_details, policy.policy_id)
            )

    def delete_policy(self, policy_id):
        with self.connection:
            self.connection.execute("DELETE FROM policies WHERE policy_id = ?", (policy_id,))

    # Claim methods
    def create_claim(self, claim):
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO claims (claim_id, policy_id, claim_date, claim_amount, claim_status, description, documents)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (claim.claim_id, claim.policy_id, claim.claim_date, claim.claim_amount, claim.claim_status, claim.description, claim.documents)
            )

    def read_claim(self, claim_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM claims WHERE claim_id = ?", (claim_id,))
        row = cursor.fetchone()
        return row

    def update_claim(self, claim):
        with self.connection:
            self.connection.execute(
                """
                UPDATE claims
                SET policy_id = ?, claim_date = ?, claim_amount = ?, claim_status = ?, description = ?, documents = ?
                WHERE claim_id = ?
                """,
                (claim.policy_id, claim.claim_date, claim.claim_amount, claim.claim_status, claim.description, claim.documents, claim.claim_id)
            )

    def delete_claim(self, claim_id):
        with self.connection:
            self.connection.execute("DELETE FROM claims WHERE claim_id = ?", (claim_id,))
