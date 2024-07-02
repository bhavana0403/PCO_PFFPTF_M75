# List(list)
"""
-> It is a collection of homogenous or heterogeneous data-items enclosed between []
-> Syntax:
            Var = [Val1, Val2, .........., Valn]
            where, the values are separated by comma operator
-> LIst will allow the user to modify the values
-> List is a mutable collection
-> The default value of list is []
"""

nums = [10, 20, 30, 40, 50]
vals = [87, 9+8j, 'hai', [8, 88]]

print(nums[2])      # 30

print(vals[1])      # (9+8j)

print(vals[2][1])   # a
print('hai'[1])     # a

print(vals[3][1])       # 88

print(id(nums))
nums[2] = 33
print(nums)     # [10, 20, 33, 40, 50]
print(id(nums))

li = []
print(type(li))     # <class 'list'>
print(bool(li))     # False

li = [386, [3, 8, 6], '386', '[3, 8, 6]']
print(len(li[3]))       #

nums = [1, 2, [3, 4, [5, 6]]]

nums = [[[[1]]]]
print(nums[0][0][0][0])


