# object method
"""
-> Methods which are used to access and modify the members of the object
-> for all object methods passing self is mandatory
-> to call the object method we make use of the syntax,
        obj_name.mname(args)
        cname.mname(self/obj, args)
"""
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     """adding a value to x and y of an object"""
#     def add_value(self, value):
#         self.x += value
#         self.y += value
#
#     """swapping the value of x and y"""
#     def swap(self):
#         self.x, self.y = self.y, self.x
#
#     """adding dx and dy to x and y"""
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     """reset x and y to 0 by default or the value specified"""
#     def reset(self, value=0):
#         self.x, self.y = value, value


# p1 = Point(10, 20)
# p2 = Point(40, 30)

# p1.add_value(5)
# Point.add_value(p2, 3)

# p1.swap()
# p2.swap()

# p1.move(0.5, 0.3)
# p2.move(10, 20)

# p1.reset()
# Point.reset(p2, 0.1)
#
# print(p1.__dict__)
# print(p2.__dict__)

# print(dir(Point))
# print(dir(p1))
# print(dir(p2))

######################################################################################

class Library:
    books = []
    def __init__(self, title, category, author):
        self.title = title
        self.category = category
        self.author = author
        Library.books.append(self)

    def display(self):
        print('*' * 50)
        print(f"Title : {self.title}")
        print(f"Category : {self.category}")
        print(f"Author : {self.author}")
        print('*' * 50)


b1 = Library("Wings Of Fire", "Autobiography", "Abdul Kalam")
b2 = Library("One Indian Girl", "Novel", "Chetan Bhagat")
b3 = Library("A Suitable Boy", "Novel", "Vikram Seth")
b4 = Library("Ghosts of the Silent Hills", "Horror", "Anita Krishan")
b5 = Library("The Girl in Room 105", "Love Story", "Chetan Bhagat")

print(Library.books)

# b1.display()
# b2.display()

# display the details of all the books
# for book in Library.books:
#     book.display()

# display the name of all the books by Chetan Bhagat
# for book in Library.books:
#     if book.author == "Chetan Bhagat":
#         print(book.title)

# display the names of all the novels
for book in Library.books:
    if book.category == "Novel":
        print(book.title)

#######################################################################################

# create a class of your choice with 3 object members
