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

# class Demo:
#     a = 10
#     b = 20
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# class Child_Demo(Demo):
#     pass

# print(dir(Demo))
# print(dir(Child_Demo))   # same as that of dir(Demo)
#
# print(Demo.__dict__)        #  'a': 10, 'b': 20,
# print(Child_Demo.__dict__)
#
# c1 = Child_Demo(9, 8)
# print(c1.__dict__)      # {'x': 9, 'y': 8}
# print(dir(c1))      # 'a', 'b', 'x', 'y'

####################################################################################

# child and parent has unique properties

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print('Demo.apple', self.value)

    def yahoo(self):
        print('Demo.yahoo', self.value)


class Demo1(Demo):
    def google(self):
        print('Demo1.google', self.value)


# obj1 = Demo(11)
# obj2 = Demo1(22)
#
# print(dir(Demo))        # 'apple', 'yahoo'
# print(Demo.__dict__)    # apple, yahoo, __init__
#
# print(dir(Demo1))       # 'apple', 'google', 'yahoo'
# print(Demo1.__dict__)   # 'google'
#
# print(dir(obj1))        # 'apple', 'value', 'yahoo'
# print(obj1.__dict__)    # {'value': 11}
#
# print(dir(obj2))        # 'apple', 'google', 'value', 'yahoo'
# print(obj2.__dict__)    # {'value': 22}


############################################################################################

# child and parent has same properties

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print('Demo.apple', self.value)

    def yahoo(self):
        print('Demo.yahoo', self.value)


class Demo1(Demo):
    def yahoo(self):
        print('Demo1.yahoo', self.value)

# obj1 = Demo(22)
# obj2 = Demo1(33)
#
# print(dir(Demo))
# print(dir(Demo1))
#
# print(Demo.__dict__)        # apple, yahoo
# print(Demo1.__dict__)       # yahoo
#
# obj1.yahoo()                # Demo.yahoo 22
# obj2.yahoo()                # Demo1.yahoo 33
# obj2.apple()                # Demo.apple 33


########################################################################################

"""
-> Suppose you override a parent method in child class but still want to make use of it in 
   child class along with some extra functionalities we make use of constructor chaining
   or method chaining
-> Constructor Chaining
    - Here we invoke constructor method of parent class by being there in constructor of 
      child class
    - Syntax:
            super().__init__(args)
            parentclassname.__init__(self/obj, args)
-> Method Chaining
    - Here we invoke a method of parent class by being there in method of child class
    - Syntax:
            super().mname(args)
            parentclassname.mname(self/obj, args)
"""

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print('Demo.apple', self.value)

    def yahoo(self):
        print('Demo.yahoo', self.value)


class Demo1(Demo):
    def __init__(self, value, extra_value):
        # super().__init__(value)
        Demo.__init__(self, value)
        self.extra_value = extra_value

    def yahoo(self):
        print('Demo1.yahoo', self.extra_value)
        # super().yahoo()
        Demo.yahoo(self)


obj1 = Demo(11)
obj2 = Demo1(22, 33)

obj1.yahoo()        # Demo.yahoo 11
obj2.yahoo()
"""
Demo1.yahoo 33
Demo.yahoo 22
"""

# create a class of your own choice and demonstrate single level inheritance

####################################################################################

# Multi Level Inheritance
"""
-> Here, we inherit the properties from one class to another class by considering
   multiple levels
-> The last derived class will have the properties from all the previous classes
-> Syntax:
            class C1:
                SB
            class C2(C1):
                SB
            .
            .
            .
            class Cn(Cn-1):
                SB
"""

class A:
    a = 10
    b = 20

    def __init__(self, p, q):
        self.p = p
        self.q = q


class B(A):
    m = 30
    n = 40


class C(B):
    x = 100


obj1 = C(22, 33)

print(dir(C))       # a, b, m, n, x
print(dir(obj1))    # 'a', 'b', 'm', 'n', 'p', 'q', 'x'

print(C.__dict__)       #  'x': 100
print(obj1.__dict__)    # {'p': 22, 'q': 33}

#######################################################################################

class A:
    def demo(self):
        print('A')

class B(A):
    def demo(self):
        super().demo()
        print('B')

class C(B):
    def demo(self):
        print('C')
        super().demo()


# obj1 = C()
# obj1.demo()     # C A B

# create a class of your choice and demonstrate multi level inheritance

########################################################################################

# Multiple Inheritance
"""
-> Here, we inherit the properties from multiple parent class to a single child class
-> Syntax:
            class PC1:
                SB
            class PC2:
                SB
            .
            .
            class PCn:
                SB
            class CC(PC1, PC2, ........, PCn):
                SB
"""

class A:
    a = 10
    b = 20

class B:
    m = 30
    n = 40

class C:
    a = 50
    p = 60
    q = 70

class CC(A, B, C):
    x = 80
    y = 90


obj = CC()
print(dir(CC))      # 'a', 'b', 'm', 'n', 'p', 'q', 'x', 'y'
print(obj.a)        # 10

########################################################################################

class A:
    def demo(self):
        print('A')

class B:
    def demo(self):
        print('B')

class C:
    def demo(self):
        print('C')


class CC(A, B, C):
    pass

obj = CC()
obj.demo()      # A

####################################################################################
class A:
    def demo(self):
        print('A')

class B:
    def demo(self):
        print('B')

class C:
    def demo(self):
        print('C')

# class CC(A, B, C):
#     def demo(self):
#         print('CC')
#
# obj = CC()
# obj.demo()      # CC

##########################################################################################

# class CC(A, B, C):
#     def demo(self):
#         super().demo()
#         print('CC')
#
# obj = CC()
# obj.demo()
"""
A
CC
"""

class CC(A, B, C):
    def demo(self):
        print('CC')
        B.demo(self)

obj = CC()
obj.demo()
"""
CC
B
"""

# Method Resolution Order
print(CC.__mro__)   # CC -> A -> B -> C -> object class

"""
Create a class called Calculator by inheriting from ADD, SUB, MUL and DIV classes
which has add, sub, mul and div methods respecitively. All the methods are static
add -> int, float, complex, bool, str, list, tuple, set, dict
sub -> int, float, complex
mul -> int, float, complex
div -> int 
"""

##########################################################################################

# 4) Hierarchical Inheritance
"""
-> Here we derive the properties from one parent class to multiple child classes
-> Syntax:
            class PC:
                SB
            class CC1(PC):
                SB
            class CC2(PC):
                SB
            .
            .
            class CCn(PC):
                SB
"""

class A:
    a1 = 10
    a2 = 20

class B(A):
    b1 = 30
    b2 = 40

class C(A):
    c1 = 50
    c2 = 60


print(dir(B))       # 'a1', 'a2', 'b1', 'b2'
print(dir(C))       # 'a1', 'a2', 'c1', 'c2'

print(B.__dict__)   # 'b1': 30, 'b2': 40,
print(C.__dict__)   # 'c1': 50, 'c2': 60


#####################################################################################

class Parent:
    def spam(self):
        print('Parent.spam')


class Child1(Parent):
    def spam(self):
        super().spam()
        print('Child1.spam')


class Child2(Parent):
    def spam(self):
        print('Child2.spam')
        super().spam()


obj1 = Child1()
obj2 = Child2()

obj1.spam()
"""
Parent.spam
Child1.spam
"""

obj2.spam()
"""
Child2.spam
Parent.spam
"""

#########################################################################################

# 5) Hybrid Inheritance
"""
-> Combination of more than one type of inheritance
"""





