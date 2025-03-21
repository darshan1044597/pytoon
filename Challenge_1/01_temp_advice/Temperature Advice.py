#-----------------------------------------------------------------------------
# Name:        temperature_advice
# Purpose:     Write a Python program that asks the user for the current temperature and gives a suggestion
#
#
# Author:      Darshan
# Created:     24-Feb-2025
# Updated:     28-Feb-2025
#-----------------------------------------------------------------------------
# Print a welcome message for the user
print("Welcome to Temperature Advice")
# Ask the user to input the current temperature
# Convert the input into a floating-point number for comparison
temp = float(input("What is the temperature?"))
# Check if the temperature is less than 10 degrees
if temp < 10:
    # Suggest clothing for cold weather
    print("It's cold outside. Wear a jacket!")
# Check if the temperature is between 10 and 25 degrees (inclusive of 10, but less than 25)
elif temp >= 10 and temp < 25:
    # Suggest clothing for mild weather
    print("It's a nice day. Wear short-sleeves!")
# Check if the temperature is 25 degrees or more
elif temp >= 25:
    # Suggest clothing for hot weather
    print("It's hot outside. Stay cool!")
# Handle unexpected cases (though unlikely, it's a good practice)
else:
    print("Unknown temperature")
