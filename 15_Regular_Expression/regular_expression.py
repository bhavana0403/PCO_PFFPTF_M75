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
