import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "neweamil@update.com"
phone = input("Please enter the phone number ")

#update_sql = "update contacts set email = 'update@update.com'"
update_sql = "update contacts set email = ? where phone = ?"
cursor = db.cursor()
cursor.execute(update_sql, (new_email, phone))
#new_statement = "update contacts set email = 'abc@email.com' where phone = 1234; update contacts set email = 'anotheremail@email.com' where phone = 6545678"
print("{} rows are affected".format(cursor.rowcount))
#cursor.executescript(new_statement)
#db.commit()

for row in db.execute("select * from contacts"):
    print(row)

cursor.close()
db.close()
