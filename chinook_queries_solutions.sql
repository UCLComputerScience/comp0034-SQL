--Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
SELECT FirstName, LastName, CustomerId, Country
from Customer
WHERE Country NOT IN ("USA");

--Provide a query only showing the Customers from Brazil.
SELECT FirstName, LastName
FROM Customer
WHERE Country LIKE "Brazil";

/* Provide a query showing the Invoices of customers who are from Brazil.
Show the customer's full name, Invoice ID, Date of the invoice and billing country.*/
SELECT InvoiceId, InvoiceDate, BillingCountry, FirstName, LastName
FROM Customer
         JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
WHERE Country LIKE "Brazil";