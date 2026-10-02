# Code athlete and time separeted by a comma, to get a table of all athletes.ALTER

SELECT athlete, time 
FROM race;

SELECT platform 
FROM games;

SELECT * # Selects all columns from the cerals table
FROM cereals;

SELECT athlete, country, time 
FROM race;

# Code SELECT, followed by DISTINCT and the platform column, to only select unique platform values.ALTER
SELECT DISTINCT platform 
FROM games;

SELECT name
FROM students
ORDER BY score;

SELECT name 
FROM students
ORDER BY score ASC;

SELECT * 
FROM students
ORDER BY score DESC;

SELECT *
FROM books
WHERE title = 'The Prince';

# Use WHERE and a condition to filter for books items where genre equals fiction
SELECT *
FROM books
WHERE genre = 'fiction';

# Code a condition to filter for items where the numeric year property equals 2011.ALTER
SELECT *
FROM books
WHERE year = 2011;

# Select only the title and year properties of items with the value 'non-fiction' in the genre column.ALTER
SELECT title, year
FROM books
WHERE genre = 'non-fiction';








