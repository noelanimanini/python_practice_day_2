import sqlite3

# many_customers = [('West', 'Brown', 'WB@gmail.com'), ('Jennie', 'Craig', 'JC@craig.com'), ('Dan', 'theGuy', 'dan@geop.com'),]
# c.execute("""CREATE TABLE demo (
#     first_name text, 
#     last_name text, 
#     description text
# )
# """)

def show_all():
  conn = sqlite3.connect("demo.db")
  c = conn.cursor()
  c.execute("SELECT rowid, * FROM demo")

  items = c.fetchall()
  for item in items: 
    print(item)
  conn.commit()
  conn.close()

def add_one(first, last, email):
  conn = sqlite3.connect("demo.db")
  c = conn.cursor()
  c.execute("INSERT INTO demo VALUES (?,?,?)", (first, last, email))
  conn.commit()
  conn.close()

def add_many(list):
  conn = sqlite3.connect("demo.db")
  c = conn.cursor()
  c.executemany("INSERT INTO demo VALUES (?,?,?)", (list))
  conn.commit()
  conn.close()

def delete_one(id):
  conn = sqlite3.connect('demo.db')
  c = conn.cursor()
  c.execute("DELETE from demo WHERE rowid=(?)", id)
  conn.commit()
  conn.close()

def email_lookup(description):
  conn = sqlite3.connect("demo.db")
  c = conn.cursor()
  c.execute("SELECT * from demo WHERE description=(?)", (description,))
  items = c.fetchall()
  for item in items: 
    print(item)
  conn.commit()
  conn.close()
# c.execute("""INSERT INTO demo VALUES (
#   'crystal', 
#   'smal',
#   'smal@gmail.com'
# )

# """)


# import sqlite3 

# conn = sqlite3.connect("customer.db")

# # create a cursor
# cursor = conn.cursor()

# many_customers = [('West', 'Brown', 'WB@gmail.com'), ('Jennie', 'Craig', 'JC@craig.com'), ('Dan', 'theGuy', 'dan@geop.com'),]

# # 1. create a table 
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
# # print("this works!")

# # example 1
# # cursor.execute("""CREATE TABLE customers (
# #   first_name text, 
# #   last_name text, 
# #   email text
# # )""")

# # cursor.execute("CREATE_TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")
# # ^unprefered syntax

# # SQLite3 datatypes: 
#   # null (does is exist?), integer (num), real (num with decimal), text (string), blob (stored as it is)

# # 2. querying the database 
# # fetchone(), fetchmany(), fetchall()

# # updating records
# # cursor.execute(""" 
# #     UPDATE customers SET first_name = 'joahnna' 
# #     WHERE rowid = 4
# # """)

# # Deleting records
# # cursor.execute(""" 
# #     DELETE from customers WHERE rowid = 6
# # """)
# # cursor.execute("DROP TABLE customer")

# # drop table 

# conn.commit()

# # conn.commit() 
# # cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2") 


# # print(cursor.fetchall())
# items = cursor.fetchall()

# for item in items: 
#   print(items)

# # commit our command 
# # conn.commit()

# # close the connection 
# conn.close()