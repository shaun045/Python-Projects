from collections import Counter

print("=== WELCOME TO WORD COUNTER ===")

total_words = 0
longest = []

text = input("Enter a sentence")
words = text.lower().split()
longest = max(words, key=len)

word_count = Counter(words)

for word, count in word_count.items():
    total_words += count
    print(f"{word}: {count}")

print(f"The total words: {total_words}")
print(f"The longest word is {longest}")
