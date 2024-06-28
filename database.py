import psycopg2
from psycopg2 import sql, OperationalError, ProgrammingError, IntegrityError
import json
from entities import Policyholder, Policy, Claim

class Database:
    def __init__(self, cms_db, postgres, password, host="localhost", port="5432"):
        try:
            self.connection = psycopg2.connect(
                dbname="cms_db",
                user="postgres",
                password="password",
                host="localhost",
                port=5432
            )
            self.create_tables()
        except OperationalError as e:
            print(f"Error connecting to the database: {e}")
            raise

    def create_tables(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS policyholders (
                        policyholder_id SERIAL PRIMARY KEY,
                        name TEXT NOT NULL,
                        address TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        email TEXT NOT NULL
                    )
                    """
                )
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS policies (
                        policy_id SERIAL PRIMARY KEY,
                        policyholder_id INTEGER NOT NULL,
                        policy_type TEXT NOT NULL,
                        start_date DATE NOT NULL,
                        end_date DATE NOT NULL,
                        premium_amount NUMERIC(10, 2) NOT NULL,
                        coverage_details JSONB NOT NULL,
                        FOREIGN KEY (policyholder_id) REFERENCES policyholders (policyholder_id)
                    )
                    """
                )
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS claims (
                        claim_id SERIAL PRIMARY KEY,
                        policy_id INTEGER NOT NULL,
                        claim_date DATE NOT NULL,
                        claim_amount NUMERIC(10, 2) NOT NULL,
                        claim_status TEXT NOT NULL,
                        description TEXT NOT NULL,
                        documents JSONB NOT NULL,
                        FOREIGN KEY (policy_id) REFERENCES policies (policy_id)
                    )
                    """
                )
                self.connection.commit()
        except (ProgrammingError, IntegrityError) as e:
            print(f"Error creating tables: {e}")
            self.connection.rollback()
            raise

    def create_policyholder(self, policyholder):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO policyholders (name, address, phone, email)
                    VALUES (%s, %s, %s, %s) RETURNING policyholder_id
                    """,
                    (policyholder.name, policyholder.address, policyholder.contact_details["phone"], policyholder.contact_details["email"])
                )
                policyholder.policyholder_id = cursor.fetchone()[0]
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error inserting policyholder: {e}")
            self.connection.rollback()
            raise

    def read_policyholder(self, policyholder_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM policyholders WHERE policyholder_id = %s", (policyholder_id,)
                )
                row = cursor.fetchone()
                return Policyholder.from_row(row) if row else None
        except OperationalError as e:
            print(f"Error reading policyholder: {e}")
            raise

    def update_policyholder(self, policyholder):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE policyholders
                    SET name = %s, address = %s, phone = %s, email = %s
                    WHERE policyholder_id = %s
                    """,
                    (policyholder.name, policyholder.address, policyholder.contact_details["phone"], policyholder.contact_details["email"], policyholder.policyholder_id)
                )
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error updating policyholder: {e}")
            self.connection.rollback()
            raise

    def delete_policyholder(self, policyholder_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM policyholders WHERE policyholder_id = %s", (policyholder_id,)
                )
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error deleting policyholder: {e}")
            self.connection.rollback()
            raise

    # Define CRUD operations for Policy
    def create_policy(self, policy):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO policies (policyholder_id, policy_type, start_date, end_date, premium_amount, coverage_details)
                    VALUES (%s, %s, %s, %s, %s, %s) RETURNING policy_id
                    """,
                    (policy.policyholder_id, policy.policy_type, policy.start_date, policy.end_date, policy.premium_amount, json.dumps(policy.coverage_details))
                )
                policy.policy_id = cursor.fetchone()[0]
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error inserting policy: {e}")
            self.connection.rollback()
            raise

    def read_policy(self, policy_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM policies WHERE policy_id = %s", (policy_id,)
                )
                row = cursor.fetchone()
                return Policy.from_row(row) if row else None
        except OperationalError as e:
            print(f"Error reading policy: {e}")
            raise

    def update_policy(self, policy):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE policies
                    SET policyholder_id = %s, policy_type = %s, start_date = %s, end_date = %s, premium_amount = %s, coverage_details = %s
                    WHERE policy_id = %s
                    """,
                    (policy.policyholder_id, policy.policy_type, policy.start_date, policy.end_date, policy.premium_amount, json.dumps(policy.coverage_details), policy.policy_id)
                )
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error updating policy: {e}")
            self.connection.rollback()
            raise

    def delete_policy(self, policy_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM policies WHERE policy_id = %s", (policy_id,)
                )
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error deleting policy: {e}")
            self.connection.rollback()
            raise

    # Define CRUD operations for Claim
    def create_claim(self, claim):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO claims (policy_id, claim_date, claim_amount, claim_status, description, documents)
                    VALUES (%s, %s, %s, %s, %s, %s) RETURNING claim_id
                    """,
                    (claim.policy_id, claim.claim_date, claim.claim_amount, claim.claim_status, claim.description, json.dumps(claim.documents))
                )
                claim.claim_id = cursor.fetchone()[0]
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error inserting claim: {e}")
            self.connection.rollback()
            raise

    def read_claim(self, claim_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM claims WHERE claim_id = %s", (claim_id,)
                )
                row = cursor.fetchone()
                return Claim.from_row(row) if row else None
        except OperationalError as e:
            print(f"Error reading claim: {e}")
            raise

    def update_claim(self, claim):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE claims
                    SET policy_id = %s, claim_date = %s, claim_amount = %s, claim_status = %s, description = %s, documents = %s
                    WHERE claim_id = %s
                    """,
                    (claim.policy_id, claim.claim_date, claim.claim_amount, claim.claim_status, claim.description, json.dumps(claim.documents), claim.claim_id)
                )
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error updating claim: {e}")
            self.connection.rollback()
            raise

    def delete_claim(self, claim_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM claims WHERE claim_id = %s", (claim_id,)
                )
                self.connection.commit()
        except IntegrityError as e:
            print(f"Error deleting claim: {e}")
            self.connection.rollback()
            raise
