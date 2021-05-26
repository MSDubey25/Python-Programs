import sqlite3 as sql


class dbconnection:
    def __init__(self):
        print("Initializing DB")

    def connect(self):

        con = sql.connect('database.db')
        print("Opened Database successfully")
        con.execute("CREATE TABLE students (name TEXT primary_key=true, addr TEXT, city TEXT, pin TEXT)")
        print("Table Created Successfully")
        con.close()

#db = dbconnection()
#db.connect()