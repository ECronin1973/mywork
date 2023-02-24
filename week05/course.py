#course.py
#This program stores a student name
# along with a list of her courses and grades in a dict
#the program will then print out her data
#Author: Edward Cronin

student = {
    "name" : "Mary",
    "modules": [
        {
            "courseName" : "Progrmming",
            "grade" : 45
        },
        {
            "courseName" : "History",
            "grade" : 99
        }
                ]
            }

print ("Student: {}".format(student ["name"]))
for module in student ["modules"]:
    print ("\t {} \t: {}".format (module ["courseName"], module["grade"]))