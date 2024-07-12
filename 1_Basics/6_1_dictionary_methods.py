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

d = {'a': 6, 'b': 82, 'e': 75, 'd': 86}
print(d.clear())        # None
print(d)        # {}

