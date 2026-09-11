class mobile:
    def __init__(self, price):
        self.__price = price
    def set_price(self, price):
        if price >= 0:
            self.__price = price
    def get_price(self):
        return self.__price

m = mobile(1000)
m.set_price(1200)
print(m.get_price())