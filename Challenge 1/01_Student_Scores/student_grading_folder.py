#-----------------------------------------------------------------------------
# Name:        Student_grading
# Purpose:     Create a Python program that asks for a student's score and then provides a grade based on the score
#
#
# Author:      Darshan
# Created:     24-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------
print("Welcome to the student grading folder")
#this will ask the user to input their score
StuGrade = float(input("enter your score out of 100"))
#the if statement says if the score is less than 60 it prits as a F
if StuGrade < 60:
    print("Grade F")
#the elif statement makes it to where if the grade is above a 59 but under a 70 it is a D
elif StuGrade < 70:
    print("Grade D")
#the elif statement makes it to where if the grade is above a 69 but under a 80 it is a C
elif StuGrade < 80:
    print("Grade C")
elif StuGrade < 90:
    print("Grade B")
elif StuGrade < 101:
    print("Grade A")
#that cycle continues until here where if the number is over 101 it will print as unknown
else:
    print("unknown")

