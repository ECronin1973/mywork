#lab6.4-readInStudent.py
#this program will read in a student name, module and grades
#Author: Edward Cronin

students= []
def readModules() :
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)

    #test
doAdd(students)

doAdd(students)
print (students)

