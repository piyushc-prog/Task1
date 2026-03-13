import pickle

class Book:
    # this class stores book data
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

class Student:
    # this class stores student data
    def __init__(self, student_id, student_name):
        self.student_name = student_name
        self.student_id = student_id
        self.borrowed_book = []


class Library:

    def __init__(self):
        self.books = []
        self.students = []
        self.load_data()

    #  it saves the  data using pickle
    def save_data(self):
        with open('books.pkl', 'wb') as f:
            pickle.dump(self.books, f)

        with open('students.pkl', 'wb') as f:
            pickle.dump(self.students, f)

    # the method load data from the pickle
    def load_data(self):
        try:
            with open('books.pkl', 'rb') as f:
                self.books = pickle.load(f)
        except:
            self.books = []

        try:
            with open('students.pkl', 'rb') as f:
                self.students = pickle.load(f)
        except:
            self.students = []

    #  this mehtod displays the  books availabilty
    def display_book(self):

        if len(self.books) == 0:
            print("No books available")
            return

        for book in self.books:

            status = "Available" if book.available else "Borrowed"

            print(book.book_id, book.title, book.author, status)

    # this mehtod add the  student detail
    def add_student(self):

        student_id = int(input('Enter student id: '))
        name = input('Enter student name: ')

        student = Student(student_id, name)

        self.students.append(student)

        self.save_data()

        print("Student added successfully")

    # add book
    def add_book(self):

        book_id = int(input('Enter book id: '))
        title = input('Enter title: ')
        author = input('Enter author: ')

        book = Book(book_id, title, author)

        self.books.append(book)

        self.save_data()

        print("Book added successfully")

    # lend book
    def lend_book(self):

        book_id = int(input('Enter book id: '))
        student_id = int(input('Enter student id: '))

        for book in self.books:

            if book.book_id == book_id and book.available:

                for student in self.students:

                    if student.student_id == student_id:

                        book.available = False
                        student.borrowed_book.append(book_id)

                        self.save_data()

                        print('Book lent successfully')

                        return

        print('Book not available or student not found')

    # return book
    def return_book(self):

        book_id = int(input('Enter book id: '))
        student_id = int(input('Enter student id: '))

        for student in self.students:

            if student.student_id == student_id and book_id in student.borrowed_book:

                student.borrowed_book.remove(book_id)

                for book in self.books:

                    if book.book_id == book_id:
                        book.available = True

                self.save_data()

                print('Book returned successfully')

                return

        print('Invalid return')

    # delete book
    def delete_book(self):

        book_id = int(input('Enter book id: '))

        for book in self.books:

            if book.book_id == book_id:

                self.books.remove(book)

                self.save_data()

                print('Book deleted')

                return

        print("Book not found")

    # menu
    def menu(self):

        while True:

            print('''

1 Press 1 to Add Book
2 Press 2 to Display Books
3 Press 3 to Add Student
4 Press 4 to Lend Book
5 Press 5 to Return Book
6 Press 6 to Delete Book
7 Press 7 to Exit

''')

            choice = int(input('Enter your choice: '))

            if choice == 1:
                self.add_book()

            elif choice == 2:
                self.display_book()

            elif choice == 3:
                self.add_student()

            elif choice == 4:
                self.lend_book()

            elif choice == 5:
                self.return_book()

            elif choice == 6:
                self.delete_book()

            elif choice == 7:
                print("Exiting...")
                break

            else:
                print("Invalid choice")


# start program
lib = Library()
lib.menu()