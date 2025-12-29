print("=== ATM ===")

print("===Transaction Menu===")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Quit")

balance = 1000

while True:
    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a number between 1-4")
        continue

    if choice == 1:
        try:
            deposit = float(input("How much will you deposit? $"))

        except ValueError:
            print("Invalid input! Deposit should only be numbers")
            continue

        if deposit < 0:
            print("Your deposit should be greater than zero!")

        balance += deposit
        print(f"You deposited: ${deposit:,.2f}")
        print(f"Your total balance is now: ${balance:,.2f}")

    elif choice == 2:
        try:
            withdraw = float(input("How much are you going to withdraw? $"))

        except ValueError:
            print("Invalid input! Withdraw should only be numbers")

        if withdraw > balance:
            print("Your withdrawal amount exceeds your balance")

        balance -= withdraw
        print(f"You took: ${withdraw:,.2f} from your account")
        print(f"Your balannce is now: {balance:,.2f}")

    elif choice == 3:
        print(f"Your current balance is: ${balance:,.2f}")

    elif choice == 4:
        print("Have a great day!")
        break

    else:
        print("Please enter numbers between 1-4")
