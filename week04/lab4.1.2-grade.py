#lab4.1.2-grade.py
#this program reads in a students percentage
#and prints out the corresponding grade
#Author: Edward Cronin

percentage = float(input("Enter the percentage: "))
#print (percentage)

if percentage <0 or percentage > 100:
    print ("please enter a number between 0 and 100")
elif percentage <40: #we know it is greater than zero
    print ("Fail")
elif percentage <50: #between 40 and 49
    print ("Pass")
elif percentage <60: #between 50 and 59
    print ("Merit2")
elif percentage <70:#between 60 and 69
    print ("Merit1")
else: #the only option left is between 70 and 100
    print ("Distinction")