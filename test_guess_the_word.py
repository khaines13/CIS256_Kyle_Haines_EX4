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
