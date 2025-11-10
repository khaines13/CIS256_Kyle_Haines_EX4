# Kyle Haines
# CIS256 Fall 2025
# EX 4
# Exercise Assignment 4

import random

class WordGuessingGame:
    """A class to represent a word guessing game where the user guesses a word letter by letter."""
    def __init__(self, word_list, max_guesses=6):
        """Initializes the WordGuessingGame, with list of words to choose from and max guesses"""

        self.word_list = word_list
        self.random_word = self.choose_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_guesses = max_guesses
        self.current_display = self.initialize_display()

    def choose_word(self):
        """Selects a random word from the word_list."""
        return random.choice(self.word_list).lower()

    def initialize_display(self):
        """Creates the initial display string (blank spaces for word, ex: "_____")."""
        return ["_" for _ in self.random_word]

    def display_game_state(self):
        """Prints the current state of the game, including the displayed word and remaining guesses."""
        print("\nWord: " + " ".join(self.current_display))
        # Display number of incorrect guesses and max allowed guesses
        print(f"Incorrect guesses: {self.incorrect_guesses}/{self.max_guesses}")
        # Display guessed letters, sorted alphabetically using sorted()
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

    def make_guess(self, letter):
        """Processes the user's letter guess."""

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

    def check_win(self):
        """Checks if the user has won the game."""
        return "_" not in self.current_display

    def check_loss(self):
        """Checks if the user has lost the game."""
        return self.incorrect_guesses >= self.max_guesses

    def play_game(self):
        """Manages the main game loop"""
        print("Welcome to the Word Guessing Game!")
        print(f"The word has {len(self.random_word)} letters.")
        # While game is not won or loss, user makes guesses
        while not self.check_win() and not self.check_loss():
            self.display_game_state()
            # Strip whitespace and lower case of the letter in user input
            guess = input("Guess one letter at a time: ").strip().lower()
            self.make_guess(guess)

        self.display_game_state()
        # Call display game state for check win - current display, to see if user has won
        if self.check_win():
            # Print congratulatory message if the word is guessed
            print(f"Congratulations!\nYou guessed the word: {self.random_word}")
        else:
            # Print game over and display the correct word
            print(f"Game over! Ran out of guesses.\nThe word was: {self.random_word}")

if __name__ == "__main__":
    words = ["python", "programming", "github", "pytest", "challenge", "commit"]
    game = WordGuessingGame(words)
    game.play_game()
