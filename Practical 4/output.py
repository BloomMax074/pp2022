from domain.STUDENTS import *
from domain.COURSES import *
from domain.MARKS import *

def ListStudents():
    print("Students List:")
    for i in STUDENTS:
        print(i)

def ListCourses():
    print("Courses List:")
    for i in COURSES:
        print(i)

def ShowMarks():
    print("Mark List:")
    for i in COURSES:
        print(f"\tCourse ID: {i.get_courseid()}")
        for j in range(0,len(MARKS)):
                print(f"\nStudent ID: {MARKS[j].get_student_id()}  |  Mark: {MARKS[j].get_mark()}")
