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

"""The above program can handle only TypeError but not other errors, we can 
create multiple except blocks to handle different types of errors"""

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
#             add()
#     except SyntaxError:
#         print("Syntax Error handled")
#         add()
#
#
# add()


# def add():
#     try:
#         a = int(input())
#         b = int(input())
#         print(a + b)
#     except ValueError as msg:
#         print(msg)
#         add()
#
# add()
#
# a = eval(input())
# b = eval(input())
# print(a / b)

# def div():
#     try:
#         a = eval(input())
#         b = eval(input())
#         print(a / b)
#     except TypeError as message:
#         print(message)
#         print('TypeError Handled')
#     except ZeroDivisionError as message:
#         print(message)
#         print('ZeroDivisionError Handled')
#     except SyntaxError:
#         print('SyntaxError Handled')
#
# div()


# 2) Generic Exception Handling
"""
-> Syntax:
        try:
            Problem Statement
        except Exception/ BaseException as msg:
            Solution
"""

# def div():
#     try:
#         a = eval(input())
#         b = eval(input())
#         print(a / b)
#     except Exception as msg:
#         print(msg)
#
# div()


# l = [10, 20, 30]
# l.remove(90)    # ValueError

# try:
#     l = [10, 20, 30]
#     l.remove(90)
# except BaseException:
#     print('Error Handled')

# while True:
#     print('Hello')

# try:
#     while True:
#         print('Hello')
# except Exception:
#     print('Error Handled')

"""
KeyboardInterrupt can not be handled by generic exception block
"""

##############################################################################

# 3) Default Exception Handling
"""
-> It can handle all kinds of exception including Keyboard Interruption
-> Syntax:
            try:
                Problem Statement
            except:
                Solution Block
"""

# try:
#     while True:
#         print('Hello')
# except:
#     print('Exception Handled')

# try:
#     print(10 / 0)
# except:
#     print('Error Handled')
#
# print('Hello')

# multiple exception blocks

def div():
    try:
        a = eval(input())
        b = eval(input())
        print(a / b)
    except TypeError as message:
        print(message)
        print('TypeError Handled')
    except Exception as msg:
        print(msg)
    except:
        print("Exception Handled")

# div()

#############################################################################

# raise exceptions as per requirement

# try:
#     actual_password = '1234'
#     entered_password = input('Enter the password : ')
#     if actual_password == entered_password:
#         print('Phone Unlocked')
#     elif entered_password.isdigit() == False:
#         raise TypeError ("Password must contain only digits")
#     elif len(entered_password) != len(actual_password):
#         raise ValueError ("Password has exactly 4 digits")
#     else:
#         raise ValueError ("Incorrect Password")
# except ValueError as message:
#     print(message)
# except TypeError as message:
#     print(message)


# Custom Exception

class PhoneLocked(Exception):
    pass

# for i in range(3):
#     try:
#         actual_password = '1234'
#         entered_password = input('Enter the password : ')
#         if actual_password == entered_password:
#             print('Phone Unlocked')
#             break
#         elif entered_password.isdigit() == False:
#             raise TypeError("Password must contain only digits")
#         elif len(entered_password) != len(actual_password):
#             raise ValueError("Password has exactly 4 digits")
#         else:
#             raise ValueError("Incorrect Password")
#     except ValueError as message:
#         print(message)
#     except TypeError as message:
#         print(message)
# else:
#     raise PhoneLocked ("No of attempts exceeded")

###############################################################################

try:
    a = eval(input())
    b = eval(input())
    print(a + b)
except TypeError:
    print('TypeError Handled')
except Exception:
    print('Generic Exception Handled')
except:
    print('Default Exception Handled')
else:
    print('In else Block')
finally:
    print('In finally block')

"""
-> else - when there are no exceptions, else block gets executed
-> finally - gets executed even if there is error or no error
-> Order 
        try -> specific -> generic -> default -> else -> finally
"""



