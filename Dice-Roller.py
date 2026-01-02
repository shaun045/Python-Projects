import random


def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results


def main():
    history = []

    while True:
        try:
            num_dice = int(input("Enter number of dice: "))

        except ValueError:
            print("Must be numbers only, please enter valid input!")
            continue

        results_of_number_of_rolls = roll_dice(num_dice)
        total_of_results_added = sum(results_of_number_of_rolls)
        history.append(results_of_number_of_rolls)

        print(f"Results: {results_of_number_of_rolls}")
        print(f"Total of results: {total_of_results_added}")

        again = input("Would you like to play again? (y/n): ").lower()
        if again != "y":
            break

    for i, roll in enumerate(history, start=1):
        print(f"{i}. {roll} -> sum: {sum(roll)}")


main()
