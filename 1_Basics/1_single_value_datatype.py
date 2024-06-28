# Datatype
"""
-> It specifies the type of the data that is stored
-> It is classified into 2 types
    1) Single Value Datatype/ Individual Datatype
        i) Numeric
            a) Integer(int)
            b) Float(float)
            c) Complex(complex)
        ii) Boolean(bool)

    2) Multi-value Datatype/ Collection
        i) Sequential Datatype
            a) String(str)
            b) List(list)
            c) Tuple(tuple)
        ii) Non-Sequential Datatype
            a) Set(set)
            b) Dictionary(dict)
"""

# Integer(int)
"""
-> Real number without decimal values
-> The default value of integer is 0 which is internally equal to False
-> Default values are used to initialise a variable for a specific datatype
"""

a = 10
print(a)        # 10
print(type(a))  # <class 'int'>
print(bool(a))  # True

b = -86
print(b)        # -86
print(type(b))  # <class 'int'>
print(bool(b))  # True

c = 0
print(c)        # 0
print(type(c))  # <class 'int'>
print(bool(c))  # False

# Float(float)
"""
-> Real number with decimal values
-> The default value of float is 0.0 which is internally equal to False
"""

a = -8.65
print(a)        # -8.65
print(type(a))  # <class 'float'>
print(bool(a))  # True

b = 0.0
print(b)        # 0.0
print(type(b))  # <class 'float'>
print(bool(b))  # False

##############################################################################

# complex
"""
-> A number in the form of a+-bj is called complex number
-> 'a' is the real part and 'bj' is the imaginary part
-> The value of 'j' is square root of -1
-> The values of 'a' and 'b' can be either integer or float number
-> The default value of complex is 0j
"""

x = 7.8-5j
print(x)        # (7.8-5j)
print(type(x))  # <class 'complex'>
print(bool(x))  # True

y = 0j
print(y)        # 0j
print(type(y))  # <class 'complex'>
print(bool(y))  # False

###############################################################################

# Boolean(bool)
"""
-> It has 2 values True and False
-> True is the non default value, False is the default value
-> We use boolean in 2 cases
    1) To assign as a value to any variable
    2) As a resultant to check the condition
"""

p = True
q = False
print(type(p))  # <class 'bool'>
print(type(q))  # <class 'bool'>

print(p)
print(q)

print(4 > 3)    # True
print(7 == 8)   # False