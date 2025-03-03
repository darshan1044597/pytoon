#-----------------------------------------------------------------------------
# Name:        day_of_the_week_activities
# Purpose:     Create a Python program that suggests an activity based on the day of the week.
#
#
# Author:      Darshan
# Created:     27-Feb-2025
# Updated:     28-Feb-2025
#-----------------------------------------------------------------------------
# Print a welcome message for the user
print("welcome to the day of the week activity recommender")
# Prompt the user to input the current day of the week
dayoftheweek = input("what day of the week is it? ")
# Check if the day is Monday and suggest an activity
if dayoftheweek == "Monday":
    print("Start your week with a workout!")
# Check if the day is Tuesday and suggest an activity
elif dayoftheweek == "Tuesday":
    print("It's a great day to read a book!")
# Check if the day is Wednesday and suggest an activity
elif dayoftheweek == "Wednesday":
    print("Mid-week movie night!")
# Check if the day is Thursday and suggest an activity
elif dayoftheweek == "Thursday":
    print("Try a new recipe!")
# Check if the day is Friday and suggest an activity
elif dayoftheweek == "Friday":
    print("Relax and enjoy the weekend!")
# Check if the day is Saturday and suggest an activity
elif dayoftheweek == "Saturday":
    print("Go for a hike!")
# Check if the day is Sunday and suggest an activity
elif dayoftheweek == "Sunday":
    print("Prepare for the week ahead with some self-care.")
# Handle invalid day inputs with an error message
else:
    print("that day doesn't exist!")
