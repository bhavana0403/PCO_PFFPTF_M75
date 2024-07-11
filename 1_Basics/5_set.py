# Set(set)
"""
-> It is a unordered, non-duplicate collection of homogenous or heterogeneous data-items
   enclosed between {}
-> Syntax:
            Var = {Val1, Val2, ..........., Valn}
            whereas, values inside the set are immutable data-items
-> The default value of set is set()
-> Set is a mutable collection
"""

# s = {}
# print(type({}))     # <class 'dict'>

# s = set()
# print(type(s))  # <class 'set'>
# print(bool(s))  # False

s = {1.87, 'hello', (1, 2), 876}
print(s)    # {1.87, (1, 2), 876, 'hello'}

s = {10, 'hai', True, 10.0, 'hai', 98, 98+0j}
print(len(s))   # 4
print(s)        # {'hai', 10, True, 98}

s = {True, 1, 0, False}
print(s)        # {0, True}

s1 = {10, 34, 23, 62, 61, 23}       # homogeneous

# s2 = {9, 19, 9.0, False, [1, 2]}    # TypeError: unhashable type: 'list'

# s3 = {9, 19, 9.0, False, (1, 2)}    #

# s4 = {9, 19, 9.0, False, {1, 2}}    # TypeError: unhashable type: 'set'

s3 = {9, 19, 9.0, False, (1, 2)}

s3.add(23)      #
print(s3)       # {False, (1, 2), 9, 19, 23}

s3.remove(False)
print(s3)



