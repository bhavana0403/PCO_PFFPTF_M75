# 1) Number Protocol
"""add, sub, mul, div"""

class Point:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        # return self.a + other.a
        # return "Hello"
        return self.a * other.a

    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a
        # raise ValueError


# p1 = Point(10)
# p2 = Point(34)
# print(p1 + p2)
# print(p1 - p2)
# print(p1 * p2)

###################################################################################

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        # return self.a + self.b + other.a + other.b      # 22
        # return self.a + other.a, self.b + other.b           # (9, 13)
        return self.a + other.a         # 9


p1 = Point(3, 4)
p2 = Point(6, 9)
print(p1 + p2)

# for the above class implement all the number protocols (sub, mul, truediv, floordiv, mod, pow)

################################################################################

# 2) comparison protocol
""" ==, !=, <, >, <=, >= """

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        # return self.x > other.x and self.y > other.y
        # return self.x > other.x or self.y > other.y
        # return self.x > other.x
        return self.x + self.y > other.x + other.y

    def __eq__(self, other):
        return self.x == other.x


# p1 = Point(3, 9)
# p2 = Point(10, 5)
# p3 = Point(100, 200)
# print(p1 < p2)
# print(p1 < p3)      # p3.__gt__(p1)
#
# p4 = Point(10, 80)
# print(p2 == p4)
# print(p2 != p4)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __eq__(self, other):
        # return self.age == other.age
        # return self.salary == other.salary
        return self.age == other.age and self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary


# e1 = Employee("John", 24, 40000)
# e2 = Employee("Mary", 24, 56000)
# e3 = Employee("Abhi", 40, 56000)
# e4 = Employee("Ram", 40, 56000)
#
# print(e1 == e2)
# print(e3 == e4)
#
# print(e1 < e3)

###################################################################################

# 3) container protocol
