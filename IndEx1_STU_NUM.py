"""
Provide Python code to create a SQLite database and insert sample data.
Your solution may make use of either Python with sqlite3 OR Python with sqlalchemy.
The structure of the database must be as follows:

Database name: rain

Table names: user, forecast, city

Columns for user table: user_id (integer, Primary Key), username (text), email (text)

Columns for city table: city_id (integer, Primary Key), city (text)

Columns for forecast table: forecast_id (integer, Primary Key), city_id (integer, Foreign Key), user_id (integer, Foreign Key), datetime (text), forecast (text), commeny (text)

Insert the following records into each table:
    [user: user_id, username, email]
        1, weatherman, jo@bloggs.com
        2, itrains, itrains@alot.co.uk
        3, sunny, sunny_grl@sunshine.co.uk
    [city: city_id, city]
        1, London
        2, Manchester
        3, Birmingham
        4, Edinburgh
        5, Belfast
        6, Cardiff
    [forecast: forecast_id, city_id, user_id, datetime, forecast, comment]
        1, 2, 2, 2020-01-27 09:00:00, Moderate rain
        2, 6, 1, 2020-01-27 09:00:00, Heavy rain
        3, 1, 3, 2020-01-27 09:00:00, No rain

Note: SQLite does not have a datetime data type, use text and enter dates as YYYY-MM-DD HH:MM:SS
"""