#-----------------------------------------------------------------------------
# Name:        Tuples_basics
# Purpose:     Create a tuple with five different elements, including an integer, a float, a string, a boolean, and another tuple. Then, write code to: Print the entire tuple. Access and print the third element. Extract the nested tuple and print its first element
#
#
# Author:      Darshan
# Created:     24-Mar-2025
# Updated:     27-Mar-2025
#-----------------------------------------------------------------------------
# Print a header
print("Tuple basics")
# Create a tuple containing different data types
tuple = (42, 3.14, 'Python', True, (1, 2, 3))
# Print the entire tuple
print(tuple)
# Access and print the third element of the tuple
print("The third element is:")
print(tuple[2])
# Access the nested tuple and print its first element
print("The first element of the nested tuple is:")
print(tuple[4][0])
