class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}, Price: ${self.price:.2f}")
class electronic(product):
    def __init__(self, warranty_years, name, price):
        super().__init__(name, price)
        self.warranty_years = warranty_years   

    def display(self):
        super().display()
        print(f"Warranty Period: {self.warranty_years} years")
ele = electronic(2, "Laptop", 999.99)
ele.display()