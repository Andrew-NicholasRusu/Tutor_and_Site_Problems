-- Type the query that enables making changes to the table.

ALTER TABLE player_info
ADD country varchar(255);
SELECT * FROM player_info;

-- Add a column named age to the player_info table of the int datatype. 

ALTER TABLE player_info
ADD age int;
SELECT * FROM player_info

-- Remove the rank column from the player_info table.

ALTER TABLE player_info
DROP COLUMN rank;
SELECT * FROM player_info;

ALTER TABLE player_info
RENAME COLUMN exp TO experience;
SELECT * FROM player_info;

-- Display all the information from the database schema.
SELECT * FROM sqlite_schema;

-- Display only the table rows having the type of table.
SELECT * FROM sqlite_schema
WHERE type = "table"; 

SELECT name FROM sqlite_schema
WHERE type = "table";

DROP TABLE past_reminders;
SELECT name FROM sqlite_schema
WHERE type="table";




