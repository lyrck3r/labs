from expense import Expense

class ExpenseManager:
    def __init__ (self, database):
        self.database = database

    def add_expense(self, name, amount, category, expense_date):
        expense = Expense(
            name,
            amount,
            category,
            expense_date
        )

        self.database.add_expense(expense)

    def show_expenses(self):
        expenses = self.database.get_expenses()

        if not expenses:
            print("\nНемає витрат")
            return

        print("\n============== ВИТРАТИ ==============")

        for expense in expenses:
            print(
                f"ID: {expense[0]} |"
                f"{expense[1]} |"
                f"{expense[2]} грн|"
                f"{expense[3]} |"
                f"{expense[4]}"
            )

    def delete_expense(self, expense_id):
        self.database.delete_expense(expense_id)

    def get_total(self):
        return self.database.get_total()