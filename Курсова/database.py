import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__ (self):
        self.connection = psycopg.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
        )

    def add_expense(self, expense):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO expenses
                (name, amount, category, expense_date )
                VALUES (%s, %s, %s, %s)
                """,
                (
                    expense.name,
                    expense.amount,
                    expense.category,
                    expense.expense_date
                )
            )

        self.connection.commit()

    def get_expenses(self):
        with self.connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT id, name, amount, category, expense_date
                        FROM expenses
                        ORDER BY id
                        """
                    )

                    return cursor.fetchall()

    def delete_expense(self, expense_id):
         with self.connection.cursor() as cursor:
                     cursor.execute(
                        """
                        DELETE FROM expenses
                        WHERE id = %s
                        """,
                        (expense_id,)
                     )

    def get_total(self):
          with self.connection.cursor() as cursor:
                      cursor.execute(
                             """
                            SELECT COALESCE(SUM(amount), 0)
                            FROM expenses
                            """
                      )

                      return cursor.fetchall()[0][0]

    def close(self):
           self.connection.close()