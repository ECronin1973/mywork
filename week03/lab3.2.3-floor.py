#lab3.2.3-floor.py
#this will give the floor value of a number
#Author: Edward Cronin

#In the question, number inputted is a float
#output is an integer rounded down

import math

numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print ( '{} floored is {}'.format(numberTofloor, flooredNumber))


