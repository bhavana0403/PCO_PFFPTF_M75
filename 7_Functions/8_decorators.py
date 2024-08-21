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


# print(demo())
# print(sam(1, 2, a=10))

#####################################################################################

# decorator to delay the execution of function by 3 seconds

from time import sleep
def delay(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} will get executed in 3 seconds")
        sleep(3)
        result = func(*args, **kwargs)
        return result
    return wrapper

@delay
def sam():
    return "In spam"

# print(sam())

#####################################################################################

# 3) decorator to calculate the time taken to execute the function

from time import time
def time_taken(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f"The total time taken to execute {func.__name__} is {end-start}")
    return wrapper


@time_taken
def perfect(m, n):
    for num in range(m, n+1):
        s = 0
        for i in range(1, num):
            if num % i == 0:
                s += i
        if s == num:
            print(num)


# perfect(1, 10000)

# 4) calculate the total number of arguments to a function

def count_args(func):
    def wrapper(*args, **kwargs):
        c = 0
        for _ in args:
            c += 1
        for _ in kwargs:
            c += 1
        print(f"The total number of arguments passed to {func.__name__} is {c}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@count_args
def sam(*args, **kwargs):
    return  args, kwargs

# print(sam(1, 2, 3, a=10, b=20))
"""
The total number of arguments passed to sam is 5
((1, 2, 3), {'a': 10, 'b': 20})
"""

# print(sam(1, 2, 3, 4, a=10, b=20, c=30))

###################################################################################

# 5) decorator to count the number of positional and keyword arguments separately

def count_args(func):
    def wrapper(*args, **kwargs):
        c1, c2 = 0, 0
        for _ in args:
            c1 += 1
        for _ in kwargs:
            c2 += 1
        print(f"The total number of positional arguments passed to {func.__name__} is {c1}")
        print(f"The total number of keyword arguments passed to {func.__name__} is {c2}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@count_args
def sam(*args, **kwargs):
    return  args, kwargs

# print(sam(1, 2, 3, a=10, b=20))
"""
The total number of positional arguments passed to sam is 3
The total number of keyword arguments passed to sam is 2
((1, 2, 3), {'a': 10, 'b': 20})
"""

# 6) decorator to execute a function 3 times

def execute_three_times(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)
    return wrapper


@execute_three_times
def greeting():
    print("hello world")

greeting()

# 7) decorator to count the number of function calls for each function

def count_func_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f"The number of times function has been called is {count}")
        return result
    return wrapper

count = {}
def count_func_calls(func):
    count[func.__name__] = 0
    def wrapper(*args, **kwargs):
        count[func.__name__] += 1
        result = func(*args, **kwargs)
        print(count)
        return result
    return wrapper

@count_func_calls       # spam = count_func_calls(spam) - > spam = wrapper
def spam():
    return "In spam"

@count_func_calls
def display():
    return "In display"

print(display())
print(display())
print(display())

print(spam())
print(spam())

