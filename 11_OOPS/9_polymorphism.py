# function overloading

# def add(a, b):
#     print(a + b)
#
#
# def add(a, b, c):
#     print(a + b + c)

# add(1, 2)   # TypeError: add() missing 1 required positional argument: 'c'
# add(1, 2, 3)    # 6

"""
-> In python if we try to overload a function, over-riding happens
-> We can achieve overloading by passing default values to parameters
"""

def add(a=0, b=0, c=0):
    print(a + b + c)


# add()
# add(10)
# add(10, 20)
# add(10, 20, 30)
# add(c=90)
# add(b=30, a=34)

###################################################################################

# operator overloading
"""
+ -> add, concatenation
* -> multiply, power, packing, unpacking
"""

# + -> __add__ gets called

print(dir(list))
print(dir(set))

a = 10
b = 87
print(a + b)
print(a.__add__(b))
print('abcd' + 'efgh')
print('abcd'.__add__('efgh'))


# - -> __sub__

print(a.__sub__(b))
print(a - b)

# magic methods

"""
ob1 + ob2           ob1.__add__(ob2)
ob1 - ob2           ob1.__sub__(ob2)
ob1 * ob2           ob1.__mul__(ob2)
ob1 / ob2           ob1.__truediv__(ob2)
ob1 // ob2          ob1.__floordiv__(ob2)
ob1 % ob2           ob1.__mod__(ob2)
ob1 < ob2           ob1.__lt__(ob2)
ob1 > ob2           ob1.__gt__(ob2)
ob1 <= ob2          ob1.__le__(ob2)
ob1 >= ob2          ob1.__ge__(ob2)
ob1 == ob2          ob1.__eq__(ob2)
ob1 != ob2          ob1.__ne__(ob2) 
"""

class Point:
    def __init__(self, a):
        self.a = a


p1 = Point(3)
p2 = Point(5)
# print(p1 + p2)      # TypeError

print(dir(Point))
"""
-> We can make any operator work for a user defined datatype by implementing
   magic methods
"""
