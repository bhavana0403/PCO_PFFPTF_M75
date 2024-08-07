# Functions
"""
-> Functions are the named memory block which has some set of instructions used to
   perform a specific task
   1) Inbuilt Function - print, input, max, min, etc
   2) User Defined Functions

User Defined Functions
-> These are the functions which are created based on user requirements
-> Syntax:
            def fname(args):            # function declaration
                function block/ SB      # function definition
                return values
            fname(args)                 # function call
            # where passing the arguments and returning the values are not mandatory
-> def - it is a keyword which is used to create a function
-> fname - name given to identify some set of instructions
-> args - parameters/ values which are used to perform the task
-> return - a keyword which makes the control come out of the function by taking the values
-> function call - only if we call the function it will be executed

User Defined Functions are classified into 4 types
1) Function without arguments and without return values
-> Syntax:
            def fname():
                SB
            fname()

2) Function with arguments and without return values
-> Syntax:
            def fname(Var1, Var2,...., Varn):
                SB
            fname(Val1, Val2, ...., Valn)

3) Function without arguments and with return values
-> Syntax:
            def fname():
                SB
                return values
            print(fname())
            res = fname()
            print(res)
            var1, var2, ....., varn = fname()

4) Function with arguments and with return values
-> Syntax:
            def fname(args):
                SB
            print(fname(args))
            res = fname(args)
            print(res)
            var1, var2, ....., varn = fname(args)
"""

# WAP to reverse the given string

st = 'hello'
rev = ''
for ch in st:
    rev = ch + rev
print(rev)

# Type1

# def greeting():
#     print('Hello Universe')
#
# print(greeting)         # <function greeting at 0x000001DB2B8F04A0>
# print(greeting())
# """
# Hello Universe
# None
# """
# greeting()  # Hello Universe

def reverse1():
    st = 'hello'        # input('Enter the string : ')
    rev = ''
    for ch in st:
        rev = ch + rev
    print(rev)

reverse1()

# WAP to print all even numbers in a list

def even_num():
    li = [101, 22, 33, 44]
    for num in li:
        if num % 2 == 0:
            print(num)

even_num()


# Type 2

def sam(name, empid):
    print(f"Hello, I'm {name}, my employee ID is {empid}")

sam("John", "ABC123")

st = 'hello'
def reverse2(st):
    rev = ''
    for ch in st:
        rev = ch + rev
    print(rev)

reverse2(st)        # 'olleh'
a = 'python'
reverse2(a)         # nohtyp -> reverse2('python')
reverse2("manual")  # launam

# Type 4 - with args, with return value

def calc(a, b):
    return a+b, a-b, a*b, a/b

calc(4, 2)
print(calc(4, 2))       # (6, 2, 8, 2.0)
res = calc(4, 2)
print(res)      # (6, 2, 8, 2.0)

add, sub, mul, div = calc(4, 2)
print(add, sub, mul, div, sep='\n')
"""
6
2
8
2.0
"""

# l = [1, 2, 3, 2, 2, 2]
# l.count(2)
# print(l.count(2))   # 4
#
# 4
# print(4)
#
# l.append(10)
# print(l.append(10))     # None


def reverse4(st):
    rev = ''
    for ch in st:
        rev = ch + rev
    return rev

print(reverse4('hello'))


# Type 3

def reverse3():
    st = 'hello'
    rev = ''
    for i in st:
        rev = i + rev
    return rev

print(reverse3())   # olleh
res = reverse3()
print(res)


