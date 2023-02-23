# This code prompts the user to enter a number, and tells the user
# whether the number is odd or even.
# It continues to prompt the user to enter numbers until the user enters the 
# number '-1'
# Author: James McEneaney


number = int(input("enter a number: "))

while number != -1:
    if (number %2 == 0):
        print (f"Number is {number}, which is even")
    elif (number %2 != 0):
        print (f"Number is {number}, which is odd")
    number = int(input("enter a number: "))
print ("Finished")
    