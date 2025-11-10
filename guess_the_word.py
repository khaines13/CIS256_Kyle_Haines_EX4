# Kyle Haines
# CIS256 Fall 2025
# EX 4
# Exercise Assignment 4

import random

def word_guessing_game():
    words = ["python", "programming", "github", "pytest", "challenge", "commit"]
    # Selects a random word from the predefined list of words
    random_word = random.choice(words).lower()
    guessed_letters = []
    attempts = 7

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(random_word)} letters.")

    # While loop to continue until user guesses or runs out of attempts
    while attempts > 0:
        display_word = ""
        # For loop to add correct guessed letters to display word
        for letter in random_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"\nWord: {display_word}")
        # Display guessed letters, sorted alphabetically using sorted()
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        # Display remaining attempts
        print(f"Attempts left: {attempts}")

        # Congratulatory message when the word is guessed
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            # Break loop if user guesses word correctly
            break

        # Prompt user to only guess one letter at a time
        guess = input("Guess one letter at a time: ").lower()

        # Ensure user only enters one letter per guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Doesn't drop attempt counter for repeat letter guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        # Reveal letters if the guess is correct
        if guess in random_word:
            print(f"Good guess! '{guess}' is in the word.")
        # Else indicate the guess is incorrect
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    else:
        # If the while loop finishes without a 'break', user runs out of attempts
        print("\nGame over! You ran out of attempts.")
        print(f"The word was: {random_word}")


if __name__ == "__main__":
    word_guessing_game()
