import random

print("=== WELCOME TO ROCK, PAPER, SCISSORS ===")

choices = {
    "r": "✊",
    "p": "🖐",
    "s": "✌"
}

user_score = 0
computer_score = 0

while True:
    computer_choice = random.choice(list(choices))

    user_choice = input("Enter your choice (r/p/s): ").lower()
    if user_choice not in list(choices):
        print("Please enter valid input!")
        continue

    print(
        f"I choose {choices[computer_choice]}. You choose {choices[user_choice]}")

    if (user_choice == "r" and computer_choice == "s") or \
        (user_choice == "p" and computer_choice == "r") or \
            (user_choice == "s" and computer_choice == "p"):
        user_score += 1
        print("You win!")

    elif user_choice == computer_choice:
        print("It's a tie!")

    elif (computer_choice == "r" and user_choice == "s") or \
        (computer_choice == "p" and user_choice == "r") or \
            (computer_choice == "s" and user_choice == "p"):
        computer_score += 1
        print("You lose!")

    else:
        print("Please enter valid input!")
        continue

    score = f"COMPUTER: {computer_score} | YOUR SCORE: {user_score}"
    print(score)

    play_again = input("Would you like to play again (y/n)? ").lower()
    if play_again == "n":
        if user_score > computer_score:
            print("\nYou are the winner!")
        elif user_score < computer_score:
            print("\nI am the winner!")
        elif user_score == computer_score:
            print("\nIt's a tie! I'll see you in the next rematch!")
        print("Alright, see you next time!")
        break

    elif play_again == "y":
        continue

    else:
        print("Please enter valid input!")
        continue
