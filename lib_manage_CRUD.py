import sqlite3

#Creating connection to the database
conn = sqlite3.connect('books.db')
print("\nSuccessfully connected to the database!")
cursor = conn.cursor()


#CRUD Functions

def EnterRecord():

    BookID = input("Enter BookID: ")
    AuthorName = input("Enter Author Name: ")
    BookName = input("Enter BookName:  ")
    Price = int(input("Enter Price: "))
    Rating = input("Enter Book's rating(out 0f 5): ")
    BookBringDate = input("Enter Book's Bring date(dd-mm-yyyy): ")
    try:
        sql_query = "INSERT INTO book_details VALUES (?,?,?,?,?,?);"
        params = (BookID, AuthorName, BookName, Price,Rating,BookBringDate)
        cursor.execute(sql_query, params)
        conn.commit()
        print("Info Added successfully!")
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)

def DisplayRecord():
    try:
        Bookid = input("Please Enter the Book ID for the Book you want to search!: ")
        sql = "SELECT * FROM book_details WHERE BookID=?"
        cursor.execute(sql, (Bookid, ))
        result = cursor.fetchone()
        print()
        print(f"BookID :{result[0]}\nAuthorName : {result[1]}\nBookName: {result[2]}\nPrice :{result[3]}\nRating(out 0f 5):{result[4]}\nBookBringDate(dd-mm-yyyy):{result[5]}")
        print()
    except (Exception, sqlite3.DatabaseError) as error:
        print("debug", error)

def UpdateRecord():
    flag = 0
    temp_id = input("Enter BookID for which do you want to update: ")
    print("Present info of the Book: ")
    try:
        sql_query6 = "SELECT * FROM book_details WHERE BookID=?"
        cursor.execute(sql_query6, (temp_id,))
        result = cursor.fetchone()
        print()
        print(f"BookID :{result[0]}\nAuthorName : {result[1]}\nBookName: {result[2]}\nPrice :{result[3]}\nRating(out 0f 5):{result[4]}\nBookBringDate(dd-mm-yyyy):{result[5]}")
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
        flag = 1
    
    if not flag:
        while True:
            print("\n1-AuthorName\n2-BookName\n3-Price\n4-Rating\n5-BookBringDate\n6-Back")
            choice2 = int(input("Enter your choice: "))  # for update choice
            if choice2 == 1:
                try:
                    sql_query2 = "UPDATE book_details SET AuthorNAME = ? WHERE BookID=?"
                    up_authorname = input("Enter new Author name: ")
                    params2 = (up_authorname, temp_id)
                    cursor.execute(sql_query2, params2)
                    conn.commit()
                    print("Info Updated successfully!!")
                except (Exception, sqlite3.DatabaseError) as error:
                    print(error)

            elif choice2 == 2:
                try:
                    sql_query3 = "UPDATE book_details SET BookName=? WHERE BookID=?"
                    up_bookname = input("Enter new Book name: ")
                    params3 = (up_bookname, temp_id)
                    cursor.execute(sql_query3, params3)
                    conn.commit()
                    print("Info Updated successfully!!")
                except (Exception, sqlite3.DatabaseError) as error:
                    print(error)

            elif choice2 == 3:
                try:
                    sql_query4 = "UPDATE book_details SET Price=? WHERE BookId=?"
                    up_price = int(input("Enter new price: "))
                    params4 = (up_price, temp_id)
                    cursor.execute(sql_query4, params4)
                    conn.commit()
                    print("Info Updated successfully!!")
                except (Exception, sqlite3.DatabaseError) as error:
                    print(error)

            elif choice2 == 4:
                try:
                    sql_query5 = "UPDATE book_details SET Rating=? WHERE BookId=?"
                    up_rating = input("Enter new book rating : ")
                    params5 = (up_rating, temp_id)
                    cursor.execute(sql_query5, params5)
                    conn.commit()
                    print("Info Updated successfully!!")
                except (Exception, sqlite3.DatabaseError) as error:
                    print(error)

            elif choice2 == 5:
                try:
                    sql_query6 = "UPDATE book_details SET BookBringDate=? WHERE BookId=?"
                    up_bookbringdate = input("Enter new book bring date: ")
                    params6 = (up_bookbringdate, temp_id)
                    cursor.execute(sql_query6, params6)
                    conn.commit()
                    print("Info Updated successfully!!")
                except (Exception, sqlite3.DatabaseError) as error:
                    print(error)

            elif choice2 == 6:
                break   
            else:
                print("Invalid choice! Please re-enter your choice: ")
    else:
        print("\nBook does not exist!\n")

def DeleteRecord():
    flag1=0
    temp_id2 = input("Enter BookID that you want to delete: ")
    print("Present info of the Book: ")
    try:
        sql_query5 = "SELECT * FROM book_details WHERE BookID=?"
        cursor.execute(sql_query5, (temp_id2,))
        result = cursor.fetchone()
        print()
        print(f"BookID :{result[0]}\nAuthorName : {result[1]}\nBookName: {result[2]}\nPrice :{result[3]}\nRating(out 0f 5):{result[4]}\nBookBringDate(dd-mm-yyyy):{result[5]}")
        print()
    except (Exception, sqlite3.DatabaseError) as error:
        print(error)
        flag1=1

    if not flag1:
        flag = int(input("Enter 1 to delete permanently: "))
        if flag == 1:
            try:
                sql_query6 = "DELETE FROM book_details WHERE BookID=?"
                cursor.execute(sql_query6, (temp_id2,))
                conn.commit()
                print("Deleted successfully!!")
            except (Exception, sqlite3.DatabaseError) as error:
                print(error)
    else:
        print("\nBook does not exist!\n")
    

#Driver Program
while True:
    print("\n----------Library Management System-----------")
    print("Press 1 to enter the records for a book")
    print("Press 2 to fetch the details for a book")
    print("Press 3 to update the details for a book")
    print("Press 4 to delete the details for a book")
    print("Press 5 to exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        EnterRecord()
        while True:
            ch1=input("Want to enter more records? Press 'y' for YES else anykey to return to main menu: ")
            print()
            if ch1!='y':
                break

            while ch1=='y':
                EnterRecord()
                ch1=''

            
    elif choice == '2':
        DisplayRecord()
        while True:
            ch2=input("Want to display more records? Press 'y' for YES else anykey to return to main menu: ")
            print()
            if ch2!='y':
                break

            while ch2=='y':
                DisplayRecord()
                ch2=''

    elif choice == '3':
        UpdateRecord()
        while True:
            ch3=input("Want to update more records? Press 'y' for YES else anykey to return to main menu: ")
            print()
            if ch3!='y':
                break

            while ch3=='y':
                UpdateRecord()
                ch3=''

    elif choice == '4':
        DeleteRecord()
        while True:
            ch4=input("Want to delete more records? Press 'y' for YES else anykey to return to main menu: ")
            print()
            if ch4!='y':
                break

            while ch4=='y':
                DeleteRecord()
                ch4=''

    elif choice == '5':
        break

    else:
        print("You've entered an invalid choice! Please enter again!!")



conn.close()
    

    

