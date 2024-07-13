# dictionary methods

# 1) pop
"""
-> It is used to remove a specified key from the dictionary
-> Syntax:
            Var.pop(key)
-> It will return the value of the key which has been popped
-> If the key is not present, pop will throw KeyError
"""

# d = {'a': 6, 'b': 82, 'e': 75, 'd': 86}
# print(d.pop('a'))   # 6
# print(d)        # {'b': 82, 'e': 75, 'd': 86}

# d.pop('f')  # KeyError: 'f'

#########################################################################################

# 2) popitem
"""
-> It is used to remove the last key which has been added to the dictionary
-> Syntax:
            Var.popitem()
-> It will return a tuple of key and value that is popped
-> It will throw KeyError if the dictionary is empty
"""
# d = {'a': 6, 'b': 82, 'e': 75, 'd': 86}
# print(d.popitem())      # ('d', 86)
#
# d = {}
# print(d.popitem())      # KeyError: 'popitem(): dictionary is empty'

#######################################################################################

# 3) clear
"""
-> It is used to remove all the key value pairs from the dictionary
-> Syntax:
            Var.clear()
-> The return type of clear is None
"""

# d = {'a': 6, 'b': 82, 'e': 75, 'd': 86}
# print(d.clear())        # None
# print(d)        # {}

######################################################################################

# 4) get
"""
-> It is used to get the value of a specified key from the dictionary
-> Syntax:
            Var.get(key)                # returns the value of a key, if the key is not present then it returns None
            Var.get(key, default_val)   # return the value of a key if it is present, if the key not present it return default_value
"""

temperature = {'Bengaluru': 38,
               'Chennai': 42,
               'Mumbai': 39,
               'Delhi': 43
               }
#
# print(temperature.get('Bengaluru'))     # 38
# print(temperature.get('Raipur'))        # None
# print(temperature.get('Raipur', 36))    # 36
# print(temperature)                      # {'Bengaluru': 38, 'Chennai': 42, 'Mumbai': 39, 'Delhi': 43}
# print(temperature.get('Mumbai', 40))    # 39

#########################################################################################

# 5) fromkeys
"""
-> It is used to create a dictionary from the values of iterable
-> Syntax:
            Var.fromkeys(iterable)         
            -> returns a dictionary whose keys are values of the iterable and value 
               for the key is set to None
            Var.fromkeys(iterable, value)
            -> returns a dictionary whose keys are values of the iterable and value 
               for the key is set to "value"
-> The return type is a dictionary
-> The original dictionary will not be modified
"""

# st = 'abc'
# print({}.fromkeys(st))      # {'a': None, 'b': None, 'c': None}
# print({}.fromkeys(st, 0))   # {'a': 0, 'b': 0, 'c': 0}
# print({}.fromkeys(st, ''))  # {'a': '', 'b': '', 'c': ''}
# print({}.fromkeys(st, 10))          # {'a': 10, 'b': 10, 'c': 10}
#
# print(temperature.fromkeys('abc'))      # {'a': None, 'b': None, 'c': None}
# print(temperature)          # {'Bengaluru': 38, 'Chennai': 42, 'Mumbai': 39, 'Delhi': 43}
#
# print({}.fromkeys(temperature, 35))     # {'Bengaluru': 35, 'Chennai': 35, 'Mumbai': 35, 'Delhi': 35}
# print(temperature)          # {'Bengaluru': 38, 'Chennai': 42, 'Mumbai': 39, 'Delhi': 43}

##################################################################################

# 6) setdefault
"""
-> It is used to add a new key value pair to the dictionary
-> Syntax:
            Var.setdefault(key)     # creates a new key with value as None
            Var.setdefault(key, value)  # creates a new key with value as "value"
-> If the key is already present, it will not alter the key
"""

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(d.setdefault('e'))        # None
# print(d)        # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': None}
#
# d.setdefault('f', 10)
# print(d)        # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': None, 'f': 10}
#
# d.setdefault('a', 23)
# print(d)        # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': None, 'f': 10}

#####################################################################################
