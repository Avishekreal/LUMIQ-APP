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

   
    def delete_claim(self, claim_id):
        with self.connection:
            self.connection.execute("DELETE FROM claims WHERE claim_id = ?", (claim_id,))
