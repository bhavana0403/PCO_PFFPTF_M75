# if else statement
"""
-> if the condition is True, control will execute TSB, if the condition is False,
   control will execute FSB
-> Syntax:
            if <condition>:
                TSB
            else:
                FSB
"""

# 1) WAP to check if a given number is even or odd

# num = int(input('Enter the number : '))
# if num % 2 == 0:
#     print('The given number is even number')
# else:
#     print('The given number is odd number')

# 2) WAP to check if a given character is a lowercase character
# char = input('Enter the character : ')
# if 'a'<=char<='z':
#     print('Lowercase Character')
# else:
#     print('not a lowercase character')

# 3) WAP to check if a character is a  special character or an alphanumeric character
# ch = input('Enter the character : ')
# if not('A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9'):
#     print('Special Character')
# else:
#     print('Alphanumeric Character')

# 4) WAP to check if a given data is a single value datatype

# data = eval(input('Enter the data : '))
# if type(data) in [int, float, complex, bool]:
#     print('Single Value Datatype')
# else:
#     print('Multi value datatype')

# 5) WAP to check whether the given data is a mutable datatype

# 6) WAP to check if a character is a vowel

# char = input('Enter the character : ')
# if char in 'aeiouAEIOU':
#     print('Vowel')
# else:
#     print('Not a vowel')

# 7) WAP to check if a given character is a consonant
# ch = input('Enter the character : ')
# if ('A' <= ch <= 'Z' or 'a' <= ch <= 'z') and ch not in 'aeiouAEIOU':
#     print('Consonant')
# else:
#     print('Not a consonant')

# 8) WAP to check if a character is present in a string
# st = input('Enter the string : ')
# ch = input('Enter the character : ')
# if ch in st:
#     print(True)
# else:
#     print(False)

# 9) WAP to check if a given string is a palindrome
"""mam, mom, malayalam, racecar, rotator, etc"""
# st = input('Enter the string : ')
# if st == st[::-1]:
#     print(f"The given string '{st}' is a palindrome")
# else:
#     print(f"The given string '{st}' is not a palindrome")

# 10) WAP to check if a string has even number of values
# st = input('Enter the string : ')
# if len(st) % 2 == 0:
#     print('The string has even number of values')
# else:
#     print('The string has odd number of values')

# 11) WAP to check if a given list has a mid-value, if it has then print the mid-value

li = [10, 20, 30, 40, 50, 80, 87]
if len(li) % 2 != 0:
    print('The list has a mid-value')
    mid_value = li[len(li)//2]
    print(mid_value)
else:
    print('The list does not have a mid-value')

"""
len     mid_index
1           0
3           1
5           2
7           3
.
.
n         n//2     
"""

# 15) WAP to check if a given number is a palindrome

# num = int(input())
# if str(num) == str(num)[::-1]:
#     print('Palindrome')
# else:
#     print('Not a palindrome')



