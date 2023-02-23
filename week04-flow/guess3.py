numberToGuess = 30

import random

guess = (random.randint(0,100))
while guess != numberToGuess:
    print (f'"Wrong, the answer is not {guess}"')
    guess = (input("Please guess again: "))
    
    if guess == numberToGuess:
        print ("Well done! Yes the number was ", numberToGuess)