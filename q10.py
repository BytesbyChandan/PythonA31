class shape:
    def __init__(self, color):
        self.color = color
class circle(shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
c = circle(5, "red")
print("Color:", c.color)
print("Area:", c.area())