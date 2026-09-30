# Often, we'll want to filter for items that satisfy a condition, like only students majoring in Biology

SELECT *
FROM students
WHERE major = 'Biology';

SELECT *
FROM membership;

# Introduce a condition by coding the WHERE keyboard
SELECT *
FROM membership
WHERE type = 'basic';

# Code a condition so that we only get users with a membership of type pro.ALTER
SELECT *
FROM membership
WHERE type = 'pro';

# We use the = operator to check if two values are equal
SELECT *
FROM students
WHERE major = 'Biology'; # Here, we use = to check if the value of an entry in the major column equals Biology

SELECT *
FROM students
WHERE year = 1; # We can also use = with numeric properties, like selecting only students that have year value 1

# Unlike string values, number values like 1 don't need any quotes

SELECT *
FROM membership
WHERE type = 'free';

SELECT *
FROM membership
WHERE type = 'pro';

SELECT *
FROM membersip
WHERE months_active = 1;

# When using conditions, we don't have to select all columns with *. We can select only a couple, like name and year here.ALTER

SELECT name, year
FROM students
WHERE year = 1;
# This query gives us the name and year properties of all students that are in their first year

SELECT name, major
FROM students
WHERE year = 1;

SELECT name, email
FROM membership
WHERE type = 'pro';
