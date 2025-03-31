#print ("times tables")
#for i in range (1, 13):
#    print(i, "x 15 =", i*15)

#total = 0
#for number in range(2):
#    total = total + number
#    print(total)

#import random
#a=random.randint(1,10)
#print(a)

#print("Welcome to the Grocery List")
#grocery_list = ['apples', 'bananas', 'milk', 'carrots', 'bread']
#grocery_list.remove('bananas')
#grocery_list.insert(1, 'grapes')
#print(grocery_list)

# Print a welcome message
print("Welcome to swapping values using tuples, here you enter two numbers and the program will swap their places")
# tell the user to enter the first number and convert the input to an integer
num1 = int(input("Enter the first number: "))
# ask the user to enter the second number and convert the input to an integer
num2 = int(input("Enter the second number: "))
# creates a tuple with the input given
tuple = (num1, num2)
# prints a message to say what the swapped values are
print("the swapped tuple is indexes are:")
# swaps the tuple index values
print(tuple[1], tuple[0])
