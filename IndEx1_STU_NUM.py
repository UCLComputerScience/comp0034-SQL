"""
Provide Python code to create a SQLite database.
Your solution may make use of either Python with sqlite3 OR Python with sqlalchemy.
The structure of the database must be as follows:

Database name: Blog

Table names: Blogger, Post

Columns for Blogger table: blogger_id (integer, Foreign Key), username (text), email (text)

Columns for Post table: post_id (integer, Primary Key), title (text), post (text), blogger_id (integer, Foreign Key)

Add the following records to each table:
    [Blogger]
        1, weatherman, jo@bloggs.com
        2, gourmand123, ieatalot@finefood.co.uk
    [Post]
        1, Weather, Today the weather is fine., 1
        2, Lunch, Fish and chips with ice-cream., 2
        3, Dinner, Green thai-curry for main with mango sticky rice for dessert., 2
"""

