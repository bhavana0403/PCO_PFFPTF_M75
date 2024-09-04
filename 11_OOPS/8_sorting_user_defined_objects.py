class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


e1 = Employee("John", 24, 40000)
e2 = Employee("Mary", 21, 56000)
e3 = Employee("Abhi", 40, 30000)
e4 = Employee("George", 44, 44000)
e5 = Employee("Krishna", 37, 80000)

employees = [e1, e2, e3, e4, e5]
print(employees)

# sort based on names
by_names = sorted(employees, key=lambda item: item.name)
for emp in by_names:
    print(emp.name)

# sort based on age
by_age = sorted(employees, key=lambda item: item.age)
for emp in by_age:
    print(emp.name, emp.age)

# sort based on salary
by_salary = sorted(employees, key=lambda item: item.salary)
for emp in by_salary:
    print(emp.name, emp.salary)

####################################################################################

class Employee:
    employees = []
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.employees.append(self)


e1 = Employee("John", 24, 40000)
e2 = Employee("Mary", 21, 56000)
e3 = Employee("Abhi", 40, 30000)
e4 = Employee("George", 44, 44000)
e5 = Employee("Krishna", 37, 80000)

employees = Employee.employees      # the value of class variable employees is stored in global variable employees

# sort based on names
by_names = sorted(employees, key=lambda item: item.name)
for emp in by_names:
    print(emp.name)

# sort based on age
by_age = sorted(employees, key=lambda item: item.age)
for emp in by_age:
    print(emp.name, emp.age)

# sort based on salary
by_salary = sorted(employees, key=lambda item: item.salary)
for emp in by_salary:
    print(emp.name, emp.salary)


####################################################################################

class BankAccount:
    details = []

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
        BankAccount.details.append(self)


# create 5 objects and sort them based on name, age and balance

###################################################################################

