percentage = round(float(input("Enter the percentage: ")))

if percentage < 0 or percentage > 100:
  print ("Please enter a number between 0 and 100")
elif percentage < 39.5: # we know it is greater than 0
  print ("Fail")
elif percentage < 49.5: # between 40 and 49
  print ("Pass")
elif percentage < 59.5: # between 50 and 59
  print ("Merit1")
elif percentage < 69.5: # between 60 and 69
  print ("Merit2")
else:
  print("Distinction")