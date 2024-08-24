# # store the value 10 and 20
# a = 10      # instance of integer
# b = 20      # instance of integer
#
# nums = [10, 20]
# t = (10, 20)
# s = {10, 20}
# d = {'a': 10, 'b': 20}
# """
# -> dictionary is the best method to store the value as we can access them using keys
# """
#
# st1 = ['Mary', 9191919191, "Bengaluru", "8th standard", "A Grade"]
# st2 = ['Mary Joseph', 9191919192, "Bengaluru", "8th standard", "C Grade"]
#
# st1 = {'name': "Mary",
#        'palce': "Bengaluru",
#        'ph_no': 9191919191,
#        'class': "8th standard",
#        "grade": "A grade"}
#
#
# # access the values
# print(nums[0], nums[1])
# print(t[0], t[1])
# # print(s[0]) # TypeError
#
# # modify the values
# nums[0] = 100
# print(nums)   #
#
# # t[0] = 100    # TypeError
#
# # adding the values
#
# nums.append(18)
# # t.append(87)         # AttributeError
#
# # s.append(87)         # AttributeError
#
# s.add(87)
#
# # concatenation
# print([10, 20] + [30, 40])         # [10, 20, 30, 40]
# print((1, 2) + (3, 4, 5))          # (1, 2, 3, 4, 5)
# # print({1, 2} + {3, 4})             # TypeError
# print(18 + 86)                     # 104


# print(dir(list))
# # print(dir(nums))
# print(dir(tuple))
# print(dir(set))
# print(dir(str))
# print(dir(int))
# print(dir(dict))
# print(dir(complex))

"""
Class
-> Class is a container which has all the functionalities that can be performed on 
   an object created for the class
-> Class is a blueprint which has the properties and functionalities of a real time entity
-> Class is a collection of functions which carry out various operations on instances

Object
-> Instance of class (memory reference)
-> It is a variable created for particular class
"""

# nums = [10, 20]
# nums.append(30)
# # list.append(80)             # TypeError
#
# list.append(nums, 87)
# print(nums)          # [10, 20, 30, 87]

# nums.swap()          # AttributeError

# nums.reset()         # AttributeError

########################################################################################

# User Defined Class
"""
-> Syntax:
        class cname:
            properties/ functionality
        obj = cname(args)
"""


# class Point:
#     """class variables"""
#     x = 4
#     y = 5
#
#
# print(Point)        # <class '__main__.Point'>
# # print(Point())      # <__main__.Point object at 0x00000181B9D9FFD0>
#
# p1 = Point()
# p2 = Point()
#
# print(p1)       # <__main__.Point object at 0x000002C33B334090>
# print(p2)       # <__main__.Point object at 0x000001DD46764050>
#
# print(dir(Point))   # few methods will be derived from object class to user defined class by default
# print(Point.__dict__)   # 'x': 4, 'y': 5
#
# print(dir(p1))      # same as that of Point
# print(p1.__dict__)  # {}
#
# print(dir(p2))
# print(p2.__dict__)  # {}
#
# # accessing the values
# print(Point.x)      # 4
# print(Point.y)      # 5
# print(p1.x)         # 4
# print(p2.y)         # 5

# modify the value wrt class
"""
modification wrt class will change the values of class as well as object created for
the class
"""
# Point.x = 100
# print(Point.x)      # 100
# print(p1.x)         # 100
# print(p2.x)         # 100

# modify the value wrt object
"""
modification wrt object will change only that object and not class or other objects 
created for the same class
"""

# print(p1.__dict__)      # {}
# print(p2.__dict__)      # {}
#
# p1.x = 11
# p2.y = 12
#
# print(p1.__dict__)          # {'x': 11}
# print(p2.__dict__)          # {'y': 12}
# print(Point.__dict__)       # 'x': 100, 'y': 5
#
# p3 = Point()
# print(p3.__dict__)          # {}
# print(p3.x, p3.y)           # 100 5

##################################################################################
"""
Generic Members or Class Members
-> These are the members which are common for each and every object created for 
   the class
-> These members are created inside the class
-> Class Variables

Specific Members or Object Members
-> These members will be different for different objects
"""


class Company:
    Comp_name = "ABC"
    Comp_loc = "Bengaluru"
    Comp_CEO = "Mr.Ram"


emp1 = Company()
emp2 = Company()

print(Company)      # <class '__main__.Company'>
print(emp1)         # <__main__.Company object at 0x000002409BDC4110>
print(emp2)         # <__main__.Company object at 0x000002409BDC4150>

print(dir(Company))
print(dir(emp1))
print(dir(emp2))

print(Company.__dict__)     # 'Comp_name': 'ABC', 'Comp_loc': 'Bengaluru', 'Comp_CEO': 'Mr.Ram'
print(emp1.__dict__)        # {}
print(emp2.__dict__)        # {}

emp1.emp_name = "John"
emp1.emp_id = "ABC123"
emp1.emp_salary = 30000

emp2.emp_name = "Mary"
emp2.emp_id = "ABC124"
emp2.emp_salary = 40000

print(dir(Company))
print(dir(emp1))
print(dir(emp2))

print(Company.__dict__)
print(emp1.__dict__)        # {'emp_name': 'John', 'emp_id': 'ABC123', 'emp_salary': 30000}
print(emp2.__dict__)        # {'emp_name': 'Mary', 'emp_id': 'ABC124', 'emp_salary': 40000}


