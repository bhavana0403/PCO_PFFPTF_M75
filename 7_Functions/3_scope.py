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

# a = 10
# def outer():
#     print(a)
#     a = 20
#     print(a)
# print(a)
# outer()
"""
10
UnboundLocalError
"""

"""
-> To access and modify the global variable inside the function we make use of keyword
    called 'global'
-> global has to be the first argument inside the function area
-> global has to followed by variables that needs to be modified
-> address of global variable will be stored in function area 
"""

# a = 10
# def outer():
#     global a
#     print(a)
#     a = 20
#     print(a)
# print(a)
# outer()
# print(a)
"""
10
10
20
20
"""

# p = 1
# q = 2
# def outer():
#     global p
#     p = 3           # modifies global variable
#     q = 4           # local var for outer
#     print(p, q)
# print(p, q)
# outer()
# print(p, q)

"""
1 2
3 4
3 2
"""

###################################################################################

# m = 1
# def outer():
#     m = 2               # local var for outer
#     def inner():
#         m = 3           # local var for inner
#         print(m)
#     print(m)
#     inner()
#     print(m)
#
# outer()
# print(m)
"""
2
3
2
1
"""


# m = 1
# def outer():
#     m = 2               # local var for outer
#     def inner():
#         print(m)
#     print(m)
#     inner()
#     print(m)
#
# outer()
# print(m)
"""
2
2
2
1
"""

# m = 1
# def outer():
#     def inner():
#         print(m)
#     print(m)
#     inner()
#     print(m)
#
# outer()
# print(m)


def outer():
    m = 1
    def inner():
        m = 2
        print(m)
    print(m)
    inner()
    print(m)

outer()
"""
1
2
1
"""

"""
-> To modify a local variable inside nested function we make use of 'nonlocal'
   keyword
"""
def outer():
    m = 1
    def inner():
        nonlocal m
        print(m)
        m = 2
        print(m)
    print(m)
    inner()
    m = 4
    print(m)

outer()
"""
1
1
2
4
"""


