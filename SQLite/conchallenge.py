import sqlite3

db = sqlite3.connect("contacts.sqlite")
#challenge2
user_input = input("Please enter the name to search ")
update_sql = "Select * from contacts where name = ? "
cursor = db.cursor()
print(user_input)
#cursor.execute("select * from contacts")
cursor.execute(update_sql, (user_input,))

print(cursor.fetchall())

cursor.close()
db.close()
