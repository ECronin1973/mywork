#randomQueue.py
#program which puts 10 random numbers into a queue
#following which it outputs all the values in the queue
#then takes the numbers from the queue one at a time, prints it and 
#the current numbers still in the queue
#Author: Edward Cronin

import random
queue = []
numberOfNumbers=10
rangeTo=300

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print (f"queue is {queue} ")
    
while len(queue) != 0:

    currentNumber = queue.pop(0)
    print(f" current Number is {currentNumber} and the queue is {queue} ")

print (f"the queue is now empty")
