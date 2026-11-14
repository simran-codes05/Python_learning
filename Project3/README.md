-- Hangman Game – Fruit Edition
-- Project Description

This is a simple Hangman Game developed using Python. The game is based on guessing the name of a fruit or vegetable within a limited number of attempts.

The computer randomly selects a word from a predefined list, and the player must guess the word one letter at a time. For every incorrect guess, the player loses one life, and a hangman stage is displayed.

The objective is to identify the hidden word before running out of lives.

-- Features

Random word selection using Python's random module.
A collection of fruits and vegetables.
Letter-by-letter guessing.
Maximum of 6 lives.
Interactive hangman drawing.
Automatic win and lose detection.
Displays the correct word when the player loses.

-- Example Output
text
Let's play Hangman Game!

['_', '_', '_', '_', '_']

You have 6 lives
Enter a letter to guess: a

['_', 'a', '_', '_', '_']

You have 6 lives
Enter a letter to guess: z

['_', 'a', '_', '_', '_']

You have 5 lives

-- Winning and Losing Conditions
Winning: Guess all the letters of the hidden word before losing all your lives.
Losing: If you make 6 incorrect guesses, the hangman is completed and you lose the game.

--Future Improvements

Prevent players from guessing the same letter multiple times.
Add hints for difficult words.
Add a score system.
Allow players to play multiple rounds.

-- Developed as a beginner-friendly Python project to practice:

Loops
Conditional statements
Lists
Strings
Random module
User input
Module imports
