#lab4.2.3-guess2.py
#user will guess number with a prompt until they guess correct number
# Author: Edward Cronin

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else: #I know it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)

