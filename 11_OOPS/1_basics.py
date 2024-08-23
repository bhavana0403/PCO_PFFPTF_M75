# store the value 10 and 20
a = 10      # instance of integer
b = 20      # instance of integer

nums = [10, 20]
t = (10, 20)
s = {10, 20}
d = {'a': 10, 'b': 20}
"""
-> dictionary is the best method to store the value as we can access them using keys
"""

st1 = ['Mary', 9191919191, "Bengaluru", "8th standard", "A Grade"]
st2 = ['Mary Joseph', 9191919192, "Bengaluru", "8th standard", "C Grade"]

st1 = {'name': "Mary",
       'palce': "Bengaluru",
       'ph_no': 9191919191,
       'class': "8th standard",
       "grade": "A grade"}


# access the values
print(nums[0], nums[1])
print(t[0], t[1])
# print(s[0]) # TypeError

# modify the values
nums[0] = 100
print(nums)   #

# t[0] = 100    # TypeError

# adding the values

nums.append(18)
# t.append(87)         # AttributeError

# s.append(87)         # AttributeError

s.add(87)

# concatenation
print([10, 20] + [30, 40])         # [10, 20, 30, 40]
print((1, 2) + (3, 4, 5))          # (1, 2, 3, 4, 5)
# print({1, 2} + {3, 4})             # TypeError
print(18 + 86)                     # 104


print(dir(list))
print(dir(nums))
print(dir(tuple))
print(dir(set))
print(dir(str))
print(dir(int))
print(dir(dict))
print(dir(complex))

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

nums = [10, 20]
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

"""