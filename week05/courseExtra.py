#courseExtra.py
#This program stores a student name
# along with a list of her courses and grades in a dict
#the program will then print out her data
#Author: Edward Cronin

student = {
    "name" : input("Enter your name: "),
    
    "modules": [
        {
            "courseName" : input("Enter your courseName: "),
            "grade" : input("Enter your grade: "),
        }
                ]
            }
print ("Student: {}".format(student ["name"]))
for module in student ["modules"]:
    print ("\t {} \t{}".format (module ["courseName"], module["grade"]))
