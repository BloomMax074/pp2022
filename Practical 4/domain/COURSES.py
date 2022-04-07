COURSES = []
class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_courseid(self):
        return self._id
    def set_studentdob(self, id):
        self._id = id

    def get_coursename(self):
        return self._name
    def set_coursename(self, name):
        self._name = name

    def __str__(self):
        return f"Courses:\n - ID: {self._id}\n - Name: {self._name}"