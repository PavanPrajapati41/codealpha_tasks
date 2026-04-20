import random

# Predefined list of words
words = ["python", "apple", "chair", "tiger", "plane"]

# Randomly choose a word
word = random.choice(words)

# Create a display with underscores
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of incorrect attempts allowed
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)