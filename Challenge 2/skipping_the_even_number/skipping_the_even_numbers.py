#-----------------------------------------------------------------------------
# Name:        skipping_the_even_numbers
# Purpose:     Write a program that prints numbers from `1` to `10`, but **skips even numbers** using "continue"
#
#
# Author:      Darshan
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------
# Welcome message for the user
print ("welcome to the even number skipping program")
#lists numbers from 1 up until to 10
for num in range(1,11):
    #checks if the number is divisible by 2
    if num % 2 == 0:
        # skips the number if it is even
        continue
    #prints the remaining numbers left
    print (num)