#-----------------------------------------------------------------------------
# Name:        Tuple_operations_and_count
# Purpose:     Create a tuple with repeated values, such as `("apple", "banana", "apple", "cherry", "banana", "apple")` and Ask the user to enter a fruit name, then Print how many times that fruit appears in the tuple.
#
#
# Author:      Darshan
# Created:     26-Mar-2025
# Updated:     27-Mar-2025
#-----------------------------------------------------------------------------
# Print a header message
print("Tuple operations and count")
# write a tuple containing some fruit names with repeated elements
tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")
# print a list of given fruits for the user to choose from
print("Fruits available for selection: apple, banana, cherry")
# ask the user to input the name of a fruit and store it as a string
fruit = str(input("Enter the name of a fruit: "))
# Count the amount of the entered fruit in the tuple
count = tuple.count(fruit)
# Print the count of the fruit in the tuple
print(count)
