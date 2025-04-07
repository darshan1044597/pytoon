#-----------------------------------------------------------------------------
# Name:        Adding_and_Removing_Elements_using_update
# Purpose:     Modify a set efficiently using `.update()` and `.discard()` for bulk modifications
#
#
# Author:      Darshan
# Created:     3-Apr-2025
# Updated:     4-Apr-2025
#-----------------------------------------------------------------------------
# Print a welcome message to the user
print("welcome to adding and removing elements using update")
# make a set named 'letters' with initial values
letters = {'a', 'b', 'c'}
# Use the update() method to add multiple elements ('d', 'e', 'f') to the set
letters.update({'d', 'e', 'f'})
# Use the discard() method to remove the element 'b' from the set
letters.discard('b')
# Print the updated 'letters' set
print(letters)
