import numpy as np

STUDENTS = []
class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def get_studentid(self):
        return self.__id
    def get_studentname(self):
        return self.__name
    def get_studentdob(self):
        return self.__dob
    def __str__(self):
        return f"Student - ID: {self.__id}\n - Name: {self.__name}\n - DOB:{self.__dob}"

COURSES = []
class Course:
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def get_courseid(self):
        return self.__id
    def get_coursename(self):
        return self.__name
    def get_credit(self):
        return self.__credit    
    def __str__(self):
        return f"Course - ID: {self.__id}\n - Name: {self.__name}\n - Credit: {self.__credit}"

MARKS = []
class Mark:
    def __init__(self,student_id, course_id, mark):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark = mark

    def get_student_id(self):
        return self.__student_id
    def get_course_id(self):
        return self.__course_id
    def get_mark(self):
        return self.__mark

GPA = []
class Gpa:
    def __init__(self, student_id, gpa):
        self.__student_id = student_id
        self.gpa = gpa
    
    def get_student_id(self):
        return self.__student_id
    def get_gpa(self):
        return self.gpa
    def __str__(self):
        return f"Student - ID: {self.__student_id} | GPA: {self.gpa}"


def inputStudentCount():
    print("================================================")
    studentcount = int(input("Please Enter Number Of Students: "))
    return studentcount

def inputStudentInfo():
    print("Student Information")  
    name = input(f"Please Enter Student Name: ")
    id = input(f"Please Enter Student ID: ")
    dob = input(f"Please Enter Student DOB: ")
    studentinfo = Student(name, id, dob)
    STUDENTS.append(studentinfo)

def inputCourseCount():
    print("================================================")
    coursecount = int(input("Please Enter Number of Courses: "))
    return coursecount

def inputCourseInfo():
    print("Course Information")
    name = input(f"Please Enter Course Name: ")
    id = input(f"Please Enter Course ID: ")
    credit = input(f"Please Enter Course Credits: ")
    courseinfo = Course(id, name, credit)
    COURSES.append(courseinfo)

def inputMARK():
    print("================================================")
    print("Mark Input System")
    for i in COURSES:
        while 1:
            CourseID = input("Please Enter a Course ID: ")
            CourseList = [course_id.get_courseid() for course_id in COURSES]
            if CourseID in CourseList:
                for j in STUDENTS:
                    while 1:
                        StudentID = input("Please Enter a Student ID: ")
                        StudentList = [student_id.get_studentid() for student_id in STUDENTS]
                        if StudentID in StudentList:
                            mark = float(input("Please Enter Mark: "))
                            M = Mark(StudentID, CourseID, mark)
                            MARKS.append(M)
                            break
                        else:
                            print("Invalid Input")
                break
            else:
                print("Invalid Input")   

def student_gpa():
    marks = np.array(MARKS)
    credits = np.array(COURSES)
    for i in STUDENTS:
        total_marks = 0
        total_credits = 0
        for j in marks:
            if j.get_student_id() == i.get_studentid():
                total_marks = total_marks + j.get_mark()
                for k in credits:
                    if j.get_course_id() == k.get_courseid():
                        total_credits = total_credits + k.get_credit()
        id = i.get_course_id()
        gpa_calculate = total_marks/total_credits
        student_gpa = Gpa(id, gpa_calculate)
        GPA.append(student_gpa)

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
        for k in range(0,len(MARKS)):
            if(MARKS[k].get_course_id() == i.get_courseid()):
                print(f"Student ID: {MARKS[k].get_student_id()}  |  Mark: {MARKS[k].get_mark()}")

def ShowGPA():
    print("GPA List:")
    for i in GPA:
        print(i)

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
inputMARK()

while 1:
    print("================================================================")
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
        GPA()
        GPA.sort(key=lambda x: x.gpa, reverse=True)
        ShowGPA()
    elif choice == 5:
        break
