class Aappliances:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
    def display(self):
        print("Brand:", self.brand)
        print("Power:", self.power)
class washingmachine(Aappliances):
    def __init__(self, capacity, brand, power):
        super().__init__(brand, power)
        self.capacity = capacity
    def display(self):
        super().display()
        print("Capacity:", self.capacity)
w = washingmachine("7kg", "LG", 2000)
w.display()