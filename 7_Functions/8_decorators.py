# decorators

def sam(some_val):
    return some_val

print(sam(10))      # 10
print(sam('hello'))     # hello

a = 'hello world'
b = sam(a)
print(b)    # hello world

def add(a, b):
    return a + b

print(add)      # <function add at 0x0000021A95E0AF20>
print(add(10, 20))      # 30

print(id(add))  # 2191515692832
print(print)    # <built-in function print>

a = sam(add)
print(a)        #  <function add at 0x0000021A95E0AF20>
print(a(10, 20))        # 30

b = add
print(b)        # <function add at 0x0000021A95E0AF20>
print(b(10, 20))    # 30

######################################################################################

def sam(a):
    def inner():
        print(a)
    return inner

li = [10, 20, 30]
print(li)       # [10, 20, 30]

a = 10
# print(inner())  # NameError

print(sam(12))      # <function sam.<locals>.inner at 0x000001F1DB7604A0>

b = sam(100)
c = sam(200)
print(b)        # <function sam.<locals>.inner at 0x000001D3A57304A0>
print(c)        # <function sam.<locals>.inner at 0x000001D3A596F600>

b()      # 100
c()      # 200

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


a = sam(greeting)
b = sam(demo)
print(a)    # <function sam.<locals>.inner at 0x0000020EF3ACF880>
print(b)    # <function sam.<locals>.inner at 0x0000020EF3ACF920>

print(a())
"""
<function greeting at 0x000001CAB5B3F600>
Hello World
"""
print(b())
"""
<function demo at 0x000001CAB5B3F7E0>
In Demo
"""