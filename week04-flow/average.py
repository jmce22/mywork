# This program reads in numbers until
# the user enters 0
# it will them print back out again
# and their average
# Note: Author is Andrew Beatty, and the source is the answer to Question 5 taken from Lab 4.2.
# I have inputted Andrew's answer to MyWork to familiarise myself with the code and to keep
# the answers available to me on VSCode

numbers = []

# first number then we check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))

while number != 0:
   numbers.append(number)

 # read the next number and check if 0
 
   number = int(input("enter another (0 to quit): "))

for values in numbers:
    print (values)

# I want average to be a float
average = float(sum(numbers)) / len(numbers)
print (f"The average is {average}")