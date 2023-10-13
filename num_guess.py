#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Oct/13/2023
# This program allows users to guess a number and returns whether they guessed correctly or incorrectly.
# Importing my constants.
import constants


def main():
    # Getting the user input ( number they guess).
    user_guess = int(input("Enter a number between 0-9 for your guess: "))

    # If Then statement to tell the user if they guessed correctly.
    if user_guess == constants.CORRECT_GUESS:
        print("You guessed correctly! The number is 7.")

    # If Then statement to tell the user if they guessed incorrectly.
    if user_guess != constants.CORRECT_GUESS:
        print("You guessed incorrectly. Please try again!")


if __name__ == "__main__":
    main()
