import random


wordlist = ["apple", "banana", "grape", "orange", "peach"]

# Choose a random word from the list
secretword = random.choice(word list)
guessed letters = []  # List to track correct and incorrect guesses
max attempts = 6
attempts left = max attempts

# Create a display version of the word with underscores
display word = ["_" for _ in secret word]

print("🎯 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max attempts} incorrect guesses allowed.\n")

# Game loop
while attempts left > 0 and "_" in display word:
    print("Word: " + " ".join(display word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetical character.\n")
        continue

    if guess in guessed letters:
        print("⏳ You already guessed that letter. Try again.\n")
        continue

    guessed letters.append(guess)

    if guess in secret word:
        print("✅ Good guess!\n")
        for i in range(len(secret word)):
            if secret word[i] == guess:
                display word[i] = guess
    else:
        attempts left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}\n")

# Final outcome
if "_" not in display word:
    print("🎉 Congratulations! You guessed the word:", secret word)
else:
    print("💀 Game Over! The word was:", secret word)
