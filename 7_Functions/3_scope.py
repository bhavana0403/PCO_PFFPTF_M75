# scope of a variable

# a = 10          # global variable
# def sam():
#     print(a)
# sam()
# print(a)


# def sam():
#     a = 10          # local variable
#     print(a)
# sam()
# print(a)
"""
10
NameError
"""

a = 10
def sam():
    a = 20          # local variable of sam
    print(a)
print(a)
sam()
print(a)
"""
10
20
10
"""

# Scope of a variable
"""
LEGB -> Local, Enclosed, Global, BuiltIn
global variables - these are the variables which gets created in the global frame
                 - we can access them in the global frame, inside the function
local variables - these are the variables which gets created inside function area/ method area
                - these can be accessed only inside the function and not in global frame 
"""
# sum = 8
# print(sum([1, 2, 3]))       # TypeError

