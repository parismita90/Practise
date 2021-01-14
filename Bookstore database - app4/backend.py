import sqlite3


def connect():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM book")
    rows=curr.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("UPDATE book SET title=?, author=?,year=?,isbn=? WHERE id = ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    curr=conn.cursor()
    curr.execute("SELECT * from book where title=? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    rows1=curr.fetchall()
    conn.close()
    return rows1

connect()
#insert("The Testament","Margaret Atwood",2001,8876637672)
#delete(3)
#update(2,"The Testament","Margaret Atwood",2005,8876637672)
#print(search(year=2001))
#print(view())