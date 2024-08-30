"""
There are 4 pillars of Object Oriented Programming
1) Inheritance
2) Encapsulation
3) Polymorphism
4) Abstraction
"""

"""
Inheritance
-> here, we derive the properties from one class to another class
-> Inheritance is a mechanism for creating a new class that specifies or modifies the 
   behavior of existing class
-> Class from which we inherit the properties is called parent class/ base class/
   super class
-> Class to which we inherit the properties is called child class/ sub class/ derived
   class/ subtype
-> Child class will inherit the properties from parent class. We can modify some of the 
   properties or completely redefine
-> There are 5 types
    1) Single Level Inheritance
    2) Multi Level Inheritance
    3) Multiple Inheritance
    4) Hierarchical Inheritance
    5) Hybrid Inheritance 
"""


"""
Single Level Inheritance
-> Here we derive the properties from parent class to child class by considering only
   one level
-> Every class is a kind of single level inheritance because when ever we create a new 
   class, some of the methods will be derived by default from object class
-> Syntax:
        class PC:
            SB
        class CC(PC):
            SB
"""


# class A:
#     pass
#
# print(dir(A))

class Demo:
    a = 10
    b = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Child_Demo(Demo):
    pass

print(dir(Demo))
print(dir(Child_Demo))   # same as that of dir(Demo)

print(Demo.__dict__)        #  'a': 10, 'b': 20,
print(Child_Demo.__dict__)

c1 = Child_Demo(9, 8)
print(c1.__dict__)      # {'x': 9, 'y': 8}
print(dir(c1))      # 'a', 'b', 'x', 'y'


