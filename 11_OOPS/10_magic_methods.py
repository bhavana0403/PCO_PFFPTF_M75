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


# p1 = Point(3, 4)
# p2 = Point(6, 9)
# print(p1 + p2)

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

# create a class of your choice and implement comparison protocol

###################################################################################

# 3) container protocol

# st = 'hello'
# print(len(st))
# print(st.__len__())
#
# print('e' in st)
# print(st.__contains__('e'))
#
# print(st[1])
# print(st.__getitem__(1))
#
# d = {'a': 1, 'b': 2}
# print(d['a'])
# print(d.__getitem__('a'))
#
# li = [1, 2, 3]
# li[1] = 10
# print(li)
#
# li.__setitem__(2, 30)
# print(li)       # [1, 10, 30]
#
# del li[0]
# print(li)       # [10, 30]
#
# li.__delitem__(0)
# print(li)       # [30]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        # return 2
        return len(self.__dict__)

    def __getitem__(self, item):
        if item in [0, 'x']:
            return self.x
        elif item in [1, 'y']:
            return self.y
        else:
            raise Exception (f"Value of {item} does not exist")

    def __setitem__(self, key, value):
        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        else:
            raise Exception

    def __delitem__(self, key):
        if key == 'x':
            del self.x
        elif key == 'y':
            del self.y
        else:
            raise KeyError


# p1 = Point(8, 3)
# print(len(p1))
#
# print(p1[0])
# # print(p1[9])
# print(p1.__dict__)
# print(p1['x'], p1['y'])
# # print(p1['z'])
#
# p1['x'] = 88
# print(p1.__dict__)
#
# del p1['x']
# print(p1.__dict__)
#
# print(len(p1))

###############################################################################

# 4) Attribute Protocol
"""
__getattribute__
__getattr__
__setattr__
__delattr__
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        # return self.item
        return "In get attribute"


# p1 = Point(2, 8)
# print(dir(p1))
# print(p1.x)
# print(p1.spam)

###############################################################################

# point class should not take any negative values

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if value < 0:
            raise ValueError ("Value can not be less than 0")
        super().__setattr__(key, value)



# p1 = Point(-9, 10)
p2 = Point(10, 20)
# p2.y = -5

###################################################################################

# create a class called employee with 3 object members and make them inaccessible

class Employee:
    def __init__(self, name, empid, salary):
        self.name = name
        self.empid = empid
        self.salary = salary

    def __getattribute__(self, item):
        raise Exception ("Can not access the attributes")

emp1 = Employee("John", "ABC123", 60000)
# print(emp1.name)

###############################################################################

# create a class your own choice and make it immutable

class Employee:
    def __init__(self, name, empid, salary):
        self.name = name
        self.empid = empid
        self.salary = salary

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ValueError ("VAlues can not be modified")
        super().__setattr__(key, value)


# emp1 = Employee("JOhn", "ABC1213", 80000)
# print(emp1.__dict__)
# emp1.phno = 9191919191
# print(emp1.__dict__)
# # emp1.phno = 9292929292      # ValueError: VAlues can not be modified
"""
In this example user will be able to add new object members but not can not modify
the existing ones
"""

#################################################################################

# class should not be able to add a new value or modify existinmg value

class Employee:
    def __init__(self, name, empid, salary):
        # self.name = name
        # self.empid = empid
        # self.salary = salary
        super().__setattr__("name", name)
        super().__setattr__("empid", empid)
        super().__setattr__("salary", salary)

    def __setattr__(self, key, value):
        raise ValueError ("Values can not be modified")


emp1 = Employee("JOhn", "ABC1213", 80000)
# emp1.phno = 9191919191      # ValueError: Values can not be modified


#################################################################################

class Point:
    def __init__(self, x):
        self.x = x

    # def __getattribute__(self, item):
    #     return "In get attribute"

    def __getattr__(self, item):
        return "In get attr"

a = Point(9)
print(a.x)
print(a.spam)

"""
-> __getattr__ will be called only if the attribute is not present in the class 
  and if __getattribute__ is not explicitly mentioned
"""

