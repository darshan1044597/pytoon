#-----------------------------------------------------------------------------
# Name:        sum_of_numbers
# Purpose:     Write a program that asks the user for a number `n` and calculates the sum of all numbers from `1` to `n`
#
#
# Author:      Darshan
# Created:     6-Mar-2025
# Updated:     18-Mar-2025
#-----------------------------------------------------------------------------
# tell the user to enter a number for the variable n
print("enter a number valued as n:")
n = int(input())

# uses variable 'sum' to store the sum of numbers
sum = 0

# repeat from 1 to n
for i in range(1, n + 1):
    sum = sum + i  # add the current number i to sum

# print the sum
print("sum of numbers is:", sum)
