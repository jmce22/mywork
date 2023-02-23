# This program prompts the user to try to guess a number, and it tells them whether
# the number they have selected is too high or too low.
# When they guess the correct number, they are told so.
# Note: Author is Andrew Beatty, and the source is the answer to Question 3 taken from Lab 4.2.
# I have inputted Andrew's answer to MyWork to familiarise myself with the code and to keep
# the answers available to me on VSCode


numberToGuess = 45

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: 

# I know it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))
    
print("Well done! Yes, the number was ", numberToGuess)

