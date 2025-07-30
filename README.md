# Number Guessing Game

A fun and colorful terminal-based number guessing game built using Python. The game picks a random number between 1 and 100, and the player has to guess it with the help of smart hints and feedback.

## How to Play

- The computer thinks of a number between 1 and 100
- You guess the number in as few attempts as possible
- After each guess, the game gives you a hint:
  - 📉 "Too low" or 📈 "Too high"
- Your best score is tracked across games
- The game includes colorful messages for a better experience!

## Features

- Random number generator using `random.randint`
- Input validation to handle non-number inputs
- Colorful output using the `colorama` library
- Best score tracking during the session
- Option to play multiple rounds

## Requirements

Make sure Python is installed, then install the required library:

```bash
pip install colorama
