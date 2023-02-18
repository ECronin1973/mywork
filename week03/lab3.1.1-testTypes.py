#testTypes.py
#This program tests variables and States
#Author: Edward Cronin

i = 3
fl = 3.5
isa = True
memo = 'how now Brown Cow'
lots = []

#print ('variable () is of type: () and value:()' .format('i', type(i), i)) #this displayed return 'variable () is of type: () and value:()'
#print ('variable () is of type: () and value:()'.format('fl', type(fl), fl)) #this displayed return 'variable () is of type: () and value:()'
#print ('variable () is of type: () and value:()'.format('isa', type(isa), isa)) #this displayed return 'variable () is of type: () and value:()'
#print ('variable () is of type: () and value:()'.format('memo', type(memo), memo)) #this displayed return 'variable () is of type: () and value:()'
#print ('variable () is of type: () and value:()'.format('lots', type(lots), lots)) #this displayed return 'variable () is of type: () and value:()'

print (f'variable () is of type:{type(i)}' ' and value:' +str(i))
print (f'variable () is of type:{type(fl)}' ' and value:' +str(fl))
print (f'variable () is of type:{type(isa)}'' and value:' +str(isa))
print (f'variable () is of type:{type(memo)}' ' and value:' +str(memo))
print (f'variable () is of type:{type(lots)}' ' and value:' +str(lots))

#rows 17 - 21 displayed the actual type and value of inputs at rows 5 - 9
# variable () is of type:<class 'int'> and value:3
#variable () is of type:<class 'float'> and value:3.5
#variable () is of type:<class 'bool'> and value:True
#variable () is of type:<class 'str'> and value:how now Brown Cow
#variable () is of type:<class 'list'> and value:[] 