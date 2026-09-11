class employee:
    def __int__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary
    def display(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
class manager(employee):
    def __init__(self, department, emp_id, salary):
        super().__init__(emp_id, salary)
        self.department = department
    def display(self):
        super().display()
        print("Department:", self.department)
manager = manager("Sales", 101, 50000)
manager.display()