class product:
    def __init__(self, quantity):
        self.__quantity = quantity
    def add_stock(self, quantity):
        if quantity >= 0:
            self.__quantity += quantity
    def reduce_stock(self, quantity):
        if 0 <= quantity <= self.__quantity:
            self.__quantity -= quantity
    def check_quantity(self):
        return self.__quantity

p = product(100)
p.add_stock(50)
print(p.check_quantity())  # Output: 150
