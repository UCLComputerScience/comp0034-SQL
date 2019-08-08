import sqlite3

# Step 1: Create a connection object that represents the database
conn = sqlite3.connect('address_sqlite.db')

# Step 2: Create a cursor object
c = conn.cursor()

# Step 3: Create the person and address tables
c.execute('''
          CREATE TABLE person
          (person_id INTEGER PRIMARY KEY,
          first_name TEXT NOT NULL, 
          last_name TEXT NOT NULL)
          ''')

c.execute('''
          CREATE TABLE address
          (address_id INTEGER PRIMARY KEY,
          street_number TEXT, 
          street_name TEXT,
          postcode TEXT NOT NULL, 
          person_id INTEGER NOT NULL,
          FOREIGN KEY(person_id) REFERENCES person(person_id))
          ''')

# Insert data for a person using values from variables
# You could use: c.execute("INSERT INTO person VALUES('Jo', 'Bloggs')")
sql = "INSERT INTO person (first_name, last_name) VALUES (?, ?)"
values = ('Jo', 'Bloggs')
c.execute(sql, values)

# Insert the address for the person
# If you know the rowid you can use:  c.execute("INSERT INTO address VALUES(1, 'My Road', 'SE1 9PZ', 1)")
# Since we just inserted Jo this was the last insert so we can get the id of the last inserted row using c.lastrowid:
sql = "INSERT INTO address (street_number, street_name, postcode, person_id) VALUES (?, ?, ?, ?)"
values = (12, 'My Road', 'SE1 9PZ', c.lastrowid)
c.execute(sql, values)

# Insert multiple rows cursor.executemany()
sql = "INSERT INTO person (first_name, last_name) VALUES (?, ?)"
values = [('David', 'Coverdale'),
          ('Robert', 'Plant'),
          ('Joe', 'Elliott')]
c.executemany(sql, values)

# Step 5: Save (commit) the changes
conn.commit()

# Step 6 (optional): Close the connection if you are done with it
# Be sure any changes have been committed or they will be lost.
conn.close()
