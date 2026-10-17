-- To simplify names like first_name or to give columns a different meaning within a query, we use aliasing.

SELECT first_name
FROM contacts; 

-- By giving a column an alias, we assign them a temporary name.
SELECT first_name AS user
FROM contacts; -- Here, we're renaming first_name to user.

SELECT score AS highest_score
FROM students
WHERE score > 7;

SELECT name AS team_leader
FROM students
WHERE name = 'Kim Lee';
-- Aliasing doesn't change the name in the original table. 

-- We can also use aliases when selecting multiple columns.
SELECT first_name AS user, email
FROM constacts;

-- When selecting multiple columns, we can provide an alias for each.
SELECT first_name AS user, email AS contact
FROM constacts;

SELECT name AS student, score
FROM students
WHERE score = 9;

SELECT name AS student, score AS max_score
FROM students
WHERE score = 9;


