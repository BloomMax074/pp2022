


def inputStudentCount():
    return int(input("Please enter number of students:"))
    

def inputStudentInfo():
    students = []
    for s in range(studentCount):
        print(f"Please enter {s + 1} students info:")
        id = input("- ID: ")
        name = input("- Name: ")
        birthday = input("- DOB: ")
        students.append ({
            "Name": name,
            "ID": id,
            "DOB": birthday,
        })
    print(f"Finished Entered {studentCount} students")
    return students
    

def inputCourseCount():
    return int(input("Please enter number of courses:"))
    

def inputCourseInfo():
    courses = []
    for c in range(studentCount):
        print(f"Please enter course {c + 1} info:")
        name = input("- Name: ")
        id = input("- ID: ")
        courses.append({
            "Name": name,
            "ID": id,
        })
    print(f"Finished Entered {courseCount} courses")
    return courses


def inputStudentMarkForCourses():
    marks = []
    for m in range(studentCount):
        print(f"Please enter mark for {m + 1} course:")
        mark = input("- Mark: ")
        marks.append({
            "Mark": mark,
        })
    print(f"Finished Entered {marks} marks")
    return marks

def listStudents(students):
    print(f"Listing {len(students)} students")
    for student in students:
        print(f"- ID: {student['ID']}, Name: {student['Name']}, DOB: {student['DOB']}")
    pass

def listCourses(courses):
    print(f"Listing {len(courses)} courses")
    for course in courses:
        print(f"- ID: {course['ID']}, Name: {course['Name']}")

def showMarks(marks):
    print(f"Listing {len(marks)} marks")
    for mark in marks:
        print(f"- Mark: {marks[mark]}")
    pass

studentCount = inputStudentCount()
students = inputStudentInfo()
listStudents(students)

courseCount = inputCourseCount()
courses = inputCourseInfo()
listCourses(courses)

StudentMarkForCourses = inputStudentMarkForCourses()
showMarks(marks)
