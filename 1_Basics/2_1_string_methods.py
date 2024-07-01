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

# 14)
