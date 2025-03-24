#-----------------------------------------------------------------------------
# Name:         remove_item_from_list
# Purpose:      Remove an item from a list
#
#
# Author:      Darshan
# Created:     19-Mar-2025
# Updated:     21-Mar-2025
#-----------------------------------------------------------------------------
# Print a welcome message
print("welcome to the to do list")
# Define a to-do list
to_do_list = ['write email', 'finish homework', 'call mom', 'clean room']
# Print the initial list
print(to_do_list)
# Remove 'call mom' from the list
to_do_list.remove('call mom')
# Print the list after removing 'call mom'
print("removed call mom:")
print(to_do_list)
# Remove 'clean room' from the list
to_do_list.remove('clean room')
# Print the list after removing 'clean room'
print("removed clean room:")
print(to_do_list)
