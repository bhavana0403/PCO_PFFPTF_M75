# Dictionary
"""
-> It is a collection of key value pairs
-> Syntax:
            Var = {k1: v1, k2: v2, ........, kn: vn}
            where, * key and value are separated by : operator
                   * key value pairs are separated by , operator
                   * keys must be of immutable datatype
                   * values can be either mutable or immutable datatype
-> The default value of dictionary is {}
-> To access the values, we make use of teh syntax,
            Var[key]
            if the key is not present, control will throw KeyError
-> To modify the values, we make use of the syntax,
            Var[key] = new_value
            if the key is present, it will modify the value,
            if the key is not present, it will add a new key value pair to the dictionary
-> To delete a key value pair we make use of the syntax,
            del Var[key]
            if the key is not present, control will throw KeyError
"""

d1 = {'python': 6, 4: 'java', (1, 2): 12, 'java': ['testing', 'development']}

d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d3 = dict(a=10, b=20, c=30, d=40)
print(d3)       # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Memory Allocation of Dictionary
"""
-> When the value is of dictionary, a key value layer is created in value space/ 
   heap memory, the address of the value will be stored wrt keys in key and value 
   layers respectively
-> Once after storing all the key and values address will be given to key layer which
   is stored wrt variable name in variable space/ stack memory
-> for control the visible layer is key layer
-> python visualizer link -> https://pythontutor.com/visualize.html#mode=edit
"""
# to access the values

# d1 = {'python': 6, 4: 'java', (1, 2): 12, 'java': ['testing', 'development']}
#
# print(d1[4])    # java
#
# print(d1['python'])     # 6
#
# # print(d1['manual'])     # KeyError
#
# d = {'a': 10, 'b': 20, 'a': 30}
# print(d)    # {'a': 30, 'b': 20}

# to modify the values

temperature = {'Bengaluru': 38,
               'Chennai': 42,
               'Mumbai': 39,
               'Delhi': 43
               }

print(temperature['Bengaluru'])     # 38

temperature['Bengaluru'] = 37
print(temperature)      # {'Bengaluru': 37, 'Chennai': 42, 'Mumbai': 39, 'Delhi': 43}

# print(temperature['Patna'])     # KeyError: 'Patna'
temperature['Patna'] = 34
print(temperature)      # {'Bengaluru': 37, 'Chennai': 42, 'Mumbai': 39, 'Delhi': 43, 'Patna': 34}

#########################################################################################

# delete the value

del temperature['Patna']
print(temperature)      # {'Bengaluru': 37, 'Chennai': 42, 'Mumbai': 39, 'Delhi': 43}

del temperature['Chennai']
print(temperature)          # {'Bengaluru': 37, 'Mumbai': 39, 'Delhi': 43}

# del temperature['Chennai']      # KeyError: 'Chennai'

holidays = {(26, 1): 'Republic Day',
            (15, 8): 'Independence Day',
            (2, 10): 'Gandhi Jayanthi'
            }

d = {'a': [1, 2, 3], 'b': ['java', 'python'], 'c': {'d': [50, 60]}}

# 3
print(d['a'][2])    # 3

# python
print(d['b'][1])

# 50
print(d['c']['d'][0])


