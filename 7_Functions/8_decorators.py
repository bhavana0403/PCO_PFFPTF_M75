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



