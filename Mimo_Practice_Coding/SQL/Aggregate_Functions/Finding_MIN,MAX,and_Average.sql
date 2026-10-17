-- Beyond just selecting items, we can use queries to perform operations on a table's data.

SELECT MIN(price)
FROM ticket;
-- To select the smallest value in a column, we code MIN and the column's name between parentheses.

-- For the greatest value, we code MAX and the column price between parentheses.
SELECT MAX(price)
FROM ticket;
-- You'll see in the result table that the selected column is no longer price, but MAX(price)
-- That is because we're actually selecting the result of an operation

SELECT MIN(km)
FROM running_distance;

SELECT MAX(km)
FROM running_distance;
-- Operations like MIN & MAX are called aggregate functions because they return a single result.

SELECT MIN(price) AS cheapest
FROM ticket; -- We can use an alias to rename the result

SELECT MIN(km) AS shortest_distance
FROM running_distance;

SELECT MAX(km) AS longest_distance
FROM running_distance;

-- Another example of an aggregate function is finding the average of a column's values.
SELECT AVG(price)
FROM ticket;
-- AVG adds all column values and then divides the result by the number of values.

-- Like before, we can rename the result with an  alias like average_price
SELECT AVG (price) AS average_price
FROM ticket;

SELECT AVG(km) AS average_distance
FROM running_distance;





