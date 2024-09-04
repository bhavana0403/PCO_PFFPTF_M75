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

