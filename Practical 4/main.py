from input import *
from output import *

print(""" 
  ------------------------------------------------------
 |======================================================| 
 |========    Student Mark Management System	========|
 |======================================================|
  ------------------------------------------------------
  """)

studentcount = int(inputStudentCount())
for i in range(0,studentcount):
    inputStudentInfo()
coursecount = int(inputCourseCount())
for i in range(0,coursecount):
    inputCourseInfo()
ChooseCourse()
inputMark()

while True:
    print("================================================================")
    print("=======================   System Menu   ========================")
    print("1.Show Students List")
    print("2.Show Courses List")
    print("3.Show Mark List")
    print("4.Show GPA List")
    print("5.End The System")
    choice = int(input("Please Enter Your Choice: "))
    if choice == 1:
        ListStudents()
    elif choice == 2:
        ListCourses()
    elif choice == 3:
        ShowMarks()
    elif choice == 4:
        GPA_calculations_For_Students()
    elif choice == 5:
        break
