# string methods

# 1) upper
"""
-> It is a method which is used to convert lowercase characters to uppercase characters
   and print it.
-> Syntax:
        Var.upper()
-> String methods do not modify the original string
-> The return type of upper is a string
"""

# st = 'hello'
# print(st.upper())   # HELLO
# print(st)           # hello
#
# print('HeLLO WoRlD 123@#$'.upper())     # HELLO WORLD 123@#$

##################################################################################

# 2) lower()
"""
-> It is a method which is used to convert all the uppercase characters to 
   lowercase characters
-> Syntax:
        Var.lower()
-> The return type of lower is a string
"""

# print('HeLLO WoRlD 123@#$'.lower())     # hello world 123@#$

#####################################################################################

# 3) swapcase
"""
-> It is used to convert uppercase to lowercase and lowercase to uppercase
-> Syntax:
        Var.swapcase()
-> The retun type of swapcase is a string
"""

# st = "heLLo WorLd"
# print(st.swapcase())    # HEllO wORlD

#####################################################################################

# 4) title()
"""
-> It is used to convert the given string to title format
-> Syntax:
        Var.title()
-> The return type of title is a string
"""

# book = "the stories of mahabharata"
# print(book.title())     # The Stories Of Mahabharata
#
# book = "the 4tune teller"
# print(book.title())     # The 4Tune Teller
#
# print('ONE MAN ARMY'.title())   # One Man Army

####################################################################################

# 5) capitalize
"""
-> It is used to convert the first character of a string to uppercase and all the 
   other alphabets to lowercase
-> Syntax:
        Var.capitalize()
-> The return type of capitalize is a string
"""

# book = "the stories of mahabharata"
# print(book.capitalize())    # The stories of mahabharata
#
# book = '3 mistakes of my life'
# print(book.capitalize())    # 3 mistakes of my life
#
# book = '4tune teller'
# print(book.capitalize())    # 4tune teller

#####################################################################################

# 6) isupper()
"""
-> It is used to check whether all the alphabets in the string are uppercase alphabets
-> Syntax:
        Var.isupper()
-> The return type of isupper is boolean
"""

# st = 'HELLO'
# print(st.isupper())     # True
#
# print('HELLO WORLD'.isupper())      # True
#
# print('HELLO 123@')     # True
#
# print('HELLo'.isupper())    # False

#################################################################################

 # 7) islower
"""
 
"""
st = 'hello world'
print(st.islower())    # True

#################################################################################

# 8) istitle
"""

"""

print('THE ONE MAN ARMY'.istitle())     # False

print('One Man Army'.istitle())     # True

###################################################################################

# 9) isalpha()
"""
-> It is used to check whether the string has only alphabets
-> Syntax:
        Var.isalpha()
-> The return type of isalpha is boolean
"""

st = 'python'
print(st.isalpha())     # True

print('PYTHON'.isalpha())   # True

print('hello WORLD'.isalpha())      # False

print('h@I'.isalpha())      # False

##################################################################################

# 10) isdigit()
"""

"""

st = '9845 123 654'
print(st.isdigit())     # FAlse

ph_no = '8123458765'
print(ph_no.isdigit())      # True

##################################################################################

# 11) isalnum
"""

"""

print('APPle 120'.isalnum())      # False
print('APpLe120'.isalnum())         # True
print('APPLE'.isalnum())        # True
print('apple'.isalnum())        # True
print('1234'.isalnum())         # True

###################################################################################

# 12) startswith
"""
-> It is used to check whether a string is starting with a specified substring
-> Syntax:
        Var.startswith(substring) 
-> The return type of startswith is 
"""

print('hello universe'.startswith('he'))    # True
print('hello universe'.startswith('H'))     # False

print('python class'.startswith('pYTHOn'))  # False

####################################################################################

# 13) endswith

#################################################################################

# 14) count
"""
-> It is used to count the number of times a substring is present in the string
-> Syntax:
            Var.count(substring)
            Var.count(substring, SI)
            Var.count(substring, SI, EI)
-> The return type of count is an integer
-> If the substring is not present, count will return 0
"""

st = 'mississippi'
print(st.count('i'))        # 4
print(st.count('i', 2))     # 3
print(st.count('i', 3, 7))      # 1
print(st.count('ssi'))      # 2

print(st.count('z'))    # 0


# print(st.count('i', 2))

#################################################################################

# 15) index
"""
-> It is used to get the index of first occurrence of given substring in a string,
   within the specified limits
-> Syntax:
            Var.index(substring)
            Var.index(substring, SI)
            Var.index(substring, SI, EI)
-> The return type of index is integer
-> If the value is not present, control will throw ValueError
"""

st = 'mississippi'
print(st.index('i'))        # 1
print(st.index('ssi'))      # 2

print(st.index('s', 4))     # 5

print(st.index('i', 2, 10))     # 4

# print(st.index('z'))        # ValueError: substring not found

# print(st[13])       # IndexError

# print(st.index('i', 15, 20))        # ValueError: substring not found

#################################################################################

# 16) rindex
"""
-> It is used to get the index of first occurrence of a given substring from right 
   to left of the collection/ specified limits
-> Syntax:
            Var.rindex(substring)
            Var.rindex(substring, SI)
            Var.rindex(substring, SI, EI)
-> The return type of index is integer
-> If the value is not present, control will throw ValueError
"""

st = 'United States'
"""
-13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
U	n	i	t	e	d		S	t	a	t	e	s
0	1	2	3	4	5	6	7	8	9	10	11	12
"""

print(st.index('e'))        # 4

print(st.rindex('e'))       # 11

print(st.rindex('t', 2, 9))     # 8

print(st.index('S', 6))     # 7

# print(st.index('Z'))        # ValueError

##################################################################################

# 17) find
"""
-> It works same as that of index method but, if the value is not present it will
   return -1 instead of throwing an error like index method
-> Syntax:
            Var.find(substring)
            Var.find(substring, SI)
            Var.find(substring, SI, EI)
-> The return type of index is integer
"""

st = 'United States'
"""
-13	-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
U	n	i	t	e	d		S	t	a	t	e	s
0	1	2	3	4	5	6	7	8	9	10	11	12
"""

print(st.index('i'))    # 2

print(st.find('i'))     # 2

# print(st.index('u'))        # ValueError

print(st.find('u'))     # -1

#################################################################################

# 18) rfind

#################################################################################

# 19) replace
"""
-> It is used to replace a substring by a new string
-> 
"""

st = 'peter piper picked a peck of pickled peppers'

print(st.replace('p', 'P'))     # Peter PiPer Picked a Peck of Pickled PePPers

print(st.replace('pe', 'Pe'))   # Peter piPer picked a Peck of pickled PepPers

print(st.replace('p', 'P', 2))      # Peter Piper picked a peck of pickled peppers

print(st.replace('x', 'X'))     # peter piper picked a peck of pickled peppers

print(st.replace('', '_'))      # _p_e_t_e_r_ _p_i_p_e_r_ _p_i_c_k_e_d_ _a_ _p_e_c_k_ _o_f_ _p_i_c_k_l_e_d_ _p_e_p_p_e_r_s_

print(st.replace(' ', '_'))     # peter_piper_picked_a_peck_of_pickled_peppers

print(st.replace(' ', '1234'))

###################################################################################

# 20) strip
"""
-> It is used to remove leading and trailing white spaces, \n, \t  characters 
   in the string
-> Syntax:
            Var.strip()     # removes leading and trailing white spaces, \n, \t
            Var.strip(ch)   # removes leading and trailing ch
-> The return type of strip is string
"""

st = '        hello world              '
print(len(st))

print(st)           # '        hello world              '
print(st.strip())       # 'hello world'

st = '______________________hello world________________'
print(st.strip())       # ______________________hello world________________
print(st.strip('_'))        # hello world

st = '___________________hello world           '

print(st)       # '___________________hello world           '
print(len(st))  # 41

print(st.strip())       # '___________________hello world'
print(len(st.strip()))  # 30

print(st.strip('_'))        # 'hello world           '

st = 'hhhhhhhhhhhhhhhhheeeeeeeeeeellllllloooooooooooooo'
print(st.strip())
print(st.strip('h'))        # eeeeeeeeeeellllllloooooooooooooo

###################################################################################

# 21) lstrip
"""
-> It is used to remove the leading whitespaces, \n, \t or specified characters
-> Syntax:
            Var.lstrip()
            Var.lstrip(ch)
"""

st = '        hello world          '
print(st.lstrip())      # 'hello world          '

st = '@@@@@@@@@@@hello world&&&&&&&&&&&&&&&'
print(st.lstrip('@'))       # hello world&&&&&&&&&&&&&&&

###################################################################################

# 22) rstrip
"""
-> It is used to remove trailing whitespaces, \n, \t or specified characters
-> Syntax:
            Var.rstrip()
            Var.rstrip(ch)
"""

st = '         hello world           '
print(st.rstrip())      # '         hello world'

st = '@@@@@@@@@@@hello world@@@@@@@@@@@@@@@@'
print(st.rstrip('@'))       # @@@@@@@@@@@hello world

st = 'jjjjjjjjjramwwwwww'
st = st.lstrip('j')
print(st)       # ramwwwwww

st = st.rstrip('w')     # ramwwwwww
print(st)       # ram

print(st.lstrip('j').rstrip('w'))       # ram

##################################################################################

# 23) split
"""
-> It is used to split the given string into list of strings
-> Syntax:
            Var.split()
            Var.split(ch)
            Var.split(ch, maxsplit=n)
            Var.split(maxsplit=n)
-> The return type of split is a list
"""

st = 'python programming is very easy'
print(st.split())       # ['python', 'programming', 'is', 'very', 'easy']

print(st.split('e'))    # ['python programming is v', 'ry ', 'asy']

print(st.split(maxsplit=2))     # ['python', 'programming', 'is very easy']

st = 'hai_hello_how_are_you_how_is_your_python_class'
print(st.split())   # ['hai_hello_how_are_you_how_is_your_python_class']

print(st.split('_'))        #

print(st.split('_', maxsplit=2))    # ['hai', 'hello', 'how_are_you_how_is_your_python_class']

print(st.split('_', 2))     # ['hai', 'hello', 'how_are_you_how_is_your_python_class']

##################################################################################

# 24) rsplit
"""

"""

st = 'python programming is very easy'

print(st.rsplit())      # ['python', 'programming', 'is', 'very', 'easy']

print(st.split(maxsplit=2))     # ['python', 'programming', 'is very easy']

print(st.rsplit(maxsplit=2))    # ['python programming is', 'very', 'easy']

##################################################################################

# 25) join
"""
-> It is used to join an iterable by a gluestring
-> Syntax:
            gluestring.join(iterable)
-> The return type of join is a string
"""

words = ['python', 'programming', 'is', 'very', 'easy']
print(' '.join(words))      # python programming is very easy

print(''.join(words))   # pythonprogrammingisveryeasy

print('_'.join(words))      # python_programming_is_very_easy

print('_'.join('abc'))      # a_b_c

# print(''.join([1, 2, 3]))       # TypeError

print('$'.join(('a', 'b', 'apple')))     # a$b$apple

##################################################################################

# 26) format
"""
-> We make use of placeholders to get dynamic input from the users
-> 
"""
emp1 = """My name is Laxmi
I am from Bengaluru
I work as a Test Enginner"""

emp2 = """My name is Mithesh
I am from Chennai
I work as a Developer"""

emp3 = """My name is Rohit
I am from Hyderabad
I work as a Data Scientist"""


emp = """My name is {}
I am from {}
I work as a {}"""

print(emp.format("Sagar", "Tamil Nadu", "Front End Developer"))
"""
My name is Sagar
I am from Tamil Nadu
I work as a Front End Developer
"""

print(emp)

emp = """My name is {0}
I am from {1}
I work as a {2}"""

print(emp.format("John", "Mangaluru", "Accounts Executive"))
"""
My name is John
I am from Mangaluru
I work as a Accounts Executive
"""

emp = """My name is {2}
I am from {0}
I work as a {1}"""

print(emp.format("John", "Mangaluru", "Accounts Executive"))
"""
My name is Accounts Executive
I am from John
I work as a Mangaluru
"""


emp = """My name is {name}
I am from {place}
I work as a {designation}"""

print(emp.format(name="John", place="Mangaluru", designation="Accounts Executive"))
"""
My name is John
I am from Mangaluru
I work as a Accounts Executive
"""

print(emp.format(place="Mangaluru", name="John", designation="Accounts Executive"))
"""
My name is John
I am from Mangaluru
I work as a Accounts Executive
"""

name = 'Bhavana'
place = "Mysuru"
designation = "Python Trainer"

emp = f"""My name is {name}
I am from {place}
I work as a {designation}"""

print(emp)
"""
My name is Bhavana
I am from Mysuru
I work as a Python Trainer
"""

name = input('Enter the name: ')
place = input('Enter the place: ')
designation = input('Enter the designation: ')

emp = f"""My name is {name}
I am from {place}
I work as a {designation}"""

print(emp)











