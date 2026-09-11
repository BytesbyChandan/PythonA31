class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class employee:
    def __init__(self, name, age, employee_id):
        person.__init__(self, name, age)
        self.employee_id = employee_id
    def display(self):
        person.display(self)
        print(f"Employee ID: {self.employee_id}")
class manager(person, employee):
    def __init__(self, name, age, employee_id, department):
        person.__init__(self, name, age)
        employee.__init__(self, name, age, employee_id)
        self.department = department
    def display(self):
        person.display(self)
        employee.display(self)
        print(f"Department: {self.department}")

manager1 = manager("Alice", 35, "E123", "HR")
manager1.display()