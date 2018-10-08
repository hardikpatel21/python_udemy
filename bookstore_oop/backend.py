"""
A backend program to interact with the database and
gives proper out put on the frontend site
"""

import sqlite3

class Database:
    # connect to database
    # define __init__ function which is being called whenever database object is called
    # __init__ is also called constructor
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn INTEGER)")
        self.conn.commit()


    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * from book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * from book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    # Create desructor
    # __del__ is refered as destroctor
    def __del__(self):
        self.conn.close()


# connect()
# insert("The Sun", "John Smith", 1918, 913123132)
# delete(2)
# update(3,"The moon", "John Smooth", 1917, 999999)
# print(view())
# print(search(author="John Smith"))
