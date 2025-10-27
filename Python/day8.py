
# Base class
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class from Person
class Employee(Person):
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

# Another derived class from Person
class PartTime(Person):
    def __init__(self, name: str, age: int, working_hours: float):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")

# Multiple inheritance from Employee and PartTime
class Consultant(Employee, PartTime):
    def __init__(self, name: str, age: int, employee_id: str, working_hours: float, project_name: str):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, "
              f"Working Hours: {self.working_hours}, Project Name: {self.project_name}")

# Creating objects with sample data
person = Person("Alice", 30)
employee = Employee("Bob", 40, "E123")
part_time = PartTime("Charlie", 25, 20.5)
consultant = Consultant("Diana", 35, "C456", 15.0, "AI Development")

# Displaying details
person.show_details()
employee.show_details()
part_time.show_details()
consultant.show_details()