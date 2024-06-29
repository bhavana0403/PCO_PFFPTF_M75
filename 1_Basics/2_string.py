# string
"""
-> String is a collection of characters enclosed between single quotes, double
   quotes or 3 pairs of single or double quotes
-> The characters can be either uppercase or lowercase or special characters or digits
-> Syntax:
            Var = 'Val1Val2.........Valn'
            Var = "Val1Val2.........Valn"
            Var = '''Val1Val2.........Valn'''
-> Even though we create a string using double quotes or 3 pairs of quotes, internally
   it will be stored in the form of single quotes only
-> The default value of string is ''
"""

st = 'hello'        # 'hello'
st1 = "hello"       # 'hello'
st2 = '''hello'''   # 'hello'
st3 = """hello"""   # 'hello'

st = ''
print(st)           # ''
print(type(st))     # ''
print(bool(st))     # False

##################################################################################

# st = 'hello everyone, welcome to python's world'    # SyntaxError

"""
-> We make use of escape character when we want to write a single quote inside the string
"""

st = 'hello everyone, welcome to python\'s world'
print(st)   # hello everyone, welcome to python's world

"""
-> We can make use of double quoted string if we want to write a single quote inside 
   the string
"""

st = "hello everyone, welcome to python's world"
print(st)   # hello everyone, welcome to python's world

####################################################################################

path = 'C:\testing\performance\new folder\soaktesting.txt'
print(path)
"""
C:	esting\performance
ew folder\soaktesting.txt
"""

"""
-> We can make use of escape character to remvoe the special meaning
"""
path = 'C:\\testing\performance\\new folder\soaktesting.txt'
print(path)     # C:\testing\performance\new folder\soaktesting.txt

"""
-> We make use of raw string('r' or 'R') to remove the special meaning
"""

path = r'C:\testing\performance\new folder\soaktesting.txt'
print(path)

##################################################################################

st = ('hello everyone'
      'how are you'
      'how was your day')
print(st)   # hello everyonehow are youhow was your day

st = """hello everyone
how are you
how was your day"""
print(st)
"""
hello everyone
how are you
how was your day
"""
"""
-> WE make use of triple quotes to write multiple lines of string and also for
   comment purpose
-> Triple quoted string is also known as doc string
"""
###################################################################################

