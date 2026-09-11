class student:
    def __init__(self, marks):
        self.__marks = marks
    def assign_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
    def display_marks(self):
        return self.__marks

s = student(85)
print(s.display_marks())
print(s.assign_marks(90))
print(s.display_marks())