"""
Number Guessing Game
---------------------
The computer picks a random number within a range you choose,
and you try to guess it within a limited number of attempts.
"""

import random


def get_int_input(prompt):
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.\n")


def get_range():
    """Ask the user for the lower and upper bounds of the range."""
    print("Let's set up the game range.")
    while True:
        low = get_int_input("Enter the lowest number in the range: ")
        high = get_int_input("Enter the highest number in the range: ")
        if low < high:
            return low, high
        print("The lowest number must be smaller than the highest. Try again.\n")


def get_attempts():
    """Ask the user how many guesses they want to be allowed."""
    while True:
        attempts = get_int_input("How many attempts would you like? ")
        if attempts > 0:
            return attempts
        print("Please enter a number greater than 0.\n")


def play_game():
    print("=" * 40)
    print("      WELCOME TO THE GUESSING GAME")
    print("=" * 40)

    low, high = get_range()
    max_attempts = get_attempts()
    secret_number = random.randint(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts to guess it. Good luck!\n")

    for attempt in range(1, max_attempts + 1):
        remaining = max_attempts - attempt + 1
        guess = get_int_input(f"Attempt {attempt}/{max_attempts} - Your guess: ")

        if guess < low or guess > high:
            print(f"Please guess a number within the range {low}-{high}.\n")
            continue

        if guess == secret_number:
            print(f"\n🎉 Correct! You guessed it in {attempt} attempt(s). "
                  f"The number was {secret_number}.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        if remaining > 1:
            print(f"You have {remaining - 1} attempt(s) left.\n")
        else:
            print(f"\n💀 Game over! You've used all your attempts. "
                  f"The number was {secret_number}.")


def main():
    play_game()
    while True:
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again == "y":
            print()
            play_game()
        elif again == "n":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
