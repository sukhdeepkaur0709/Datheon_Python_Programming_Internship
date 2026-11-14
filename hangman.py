
import random

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

words = ["PYTHON", "COMPUTER", "PROGRAM", "DEVELOPER", "CODING"]

secret_word = random.choice(words)

print("Guess the hidden word!")
print("You have 6 attempts.")

display_word = ["_"] * len(secret_word)

attempts = 6
guessed_letters = []


hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]


while attempts > 0:

    print("\nWord:", " ".join(display_word))

    guess = input("Guess a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
     print("Please enter only one letter!")
     continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")
        attempts = attempts - 1
        print("Attempts left:", attempts)

        print(hangman_stages[6 - attempts])

    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

if attempts == 0:
    print(hangman_stages[6])
    print("GAME OVER!")
    print("The correct word was:", secret_word)
