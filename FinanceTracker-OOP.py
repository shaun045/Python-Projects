class Transaction:
    def __init__(self, amount, category, description, date, transaction_type):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.type = transaction_type

    def __str__(self):
        sign = "+" if self.type == "income" else "-"
        return f"{self.date} | {self.category} | {sign}${self.type} | {self.description}"


class Account:
    def __init__(self, name, initial_balance=0.0):
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def add_transaction(self, transaction):
        if transaction.amount <= 0:
            print(
                f"Error: Amount must be positive! You entered ${transaction.amount}")
            return False

        if transaction.type not in ["income", "expense"]:
            print(
                f"Error: Type must be 'income' or 'expense', not '{transaction.type}'")
            return False

        if transaction.type == "expense":
            if transaction.amount > self.balance:
                print(f"Insufficient funds!")
                print(f"Balance: ${self.balance:.2f}")
                print(f"Short: ${transaction.amount - self.balance:.2f}")
                return False

        self.transactions.append(transaction)

        if transaction.type == "income":
            self.balance += transaction.amount
        elif transaction.type == "expense":
            self.balance -= transaction.amount

        print(f"Success! New balance: ${self.balance:.2f}")
        return True

    def get_balance(self):
        return self.balance

    def show_transactions(self):
        if len(self.transactions) == 0:
            print("No transactions yet.")
            return

        print(f"\n=== Transactions for {self.name} ===")
        for transaction in self.transactions:
            print(transaction)
        print()

    def get_total_spend_by_category(self, category):
        total = 0

        for transaction in self.transactions:
            if transaction.type == "expense" and transaction.category == category:
                total += transaction.amount

        return total

    def show_category_spending(self, category):
        total = self.get_total_spend_by_category(category)

        if total == 0:
            print(f"No spending on {category} yet.")
        else:
            print(f"Total spent on {category}: ${total:.2f}")

    def get_monthly_summary(self, month):
        income_total = 0
        expenses_total = 0

        print(f"Monthly summary for Month {month}")

        for transaction in self.transactions:
            transaction_month = int(transaction.date.split('-')[1])
            if transaction_month == month:
                if transaction.type == "income":
                    income_total += transaction.amount
                    print(
                        f"[INCOME] {transaction.date}: +${transaction.amount:.2f} - {transaction.description}")
                elif transaction.type == "expense":
                    expenses_total += transaction.amount
                    print(
                        f"[EXPENSE] {transaction.date}: -${transaction.amount} - {transaction.description}")

        print(f"Total Income: ${income_total}")
        print(f"Total Expenses: ${expenses_total}")
        print(f"Net Summary: {income_total - expenses_total}")
        return

    def save_to_file(self, filename):
        pass

    def load_from_file(self, filename):
        pass


if __name__ == "__main__":
    print("="*50)
    print("PERSONAL FINANCE TRACKER - TEST")
    print("="*50)

    print("[TEST 1] Creating Account...")
    account = Account("My Wallet", 1000.0)
    print(f"Account created: {account.name}")
    print(f"Starting balance: ${account.get_balance():.2f}")

    print("[TEST 2] Adding Transactions...")
    print("November")
    t1 = Transaction(500, "Income", "Salary", "2024-11-01", "income")
    t2 = Transaction(50, "Food", "Lunch at restaurant",
                     "2024-11-05", "expense")
    t3 = Transaction(30, "Transport", "Bus fare", "2024-11-10", "expense")
    t4 = Transaction(200, "Income", "Freelance work", "2024-11-15", "income")
    t5 = Transaction(75, "Food", "Groceries", "2024-11-18", "expense")
    t6 = Transaction(25, "Entertainment", "Movie ticket",
                     "2024-11-20", "expense")
    print()
    print("October")
    t7 = Transaction(100, "Food", "Dinner", "2024-10-20", "expense")
    t8 = Transaction(300, "Income", "Bonus", "2024-10-25", "income")
    t9 = Transaction(40, "Transport", "Taxi", "2024-10-28", "expense")
    print()
    print("December")
    t10 = Transaction(150, "Entertainment", "Concert", "2024-12-05", "expense")

    account.add_transaction(t1)
    account.add_transaction(t2)
    account.add_transaction(t3)
    account.add_transaction(t4)
    account.add_transaction(t5)
    account.add_transaction(t6)
    account.add_transaction(t7)
    account.add_transaction(t8)
    account.add_transaction(t9)
    account.add_transaction(t10)

    print(f"✅ Added 10 transactions")
    print(f"✅ Current balance: ${account.get_balance():.2f}")
    print()
    print("[TEST 3] Showing all transactions...")
    account.show_transactions()
    print()
    print("[TEST 4] Testing get_total_spend_by_category()...")
    food_total = account.get_total_spend_by_category("Food")
    transport_total = account.get_total_spend_by_category("Transport")
    entertainment_total = account.get_total_spend_by_category("Entertainment")
    utilities_total = account.get_total_spend_by_category("Utilities")

    print(f"Total spent on Food: ${food_total:.2f}")
    print(f"Total spent on Transport: ${transport_total:.2f}")
    print(f"Total spent on Entertainment: ${entertainment_total:.2f}")
    print(f"Total spent on Utilities: ${utilities_total:.2f}")
    print()
    print("[TEST 5] Testing get_monthly Summary()- Nov....")
    account.get_monthly_summary(11)
    print("\n[TEST 6] Testing get_monthly_summary() - October...")
    account.get_monthly_summary(10)
    print("\n[TEST 7] Testing get_monthly_summary() - December...")
    account.get_monthly_summary(12)
    print("\n[TEST 8] Testing get_monthly_summary() - September (no transactions)...")
    account.get_monthly_summary(9)
    print()
    print("\n[TEST 9] Testing Error Handling - Negative Amount...")
    bad_transaction = Transaction(-50, "Food",
                                  "Invalid", "2024-11-25", "expense")
    account.add_transaction(bad_transaction)
    print("\n[TEST 10] Testing Error Handling - Insufficient Funds...")
    account2 = Account("Small Wallet", 50.0)
    print(f"Account balance: ${account2.get_balance():.2f}")
    expensive = Transaction(200, "Food", "Too expensive",
                            "2024-11-25", "expense")
    account2.add_transaction(expensive)
    print(f"Balance after failed transaction: ${account2.get_balance():.2f}")
    print()
    print("\n[TEST 11] Testing Error Handling - Invalid Type...")
    bad_type = Transaction(50, "Food", "Test", "2024-11-25", "shopping")
    account.add_transaction(bad_type)
