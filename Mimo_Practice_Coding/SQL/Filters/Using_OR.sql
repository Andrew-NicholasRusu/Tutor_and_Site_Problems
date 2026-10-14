-- We can use OR to chain different filtering options, like selecting students who are majoring in Biology or are in 
-- their first year.

SELECT *
FROM students 
WHERE major = 'Biology'
OR year = 1; -- Like AND, we use the logical operator (OR) to chain two or more conditions.

SELECT *
FROM students 
WHERE major = 'Physics'
OR year = 1; -- OR gives us items that satisfy atleast one of the chained conditions.

-- Using OR doesn't give dupliate results. Items that satisfy both conditions get selected only once.
SELECT *
FROM students 
WHERE major = 'Biology'
OR year = 1; 

SELECT *
FROM inventory 
WHERE ID = 1
OR manufacturer = 'Ford'; -- Selects items that satisfy at least one of the conditions linked with OR

SELECT *
FROM inventory 
WHERE manufacturer = 'Ford'
OR year = 2019; -- Chooses items with at least the manufacturer being Ford or if the year is 2019.

SELECT *
FROM inventory 
WHERE manufacturer = 'Jaguar'
OR year = 2019;

SELECT *
FROM inventory 
WHERE manufacturer = 'Bentley'
OR year = 1970;

-- We can use OR to chain any kind of conditions, like selecting studetns majoring in 'Biology' or students in a year <= 2.

SELECT *
FROM students 
WHERE major = 'Biology'
OR year <= 2; -- Gives us all students items with major = 'Biology' plus all studetns that are in their first and second years.

-- We can also use IN, BETWEEN, or LIKE. 
SELECT *
FROM students 
WHERE major = 'Biology'
OR name LIKE 's%;'; -- Selects students majoring in 'Biology' or having a name starting with s.

-- We can chain as many conditions as we want.
SELECT *
FROM students 
WHERE major = 'Biology'
OR name LIKE 's%;'
OR year = 1; 

SELECT *
FROM inventory 
WHERE ID = 2
OR year > 1970; -- Selects items with an ID of 2, or year greater than 1970

SELECT *
FROM inventory
WHERE ID BETWEEN 1 AND 3
OR manufacturer IN ('Jaguar', 'Ford'); -- Selects items with an ID between 1 and 3, or a manufacturer of either 'Jaguar' or 'Ford'

SELECT *
FROM inventory
WHERE year
BETWEEN 1950 AND 1970
OR manufacturer LIKE 'j%'; -- Selects items with a year between 1950 and 1970 or a manufacturer starting with the letter j.

SELECT *
FROM inventory
WHERE year
BETWEEN 1950 AND 1970
OR manufacturer LIKE 'j%'
OR ID = 4; --  Selects items with a year between 1950 and 1970 or a manufacturer starting with the letter j, or if the id is 4.

-- As a special case, a condition like major = 'History' OR major = 'Physics' is equivalent to major IN ('History', 'Physics').

SELECT *
FROM students
WHERE major = 'History'
OR major = 'Physics'; -- We can replace IN condtions with OR when rach condition uses the = operator and restricts the same column, like major.

-- If we replace the previous conditions with major IN ('History', 'Physics'), we get the same result table.
SELECT *
FROM students
WHERE major IN('History', 'Physics'); 

-- We can't use IN to replace a condition like major = 'History' OR name = 'Ava Smith', since it restricts two columns: major and name.
SELECT *
FROM students
WHERE major = 'History'
OR name = 'Ava Smith';

-- We can't replace with IN the condition major = 'History' OR major <> 'Physics' since both operators need to be =.
SELECT *
FROM students
WHERE major = 'History'
OR major <> 'Physics';

SELECT *
FROM inventory
WHERE ID IN (1, 3); -- equivalent to ID = 1 OR ID = 3.






