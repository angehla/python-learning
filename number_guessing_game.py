"""
Number Guessing Game
A beginner Python project practicing variables, loops, conditionals,
functions, user input, and error handling.
"""

import random


def get_guess(low, high):
    """Ask the player for a number until they enter a valid one."""
    while True:
        entry = input(f"Guess a number between {low} and {high}: ")
        try:
            guess = int(entry)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if low <= guess <= high:
            return guess
        print(f"Your guess must be between {low} and {high}.")


def play_round(low=1, high=100):
    """Play one round and return how many guesses it took."""
    secret = random.randint(low, high)
    attempts = 0

    while True:
        guess = get_guess(low, high)
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it! The number was {secret}.")
            return attempts


def main():
    print("Welcome to the Number Guessing Game!")
    best_score = None

    while True:
        attempts = play_round()
        print(f"It took you {attempts} guesses.")

        if best_score is None or attempts < best_score:
            best_score = attempts
            print("New best score!")
        print(f"Best score so far: {best_score} guesses.")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
