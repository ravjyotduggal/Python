import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE if not exists contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) values('Tim',6545678,'tim@email.com')")
db.execute("INSERT INTO contacts values('Brian', 1234, 'brian@myemail.com')")

# cursor = db.cursor()
# cursor.execute("select * from contacts")

#print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchone())

#print(cursor.fetchmany())

# for i in cursor:
#     print(i)


for row in db.execute("select * from contacts"):
    print(row)

db.commit()

#cursor.close()
db.close()

