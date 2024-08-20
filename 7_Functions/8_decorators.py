# decorators

# def sam(some_val):
#     return some_val
#
# print(sam(10))      # 10
# print(sam('hello'))     # hello
#
# a = 'hello world'
# b = sam(a)
# print(b)    # hello world
#
# def add(a, b):
#     return a + b
#
# print(add)      # <function add at 0x0000021A95E0AF20>
# print(add(10, 20))      # 30
#
# print(id(add))  # 2191515692832
# print(print)    # <built-in function print>
#
# a = sam(add)
# print(a)        #  <function add at 0x0000021A95E0AF20>
# print(a(10, 20))        # 30
#
# b = add
# print(b)        # <function add at 0x0000021A95E0AF20>
# print(b(10, 20))    # 30

######################################################################################

def sam(a):
    def inner():
        print(a)
    return inner

# li = [10, 20, 30]
# print(li)       # [10, 20, 30]
#
# a = 10
# print(inner())  # NameError

# print(sam(12))      # <function sam.<locals>.inner at 0x000001F1DB7604A0>
#
# b = sam(100)
# c = sam(200)
# print(b)        # <function sam.<locals>.inner at 0x000001D3A57304A0>
# print(c)        # <function sam.<locals>.inner at 0x000001D3A596F600>
#
# b()      # 100
# c()      # 200

#####################################################################################

def sam(func):
    def inner():
        print(func)
        return func()
    return inner


def greeting():
    return "Hello World"

# print(greeting())       # Hello World

def demo():
    return "In Demo"


# a = sam(greeting)
# b = sam(demo)
# print(a)    # <function sam.<locals>.inner at 0x0000020EF3ACF880>
# print(b)    # <function sam.<locals>.inner at 0x0000020EF3ACF920>

# print(a())
"""
<function greeting at 0x000001CAB5B3F600>
Hello World
"""
# print(b())
"""
<function demo at 0x000001CAB5B3F7E0>
In Demo
"""

#####################################################################################

def sam(func):
    def inner():
        print(func)
        return func()
    return inner


def greeting():
    return "Hello World"


def demo():
    return "In Demo"


# a = sam(greeting)
# print(a)        # <function sam.<locals>.inner at 0x000001B73566F9C0>

# greeting = sam(greeting)
# print(greeting)     # <function sam.<locals>.inner at 0x000001869E3FF9C0>

# demo = sam(demo)
# print(demo)     # <function sam.<locals>.inner at 0x0000021956DEFA60>

# print(greeting())
"""
<function greeting at 0x000001EFB2CDF6A0>
Hello World
"""
# print(demo())
"""
<function demo at 0x000001EFB2CDF920>
In Demo
"""

##################################################################################

def calculate(func):
    def wrapper(a, b):
        print('Calculating........')
        result = func(a, b)
        return result
    return wrapper


def add(x, y):
    return x + y

def sub(x, y):
    return x - y


# add = calculate(add)
# print(add)      # <function calculate.<locals>.wrapper at 0x0000017DF977FC40>
#
# sub = calculate(sub)
# print(sub)      # <function calculate.<locals>.wrapper at 0x0000017DF977FCE0>
#
# print(add(3, 4))    # 7

#######################################################################################

def calculate(func):
    def wrapper(*args, **kwargs):
        print('Calculating........')
        result = func(*args, **kwargs)
        return result
    return wrapper


def add(x, y, z):
    return x + y + z

def sub(x, y):
    return x - y


# add = calculate(add)
# print(add)      # <function calculate.<locals>.wrapper at 0x0000017DF977FC40>
#
# sub = calculate(sub)
# print(sub)      # <function calculate.<locals>.wrapper at 0x0000017DF977FCE0>
#
# print(add(3, 4, 8))
# print(sub(20, 7))

######################################################################################

# Decorator
"""
-> Adding an extra functionality to the main function without modifying it is
   known as a decorator
-> Syntax:
            def deco(func):
                def wrapper(*args, **kwargs):
                    PRE-TASK
                    result = func(*args, **kwargs)
                    POST-TASK
                    return result
                return wrapper
-> decorator function must have a nested function 
-> Outer function / decorator function must take only one argument that is the 
   address of main function
-> nested function/ inner function/ wrapper function must take the arguments that must
   be taken by the main function
-> main function must be called inside wrapper function 
-> decorator function must return the address of wrapper function
"""

def calculate(func):
    def wrapper(*args, **kwargs):
        print('Calculating........')
        result = func(*args, **kwargs)
        return result
    return wrapper


@calculate          # add = calculate(add)
def add(x, y, z):
    return x + y + z


@calculate          # sub = calculate(sub)
def sub(x, y):
    return x - y

# add = calculate(add)
# sub = calculate(sub)
"""
-> instead of writing this we write @decorator_name before creating the main function
"""
# print(add(10, 5, 7))
# print(sub(10, 5))

######################################################################################

# 1) decorator to print the name of the function which is executed

def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} function will be executed")
        result = func(*args, **kwargs)
        return result
    return wrapper

@print_func_name        # sam = print_func_name(sam)
def sam(*args, **kwargs):
    return args, kwargs

@print_func_name        # demo = print_func_name(demo)
def demo():
    return "In demo"


print(demo())
print(sam(1, 2, a=10))
