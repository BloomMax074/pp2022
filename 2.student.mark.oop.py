STUDENTS = []
COURSES = []
MARKS = []

class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def get_studentid(self):
        return self._id
    def get_studentname(self):
        return self._name
    def get_studentdob(self):
        return self._dob
    def __str__(self):
        return f"Student - ID: {self._id}\n Name: {self._name}\n DOB:{self._dob}"

class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_courseid(self):
        return self._id
    def get_coursename(self):
        return self._name
    def __str__(self):
        return f"Course - ID: {self._id}\n Name: {self._name}"

class Mark:
    def __init__(self,student_id, course_id, mark):
        self._student_id = student_id
        self._course_id = course_id
        self._mark = mark

    def get_student_id(self):
        return self._student_id
    def get_course_id(self):
        return self._course_id
    def get_mark(self):
        return self._mark

def inputStudentCount():
    print("--------------------")
    studentcount = int(input("Please Enter Number Of Students: "))
    return studentcount

def inputStudentInfo():
    print("Student Information")
    id = input(f"Please Enter Student ID: ")
    name = input(f"Please Enter Student Name: ")
    dob = input(f"Please Enter Student DOB: ")
    studentinfo = Student(id,name,dob)
    STUDENTS.append(studentinfo)

def inputCourseCount():
    print("--------------------")
    coursecount = int(input("Please Enter Number of Courses: "))
    return coursecount

def inputCourseInfo():
    print("Course Information")
    name = input(f"Please Enter Course Name: ")
    id = input(f"Please Enter Course ID: ")
    courseinfo = Course(id,name)
    COURSES.append(courseinfo)

def inputMARK():
    print("--------------------")
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
                            M = Mark(StudentID,CourseID,mark)
                            MARKS.append(M)
                            break
                        else:
                            print("Invalid Value")
                break
            else:
                print("Invalid Value")

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

print("Student Mark Management System\n")

studentcount = int(inputStudentCount())
for i in range(0,studentcount):
    inputStudentInfo()
coursecount = int(inputCourseCount())
for i in range(0,coursecount):
    inputCourseInfo()
inputMARK()

while 1:
    print("----------------------")
    print("1.Show Students List")
    print("2.Show Courses List")
    print("3.Show Mark List")
    print("4.End The System")
    choice = int(input("Please Enter Your Choice: "))
    if choice == 1:
        ListStudents()
    elif choice == 2:
        ListCourses()
    elif choice == 3:
        ShowMarks()
    elif choice == 4:
        break
