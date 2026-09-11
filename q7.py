class A:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")
class B:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

class C(A, B):
    def __init__(self, value):
        A.__init__(self, value)
        B.__init__(self, value)

    def display(self):
        A.display(self)
        B.display(self)

c = C(10)
c.display()