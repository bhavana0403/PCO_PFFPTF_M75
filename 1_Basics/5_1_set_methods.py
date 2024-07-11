# set methods

# 1) add
"""
-> It is used to add the values to a set
-> Syntax:
            Var.add(Val)
-> using add method we can add only one value
-> The return type of add is None
"""

s = {10, 20}
print(s.add(30))    # None
print(s)        # {10, 20, 30}

s.add('hai')
print(s)        # {10, 'hai', 20, 30}

# s.add('hello', 87)   # TypeError: set.add() takes exactly one argument (2 given)

s.add(('hello', 86))    #
print(s)        # {10, 'hai', 20, ('hello', 86), 30}

# s.add(['a', 'b'])       # TypeError: unhashable type: 'list'

########################################################################################

# 2) update
"""
-> It is used to add all the values from the iterable individually
-> Syntax:
            Var.update(iterable)
-> It updates the set with an iterable
-> The return type of update is None
"""

s1 = {1, 2, 3}
s2 = {4, 5, 6}
# print(s1.update(s2))    # None
# print(s1)       # {1, 2, 3, 4, 5, 6}
# print(s2)       # {4, 5, 6}

# s1.update(('hai', 'hello'))
# print(s1)       # {1, 2, 3, 'hello', 'hai'}

# s1.update([10, 20, 30])
# print(s1)   # {1, 2, 3, 10, 20, 30}

# s2.update([10, 20, [30, 40]])   # TypeError: unhashable type: 'list'

# s1.update('hello world')
# print(s1)       # {1, 2, 3, 'h', 'w', ' ', 'r', 'l', 'd', 'o', 'e'}

#########################################################################################

# 3) pop
"""
-> It is used to remove a random element from a set
-> Syntax:
            Var.pop()
-> pop will return the value which has been removed from the set
-> pop will not take any arguments
"""

s = {1, 2, 3, 'h', 'w', ' ', 'r', 'l', 'd', 'o', 'e'}
print(s.pop())  # h -> some random element will be removed

# print(s.pop(1))     # TypeError: set.pop() takes no arguments (1 given)

##########################################################################################

# 4) remove
"""
-> It is used to remove the specified element from the set
-> Syntax:
            Var.remove(Val)
-> If the value is not present, remove will throw KeyError
-> The return type of remove is None
"""

s = {1, 2, 3, 'h', 'w', ' ', 'r', 'l', 'd', 'o', 'e'}
#
# print(s.remove('r'))    # None
# print(s)        # {1, 2, 3, 'd', ' ', 'h', 'w', 'l', 'o', 'e'}

# print(s.remove(10))     # KeyError: 10

######################################################################################

# 5) discard
"""
-> It works same as remove, but will not throw any error if the value is not present
-> Syntax:
            Var.discard(Val)
-> The return type of discard is None
"""
# print(s.discard('l'))       # None
# print(s)
#
# print(s.discard(10))        # NOne

########################################################################################

# 6) clear
"""
-> It is used to remove all the values from the set
-> Syntax:
            Var.clear()
-> The return type of clear is None
"""

# print(s.clear())        # None
# print(s)            # set()

#######################################################################################

