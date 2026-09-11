class employee:
    def __init__(self, salary):
        self.__salary = salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary + (salary * 0.1)
    def get_salary(self):
        return self.__salary

e = employee(50000)
e.set_salary(60000)
print(e.get_salary())
