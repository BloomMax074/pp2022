import numpy as np

from domain.STUDENTS import *
from domain.COURSES import *
from domain.MARKS import *
from domain.GPA import *

def inputStudentCount():
    print("================================================")
    studentcount = int(input("Please Enter Number Of Students: "))
    return studentcount

def inputStudentInfo():
    print("Student Information")
    student_id = input("Please Enter Student ID: ")
    student_name = input("Please Enter Student Name: ")
    student_dob = input("Please Enter Student DOB: ")
    student_info = Student(student_id,student_name,student_dob)
    STUDENTS.append(student_info)

def inputCourseCount():
    print("================================================")
    coursecount = int(input("Please Enter Number of Courses: "))
    return coursecount

def inputCourseInfo():
    print("Course Information")
    course_name = input("Please Enter Course Name: ")
    course_id = input("Please Enter Course ID: ")
    course_credits = input("Please Enter Course Credits: ")
    course_info = Course(course_id,course_name,course_credits)
    COURSES.append(course_info)

def ChooseCourse():
    print("================================================")
    print("Choose Course")
    for i in COURSES:
            CourseID = input("Please Enter a Course ID: ")
            CourseList = [course_id.get_courseid() for course_id in COURSES]
            if CourseID in CourseList:
                print("Continue...")
                break
            else:
                print("Course ID not found")

def inputMark():
    print("Mark Input System")
    for i in STUDENTS:
        StudentID = input("Please Enter a Student ID: ")
        StudentList = [student_id.get_studentid() for student_id in STUDENTS]
        if StudentID in StudentList:
            mark = float(input("Please Enter Mark: "))
            Mark_Of_A_Student = Mark(StudentID,mark)
            MARKS.append(Mark_Of_A_Student)
            break
        else:
            print ("Invalid Value")

def GPA_calculations_For_Students():
    All_Marks = [marks.get_mark() for marks in MARKS]
    All_Credits = [credits.get_coursecredits() for credits in COURSES]
    gpa = np.add(All_Marks,All_Credits)
    coursegpa = Gpa(gpa)
    GPA.append(coursegpa)
    for j in GPA:
        if j in range(0,len(GPA)):
            print(f"\nStudent ID: {GPA[j].get_student_id()}  |  Gpa: {GPA[j].get_gpa()}")     