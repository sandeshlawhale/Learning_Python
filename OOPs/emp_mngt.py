class Employee:
    employee_count = 0

    def __init__(self, name, emp_id, salary, dept="General"):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = dept
        Employee.employee_count += 1

    def give_raise(self, amt):
        self.salary += amt

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.department} {self.salary}"

    @classmethod
    def from_string(cls, employee_string):
        name, emp_id, salary, dept = employee_string.split(",")
        return cls(name, emp_id, salary, dept)


employee1 = Employee("John", 101, 50000, "Engineering")
employee2 = Employee("Sarah", 102, 60000)
employee3 = Employee.from_string("Jane,103,55000,Developer")

employee1.give_raise(5000)

print(employee3)

print(Employee.employee_count)
