def c_to_f(c):
    return (c * 9/5) + 32


def f_to_c(f):
    return (f - 32) * 5/9


def f_to_k(f):
    return (f - 32) * 5/9 + 273.15


def k_to_f(k):
    return (k - 273.15) * 9/5 + 32


def c_to_k(c):
    return c + 273.15


def k_to_c(k):
    return k - 273.15


def menu():
    print("=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Fahrenheit to Kelvin")
    print("4. Kelvin to Fahrenheit")
    print("5. Celsius to Kelvin")
    print("6. Kelvin to Celsius")
    print("7. Quit")


def main():
    menu()
    while True:
        try:
            choice = float(input("Enter converter of your choice (1-7): "))

        except ValueError:
            print("Please enter number between 1-6")
            continue

        if choice == 1:
            print("Welcome to Celsius to Fahrenheit converter!")
            try:
                num = float(input("Enter °C: "))

            except ValueError:
                print("Please enter valid input!")
                continue

            print(f"Your converted temp: {c_to_f(num):.2f}°F")

        elif choice == 2:
            print("Welcome to Fahrenheit to Celsius converter!")
            try:
                num = float(input("Enter °F: "))

            except ValueError:
                print("Please enter valid input!")
                continue

            print(f"Your converted temp: {f_to_c(num):.2f}°C")

        elif choice == 3:
            print("Welcome to Fahrenheit to Kelvin converter!")
            try:
                num = float(input("Enter °F: "))

            except ValueError:
                print("Please enter valid input!")
                continue

            print(f"Your converted temp: {f_to_k(num):.2f} K")

        elif choice == 4:
            print("Welcome to Kelvin to Fahrenheit converter!")
            try:
                num = float(input("Enter K: "))

            except ValueError:
                print("Please enter valid input!")
                continue

            print(f"Your converted temp: {k_to_f(num):.2f} °F")

        elif choice == 5:
            print("Welcome to Celsius to Kelvin converter!")
            try:
                num = float(input("Enter °C: "))

            except ValueError:
                print("Please enter valid input!")
                continue

            print(f"Your converted temp: {c_to_k(num):.2f} K")

        elif choice == 6:
            print("Welcome to Kelvin to Celsius converter!")
            try:
                num = float(input("Enter K: "))

            except ValueError:
                print("Please enter valid input!")
                continue

            print(f"Your converted temp: {k_to_c(num):.2f}°C")

        else:
            print("Thank you for using Temperature converter, good bye!")
            break


main()
