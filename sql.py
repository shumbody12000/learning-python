######
#Learning Python
#David
###########
#connect to sqlite
#clear the terminal screen
import sqlite3
import os
os .system('clear')


#connect to database
conn = sqlite3.connect('customers.db')
#create a cursor
c = conn.cursor()
#create table
'''
c.execute("""CREATE TABLE customers(
			first_name text,
			last_name text,
			email text
			)""")

c.execute("INSERT INTO customers VALUES ('john','elder','j@d.com')")
'''
c.execute("SELECT * from customers")
items = c.fetchall()

for name in items:
	print(name[0] + " " + name [1])

#commit our changes
conn.commit()


#close database connection
conn.close()


