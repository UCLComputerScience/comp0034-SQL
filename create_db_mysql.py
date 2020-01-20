import mysql.connector
from mysql.connector import errorcode

# 1. Create the connection object (replace with your username and password for mysql)
conn = mysql.connector.connect(
    host="localhost",
    user="username",  # Replace with your MySQL user name
    passwd="pwd",  # Replace with your MySQL password 
    port=8889  # Replace with your port number
)

# 2. Create the cursor object
c = conn.cursor()

# 3. Create the database and the use it
c.execute("CREATE DATABASE IF NOT EXISTS address_mysql DEFAULT CHARACTER SET 'utf8'")
c.execute("USE address_mysql")

# 4. Create the tables
sql = '''CREATE TABLE `person` (
        `person_id` int NOT NULL AUTO_INCREMENT,
        `first_name` varchar(14) NOT NULL,
        `last_name` varchar(16) NOT NULL,
        PRIMARY KEY (`person_id`)
        ) ENGINE=InnoDB'''
c.execute(sql)

sql = '''CREATE TABLE `address` (
        `address_id` int NOT NULL AUTO_INCREMENT, 
        `street_number` varchar(6) NOT NULL, 
        `street_name` varchar(120) NOT NULL, 
        `postcode` varchar(10) NOT NULL, 
        `person_id` int NOT NULL, 
        PRIMARY KEY (`address_id`), 
        FOREIGN KEY (`person_id`) REFERENCES `person` (`person_id`)
        ) ENGINE=InnoDB'''
c.execute(sql)

# 4. Insert muliple rows into person
values = [('David', 'Coverdale'),
('Robert', 'Plant'),
('Joe', 'Elliott')]
sql = ("INSERT INTO person (first_name, last_name) VALUES (%s, %s)")
c.executemany(sql, values)

# 5. Insert single row into address (for the last person entered)
sql = "INSERT INTO address (street_number, street_name, postcode, person_id) VALUES (%s, %s, %s, %s)"
values = (12, 'My Road', 'SE1 9PZ', c.lastrowid)
c.execute(sql, values)

# 6. Insert address for a specific person (first select the id of the person and then insert the new address record)
sql = '''INSERT INTO address (street_number, street_name, postcode, person_id) VALUES (%s, %s, %s, 
            (SELECT person_id FROM person WHERE last_name LIKE "Plant"))'''
values = (134, 'The Street', 'EN7 3RT')
c.execute(sql, values)

# 7. Commit the changes
conn.commit()

# 8. Close the cursor and the connection
c.close()
conn.close()
