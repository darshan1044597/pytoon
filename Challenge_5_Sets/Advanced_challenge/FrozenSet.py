#-----------------------------------------------------------------------------
# Name:        FrozenSet
# Purpose:     Work with frozensets to understand their immutability
#
#
# Author:      Darshan
# Created:     Apr-4-2025
# Updated:     Apr-7-2025
#-----------------------------------------------------------------------------
# print a welcome message
print ("welcome to the frozenset")
# create a forzenset called frozen_numbers
frozen_numbers = frozenset({1, 2, 3, 4, 5})
# attempt to add a element to the frozen set
frozen_numbers.add(6)
# prints the frozen set after tring to add a element
# this will cause a error which is: AttributeError: 'frozenset' object has no attribute 'add'
print(frozen_numbers)