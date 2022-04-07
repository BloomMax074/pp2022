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
    print(f'''
    ================================================================
    =======================   System Menu   ========================
    1. View Students List
    2. View Courses List
    3. View Marks List
    4. View GPA List
    5. Exit 
''')
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
