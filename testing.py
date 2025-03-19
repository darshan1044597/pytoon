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

print ("welcome to the countdown timer")
import time
for i in range(10,0,-1):
    print(i)
    user_stop = input("Enter stop to cancel or press Enter to continue:")
    if user_stop == "stop":
        print("Timer stopped")
        break
#    else:
#        print("Timer started")
#    time.sleep(1)
