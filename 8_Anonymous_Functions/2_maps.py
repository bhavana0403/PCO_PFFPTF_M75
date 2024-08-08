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


