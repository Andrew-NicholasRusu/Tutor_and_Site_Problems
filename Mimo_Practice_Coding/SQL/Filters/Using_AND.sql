-- Sometimes we'll need to use more complex filters, like when looking for students majoring in Biology

SELECT *
FROM students
WHERE major = 'Biology' -- filters multiple conditions.
-- We then code the logical operator AND, followed by the second condition.
AND year = 1; -- chains 2 or more conditions

SELECT *
FROM inventory
WHERE manufacturer = 'Ford'; -- Selects only cars manufactured by Ford

SELECT *
FROM inventory
WHERE manufacturer = 'Ford'
AND year = 1970; -- Selects only cars manufactured by Ford in 1970

-- We can chain as many conditions as we want.

SELECT *
FROM students
WHERE major = 'Biology'
AND name = 'Lin Wong'
AND year = 3; -- Selects students majoring in 'Biology' whose name is 'Lin Wong' and are in the third year

SELECT *
FROM students
WHERE major = 'Biology'
AND year <> 1; -- Selects students majoring in 'Biology' that are not in the first year.

-- We can also use AND with the <, >, <=, and >= operators.

SELECT *
FROM students
WHERE year >= 2
AND year <= 4; -- Gives us items with a year between 2 and 4

SELECT *
FROM students
WHERE year BETWEEN 2 AND 4; -- Also selects items between 2 and 4

SELECT *
FROM inventory
WHERE manufacturer = 'Ford'
AND year >= 1970;

SELECT *
FROM inventory
WHERE ID < 3
AND year > 2000;

SELECT *
FROM inventory
WHERE year BETWEEN 1950 AND 1970;

SELECT *
FROM inventory 
WHERE year < 1970
AND manufacturer = 'Ford'
AND ID < 3;

SELECT *
FROM inventory 
WHERE year < 1970
AND manufacturer <> 'Ford';

SELECT *
FROM inventory
WHERE ID >= 2
AND year > 1955; -- Selects items with an ID of 2 or more, and a year greater than 1955.

SELECT *
FROM inventory
WHERE year >= 1970
AND year <= 2000; -- Selects items with a year between 1970 and 2000.

-- We can also use AND to chain conditions with BETWEEN, IN, and LIKE.

SELECT *
FROM students
WHERE major = 'Biology'
AND year BETWEEN 2 AND 4; -- Selects items where major = 'Biology; and year BETWEEN 2 AND 4

SELECT *
FROM inventory 
WHERE manufacturer IN ('Ford', 'Jaguar')
AND year BETWEEN 1950 AND 1960; -- Selects items manufactured by either Ford or Jaguar between the years 1950 and 1960.

SELECT *
FROM inventory
WHERE year BETWEEN 1950 AND 1960
AND manufacturer LIKE 'f%'; -- Checks if the manufacturer starts with the letter f

SELECT *
FROM inventory
WHERE ID BETWEEN 2 AND 4
AND year IN (1960, 1970); -- Selects items with an ID between 2 and 4, and a year of either 1960 ir 1970.


