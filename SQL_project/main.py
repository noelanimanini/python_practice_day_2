import sqlite3 

conn = sqlite3.connect("customer.db")

# create a cursor
cursor = conn.cursor()

# many_customers = [('West', 'Brown', 'WB@gmail.com'), ('Jennie', 'Craig', 'JC@craig.com'), ('Dan', 'theGuy', 'dan@geop.com'),]

# 1. create a table 
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# print("this works!")

# example 1
# cursor.execute("""CREATE TABLE customers (
#   first_name text, 
#   last_name text, 
#   email text
# )""")

# cursor.execute("CREATE_TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")
# ^unprefered syntax

# SQLite3 datatypes: 
  # null (does is exist?), integer (num), real (num with decimal), text (string), blob (stored as it is)

# 2. querying the database 
# fetchone(), fetchmany(), fetchall()

# updating records
cursor.execute(""" 
    UPDATE customers set first_name = 'billy' 
    WHERE rowid = 1
""")

conn.commit() 
cursor.execute("SELECT rowid, * FROM customers") 

# print(cursor.fetchall())
items = cursor.fetchall()

for item in items: 
  print(item)

# commit our command 
# conn.commit()

# close the connection 
conn.close()