# This program prompts the user to guess a number, and continues to prompt them
# until they guess the correct number.
# They are then told they have correctly guess the number.
# Note: Author is Andrew Beatty and the source is the answer to Question 2 taken from Lab 4.2.
# I have inputted Andrew's answer to MyWork to familiarise myself with the code and to keep
# the answers available to me on VSCode


numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)