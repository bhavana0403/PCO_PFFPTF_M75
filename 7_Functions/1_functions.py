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

3) Function without arguments and with return values
4) Function with arguments and with return values
"""

# WAP to reverse the given string

st = 'hello'
rev = ''
for ch in st:
    rev = ch + rev
print(rev)

# Type1

def greeting():
    print('Hello Universe')

print(greeting)         # <function greeting at 0x000001DB2B8F04A0>
print(greeting())
"""
Hello Universe
None
"""
greeting()  # Hello Universe

# def reverse1():
#     st = input('Enter the string : ')
#     rev = ''
#     for ch in st:
#         rev = ch + rev
#     print(rev)
#
# reverse1()