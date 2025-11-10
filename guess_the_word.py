# Kyle Haines
# CIS256 Fall 2025
# EX 4
# Exercise Assignment 4

import random

class WordGuessingGame:
    def __init__(self, word_list, max_guesses=6):
        self.word_list = word_list
        self.random_word = self.choose_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_guesses = max_guesses
        self.current_display = self.initialize_display()

    def choose_word(self):
        return random.choice(self.word_list).lower()

    def initialize_display(self):
        return ["_" for _ in self.random_word]

    def display_game_state(self):
        print("\nWord: " + " ".join(self.current_display))
        # Display number of incorrect guesses and max allowed guesses
        print(f"Incorrect guesses: {self.incorrect_guesses}/{self.max_guesses}")
        # Display guessed letters, sorted alphabetically using sorted()
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

    def make_guess(self, letter):

        # Ensure user only enters one letter per guess
        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input. Please enter a single letter.")
            return False
        # Doesn't increase incorrect guess counter for repeat letter guesses
        if letter in self.guessed_letters:
            print("You already guessed that letter. Try again.")
            return False

        # Add user guessed letter to list of guessed letters
        self.guessed_letters.append(letter)

        if letter in self.random_word:
            for i, char in enumerate(self.random_word):
                if char == letter:
                    self.current_display[i] = letter
            print(f"Good guess! '{letter}' is in the word.")
        else:
            self.incorrect_guesses += 1
            print(f"Sorry, '{letter}' is not in the word.")
        return True
