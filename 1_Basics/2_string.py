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

# Memory Allocation of Sequential Datatype
"""
-> When the value is a sequential datatype, a layer of memory will be created in 
   value space which gets divided into number of blocks which is equal to length of
   the collection.
-> Each value of the collection will get stored in individual blocks.
-> Once after storing all the values, an address will be given to this memory
   layer which gets stored wrt variable name in variable space
"""

# Indexing
"""
-> We can get individual values from the collection using index numbers
-> There are 2 types
      1) positive indexing - positive index numbers are given from left to right
                             of the collection starting from 0 to len(coll)-1
      2) negative indexing - negative index numbers are given from right to left 
                             of the collection starting from -1 to -len(collection)
-> To access individual values we make use of the syntax
            Var[index_no]
-> Even if we make use of negative indexing, internally it will be considered as
   positive indexing only
-> To modify the values of sequential collection we make use of the syntax
            Var[index_no] = new_value
"""

st = "Hai Mary"
"""
-8	-7	-6	-5	-4	-3	-2	-1
 H	 a	 i 		 M	 a	 r	 y
 0	 1	 2	 3	 4	 5	 6	 7
"""
print(st)
print(len(st))

print(st[4])      # M
print(st[-2])     # r

# st[4] = 'm'       # TypeError

"""
-> String doesn't allow to modify it's values
-> String is a immutable collection
-> A collection that does not allow the user to modify or add or remove the values
"""

st = 'mississippi'
st1 = 'pepsi'
"""
-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
 m 	 i	 s	 s	 i	 s	 s	 i	 p	 p	 i
 0	 1	 2	 3	 4	 5	 6	 7	 8	 9	 10
 
-5 -4  -3  -2  -1
p	e	p	s	i
0	1	2	3	4
"""

print(id(st[2]))        # 140722970270448
print(id(st[3]))        # 140722970270448
print(id(st1[3]))       # 140722970270448
print(id(st[-5]))       # 140722970270448






