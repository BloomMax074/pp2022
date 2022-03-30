def inputStudentCount():
    studentcount = int(input("Please Enter Number Of Students: "))
    return studentcount

def inputStudentInfo(studentCount):
    students = {}
    for i in range(0, studentCount):
        id = input("Please Enter Student ID: ")
        name = input("Please Enter Student Name: ")
        dob = input("Please Enter Student DOB: ")
        students[id] = {
            "name": name,
            "dob": dob,
            "marks": {}
        }
    return students

def inputCourseCount():
    coursecount = int(input("Please Enter Number Of Courses: "))
    return coursecount

def inputCourseInfo(courseCount):
    courses = {}
    for i in range(0, courseCount):
        name = input("Please Enter Course Name: ")
        id = input("Please Enter Course ID: ")
        courses[id] = name
    return courses

def selectCourse(courses):
    listCourses(courses)
    course_id = input("Please Enter Course ID From Course List: ")
    return course_id

def inputMark(course_id, students):
    print("Please Enter Marks Of The Course {course_id} For Students: ")
    for id in students:
        mark = float(input(f"- Students {students[id]['name']}:"))
        students[id]["marks"][course_id] = mark

def listCourses(courses):
    print("\nAll Courses List")
    for id in courses:
        print(f"{id: <10} {courses[id]: <20}")

def listStudents(students):
    print("\n All Students List")
    for id in students:
        print(f"{id: <10} {students[id]['name']: <20} {students[id]['dob']: <15}")

def showMark(course_id, students):
    print("\nAll Marks For The Course {course_id}")
    for id in students:
        print(f"{students[id]['name'] <20} {students[id]['marks']['course_id']}")


studentCount = inputStudentCount()
students = inputStudentInfo(studentCount)    
listStudents(students)

courseCount = inputCourseCount()
courses = inputCourseInfo(courseCount)
listCourses(courses)

course_id = selectCourse(courses)
inputMark(course_id, students)

course_id = selectCourse(courses)
showMark(course_id, students)
