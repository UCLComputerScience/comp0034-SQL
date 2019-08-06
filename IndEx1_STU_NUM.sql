/*
Write queries to answer the following questions
Save your work to this .sql file
Right click on the file name in the Project pane and select Refactor > Rename, and replace STU_NUM with your student number.
*/

--1. Which employees have 'IT' in their job title? (list their EmployeeId, FirstName, LastName and Title)
SELECT EmployeeId, FirstName, LastName, Title FROM Employee WHERE Title LIKE "IT%";

--2. List the names of all Artists and the titles of their albums
SELECT Artist.Name, Album.title FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId ORDER BY Artist.Name;

--3. Which track is features on the greatest number of times in playlists and how many times is it included? (display Trac
SELECT Track.Name, COUNT(PlaylistTrack.TrackId) FROM Track JOIN PlaylistTrack ON Track.TrackId = PlaylistTrack.TrackId LIMIT 5;

--4. Provide a list of the number of tracks by each artist


--5. How much money has been invoiced for the artist Deep Purple? (display each line item from the invoices and the total amount)
SELECT Artist.Name, SUM(InvoiceLine.UnitPrice*InvoiceLine.Quantity) FROM Artist
    JOIN Album on Artist.ArtistId = Album.ArtistId
    JOIN Track on Album.AlbumId = Track.AlbumId
    JOIN InvoiceLine on Track.TrackId = InvoiceLine.TrackId
WHERE Artist.Name LIKE "Deep Purple";

UPDATE InvoiceLine SET Quantity=2 WHERE InvoiceLineId=96;
UPDATE InvoiceLine SET Quantity=3 WHERE InvoiceLineId=129;
UPDATE InvoiceLine SET Quantity=4 WHERE InvoiceLineId=130;

SELECT Artist.Name, InvoiceLine.InvoiceLineId, InvoiceLine.UnitPrice, InvoiceLine.Quantity FROM Artist
    JOIN Album on Artist.ArtistId = Album.ArtistId
    JOIN Track on Album.AlbumId = Track.AlbumId
    JOIN InvoiceLine on Track.TrackId = InvoiceLine.TrackId
WHERE Artist.Name LIKE "Deep Purple";

/*
Provide SQL to create a SQLite database with the following:
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
 */

