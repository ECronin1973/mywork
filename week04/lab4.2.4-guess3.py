#lab4.2.4-guess3.py
#user will guess number with a prompt until they guess correct number
# Author: Edward Cronin

import random

numberToGuess = random.randint(1, 100)

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else: #I know it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)

