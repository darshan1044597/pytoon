#-----------------------------------------------------------------------------
# Name:        Set_Operations
# Purpose:     Combine and compare sets using set operations
#
#
# Author:      Darshan
# Created:     2-Apr-2025
# Updated:     4-Apr-2025
#-----------------------------------------------------------------------------
# Print a welcome message to the user
print("welcome to set operations")
# Define two sets, 'set1' and 'set2'
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# use union on set1 and set2, combining all the same elements
total = set1.union(set2)
# Print the result of the union
print("Union:", total)
# do the intersection operation keeping only elements common to both sets
inter = set1.intersection(set2)
# Print the result of the intersection
print("Intersection:", inter)
# use the difference operation keeping elements in set1 but not in set2
dif = set1.difference(set2)
# Print the result of the difference
print("Difference:", dif)
