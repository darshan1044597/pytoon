#-----------------------------------------------------------------------------
# Name:        Grocery_list_modification
# Purpose:     Modify a grocery list by changing an existing item
#
#
# Author:      Darshan
# Created:     18-Mar-2025
# Updated:     21-Mar-2025
#-----------------------------------------------------------------------------
print("Welcome to the Grocery List")
grocery_list = ['apples', 'bananas', 'milk', 'carrots', 'bread']
grocery_list.remove('bananas')
grocery_list.insert(1, 'grapes')
print(grocery_list)
print("updated grocery list")
print(grocery_list[1:2])