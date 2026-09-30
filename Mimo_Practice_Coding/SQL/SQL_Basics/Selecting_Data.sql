# Many apps allow you to interact with stored data, such as usernames, passwords, or friends lists.
# This kind of data lives in a database.

SELECT name
FROM users;

SELECT title
FROM movies;

SELECT species
FROM animals;

# Select values from both the name and email columns by coding SELECT name, email
SELECT name, email
FROM users;

SELECT description, s, m, l 
FROM stock;

# To make things easier, we can select all columns of a table using the select all symbol * instead
SELECT*
FROM stock;