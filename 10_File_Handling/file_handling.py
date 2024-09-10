# file handling
# open() - returns the file object - we can get access to the file

sample_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\10_File_Handling\sample.txt"

# without context manager

file_obj = open(sample_path)
print(file_obj)

# file attributes
print(file_obj.name)        # C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\10_File_Handling\sample.txt
print(file_obj.mode)        # r
print(file_obj.readable())      # True
print(file_obj.writable())      # False
print(file_obj.closed)      # False

print(file_obj.close())
print(file_obj.closed)      # True

# with context manager

with open(sample_path) as file:
    print(file.name)
    print(file.closed)  # False

print(file.closed)      # True

