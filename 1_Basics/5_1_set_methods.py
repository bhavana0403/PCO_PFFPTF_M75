# set methods

# 1) add
"""
-> It is used to add the values to a set
-> Syntax:
            Var.add(Val)
-> using add method we can add only one value
-> The return type of add is None
"""

# s = {10, 20}
# print(s.add(30))    # None
# print(s)        # {10, 20, 30}
#
# s.add('hai')
# print(s)        # {10, 'hai', 20, 30}

# s.add('hello', 87)   # TypeError: set.add() takes exactly one argument (2 given)

# s.add(('hello', 86))    #
# print(s)        # {10, 'hai', 20, ('hello', 86), 30}

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
# print(s1.union(s2))     # {1, 2, 3, 4, 5, 6}
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
# print(s.pop())  # h -> some random element will be removed

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

# 7) union
"""
-> It returns a set which has the values of a set and an iterable
-> Syntax:
            Var.union(iterable)
-> Update will not modify original set
-> The return type of union is set
"""

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# print(s1.union(s2))     # {1, 2, 3, 4, 5, 6}
# print(s1)   # {1, 2, 3}
# print(s2)   # {4, 5, 6}
#
# print(s1.union('abc'))  # {1, 2, 3, 'b', 'a', 'c'}
#
# print(s1.union([10, 20, 30]))       # {1, 2, 3, 10, 20, 30}

#######################################################################################

# 8) intersection
"""
-> It is used to return the common elements present in set and an iterable
-> Syntax:
            Var.intersection(iterable)
-> The return type of intersection is set
-> If there is no common elements, it will return empty set set()
"""

s1 = {1, 2, 3, 'a', (10, 20)}
s2 = {2, 4, 6}
s3 = {(10, 20), 'b', 'c', 3}

# print(s1.intersection(s2))      # {2}
#
# print(s1)       #
# print(s2.intersection(s3))      # set()

########################################################################################

# 9) difference
"""
-> It is used to get the values of set1 excluding the common elements of set1 and
   iterable
-> Syntax:
            Var.difference(iterable)
-> The return type of difference is set
"""

# s1 = {1, 2, 3, 'a', (10, 20)}
# s2 = {2, 4, 6}
# s3 = {(10, 20), 'b', 'c', 3, 2}
#
# print(s1.difference(s2))        # {1, 3, 'a', (10, 20)}
# print(s3.difference(['a', 'b', 'c', 3]))        # {(10, 20)}
#
# print(s1.intersection(s3, s2))

######################################################################################

# 10) intersection_update
"""
-> It is used to change the original set with the resultant obtained from intersection 
   method
-> Syntax:
            Var.intersection_update(iterable)
-> The return type of intersection_update is None 
"""
# s1 = {1, 2, 3, 'a', (10, 20)}
# s2 = {2, 4, 6}
# s3 = {(10, 20), 'b', 'c', 3}

# print(s1.intersection_update(s2))   # None
# print(s1)       # {2}

# s1.intersection_update(s3)
# print(s1)       # {3, (10, 20)}

# s2.intersection_update(set())
# print(s2)   # set()

#######################################################################################

# 11) difference_update
"""
-> Syntax:
            Var.difference_update(iterable)
"""
# s1 = {1, 2, 3, 'a', (10, 20)}
# s2 = {2, 4, 6}
# s3 = {(10, 20), 'b', 'c', 3, 2}
#
# print(s1.difference(s3))
# print(s1.difference_update(s3))
# print(s1)       # {1, 'a'}

#####################################################################################


