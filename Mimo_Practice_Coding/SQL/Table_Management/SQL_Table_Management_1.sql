INSERT INTO toys (name, price)
VALUES ("Beyblade", 13);
SELECT * FROM toys;

INSERT INTO toys (name, price)
VALUES ("Clay mix", 9);
SELECT * FROM toys;

# Delete all the values of the toys TABLE
DELETE FROM toys;
SELECT * FROM toys;

UPDATE Reservations SET time = '18:30' 
WHERE name = 'Powers';
SELECT * FROM Reservations;

UPDATE Songs SET certifications = 'Silver';
SELECT * FROM Songs;

UPDATE Songs SET streams = 130 
WHERE songname = 'Paradise';
SELECT * FROM Songs; 
# Increase Paradise's streams count to 130.

UPDATE Flights SET mealservice = 1 
WHERE number = 'PA76' OR number = 'PA67';
SELECT * FROM Flights;
# Sets mealservice to 1 for the flights numbered PA76 & PA67.

CREATE TABLE Tickets (
    qty INTEGER,
    name TEXT
);


