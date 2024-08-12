# parameters
"""
def sam(ref1, ref2):        # formal arguments/ parameters
    pass
sam(val1, val2)             # actual arguments/ arguments
"""

# def sam(a, b):
#     print(a, b)


# sam(1, 2)       # 1 2
# sam(1)          # TypeError:


def greeting(message):
    print(message)


# greeting("Hello World")
# greeting(input('Enter the message : '))
# greeting(message)       # NameError

# st = 'python programming class'
# greeting(st)

# greeting()      # TypeError

#####################################################################################

# Types of arguments
"""
1) Positional Arguments
2) Keyword Arguments
"""

# 1) Positional Arguments

def display(name, empid, sal):
    print(f"My name is {name}, my employee ID is {empid}, I earn Rs.{sal} a month")


# display("John", "AB123", 80000)     # My name is John, my employee ID is AB123, I earn Rs.80000 a month
# display("AB123", 80000, "John")     # My name is AB123, my employee ID is 80000, I earn Rs.John a month
# # display("Alex", "AB234")        # TypeError: display() missing 1 required positional argument: 'sal'

# 2) Keyword Arguments

def sam(a, b, c):
    print(f"The values of a, b and c are {a}, {b} and {c}")


# sam(1, 2, 3)
# sam(a=1, b=2, c=3)
# sam(b=2, c=3, a=1)
# # sam(b=2, c=3)   # TypeError
#
# display(empid="ABC123", name="ALex", sal=80000)     # My name is ALex, my employee ID is ABC123, I earn Rs.80000 a month

#####################################################################################

# default parameters

def greeting(message='hai'):
    print(message)

# greeting()      # hai
# greeting("Hello World")     # Hello World


#######################################################################################

def sam(a, b=2, c=3):
    print(f"The values of a, b and c are {a}, {b} and {c}")


sam(10, 20, 30)     # The values of a, b and c are 10, 20 and 30
sam(b=20, c=30, a=10)       # The values of a, b and c are 10, 20 and 30
sam(10)                     # The values of a, b and c are 10, 2 and 3
sam(10, 20)            # The values of a, b and c are 10, 20 and 3
sam(10, 20, c=30)       # The values of a, b and c are 10, 20 and 30
sam(10, c=30)               # The values of a, b and c are 10, 2 and 30
sam(10, c=30, b=20)         # The values of a, b and c are 10, 20 and 30
# sam(a=10, 20, 30)           # SyntaxError: positional argument follows keyword argument

# sam()   # TypeError: sam() missing 1 required positional argument: 'a'

# st = 'mississippi'
# # print(st.count())       # TypeError: count() takes at least 1 argument (0 given)

