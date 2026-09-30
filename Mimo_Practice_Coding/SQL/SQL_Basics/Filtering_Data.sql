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