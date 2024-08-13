# packing

# variable positional arguments

# def add_num(*args):
#     print(args)
#     print(type(args))
#     print(*args)
#     s = 0
#     for i in args:
#         s += i
#     print(s)
#
#
# add_num(1, 2, 3)
# add_num(1, 2, 3, 4, 5, 6)
# add_num()
#
# l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# add_num(*l2)
# # add_num(a=1, b=2)       # TypeError
#
# # combination
#
# def sam(name, *args):     # name is a positional argument
#     print(name)
#     print(args)
#
# # sam()   # TypeError
# sam("John")
# """
# John
# ()
# """
#
# sam("JOhn", 1, 2, 3)
# """
# JOhn
# (1, 2, 3)
# """
#
# sam("John", "Abraham", "Alex", "Joseph")
# """
# John
# ('Abraham', 'Alex', 'Joseph')
# """

######################################################################################

# variable keyword arguments

def sam(**kwargs):      # packs in the form of dictionary
    print(kwargs)
    print(type(kwargs))
    print(*kwargs)
    print(*kwargs.values())
    print(*kwargs.items())


# sam(1, 2, 3)        # TypeError
sam(a=1)
sam(a='hai', b=[1, 2, 3], c={1, (8, 7+6j)})
sam()

# combination


def sam(name, **kwargs):        # name can be either positional or keyword argument
    print(name)
    print(kwargs)


sam(name="john", lname='patrick')
"""
john
{'lname': 'patrick'}
"""

sam(name='john')
"""
john
{}
"""

sam("Steve")
"""
Steve
{}
"""

sam("Stella", lname="Peter", marks={'physics': 95, 'chemistry': 93, 'maths': 99, 'biology': 90})
"""
Stella
{'lname': 'Peter', 'marks': {'physics': 95, 'chemistry': 93, 'maths': 99, 'biology': 90}}
"""

######################################################################################

# variable positional and variable keyword

def sam(*args, **kwargs):
    print(args, kwargs)

sam()       # () {}
sam(1, 2, 3)     # (1, 2, 3) {}
sam(a='hello', b='basket', c='cat')     # () {'a': 'hello', 'b': 'basket', 'c': 'cat'}
sam(1, 2, 3, a=10, b=20, c=30)      # (1, 2, 3) {'a': 10, 'b': 20, 'c': 30}
# sam(a=10, b=20, c=30, 1, 2, 3)      # SyntaxError

######################################################################################

# only positional arguments
"""
parameters before / will take only positional arguments, parameters after / can be 
either positional or keyword 
"""

def sum_of_num(a, b, /, c):
    print(a + b + c)

sum_of_num(1, 2, 3)
sum_of_num(1, 2, c=3)
# sum_of_num(a=1, b=2, c=3)   # TypeError ->  positional-only arguments passed as keyword arguments: 'a, b'


# l1 = [10, 785, 12, 8678]
# l1.sort(reverse=True)


# only keyword arguments
"""
parameters after * must be given as keyword only arguments, parameters before * can
be either positional or keyword
"""

def sum_of_nums(a, *, b, c):
    print(a, b, c)

sum_of_nums(a=11, b=22, c=33)
sum_of_nums(11, b=22, c=33)
# sum_of_nums(11, 22, 33)     # TypeError
sum_of_nums(11, c=3, b=2)       # 11 2 3


######################################################################################

# combination
"""
a, b -> positional only
c, d -> either positional or keyword
e, f -> only keyword
"""

def sam(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


# sam(1, 2, 3, 4, 5, 6)   # TypeError: sam() takes 4 positional arguments but 6 were given

sam(1, 2, 3, 4, f=6, e=5)
sam(1, 2, c=3, d=4, e=5, f=6)
# sam(1, 2, c=3, 4, e=5, f=6)     # SyntaxError: positional argument follows keyword argument
sam(1, 2, 3, d=4, e=7, f=7)





