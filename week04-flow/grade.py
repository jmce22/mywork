# This code asks the user for a percentage score on an exam, 
# and returns a grade based on that score
# Author: James McEneaney
# Note: Be careful when using "and"s and "or"s



percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
  print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
  print ("Fail")
elif percentage < 50: # between 40 and 49
  print ("Pass")
elif percentage < 60: # between 50 and 59
  print ("Merit1")
elif percentage < 70: # between 60 and 69
  print ("Merit2")
else:
  print("Distinction")