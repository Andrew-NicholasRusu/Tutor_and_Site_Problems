-- We can use aggregate functions to find out how many items we have in a table like wishlist.
SELECT COUNT(item)
FROM wishlist;

-- To get the number of rows in a table, we use the COUNT operation.
SELECT COUNT(*) -- Then, we code the wildcard * between parentheses().
FROM wishlist;

-- Like before, we use an alias to rename our result.
SELECT COUNT(*) AS items
FROM wishlist;

SELECT COUNT(*) 
FROM team;

SELECT COUNT(*) AS team_size
FROM team;

-- We can also count values in a column by coding a column name like price between parentheses
SELECT COUNT(price)
FROM wishlist; -- We omit empty table cells when counting by column

-- When counting by column, we can use DISTINCT to avoid counting duplicates
SELECT COUNT(DISTINCT item)
FROM wishlist;
-- DISTINCT comes before the column's name because we're getting the distinct values, and then counting them

SELECT COUNT(name)
FROM team; -- counts the values in the name column

SELECT COUNT(age)
FROM team; -- counts the values in the age column

SELECT COUNT(DISTINCT name)
FROM team; -- counts unique values in the name column

SELECT COUNT(DISTINCT age)
FROM team;

-- To sum up the number values in a column, we use the SUM operation
SELECT SUM(price)
FROM wishlist;

-- Like before, we can use an alias for the result of our operation
SELECT SUM(price) AS total_price
FROM wishlist;

SELECT SUM(age)
FROM team;

SELECT SUM(age) AS total_age
FROM team;




