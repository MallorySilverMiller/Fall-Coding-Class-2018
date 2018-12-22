# 2.3 ACTIVITY #1 + #2
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        print("One car is a {} {}".format(car_a.color, car_a.name))
        print("The other car is a {} {}".format(car_b.color, car_b.name))


car_a = Car("Odyssey", "red")
car_b = Car("Escape", "forest green")
# #1
print("One car is a {} {}".format(car_a.color, car_a.name))
print("The other car is a {} {}".format(car_b.color, car_b.name))
# #2
car_a.display()
car_b.display()
# 2.3 ACTIVITY #3


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * 3.14

    def perimeter(self):
        return 2 * 3.14 * self.radius


circle_a = Circle(8)
print(circle_a.area())
print(circle_a.perimeter())


# ADDITIONAL PRACTICE
class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def dis_employee(self):
        print("Name:", self.name, "\n Salary: $" + str(self.salary))

    @classmethod
    def dis_count(cls):
        print("Number of Employees:", Employee.emp_count)


# MORE ADVANCED PRACTICE
emp1 = Employee("Willow", 10)
emp1.dis_employee()
emp2 = Employee("Bella", 10)
emp2.dis_employee()
Employee.dis_count()
