class shape:
    def area(self):
        print("Calculating area of shape")
class rectangle(shape):
    def area(self,x,y): 
        print("Area of rectangle:", x*y)
class square(shape):
    def area(self,x): 
        print("Area of square:", x*x)

s = square()
s.area(5)
r = rectangle()
r.area(4,6)