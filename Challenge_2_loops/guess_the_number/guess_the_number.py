#-----------------------------------------------------------------------------
# Name:        guess_the_number
# Purpose:     Write a program that generates a random number between `1` and `10` and keeps asking the user to guess until they guess correctly
#
#
# Author:      Darshan
# Created:     7-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------
# Import random module to generate a random number
import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Ask the player to guess the number for the first time
guess = int(input("guess a number between 1 and 10: "))

# Loop until the player guesses the correct number
while guess != number:
    # Checks if the user guessed right and ends the code
    if guess == number:
        print("correct")
    else:
        # Prompt the player to try again if they guessed incorrectly
        guess = int(input("guess again: "))

# Congratulate the player for guessing the number correctly
print("you guessed it right!")
