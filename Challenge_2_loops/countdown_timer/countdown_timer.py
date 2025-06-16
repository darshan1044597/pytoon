#-----------------------------------------------------------------------------
# Name:        countdown_timer
# Purpose:     Write a program that starts at `10` and counts down to `1`, but if the user enters `"stop"`, the countdown should break
#
#
# Author:      Darshan
# Created:     18-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
# loop starts from 10 and decreases down to 1
for i in range(10, 0, -1):
    # print the value of the countdown
    print(i)
    # asks the user to stop the timer or continue it
    user_stop = input("Enter stop to cancel or press Enter to continue:")
    # checks if the user entered "stop"
    if user_stop == "stop":
        # prints a message saying the timer is stopped
        print("Timer stopped")
        # breaks the loop to stop the countdown
        break
