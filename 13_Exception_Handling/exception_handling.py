# exception handling

a = 10
b = '20'
# print(a + b)    # TypeError

l = [1, 2, 3]
# l.extend(4)     # TypeError
l.extend('hai')

# l.add(76)       # AttributeError

# l.remove(5)     # ValueError

# print(l[10])        # IndexError

d = {'a': 10, 'b': 20}
# print(d['c'])       # KeyError

s = {1, 2}
# s.append(8)     # AttributeError
s.add(8)
s.add((1, 2))
# s.add([1, 2])       # TypeError

# l.index(23)     # ValueError

# if 5        # SyntaxError

# if 5:       # IndentationError

# a, b, c = 1, 2, 3, 4        # ValueError
# a, b, c = 1, 2

t = (1, 2)
# t.append(5)     # AttributeError

# t[0] = 10       # TypeError

# print(5 / 0)        # ZeroDivisionError

# with open("sample.txt") as file:        # FileNotFoundError
#     pass

# with open("sample1.txt", 'x') as file:        # FileExistsError
#     pass

def sam(a, b, c):
    pass

# sam(1, 2)       # TypeError

# for i in 87:        # TypeError
#     pass

#################################################################################


"""
-> We can handle these exceptions using try and except block
-> Try block includes problem statement which throws an error
-> except block takes control when try block has some exception
-> 1) Specific Exception Handling
   2) Generic Exception Handling
   3) Default Exception Handling
"""

# 1) Specific Exception Handling

def add():
    a = eval(input('Enter the value of a : '))
    b = eval(input('Enter the value of b : '))
    print(a + b)

# add()

# try:
#     add()
# except TypeError:
#     print('Datatype not matching')
#
# try:
#     add()
# except TypeError as message:
#     print(message)

# def add():
#     try:
#         a = eval(input('Enter the value of a : '))
#         b = eval(input('Enter the value of b : '))
#         print(a + b)
#     except TypeError:
#         add()
#
# add()

# for i in range(3):
#     try:
#         a = eval(input('Enter the value of a : '))
#         b = eval(input('Enter the value of b : '))
#         print(a + b)
#         break
#     except TypeError as msg:
#         print(msg)
#         print('Try again')
#
# else:
#     raise TypeError


# def add():
#     try:
#         a = eval(input('Enter the value of a : '))
#         b = eval(input('Enter the value of b : '))
#         print(a + b)
#     except TypeError as msg:
#         if type(a) == set and type(b) == set:
#             print(a.union(b))
#         elif type(a) == dict and type(b) == dict:
#             print({**a, **b})
#         else:
#             print(msg)
# add()





