-- To list the tables, we'll use sqlite_schema since we're using SQLite. sqlite_schema is a table that stores the schema of a database.

SELECT *
FROM sqlite_schema;
-- A schema contains information about a database, including details about the tables.

SELECT *
FROM sqlite_schema
WHERE type = "table";

SELECT name FROM sqlite_schema -- To make a list of tables, we only need the name column.
WHERE type = "table";

-- Now that we have the list of tables, let's delete the entire past_events table with the DROP TABLE query. 

DROP TABLE past_events;
SELECT name FROM sqlite_schema
WHERE type = "table";

