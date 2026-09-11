class votingsystem:
    def __init__(self, age):
        self.__age = age
    def set_age(self, age):
        if age >= 18:
            self.__age = age

    def get_age(self):
        return self.__age
v = votingsystem(20)
print(v.get_age())
