#lab3.2.4-convert.py
#this will convert an amount into cent
#Author: Edward Cronin

#In the question, number inputted is ambiguous
#output implies that we should be dealing with int values
#I am casting the input to a float, then changing from float to int 

number = float(input("Please enter an amount:"))
absoluteValue = int(number*100)
print ( 'That amount in cent is {}'.format(absoluteValue))

#number changed from float to int to remove the .0 at end of returned value
