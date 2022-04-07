GPA = []
class Gpa:
    def __init__(self, student_id, gpa):
        self._student_id = student_id
        self._gpa = gpa

    def get_student_id(self):
        return self._student_id
    def set_student_id(self, student_id):
        self._student_id = student_id

    def get_gpa(self):
        return self._gpa
    def set_gpa(self, gpa):
        self._gpa = gpa