import random

HANGMANPICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

words = ["python", "hangman", "wizard", "banana", "notebook", "puzzle"]
word = random.choice(words)
guessed = []
wrong = 0

print("=== Hangman Game ===")

while wrong < len(HANGMANPICS) - 1:
    print(HANGMANPICS[wrong])

    display = " ".join(
        ["_" if letter not in guessed else letter for letter in word])

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that!")
        continue

    guessed.append(guess)

    if guess not in word:
        wrong += 1
        print("Wrong guess!")
    else:
        print("Correct!")

    if all(letter in guessed for letter in word):
        print("You win! The word was: ", word)
        break

    if wrong == len(HANGMANPICS) - 1:
        print(HANGMANPICS[wrong])
        print("You lost! The word was:", word)
