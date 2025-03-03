#-----------------------------------------------------------------------------
# Name:        odd_or_even
# Purpose:     Create a Python program that asks the user for a number and then tells them if the number is even or odd
#
#
# Author:      Darshan
# Created:     25-Feb-2025
# Updated:     28-Feb-2025
#-----------------------------------------------------------------------------
# Print a welcome message for the user
print("Welcome to Odd or Even finder")
# Prompt the user to enter a number
# Convert the input into an integer for mathematical operations
num = int(input("enter your specified number"))
# Check if the number is divisible by 2 (i.e., an even number)
if num % 2 == 0:
    # If the number is even, print a message
    print("The number is even.")
# Check if the number is not divisible by 2 (i.e., an odd number)
elif num % 2 != 0:
    # If the number is odd, print a message
    print("The number is odd")
# Handle unexpected cases (this condition is redundant but included in case of edge scenarios)
else:
    print("unknown")
