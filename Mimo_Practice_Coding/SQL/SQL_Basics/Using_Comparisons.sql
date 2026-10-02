# We can use conditions to select items having a property less than a threshold value, like chocolate items with a price of less than 2$.ALTER

SELECT *
FROM chocolate
WHERE price < 2;
# The less than operator (<) checks if the value on the left is less than that on the right

# To select items with a price less than or equal to a value like 2, we use the <= operator.

SELECT *
FROM chocoloate
WHERE price <= 2;

SELECT city
FROM pollution
WHERE pollution_index < 80;

SELECT *
FROM pollution
WHERE pollution_index < 72;

SELECT *
FROM pollution
WHERE pollution_index < 100;

SELECT *
FROM pollution
WHERE pollution_index < 150;

SELECT *
FROM pollution
WHERE pollution_index < 122;

SELECT *
FROM pollution
WHERE pollution_index <= 122;

# With conditions, we can select items that have a property over a certain threshold value, like all chocolate items with a price over 2$.

SELECT *
FROM chocolate
WHERE price > 2;
# The greater than operator > checks if the value on the left is greater than that on the right, like here with price > 2.

# To select values greater than or equal to a threshold, like price values of 2$ or more, we use the >= operator.

SELECT *
FROM chocolate
WHERE price >= 2;

SELECT *
FROM pollution
WHERE pollution_index >= 122;

SELECT *
FROM pollution
WHERE pollution_index > 100;

