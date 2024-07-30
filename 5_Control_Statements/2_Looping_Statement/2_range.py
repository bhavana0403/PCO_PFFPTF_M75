# range
"""
-> It is used to generate the numbers between specified limits
-> Syntax:
            range(SV, EV+-1, UP)
-> By default value of updation is 1
            range(SV, EV+-1)
"""

print(range(1, 11))     # range(1, 11)
print(type(range(1, 11)))   # <class 'range'>

"""
-> It is an inbuilt collection
-> range doesn't have a proper structure to display the output, so we make 
   use of typecasting
"""

print(list(range(1, 11)))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(set(range(-3, -31, -3)))  # {-30, -27, -24, -21, -18, -15, -12, -9, -6, -3}

"""
if SV == 0 and up == 1
        range(EV+1)
"""

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 21, 2)))        # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

st = 'apple'

print(list(range(len(st))))     # [0, 1, 2, 3, 4]

