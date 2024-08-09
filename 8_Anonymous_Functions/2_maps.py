# map

square = lambda num: num**2

nums = [1, 2, 3, 4]
res = []
for i in nums:
    res.append(square(i))
print(res)      # [1, 4, 9, 16]
"""
-> Syntax:
            map_object = map(func, iterable)
-> Each value from the iterable will be given as input to function, the return from 
   the function will be store in map object
-> Since map object doesn't have a proper structure to display the output we have to 
   typecast the map object
"""

_res = map(square, nums)    # 1 4 9 16
print(_res)     # <map object at 0x000001EE0FF793F0>
print(type(_res))   # <class 'map'>
print(list(_res))   # [1, 4, 9, 16]

_res2 = map(lambda num: num**2, nums)
print(list(_res2))      # [1, 4, 9, 16]

print(list(map(lambda num: num**2, nums)))      # [1, 4, 9, 16]

# square and cube of numbers from 1 to 5
sq_cube = lambda num: (num**2, num**3)
res1 = map(sq_cube, range(1, 6))
print(list(res1))       # [(1, 1), (4, 8), (9, 27), (16, 64), (25, 125)]

res2 = map(lambda num: (num**2, num**3), range(1, 6))
print(list(res2))    # [(1, 1), (4, 8), (9, 27), (16, 64), (25, 125)]

# check if names are palindrome
names = ['steve', 'eve', 'alex', 'gagan', 'bob']
check = lambda name: name == name[::-1]
res = map(check, names)
print(list(res))    # [False, True, False, False, True]

######################################################################################
l1 = ['a', 'b', 'c', 'd']
l2 = [1, 2, 3, 4]
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

a = lambda item1, item2: (item1, item2)
print(a(1, 2))  # (1, 2)

res = map(lambda item1, item2: (item1, item2), l1, l2)
print(list(res))    # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

l1 = ['a', 'b']
l2 = [1, 2, 3, 4]
res = map(lambda item1, item2: (item1, item2), l1, l2)
print(list(res))    # [('a', 1), ('b', 2)]

# WAP to create a list of factorial of numbers from 1 to 10

from math import factorial
_res = map(factorial, range(1, 11))
print(list(_res))       # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# WAP to get the following output
li = ['good', 'evening', 'all']
# o/p1 = [4, 5, 3]
# o/p2 = ['GOOD', 'EVENING', 'ALL']
res1 = map(len, li)
print(list(res1))       # [4, 7, 3]

res2 = map(str.upper, li)
print(list(res2))       # ['GOOD', 'EVENING', 'ALL']
"""
Whenever we want to use method inside map we write the method as 
        map(cls.mname, iterable)
"""

nums = [-7, 76, -377, -78, 23, -54, -6, -3]
# o/p = [7, 76, 377, 78, 23, 54, 6, 3]

res = map(abs, nums)
print(list(res))        # [7, 76, 377, 78, 23, 54, 6, 3]







