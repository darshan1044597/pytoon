#-----------------------------------------------------------------------------
# Name:        Grocery_list_modification
# Purpose:     Modify a grocery list by changing an existing item
#
#
# Author:      Darshan
# Created:     18-Mar-2025
# Updated:     21-Mar-2025
#-----------------------------------------------------------------------------
# Print a welcome message to the user
print("Welcome to the Grocery List")
# Define the initial grocery list
grocery_list = ['apples', 'bananas', 'milk', 'carrots', 'bread']
# Print the original list
print(grocery_list)
# Remove the 'bananas' from the grocery list
grocery_list.remove('bananas')
# Insert the item 'grapes'
grocery_list.insert(1, 'grapes')
# Print a message indicating the updated list is being shown
print("updated grocery list")
# Print the changed grocery list to display the changes
print(grocery_list)
# Prints the thrid item
print ("third item in the list is:")
# Print the item at index 1 (the newly inserted 'grapes') as a sublist
print(grocery_list[2:3])
