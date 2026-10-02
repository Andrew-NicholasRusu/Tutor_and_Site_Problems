# We don't want to simple INSERT a new table entry, otherwise we'll have duplicate reservations under the same name.
# Using SQL's UPDATE is a better and simple alternative

UPDATE Reservations SET time = '19:00' WHERE name = 'Smith';
SELECT * FROM Reservations;
# UPDATE cannot be used to insert new entries into a table

UPDATE Reservations SET name = 'Kelly' WHERE id = 4;
SELECT * FROM Reservations;

# An UPDATE statement always start with the keyword UPDATE followed by the table name.
UPDATE Directory SET company = 'Smith Tax & Audit';
SELECT * FROM Directory;

UPDATE Directory SET company = 'Smith Tax & Audit' WHERE floor = 3;
SELECT * FROM Directory;
# Adding a conditional into our UPDATE statement's WHERE clause allows us to update multiple rows satisfying our condition at once.

UPDATE Flights SET mealservice = True WHERE duration >= 6;
SELECT * FROM Flights;

UPDATE Songs
SET certifications = 'Platinum'
WHERE streams >= 100;

UPDATE SONGS SET streams = 88
WHERE songname = 'California Highway';
SELECT * FROM Songs;

UPDATE Directory SET company = '(Vacant)';
SELECT * FROM Songs;

UPDATE Reservations SET partysize = 2 WHERE name = 'Smith';
SELECT * FROM Reservations;

UPDATE Flights SET mealservice = 1 WHERE type = 'International';
SELECT * FROM Flights;



