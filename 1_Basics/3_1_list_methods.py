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

# 4) pop
"""
-> It is used to remove the value from the list
-> Syntax:
            Var.pop()   # removes the last values
            Var.pop(index_no)   # removes the value present at specified index position
-> pop will return the value which has been removed
-> If the index is not present pop will throw IndexError
"""

# l = [1, 2, 'hai', (8+7j), 10, 20, 30]
# print(l.pop())      # 30
# print(l)        # [1, 2, 'hai', (8+7j), 10, 20]
#
# print(l.pop())  # 20
# print(l)        # [1, 2, 'hai', (8+7j), 10]
#
# print(l.pop(2))     # hai
# print(l)        # [1, 2, (8+7j), 10]

# print(l.pop(8))     # IndexError

#################################################################################

# 5) remove
"""
-> It is used to remove the specified element from the list
-> Syntax:
            Var.remove(Val)
-> The return type of remove is None
-> If the value is not present remove will throw ValueError
-> If there are multivalues, the first value from left to right of the collection 
   will be removed 
"""

# l = [1, 2, 'hai', (8+7j), 'a', 'b', 'c']
# print(l.remove(2))      # None
# print(l)        # [1, 'hai', (8+7j), 'a', 'b', 'c']
#
# l.remove('hai')
# print(l)        # [1, (8+7j), 'a', 'b', 'c']

# l.remove('hai')     # ValueError: list.remove(x): x not in list

# l = [1, 2, 10, 20, 1, 3, 2]
# l.remove(1)
# print(l)    # [2, 10, 20, 1, 3, 2]
#
# l.remove(1)
# print(l)    # [2, 10, 20, 3, 2]

##################################################################################

# 6) clear
"""
-> It is used to remove all the values from the list
-> Syntax:
            Var.clear()
-> The return type of clear is None
"""

# l = [1, (8+7j), 'a', 'b', 'c']
# print(l.clear())    # None
# print(l)    # []

################################################################################

# 7) index

################################################################################

# 8) count
"""
-> It is used to count the number of occurrences of a given value in the list
-> Syntax:
            Var.count(Val)
-> The return type of count is an integer
-> If the value is not present count will return 0
"""

# l = ['a', 10, 'b', 65, 10, 10, 65, 'b', 'c', 'b', 'b']
# print(l.count('b'))     # 4
#
# print(l.count(10))  # 3
#
# print(l.count(65))      # 2
#
# print(l.count('hai'))   # 0

###############################################################################

# 9) reverse
"""
-> It is used to reverse the values of the list
-> Syntax:
            Var.reverse()
-> the return type of reverse is None
"""

# l = [1, 'python', (9+7j), [1, 2, 3]]
# print(l.reverse())      # None
# print(l)        # [[1, 2, 3], (9+7j), 'python', 1]

##################################################################################

# 10) sort
"""
-> It is used to sort the given list
-> Syntax:
            Var.sort()      # sort the values in ascending order
            Var.sort(reverse=True)  # sort the values in descending order
-> The return type of sort is None
"""

l = [8, 5, 10, 3, 45, 13, 97, 38]
# print(l.sort())     # None
# print(l)            # [3, 5, 8, 10, 13, 38, 45, 97]

# print(l.sort(reverse=True))     # None
# print(l)            # [97, 45, 38, 13, 10, 8, 5, 3]

# l.reverse()
# print(l)    # [38, 97, 13, 45, 3, 10, 5, 8]


names = ['john', 'alex', 'mary', 'bob', 'eve', 'steve']
# names.sort()
# print(names)        # ['alex', 'bob', 'eve', 'john', 'mary', 'steve']

names.sort(reverse=True)
print(names)        # ['steve', 'mary', 'john', 'eve', 'bob', 'alex']

##################################################################################

# 11) copy
"""
-> It is used to perform shallow copy operation
-> Syntax:
            Var.copy()
"""

####################################################################################



