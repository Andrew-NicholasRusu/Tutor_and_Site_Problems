# Sometimes we want to select data that doesn't satisfy a condition, like all students that are not in their first year.ALTER
SELECT *
FROM students
WHERE year <> 1; #<> checks if a column's value is not equal to another

# We can also use the inequality operator with text values, like getting all students that don't major in 'Biology'
SELECT *
FROM students
WHERE major <> 'Biology';

SELECT *
FROM companies
WHERE years_active <> 3;

SELECT *
FROM companies
WHERE years_active <> 8;

# Code a condition to exclude the companies item with the name property 'Hyped' from the result table.
SELECT *
FROM companies
WHERE name <> 'Hyped';