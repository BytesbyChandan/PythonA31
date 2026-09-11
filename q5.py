class calculator1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
class calculator2:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def multiply(self):
        return self.a * self.b
class hybrid_calculator(calculator1, calculator2):
    def __init__(self, a, b):
        calculator1.__init__(self, a, b)
        calculator2.__init__(self, a, b)

hy = hybrid_calculator(5, 10)
print("Addition:", hy.add())
print("Multiplication:", hy.multiply())