#div.py
#This program reads in two numbers and
#outputs the integer answer and remainder
#Author: Edward Cronin

x = int(input("Enter first number: ")) #this allows for capturing input 1
y = int(input("Enter number you want to divide by: ")) #this allows for capturing input 2
answer = int(x // y) #// gives int division
remainder = x%y      #gives the remainder

print ("{} divided by {} is {} with remainder {} ".format(x, y, answer, remainder)) #this presents answer based on the format in brackets