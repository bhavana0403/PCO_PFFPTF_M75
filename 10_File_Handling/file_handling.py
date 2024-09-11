# file handling
# open() - returns the file object - we can get access to the file

sample_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\10_File_Handling\sample.txt"

# without context manager

# file_obj = open(sample_path)
# print(file_obj)

# # file attributes
# print(file_obj.name)        # C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\10_File_Handling\sample.txt
# print(file_obj.mode)        # r
# print(file_obj.readable())      # True
# print(file_obj.writable())      # False
# print(file_obj.closed)      # False
#
# print(file_obj.close())
# print(file_obj.closed)      # True

# with context manager

# with open(sample_path) as file:
#     print(file.name)
#     print(file.closed)  # False
#
# print(file.closed)      # True

###############################################################################

# Modes of file
"""
1) read - default - r
-> It is the default modw which is used to read a file
-> If the file is not existing, control will throw FileNotFoundError 

2) write - w
-> If the file is not present it creates the file in the same directory
-> If the directory is specified, the file will be created in that directory
-> if the file is already present, it will be overwritten

3) append - a
-> It is used to append the data to an existing file
-> If the file is not present, a new file will be created

4) create - x
-> It is used to create a new file and write into it
-> If the file is existing, it will throw FileExistsError
-> It is used to avoid over writing of files
"""

# 1) read - r

# without context manager

# # file_obj = open("sample1.txt")      # FileNotFoundError
# file_obj = open("sample.txt")
# print(file_obj.name)        # sample.txt
# print(file_obj.mode)        # r
# print(file_obj.readable())  # True
# print(file_obj.writable())  # False
# print(file_obj.closed)      # False
#
# file_obj.close()
# print(file_obj.closed)      # True

# with context manager

# with open("sample.txt") as file:
#     print(file.mode)
#     print(file.name)
#     print(file.closed)
#
# print(file.closed)

###############################################################################

# 2) write - w

# # file_obj = open("sample1.txt", 'w')
# # file_obj = open(r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\7_Functions\sample2.txt", 'w')
# file_obj = open(sample_path, 'w')
# print(file_obj.name)            # C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\10_File_Handling\sample.txt
# print(file_obj.mode)            # w
# print(file_obj.readable())      # False
# print(file_obj.writable())      # True

###############################################################################

# 3) append - a

# # file_obj = open("sample2.txt", 'a')
# file_obj = open("sample.txt", 'a')
# print(file_obj.name)
# print(file_obj.mode)
# print(file_obj.readable())
# print(file_obj.writable())
# print(file_obj.closed)
# file_obj.close()
# print(file_obj.closed)

################################################################################

# 4) create

# # # file_obj = open("sample3.txt", 'x')     # FileExistsError
# file_obj = open("sample4.txt", 'x')
# print(file_obj.name)            # sample4.txt
# print(file_obj.mode)            # x
# print(file_obj.readable())      # False
# print(file_obj.writable())      # True
# print(file_obj.closed)          # False
# file_obj.close()
# print(file_obj.closed)          # True

##################################################################################

# read - read(), readline(), readlines()

# read()

# with open(sample_path) as file:
#     data = file.read()
#     print(data)
#     print(type(data))

"""
good evening everyone
how are you
hope you had a good day
today's topic is file handling
<class 'str'>
"""

with open(sample_path) as file:
    print(file.read(4))
    print(file.tell())
    print(file.read(10))
    print(file.read(10))
    print(file.tell())      # 25
    print(file.seek(0))
    print(file.read(10))
    print(file.tell())      # 10








