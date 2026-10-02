# The basic syntax for creating a SQL table always starts with the keywords CREATE TABLE followed by the table name.

CREATE TABLE Directory (
    # Next, we want to declare which columns we want to create.
    floor INTEGER, company TEXT
);

# Once the table structure is created, all that's left is to insert a few values.

INSERT INTO Directory (floor, company) VALUES (1, 'Acme Inc.');
INSERT INTO Directory (floor, company) VALUES (2, 'Homeflix');

# We can add IF NOT EXISTS to esnure the table is only created if it doesn't exist already to avoid errors.

CREATE TABLE IF NOT EXISTS Directory (
    floor INTEGER, company TEXT
);

CREATE TABLE Birthdays (name TEXT, birthday TEXT);

CREATE TABLE Tickets (qty INTEGER, email TEXT);