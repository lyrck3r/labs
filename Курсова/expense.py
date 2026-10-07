class Expense:
    def __init__ (self, name, amount, category, expense_date):
        self.name = name
        self.amount = amount
        self.category = category
        self.expense_date = expense_date

    def __stf__ (self):
        return(
            f"(self.name) | "
            f"(self.amount) грн | "
            f"(self.category) | "
            f"(self.expense_date)"
        )