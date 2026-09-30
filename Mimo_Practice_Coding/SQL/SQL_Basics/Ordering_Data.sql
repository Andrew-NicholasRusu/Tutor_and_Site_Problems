# Understanding data is easier when the items are ordered like patients ordered by their name.ALTER

SELECT * # To order items in a table, we first need to SELECT them. 
FROM patients 
ORDER BY name;

# Why would we want to order them in a table?
# Answer: To easier understand and manages the stored data.ALTER

SELECT *
FROM countries 
ORDER BY name;

# Ordering by text properties like name is different than ordering by numeric properties like age. 

SELECT *
FROM patients
ORDER BY age;

# We can order items ascending starting with the smallest value, or descending.ALTER

SELECT *
FROM patients
ORDER BY age ASC; 

SELECT *
FROM patients
ORDER BY age DESC; # Orders items in descending order

SELECT *
FROM countries
ORDER BY gdp;

SELECT *
FROM countries
ORDER BY gdp ASC;

