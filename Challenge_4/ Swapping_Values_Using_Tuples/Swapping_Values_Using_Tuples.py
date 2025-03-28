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
num1 = int(input("Enter the first number: "))
# ask the user to enter the second number and convert the input to an integer
num2 = int(input("Enter the second number: "))
# make a tuples for num1 and num2
num1, num2 = (num1, num2)
# Swap the values of num1 and num2
num1, num2 = num2, num1
# Print the swapped values to the user
print("The swapped values are:", num1, num2)
