# csv -> comma separated value
# to handle csv file we have to import csv module

import csv

# Read from a file
"""
We can read a csv file in 2 ways
1) list of strings - csv.reader(file_obj)
2) dictionary - csv.DictReader(file_obj)
"""

example_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\12_CSV_File_Handling\example.csv"

# Reader
with open(example_path) as file:
    reader_obj = csv.reader(file)
    # print(reader_obj)
    next(reader_obj)
    for line in reader_obj:
        print(line)

"""
['John', 'TY123', 'Bengaluru']
['Mary', 'TY124', 'Chennai']
['Joseph', 'TY125', 'Hyderabad']
['Steve', 'TY126', 'Mumbai']
['Alex', 'TY127', 'Bengaluru']
['Bob', 'TY128', 'Hyderabad']
"""

# DictReader
with open(example_path) as file:
    reader_obj = csv.DictReader(file)
    for data in reader_obj:
        print(data)
"""
{'name': 'John', 'emp_id': 'TY123', 'place': 'Bengaluru'}
{'name': 'Mary', 'emp_id': 'TY124', 'place': 'Chennai'}
{'name': 'Joseph', 'emp_id': 'TY125', 'place': 'Hyderabad'}
{'name': 'Steve', 'emp_id': 'TY126', 'place': 'Mumbai'}
{'name': 'Alex', 'emp_id': 'TY127', 'place': 'Bengaluru'}
{'name': 'Bob', 'emp_id': 'TY128', 'place': 'Hyderabad'}
"""

#############################################################################

# write into a file
"""
-> To write into a csv file we have to create a writer object by passing file object to it
-> 1) writer
        writer_obj = csv.writer(file_obj)
        -> writerow() - list of data
        -> writerows() - nested list of data
    2) DictWriter
        writer_obj = csv.DictWriter(file_obj)
        -> writeheader() - to write fieldnames
        -> writerow() - dictionary
        -> writerows() - list of dictionaries
"""


# writer

path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\12_CSV_File_Handling\sample.csv"

with open(path, 'w') as file:
    writer_obj = csv.writer(file)
    data = ['name', 'phno', 'salary']
    writer_obj.writerow(data)
    writer_obj.writerows([
        ['Ram', '9191919191', '65000'],
        ['Sita', '9292929292', '90000'],
        ['Laxman', '9393939393', '60000']
    ])


# DictWriter
path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\12_CSV_File_Handling\sample1.csv"
with open(path, 'w') as file:
    writer_obj = csv.DictWriter(file, ['name', 'empid', 'salary'])
    writer_obj.writeheader()
    writer_obj.writerow({'name': "Ram", "empid": "ABC123", "salary": '70000'})
    writer_obj.writerows([
        {'name': "Sita", "empid": "AB142", "salary": "80000"},
        {'name': "Laxman", "empid": "AB234", "salary": "90000"}
    ])

###############################################################################

# print all the names in employess.csv

employee_path = r"C:\Users\QSP\PycharmProjects\PCO_PFFPTD_E75\12_CSV_File_Handling\employees.csv"

# with open(employee_path) as file:
#     reader_obj = csv.reader(file)
#     names = []
#     next(reader_obj)
#     for line in reader_obj:
#         names += [line[0]]
#     print(names)

# with open(employee_path) as file:
#     reader_obj = csv.DictReader(file)
#     names = []
#     for data in reader_obj:
#         names.append(data['name'])
#     print(names)


###############################################################################

# group the male and female employees

# with open(employee_path) as file:
#     reader_obj = csv.reader(file)
#     next(reader_obj)
#     male, female = [], []
#     for line in reader_obj:
#         if line[1] == 'male':
#             male.append(line[0])
#         else:
#             female.append(line[0])
#     print(male)
#     print(female)

# with open(employee_path) as file:
#     reader_obj = csv.DictReader(file)
#     male, female = [], []
#     for data in reader_obj:
#         if data['gender'] == 'male':
#             male.append(data['name'])
#         else:
#             female.append(data['name'])
#     print(female)
#     print(male)

# print the names of employees who earn more than 70000

# with open(employee_path) as file:
#     reader_obj = csv.DictReader(file)
#     for data in reader_obj:
#         if int(data['pay']) >= 70000:
#             print(data['name'])


# print the names of employees who earn more than the average salary

# with open(employee_path) as file:
#     reader_obj = csv.DictReader(file)
#     salaries = [int(data['pay']) for data in reader_obj]
#     print(salaries)
#     avg_sal = sum(salaries) // len(salaries)
#     print(avg_sal)
#     file.seek(0)
#     reader_obj = csv.DictReader(file)
#     for data in reader_obj:
#         if int(data['pay']) >= avg_sal:
#             print(data['name'])


####################################################################

# print the names of employees who earn the least and most salary

with open(employee_path) as file:
    reader_obj = csv.reader(file)
    next(reader_obj)
    by_pay = sorted(reader_obj, key=lambda line: int(line[3]))
    # print(by_pay)
    least, *rest, highest = by_pay
    print(least)
    print(highest)

with open(employee_path) as file:
    reader_obj = csv.DictReader(file)
    by_pay = sorted(reader_obj, key=lambda data: int(data['pay']))
    least, *rest, highest = by_pay
    print(least)
    print(highest)

