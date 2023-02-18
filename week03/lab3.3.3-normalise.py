#lab3.3.4-normalise.py
#this program reads in a string and strips
#any leading or trailing spaces.
#It also converts all the letters to lower case.
#It then outputs the lengths of the original string
#and the normalised one

#Author: Edward Cronin

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print(f"That String normalised is :{normalisedString}")
print(f"we reduce the input string from {lenghtOfRawString} to {lengthOfNormalised} characters")
