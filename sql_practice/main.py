import sqlite3

# create a database and connect it 
# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()

# create the table
# cursor.execute("""CREATE TABLE test (
#     name test, 
#     age int 
# )""")

# insert values into the table 
# cursor.execute("INSERT INTO test VALUES (?,?)", ('crystal', '24'))

# insert many values 
# list = [('smol', '12'),('manini','13'),('noe', '15')]
# cursor.executemany("INSERT INTO test VALUES (?,?)", list)

# # select from the table 
# cursor.execute('SELECT * FROM test')

# delete from the table
# cursor.execute("DELETE FROM test WHERE rowid='1'")

# update a table 
# cursor.execute("UPDATE test SET name='beanie' WHERE rowid='2'")

# LIMIT /ORDER 
# cursor.execute("SELECT * FROM test ORDER BY name DESC LIMIT 2")
# print(cursor.fetchall())

# conn.commit()
# conn.close()

def select_all():
  conn = sqlite3.connect('test.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM test')
  stuff = cursor.fetchall()
  for i in stuff:
    print(i) 
  conn.commit()
  conn.close()
  
