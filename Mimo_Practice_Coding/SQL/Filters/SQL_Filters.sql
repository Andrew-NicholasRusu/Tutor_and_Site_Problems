SELECT *
FROM mario_games
WHERE release BETWEEN 2000 AND 2020;

SELECT *
FROM players
WHERE score BETWEEN 0 AND 50; -- Selects players with a score between 0 and 50

SELECT *
FROM players
WHERE score BETWEEN 70 AND 100;

SELECT *
FROM users 
WHERE email LIKE 'ben%'; -- Selects values that start with the text 'ben'

SELECT *
FROM users 
WHERE email LIKE '%.uk'; -- Selects values that end in '.uk'

SELECT *
FROM users 
WHERE email LIKE '%gmail%'; -- Selects the values that contain 'gmail'

SELECT *
FROM membership
WHERE type IN ('basic', 'pro'); 

SELECT *
FROM membership
WHERE type IN ('pro', 'free'); 

SELECT *
FROM membership
WHERE months_active IN (1, 12); -- Selects items with a months_active property to either 1 or 12

