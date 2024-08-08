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




