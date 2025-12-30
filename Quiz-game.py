print("=== WELCOME TO SIMPLE QUIZ GAME ===")

score = 0
correct = 0
incorrect = 0

while True:
    print("-----QUESTION 1-----")
    print("Who started Tesla?")
    print("A. Elon Musk")
    print("B. Jeff Bezos")
    print("C. Mark Zuckerberg")
    print("D. Larry Ellison")
    answer = input("Choose your answer: ").lower()
    if answer == "a":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 2-----")
    print("Who started Facebook?")
    print("A. Elon Musk")
    print("B. Jeff Bezos")
    print("C. Mark Zuckerberg")
    print("D. Larry Ellison")
    answer = input("Choose your answer: ").lower()
    if answer == "c":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 3-----")
    print("Who started Oracle?")
    print("A. Elon Musk")
    print("B. Jeff Bezos")
    print("C. Mark Zuckerberg")
    print("D. Larry Ellison")
    answer = input("Choose your answer: ").lower()
    if answer == "d":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 4-----")
    print("Who started Amazon?")
    print("A. Elon Musk")
    print("B. Jeff Bezos")
    print("C. Mark Zuckerberg")
    print("D. Larry Ellison")
    answer = input("Choose your answer: ").lower()
    if answer == "b":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 5-----")
    print("Who Founded Standard Oil")
    print("A. JP Morgan")
    print("B. Andrew Carnegie")
    print("C. John D. Rockefeller")
    print("D. Henry Ford")
    answer = input("Choose your answer: ").lower()
    if answer == "c":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 6-----")
    print("Who founded the first Billion-Dollar Corporation? ")
    print("A. JP Morgan")
    print("B. Andrew Carnegie")
    print("C. John D. Rockefeller")
    print("D. Henry Ford")
    answer = input("Choose your answer: ").lower()
    if answer == "a":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 7-----")
    print("Who founded the biggest Steel Company? ")
    print("A. JP Morgan")
    print("B. Andrew Carnegie")
    print("C. John D. Rockefeller")
    print("D. Henry Ford")
    answer = input("Choose your answer: ").lower()
    if answer == "b":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 8-----")
    print("Who founded Ford Motors? ")
    print("A. JP Morgan")
    print("B. Andrew Carnegie")
    print("C. John D. Rockefeller")
    print("D. Henry Ford")
    answer = input("Choose your answer: ").lower()
    if answer == "d":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 9-----")
    print("Who was the first conqueror who conquered the known world? ")
    print("A. Genghis Khan")
    print("B. Alexander the Great")
    print("C. Julius Caesar")
    print("D. Marcus Aurelius")
    answer = input("Choose your answer: ").lower()
    if answer == "b":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    print("-----QUESTION 10-----")
    print("Name of the Stoic Roman Emperor? ")
    print("A. Genghis Khan")
    print("B. Alexander the Great")
    print("C. Julius Caesar")
    print("D. Marcus Aurelius")
    answer = input("Choose your answer: ").lower()
    if answer == "d":
        print("✅ Correct!")
        correct += 1
    else:
        print("❌ Incorrect")
        incorrect += 1

    if correct >= 9:
        letter_grade = "A"

    elif correct == 8:
        letter_grade = "B"

    elif correct == 7:
        letter_grade = "C"

    elif correct == 6:
        letter_grade = "D"

    elif correct == 5:
        letter_grade = "E"

    elif correct == 4:
        letter_grade = "F"

    print()
    print("=== YOU COMPLETED THE QUIZ! ===")
    print()
    print(f"You scored {correct} with {incorrect} mistakes")
    print(f"Your Grade is {letter_grade}")

    again = input("Would you like to try again? (y/n): ").lower()
    if again != "y":
        print("Alright, see you next time!👋")
        break
