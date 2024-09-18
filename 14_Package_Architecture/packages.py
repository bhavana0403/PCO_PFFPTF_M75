# package
"""
-> module - a file that contains python code such as functions, classes and
            variables
            Ex: math, collections, time, copy, etc
-> package - are folders that contain multiple modules
            Ex: selenium, numpy, pandas, etc

import -> a keyword which is used to import the module or get access to the module
dir -> get all the functions, var, etc present the module in the form of list of
       strings
-> to access the functions present in the module we make use of the syntax,
        module_name.fname(args)
from -> which is used to import a particular member/ function from the module
* -> used to import all the functions which are present inside the module and use
     it as it is, fname(args)
as -> we can give alias name to the module using as keyword
"""
# import math

# import math
#
# print(math.factorial(8))
#
# print(dir(math))
"""
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 
'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 
'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 
'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 
'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 
'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 
'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
"""

# print(math.e)
# print(math.pi)
# print(math.sqrt(87))

######################################################################################

# import math as m
#
# # print(math.factorial(9))        # NameError
# print(m.factorial(9))       # 362880
# print(m.gcd(8, 12))      # 4

####################################################################################

from math import factorial, sqrt, gcd

# print(factorial(9))
# print(sqrt(100))
# print(gcd(4, 8))

#######################################################################################

# from math import *
# print(factorial(9))
# print(pi)
# print(e)
# print(sin(pi/6))

####################################################################################