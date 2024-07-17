# TypeCasting
"""
-> Converting one datatype to another
-> Syntax:
            dest_var = dest_datatype(source_var)
"""

# 1) Typecasting of integer to other datatypes

num = 43

print(float(num))       # 43.0

print(complex(num))     # (43+0j)

print(bool(num))       # True
print(bool(0))          # False

print(str(num))         # '43'

# print(list(num))        # TypeError

# print(tuple(num))       # TypeError

# print(set(num))         # TypeError

# print(dict(num))        # TypeError

""" We can not typecast integer to multivalue datatypes except string"""
##########################################################################################

# 2) Typecasting of float to other datatypes

num = 12.77

print(int(num))     # 12

print(complex(num))     # (12.77+0j)

print(bool(num))        # True
print(bool(0.0))        # False

print(str(num))         # '12.77'
print(len(str(num)))    # 5

# print(list(num))        # TypeError

# print(tuple(num))       # TypeError

# print(set(num))         # TypeError

# print(dict(num))        # TypeError

#######################################################################################

# 3) Typecasting of complex to otehr datatypes

num = 10-5j

# print(int(num))         # TypeError

# print(float(num))       # TypeError

print(bool(num))        # True
print(bool(0j))         # False

print(str(num))         # '(10-5j)'

# print(list(num))        # TypeError

# print(tuple(num))       # TypeError

# print(set(num))         # TypeError

# print(dict(num))         # TypeError
"""complex can not be converted to other datatypes except string and boolean"""
######################################################################################

# 4) Typecasting of boolean to other datatypes

a = True
b = False

print(int(a))           # 1
print(int(b))           # 0

print(float(a))         # 1.0
print(float(b))         # 0.0

print(complex(a))       # (1+0j)
print(complex(b))       # 0j

print(str(a))           # 'True'
print(str(b))           # 'False'

# print(list(a))          # TypeError

# print(tuple(a))         # TypeError

# print(set(a))           # TypeError

# print(dict(a))          # TypeError

########################################################################################

# 5) Typecasting of string to other datatypes

a = 'hai'
b = '87'

# print(int(a))           # ValueError
print(int(b))           # 87
# print(int('23.78'))     # ValueError

print(float(b))         # 87.0
print(float('23.78'))   # 23.78

print(complex(b))       # (87+0j)
print(complex('24.86')) # (24.86+0j)
print(complex('3+7j'))  # (3+7j)

print(bool(b))          # True
print(bool('True'))     # True
print(bool('False'))    # True
print(bool(''))         # False

print(list(a))          # ['h', 'a', 'i']

print(tuple(a))         # ('h', 'a', 'i')

print(set(a))           # {'h', 'i', 'a'}

# print(dict(a))          # ValueError
# print(dict("{'a': 1}"))     # ValueError

########################################################################################

# 6) Typecasting of list to other datatypes

l = [1, 2, 3]

# print(int(l))           # TypeError

# print(float(l))         # TypeError

# print(complex(l))       # TypeError

print(bool(l))          # True

print(str(l))           # '[1, 2, 3]'
print(len(str(l)))      # 9

print(tuple(l))         # (1, 2, 3)

print(set(l))           # {1, 2, 3}

# print(dict(l))          # TypeError

l1 = [('a', 1), ('b', 2), ('c', 3)]
print(dict(l1))      # {'a': 1, 'b': 2, 'c': 3}

l1 = [['a', 1], ['b', 2], ['c', 3]]
print(dict(l1))     # {'a': 1, 'b': 2, 'c': 3}

l1 = [{'a', 1}, {'b', 2}, {'c', 3}]
print(l1)
print(dict(l1))     # {'a': 1, 'b': 2, 3: 'c'}

#########################################################################################

# 7) Typecasting of tuple to other datatypes
""" Same as that of typecasting list to other datatypes """

##########################################################################################

# 8) Typecasting of set to other datatypes
""" Same as that of typecasting list to other datatypes """

##########################################################################################

# 9) Typecasting of dictionary to other datatypes

d = {'a': 1, 'b': 2, 'c': 3}

# print(int(d))       # TypeError

# print(float(d))     # TypeError

# print(complex(d))       # TypeError

print(bool(d))      # True

print(str(d))       # '{'a': 1, 'b': 2, 'c': 3}'
print(len(str(d)))  # 24

print(list(d))      # ['a', 'b', 'c']
print(list(d.keys()))   # ['a', 'b', 'c']
print(list(d.values()))     # [1, 2, 3]
print(list(d.items()))  # [('a', 1), ('b', 2), ('c', 3)]

print(tuple(d))     # ('a', 'b', 'c')
print(tuple(d.keys()))  # ('a', 'b', 'c')
print(tuple(d.values()))    # (1, 2, 3)
print(tuple(d.items()))    # (('a', 1), ('b', 2), ('c', 3))

print(set(d))       # {'b', 'a', 'c'}
print(set(d.keys()))    # {'b', 'a', 'c'}
print(set(d.values()))  # {1, 2, 3}
print(set(d.items()))   # {('c', 3), ('a', 1), ('b', 2)}

