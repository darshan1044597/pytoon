#-----------------------------------------------------------------------------
# Name:        voting_eligibility
# Purpose:     Write a Python program that checks if a person is eligible to vote based on their age.
#
#
# Author:      Darshan
# Created:     26-Feb-2025
# Updated:     28-Feb-2025
#-----------------------------------------------------------------------------
# Print a welcome message for the voting eligibility checker
print("welcome to the voting eligibility checker")
# Prompt the user to enter their age
# Convert the input into an integer for comparison
age = int(input("what is your age?"))
# Check if the user's age is 18 or older
if age >= 18:
    # If the user is 18 or older, they are eligible to vote
    print("You are eligible to vote!")
# If the user's age is less than 18
else:
    # tell the user that they are not eligible to vote
    print("Sorry, you are not eligible to vote yet.")
