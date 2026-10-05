-- We can use a condition to select items that have a property with in a range, like movies with a rating between 9 and 10.
SELECT *
FROM movies
-- When writing the condition, we start with the column whose values we're checking, like rating here.
WHERE rating BETWEEN 9 AND 10;

SELECT *
FROM movies
WHERE rating BETWEEN 8 AND 9; -- Selecting movies rated 8 and 9.

SELECT *
FROM patients 
WHERE age BETWEEN 10 AND 20;

SELECT *
FROM patients 
WHERE age BETWEEN 30 AND 60;

SELECT *
FROM patients 
WHERE age BETWEEN 20 AND 30;

SELECT *
FROM patients 
WHERE age BETWEEN 20 AND 50;

