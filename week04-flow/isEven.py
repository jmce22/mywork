# This code asks the user to input an integer, and tells the user
# whether the integer is even or odd
# Author: James McEneaney



number = int(input("enter an integer: "))
if (number % 2) == 0:
    print (f"{number} is an even number")
          
else:
    print(f"{number} is an odd number")