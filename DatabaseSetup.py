import sqlite3

#Database SETUP Script
con=sqlite3.connect("books.db")
print("Database created sucessfully!")
con.execute("""
    CREATE TABLE IF NOT EXISTS book_details (
        BookId           TEXT       NOT NULL    PRIMARY KEY,
        AuthorName       TEXT       NOT NULL,   
        BookName         TEXT       NOT NULL,
        Price            INTEGER    NOT NULL,
        Rating           INTEGER    NOT NULL,
        BookBringDate    TEXT       NOT NULL
    )
""")
print("Table created successfully!")
con.commit()
con.close()