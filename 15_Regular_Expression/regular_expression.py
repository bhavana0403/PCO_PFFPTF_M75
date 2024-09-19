# regular expression
"""
-> Here we write an expression to match the patterns and get the data from a huge data
-> to work with expressions we have to import re module
"""

import re

# Character
"""
. -> matches any character except new line
\. -> matches a dot
\\ -> match backslash
\* -> matches astrick
"""

# Character Set
"""
[abcd] -> matches either a or b or c or d
[^abcd] -> matches any character except a or b or c or d
[234] -> matches '2' or '3' or '4'
[^234] -> matches any character except '2' or '3' or '4'
[aeiouAEIOU] -> matches any vowel
[a-z] -> matches any lowercase character
[A-Z] -> matches any uppercase characters
[0-9] -> matches any numeric characters
[a-zA-Z] -> matches any alphabet
[A-Za-z0-9] -> matches alphanumeric character
"""

# special characters
"""
\w -> word character same as [A-Za-z0-9_] -> matches alphanumeric and _ 
\W -> non-word character same as [^A-Za-z0-9_] 
\d -> matches a digit same as [0-9]
\D -> matches a non-digit, same as [^0-9]
\s -> matches only whitespace
\S -> matches non white space
"""

# anchors
"""
\b -> word boundary
\B -> not a word boundary
[] -> matches characters in square bracket
[^] -> matches all the characters except the one in square bracket
"""

# Quantifiers
"""
* -> match the expression 0 or more times
+ -> match the expression 1 or more times
? -> matches the expression 0 or 1 time
{min,max} -> matches atleast 'min' number of characters and atmost 'max' number of
             characters
{num} -> matches exactly 'num' values 
"""

# Grouping
"""
(A|B|C) -> match either A or B or C
"""

# word boundary (\b)
"""
-> start of the word is where sequence of alphanumeric characters begin
-> end of the word is where sequence of alphanumeric characters end
-> Rule: The match that begins teh earliest wins
        Ex: 'abcda', st = 'abcdabcda'
"""

# functions
"""
re.findall(expression, string) -> return a list of all the matches
"""

print(re.findall(r"the", "the theory of relativity"))       # ['the', 'the']

print(re.findall(r"cat", "the dragging belly indicates the cat is too fat"))    # ['cat', 'cat']

print(re.findall(r"python", "python is a programming language"))    # ['python']

print(re.findall(r"aeiou", "hello how are you"))        # []

print(re.findall(r"[aeiou]", "hello how are you"))      # ['e', 'o', 'o', 'a', 'e', 'o', 'u']

print(len(re.findall(r"[aeiou]", "hello how are you")))       # 7

print(''.join(re.findall(r"[aeiou]", "hello how are you")))     # eooaeou

# match smith and Smith

print(re.findall(r"smith", "SilverSmith and goldsmith"))        # ['smith']

print(re.findall(r"Smith", "SilverSmith and goldsmith"))        # ['Smith']

print(re.findall(r"[sSmith]", "SilverSmith and goldsmith"))     # ['S', 'i', 'S', 'm', 'i', 't', 'h', 's', 'm', 'i', 't', 'h']

print(re.findall(r"[sS]mith", "SilverSmith and goldsmith"))     # ['Smith', 'smith']

# match seperate and separate
print(re.findall(r"sep[ae]rate", "seperate and separate"))      # ['seperate', 'separate']

# grey and gray

# count the vowels in a string
st = "python prOgrammIng"
print(len(re.findall(r"[aeiouAEIOU]", st)))     # 4

# match any number between 0 to 9
st = "The cost of 10 gram gold is Rs. 75640"
print(re.findall(r"[0123456789]", st))      # ['1', '0', '7', '5', '6', '4', '0']

print(re.findall(r"[0-9]", st))     # ['1', '0', '7', '5', '6', '4', '0']

# match all html header tags -> <h1> <h2> <h3> <h4> <h5> <h6>
print(re.findall(r"<h[1-6]>", "<h1> <h2> <h3> <h4> <h5> <h6>"))

# match all lowercase characters
print(re.findall(r"[a-z]", "Hello HoW ArE YOu"))        # ['e', 'l', 'l', 'o', 'o', 'r', 'u']

# match all uppercase characters
print(re.findall(r"[A-Z]", "Hello HoW ArE YOu"))        # ['H', 'H', 'W', 'A', 'E', 'Y', 'O']

# match both uc and lc
print(re.findall(r"[A-Za-z]", "Hello HoW ArE YOu"))

# count the total number of alphabets
print(len(re.findall(r"[A-Za-z]", "Hello HoW ArE YOu")))        # 14

# count the number of white spaces
print(len(re.findall(r"\s", "Hello HoW ArE YOu")))   # 3





