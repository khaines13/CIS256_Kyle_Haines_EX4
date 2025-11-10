# Kyle Haines
# CIS256 Fall 2025
# EX 4
# Exercise Assignment 4

import pytest
from guess_the_word import WordGuessingGame

@pytest.fixture
# Learned about fixture from Pytest Quick Guide (link in EX4 - tutorialspoint)
def word_guessing_game_instance():
    """Provides a WordGuessingGame instance for testing."""
    words = ["python", "programming", "github", "pytest", "challenge", "commit"]
    return WordGuessingGame(words)

def test_choose_word(word_guessing_game_instance):
    words = ["python", "programming", "github", "pytest", "challenge", "commit"]
    selected_word = word_guessing_game_instance.choose_word()
    assert selected_word in words

def test_guess_correct_letter(word_guessing_game_instance):
    # Assuming 'python' is the random word for testing purposes
    word_guessing_game_instance.random_word = "python"
    letter = "p"
    result = word_guessing_game_instance.make_guess(letter)
    # Displays message for correct guess "Good guess! 'p' is in the word."
    assert result == True
    assert letter in word_guessing_game_instance.guessed_letters

def test_guess_incorrect_letter(word_guessing_game_instance):
    initial_attempts = word_guessing_game_instance.incorrect_guesses
    word_guessing_game_instance.random_word = "python"
    letter = "z"
    result = word_guessing_game_instance.make_guess(letter)
    # Displays message for incorrect guess "Sorry, 'z' is not in the word."
    assert result == True
    assert letter in word_guessing_game_instance.guessed_letters
    assert word_guessing_game_instance.incorrect_guesses == initial_attempts + 1
