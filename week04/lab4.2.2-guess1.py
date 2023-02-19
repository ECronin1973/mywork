#lab4.2.2-guess1.py
#user will guess number with a prompt until they guess correct number
# Author: Edward Cronin

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)
