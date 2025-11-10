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
