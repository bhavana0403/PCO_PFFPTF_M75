# list method

# 1) append
"""
-> It is used to add the value to the last position of the list
-> Syntax:
            Var.append(Val)
-> The return type of append is None
-> append will modify the original list
"""

# l = [1, 2, 'hai', 8+7j]
# print(id(l))    # 2297409785344
# print(l.append(10))     # None
# print(l)    # [1, 2, 'hai', (8+7j), 10]
# print(id(l))    # 2297409785344

###############################################################################

# 2) insert
"""
-> It is used to add a value to specified index position
-> Syntax:
            Var.insert(index, value)
-> The return type of insert is None
"""

# l = [1, 2, 'hai', 8+7j]
# print(l.insert(1, 99))      # NOne
# print(l)        # [1, 99, 2, 'hai', (8+7j)]

# print(l.insert(2, 22))      # NOne
# print(l)        # [1, 2, 22, 'hai', (8+7j)]

# l.insert(-1, 234)       # l.insert(3, 234)
# print(l[-1])        # (8+7j)
# print(l)        # [1, 2, 'hai', 234, (8+7j)]

# print(l[-2])        # l[2]
# print(l[-4])        # l[0]

# l.insert(-2, 88)    # l.insert(2, 88)
# print(l[-2])    # hai
# print(l)        # [1, 2, 88, 'hai', (8+7j)]
# print(l[2])     # 88

# l = [1, 2, 'hai', 8+7j]
# l.insert(3, 'hello')
# print(l)    # [1, 2, 'hai', 'hello', (8+7j)]

# l.insert(4, 12)
# print(l)        # [1, 2, 'hai', (8+7j), 12]

# l.insert(10, 100)
# print(l)        # [1, 2, 'hai', (8+7j), 100]

################################################################################

# 3) extend
"""
-> It is used to extend the list by the values of iterable
-> Syntax:
            Var.extend(iterable)
-> The return type of extend is None
-> It will add the values of iterable to the last 
"""

l = [1, 2, 'hai', 8+7j]
# print(l.extend('abc'))      # None
# print(l)        # [1, 2, 'hai', (8+7j), 'a', 'b', 'c']

# l.extend(123)   # TypeError

# l.extend([10, 20, 30])
# print(l)    # [1, 2, 'hai', (8+7j), 10, 20, 30]

# l.extend("123")
# print(l)    # [1, 2, 'hai', (8+7j), '1', '2', '3']

# l.extend([123])
# print(l)    # [1, 2, 'hai', (8+7j), 123]

####################################################################################

