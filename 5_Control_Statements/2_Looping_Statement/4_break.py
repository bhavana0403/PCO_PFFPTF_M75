# break
"""
-> It is a keyword which is used to terminate from the loop
-> we can break both for and while loop
"""

# for i in range(1, 11):
#     print(i)
#     if i == 5:
#         break
"""
1
2
3
4
5
"""

# 1) WAP to print the index of first occurrence of a given character in a string
# st = 'mississippi'
# ch = 's'
# for i in range(len(st)):
#     if st[i] == ch:
#         print(i)
#         break

# 2) WAP to print the index of second occurrence of a given character in a string
# st = 'mississippi'
# ch = 's'
# count = 0
# for i in range(len(st)):
#     if st[i] == ch:
#         count += 1
#         if count == 2:      # i is having 2nd index of ch
#             print(i)
#             break

"""
3) WAP to print the index of first occurrence of a given character in a string, if the
   character is not present then print False
"""
# st = 'mississippi'
# ch = 'z'
# for i in range(len(st)):
#     if st[i] == ch:
#         print(i)
#         break
# else:
#     print(False)

# 4) WAP to print the first vowel in a given string

# st = 'rgh'
# for i in st:
#     if i in 'aeiouAEIOU':
#         print(i)
#         break
# else:
#     print(False)

# 5) WAP to print the no of occurrence of the first vowel in a given string

st = 'gmail youtube facebook instagram'
for i in st:
    if i in 'aeiouAEIOU':
        break

count = 0
for j in st:
    if j == i:
        count += 1
print(f"The first vowel in the string is '{i}' and is present {count} number of times")


# 6) WAP to check if a given list is homogenous

# li = [1, 2.8, 3, 4, 5]
# for i in li:
#     if type(i) != type(li[0]):
#         print('Heterogeneous List')
#         break
# else:
#     print('Homogenous List')

# 7) WAP to check whether a given number is a prime number

# num = 289
# """
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20
# """
# for i in range(2, num):
#     if num % i == 0:        # if i is a factor of num
#         print('Not a prime number')
#         break
# else:
#     print('Prime number')


# from math import sqrt
# for i in range(2, round(sqrt(num))+1):
#     if num % i == 0:        # if i is a factor of num
#         print('Not a prime number')
#         break
# else:
#     print('Prime number')

# 8) WAP to check if a given string has only alphabets
# st = 'HeLlo'
# for i in st:
#     if not ('A' <= i <= 'Z' or 'a' <= i <= 'z'):
#         print(False)
#         break
# else:
#     print(True)


# 9) WAP to check if a given string has only uppercase characters
# 10) WAP to check if a given string has only lowercase characters
# 11) WAP to check if a given string has only numeric characters
# 12) WAP to check if a given string has only special characters

# 13) Guessing the number

num = 545
while True:
    n = int(input("Guess the number : "))
    if n == num:
        print("Hurray!!!! Correct Guess")
        break
    elif n < num:
        print("Enter a larger number")
        print()
    else:
        print("Enter a lesser number")
        print()

