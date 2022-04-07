STUDENTS = []
class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def get_studentid(self):
        return self._id
    def set_studentid(self, id):
        self._id = id

    def get_studentname(self):
        return self._name
    def set_studentname(self, name):
        self._name = name

    def get_studentdob(self):
        return self._dob
    def set_studentdob(self, dob):
        self._dob = dob

    def __str__(self):
        return f"Students:\n - ID: {self._id}\n - Name: {self._name}\n - DOB:{self._dob}"