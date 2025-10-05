# ============================================
# Hangman Game
# --------------------------------------------
# Classic Hangman console game in Python.
# A random word is fetched from an online API,
# and the player guesses letters until they
# either complete the word or run out of lives.
#
# Author: Manupriya Dhanush Vayalambron
# Language: Python 3
# ============================================

import random
import requests

# Hangman ASCII art stages from full body to empty gallows
hang = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Initialize game state
game_over = False

# Fetch a random word from API
word = requests.get("https://random-word-api.herokuapp.com/word?number=1").json()[0]

# List to track correctly guessed letters
correct = []

# Placeholder string to show unguessed letters
placeholder = ""

# Number of lives
lives = 6

# Fill placeholder with underscores for each letter in the word
for i in range(len(word)):
    placeholder += "_"

# Display welcome message
print("""
    /=======================\\
    | Welcome to Hangman!!! |
    \\=======================/
""")
print("Guess the word: ", placeholder)

# Main game loop
while not game_over:
    print("**********************", lives, " lives left **********************")
    
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()
    
    # Check if letter was already guessed
    if guess in correct:
        print("You already guessed this letter")
    
    # Build the display string based on current guesses
    display = ""
    for letter in word:
        if letter == guess:
            display += letter
            correct.append(guess)  # Add new correct guess
        elif letter in correct:
            display += letter  # Show previously guessed letters
        else:
            display += "_"  # Keep unguessed letters hidden
    
    # Handle incorrect guesses
    if guess not in word:
        lives -= 1  # Deduct a life
        if lives == 0:
            game_over = True
            print("\n**********************You Lose**********************")
            print("Correct answer: ", word)
    
    # Show current state of guessed word
    print("\nYour Guess: ", display)
    
    # Check for win condition
    if "_" not in display:
        game_over = True
        print("\n**********************You Won**********************")
    
    # Display current Hangman ASCII art
    print(hang[lives])
