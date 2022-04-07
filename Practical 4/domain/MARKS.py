MARKS = []
class Mark:
    def __init__(self, student_id, mark):
        self._student_id = student_id
        self._mark = mark

    def get_student_id(self):
        return self._student_id
    def set_student_id(self, student_id):
        self._student_id = student_id

    def get_mark(self):
        return self._mark
    def set_mark(self, mark):
        self._mark = mark