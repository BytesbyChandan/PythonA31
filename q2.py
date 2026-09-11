class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class teacher(person):
    def __init__(self, subject, name, age):
        super().__init__(name, age)
        self.subject = subject
    def display(self):
        super().display()
        print("Subject:", self.subject)
t = teacher("Mathematics", "Alice", 30)
t.display()