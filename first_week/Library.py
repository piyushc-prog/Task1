import psycopg2
from datetime import datetime

# 🔹 This method makes the Db Connection
def get_db():
    return psycopg2.connect(
        host="localhost",
        database="library_db",
        user="postgres",
        password="1234",
        port=5432
    )


#  THis is parent class
class User:
    def __init__(self, user_id, password, role):
        self.user_id = user_id
        self.password = password
        self.role = role


class Library:

    # this is login method
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
            return User(user_id, password, result[0])
        else:
            print("Invalid login")
            return None

    # This method adds an user 
    def add_user(self):
        conn = get_db()
        cur = conn.cursor()

        user_id = int(input("User ID: ")),
        password = input("Password: "),
        name = input('Name'),
        role = input("Role (librarian/student): ")

        cur.execute("""
            INSERT INTO users (user_id, password, 1name, role)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (user_id) DO NOTHING
        """, (user_id, password, name, role))

        conn.commit()
        conn.close()
        print("✅ User Added")

    # this method delete an user
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

    # 
    def add_book(self):
        conn = get_db()
        cur = conn.cursor()

        book_id = int(input("Book ID: ")),
        title = input('Title:'),
        author = input("Author: "),
        price = float(input("Price: ")),
        publisher = input("Publisher: ")

        print(book_id, title, author, price, publisher)
        cur.execute("""
            INSERT INTO books (book_id, title, author, price, publisher)
                    VALUES (%s, %s, %s, %s, %s)
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

    # this method deltes an book from the db
    def delete_book(self):
        conn = get_db()
        cur = conn.cursor()
    

        book_id = int(input("Book ID: "))

        cur.execute("DELETE FROM inventory WHERE book_id=%s", (book_id,))
        cur.execute("DELETE FROM books WHERE book_id=%s", (book_id,))

        conn.commit()
        conn.close()
        print("✅ Book Deleted")

    # this method displays the available books
    def display_books(self):
        conn = get_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM books")
        books = cur.fetchall()

        if not books:
            print("No books found")
            return

        print("\n BOOK LIST:")
        print("-" * 50)

        for b in books:
            print(f"""
    ID: {b[1]}
    Title: {b[2]}
    Author: {b[3]}
    Price: {b[4]}
    Publisher: {b[5]}
    ---------------------------
    """)

        conn.close()

    # this method check the inventory
    def check_inventory(self):
        conn = get_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM inventory")
        for row in cur.fetchall():
            print(row)

        conn.close()

    # this method issues the book
    def issued_books(self):
        conn = get_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM issued_books")
        for row in cur.fetchall():
            print(row)

        conn.close()

    # this method os is used to borrorw books
    def borrow_book(self, user):
        conn = get_db()
        cur = conn.cursor()

        book_id = int(input("Book ID: "))

        # here we check the limit
        cur.execute("""
            SELECT COUNT(*) FROM issued_books WHERE user_id=%s
        """, (user.user_id,))
        count = cur.fetchone()[0]

        if count >= 3:
            print("Max 3 books allowed")
            return

        # it checks the stock
        cur.execute("SELECT count FROM inventory WHERE book_id=%s", (book_id,))
        res = cur.fetchone()

        if not res or res[0] <= 0:
            print(" Book not available")
            return

        # this issues a book
        cur.execute("""
            INSERT INTO issued_books (book_id, user_id, issued_date)
            VALUES (%s, %s, %s)
        """, (book_id, user.user_id, datetime.now()))

        cur.execute("""
            UPDATE inventory SET count = count - 1 WHERE book_id=%s
        """, (book_id,))

        conn.commit()
        conn.close()
        print("✅ Book Borrowed")

    # this method return the book
    def return_book(self, user):
        conn = get_db()
        cur = conn.cursor()

        book_id = int(input("Book ID: "))

        cur.execute("""
            DELETE FROM issued_books 
            WHERE book_id=%s AND user_id=%s
        """, (book_id, user.user_id))

        cur.execute("""
            UPDATE inventory SET count = count + 1 WHERE book_id=%s
        """, (book_id,))

        conn.commit()
        conn.close()
        print("✅ Book Returned")

    # this is menu from which each method can be called 
    def menu(self):
        user = self.login()
        if not user:
            return

        while True:
            print("\n1 Add Book\n2 Display Books\n3 Borrow Book\n4 Return Book\n5 Inventory\n6 Issued Books\n7 Add User\n8 Delete User\n0 Exit")

            ch = int(input("Choice: "))

            if ch == 1 and user.role == "librarian":
                self.add_book()
            elif ch == 2:
                self.display_books()
            elif ch == 3:
                self.borrow_book(user)
            elif ch == 4:
                self.return_book(user)
            elif ch == 5 and user.role == "librarian":
                self.check_inventory()
            elif ch == 6 and user.role == "librarian":
                self.issued_books()
            elif ch == 7 and user.role == "librarian":
                self.add_user()
            elif ch == 8 and user.role == "librarian":
                self.delete_user()
            elif ch == 0:
                break
            else:
                print("Invalid / Unauthorized")



if __name__ == "__main__":
    lib = Library()
    lib.menu()