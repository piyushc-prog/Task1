import psycopg2
from datetime import datetime

#  Database connection
def get_db():
    return psycopg2.connect(
        host="localhost",
        database="library_db",
        user="postgres",
        password="1234",
        port=5432
    )


class User:
    def __init__(self, user_id, password, role):
        self.user_id = user_id
        self.password = password
        self.role = role

  
class LibraryUser(User):
    def __init__(self, user_id, password, role):
        super().__init__(user_id, password, role)
        self.borrowed_books = []

class Library:

   
    def login(self):
        user_id = int(input("Enter ID: "))
        password = input("Enter Password: ")

        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            SELECT role FROM users
            WHERE user_id=%s AND password=%s
        """, (user_id, password))

        result = cur.fetchone()
        conn.close()

        if result:
            print("Login Success")
            return LibraryUser(user_id, password, result[0])
        else:
            print("Invalid login")
            return None

  
    def add_user(self):
        conn = get_db()
        cur = conn.cursor()

        user_id = int(input("User ID: "))
        password = input("Password: ")
        name = input('Name: ')
        role = input("Role (librarian/student): ")

        cur.execute("""
            INSERT INTO users (user_id, password, 1name, role)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (user_id) DO NOTHING
        """, (user_id, password, name, role))

        conn.commit()
        conn.close()
        print("✅ User Added")

    
    def delete_user(self):
        conn = get_db()
        cur = conn.cursor()

        user_id = int(input("User ID: "))

        if user_id == 1:
            print("Cannot delete admin")
            return

        cur.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
        conn.commit()
        conn.close()
        print("✅ User Deleted")

    
    def add_book(self):
        conn = get_db()
        cur = conn.cursor()

        book_id = int(input("Book ID: "))
        title = input('Title: ')
        author = input("Author: ")
        price = float(input("Price: "))
        publisher = input("Publisher: ")

        cur.execute("""
            INSERT INTO books (book_id, title, author, price, publisher)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (book_id) DO NOTHING
        """, (book_id, title, author, price, publisher))

        cur.execute("""
            INSERT INTO inventory (book_id, count)
            VALUES (%s, 1)
            ON CONFLICT (book_id) DO UPDATE
            SET count = inventory.count + 1
        """, (book_id,))

        conn.commit()
        conn.close()
        print("✅ Book Added")

    
    def borrow_book(self, user: LibraryUser):
        conn = get_db()
        cur = conn.cursor()

        book_id = int(input("Book ID: "))

        # check user limit
        cur.execute("SELECT COUNT(*) FROM issued_books WHERE user_id=%s", (user.user_id,))
        count = cur.fetchone()[0]

        if count >= 3:
            print("Max 3 books allowed")
            return

        # check inventory
        cur.execute("SELECT count FROM inventory WHERE book_id=%s", (book_id,))
        res = cur.fetchone()

        if not res or res[0] <= 0:
            print("Book not available")
            return

        # issue book
        cur.execute("""
            INSERT INTO issued_books (book_id, user_id, issued_date)
            VALUES (%s, %s, %s)
        """, (book_id, user.user_id, datetime.now()))

        cur.execute("UPDATE inventory SET count = count - 1 WHERE book_id=%s", (book_id,))
        conn.commit()
        conn.close()

        user.borrowed_books.append(book_id)  # track in object
        print("✅ Book Borrowed")

    # Return Book
    def return_book(self, user: LibraryUser):
        conn = get_db()
        cur = conn.cursor()

        book_id = int(input("Book ID: "))

        cur.execute("""
            DELETE FROM issued_books 
            WHERE book_id=%s AND user_id=%s
        """, (book_id, user.user_id))

        cur.execute("UPDATE inventory SET count = count + 1 WHERE book_id=%s", (book_id,))
        conn.commit()
        conn.close()

        if book_id in user.borrowed_books:
            user.borrowed_books.remove(book_id)
        print("✅ Book Returned")

    # Menu
    def menu(self):
        user = self.login()
        if not user:
            return

        while True:
            print("\n1 Add Book\n2 Borrow Book\n3 Return Book\n0 Exit")
            ch = int(input("Choice: "))

            if ch == 1 and user.role == "librarian":
                self.add_book()
            elif ch == 2:
                self.borrow_book(user)
            elif ch == 3:
                self.return_book(user)
            elif ch == 0:
                break
            else:
                print("Invalid / Unauthorized")


if __name__ == "__main__":
    lib = Library()
    lib.menu()