#-----------------------------------------------------------------------------
# Name:        Swapping_Values_Using_Tuples
# Purpose:     The purpose of this program is to swap two input values using tuples and display the result
#
#
# Author:      Darshan
# Created:     25-Mar-2025
# Updated:     27-Mar-2025
#-----------------------------------------------------------------------------
# Print a welcome message
print("Welcome to swapping values using tuples, here you enter two numbers and the program will swap their places")
# tell the user to enter the first number and convert the input to an integer
num1 = int(input("Please enter the first number: "))
# ask the user to enter the second number and convert the input to an integer
num2 = int(input("Please enter the second number: "))
# creates a tuple with the input given
tuple = (num1, num2)
# prints a message to say what the swapped values are
print("The swapped tuple indexes for your numbers are:")
# swaps the tuple index values
print(tuple[1], tuple[0])