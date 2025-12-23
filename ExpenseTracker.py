class Expense:
    CATEGORIES = ["Food", "Transport",
                  "Entertainment", "Bills", "Shopping", "Other"]

    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.amount} | {self.category} | {self.date} | {self.description}"

    def to_dict(self):
        pass

    @staticmethod
    def from_dict(data):
        pass


class ExpenseTracker:
    def __init__(self, monthly_budget=0.0):
        self.monthly_budget = monthly_budget
        self.expense_list = []

    def add_expense(self, expense):
        if expense.category in Expense.CATEGORIES:
            self.expense_list.append(expense)
            print(
                f"Added Expense: {expense.description} (${expense.amount:.2f})")
        else:
            print("Invalid Category!")

    def get_total(self):
        total = 0
        for expense in self.expense_list:
            total += expense.amount
        return total

    def get_total_by_category(self, category):
        total = 0
        for expense in self.expense_list:
            if expense.category == category:
                total += expense.amount

        return total

    def get_expenses_by_month(self, month):
        results = []
        for expense in self.expense_list:
            expense_month = int(expense.date.split('-')[1])

            if expense_month == month:
                results.append(expense)

        return results

    def get_monthly_summary(self, month):
        monthly_expenses = self.get_expenses_by_month(month)

        if len(monthly_expenses) == 0:
            print(f"No Expenses for month {month}")
            return

        print(f"=== Month {month} Summary ===")

        for category in Expense.CATEGORIES:
            total = 0
            for expense in monthly_expenses:
                if expense.category == category:
                    total += expense.amount

            if total > 0:
                print(f"{category}: ${total:.2f}")

        total = sum(expense.amount for expense in monthly_expenses)
        print(f"-----------------------------------------------------")
        print(f"Total: ${total:.2f}")
        print(f"Budget: ${self.monthly_budget:.2f}")

        if total > self.monthly_budget:
            print(f"Over budget by ${total - self.monthly_budget:.2f}")
        else:
            print(f"Under budget by ${self.monthly_budget - total:.2f}")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            amount=data["amount"]
            category=data["category"]
            description=data["description"]
            date=data["date"]
        )

    def save_to_file(self, filename="expenses.json"):
        expense_data = []
        for expense in self.expenses:
            expense_data.append(expense.to_dict())

        try:
            with open(filename, 'w') as f:
                json.dump(expense_data, f, indent=4)
            print(f"✅ Saved {len(self.expenses)} expense(s) to '{filename}'")

        except IOError as e:
            print(f"❌ Error saving: {e}")

    def load_from_file(self, filename="expenses.json"):
        try:
            with open(filename, 'r') as f:
                expenses_data = json.load(f)

            self.expenses = []
            for exp_dict in expenses_data:
                expense = Expense.from_dict(exp_dict)
                self.expenses.append(expense)

            print(
                f"✅ Loaded {len(self.expenses)} expense(s) from '{filename}'")
        except FileNotFoundError:
            print(f"❌ File '{filename}' not found")
        except json.JSONDecodeError:
            print(f"File '{filename}' is corrupted")
