import sqlite3
db = sqlite3.connect("notesdb.sqlite")
cursor = db.cursor()
cursor.execute("select * from folder")


for row in cursor:
    print(row)

db.close()