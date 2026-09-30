import random
import time
words = 'apple banana cherry date elderberry fig grape honeydew'.split()
words= random.choice(words)
guessed = []
wrong_guesses = 0
max_attempts = 6
hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hangman!")
time.sleep(1)
print("You have", max_attempts, "attempts to guess the word.")
time.sleep(1)
print("The word has", len(words), "letters.")
time.sleep(1)
hint = input("Do you want a hint? (y/n): ")
if hint.lower() == 'y':
    print("The word is related to fruit.")

    time.sleep(3)
while wrong_guesses < max_attempts and all(letter in guessed for letter in words)== False:
    
    print(hangman[wrong_guesses])
    display_word = ""
    for letter in words:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed:
        print("You already guessed that letter.")
    elif guess in words:
        print("Good guess!")
        guessed.append(guess)
    else:
        print("Wrong guess.")
        guessed.append(guess)
        wrong_guesses += 1
    
    if all(letter in guessed for letter in words)== True:
        time.sleep(1)
        print("Congratulations! You guessed the word:", words)


if wrong_guesses>=max_attempts:

    print("HAHAHA! you've run out of attempts. The word was:", words)

