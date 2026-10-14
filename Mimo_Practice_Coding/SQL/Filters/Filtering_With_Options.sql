-- We've learned to use = to filter for items with a certain property.
SELECT *
FROM customers
WHERE country = 'France';

-- We use the IN keyword to specify options when filtering.
SELECT *
FROM customers
WHERE country IN ('France', 'Germany'); -- Selects countries with France and Germany

-- We can add many options as we want
SELECT *
FROM customers
WHERE country IN ('France', 'Germany', 'Japan');

SELECT *
FROM customers
WHERE country IN (0, 8); -- Selects values of either 0 or 8

SELECT *
FROM restaurants
WHERE cuisine = 'French'; -- Selects items in the cuisine property that are equal to French

SELECT *
FROM restaurants
WHERE cuisine = 'Indian'; -- Selects items in the cuisine property that are equal to Indian 

SELECT *
FROM restaurants
WHERE cuisine IN ('Italian', 'Indian'); -- Selects cuisines in Italian and Indian

SELECT *
FROM restaurants
WHERE cuisine IN ('Indian', 'French'); -- Filters cuisine that matches either Indian or French

SELECT *
FROM restaturants 
WHERE rating IN (3, 5);

SELECT *
FROM reastaurants
WHERE name In ('Naan', 'Les Amis', 'Giggetto'); 



 
