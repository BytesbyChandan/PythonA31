class grandparent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from grandparent {self.name}!"
class parent(grandparent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        return f"Hello from parent {self.name}, age {self.age}!"    
class child(parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def greet(self):
        return f"Hello from child {self.name}, age {self.age}, attending {self.school}!"
c = child("Alice", 10, "Greenwood Elementary")
print(c.greet())