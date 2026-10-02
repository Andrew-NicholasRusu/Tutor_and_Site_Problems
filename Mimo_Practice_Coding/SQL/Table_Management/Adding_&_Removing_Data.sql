# We can use INSERT INTO to add data for a new order.ALTER

INSERT INTO orders (name, id, price) # inserts a new row filled with new data in an existing table.
VALUES ("Teddy bear", 6574, 13); # Lets you add specific data to the newly added row.
SELECT * FROM orders;
# You have to specify the table and then the column names inside the brackets.

# You can also delete a row from an existing tabel based on a condition.

DELETE FROM orders
WHERE price < 10;
SELECT * FROM orders;

INSERT INTO users (name, id, password)
VALUES ("Alex", 98732, "alex001");
SELECT * FROM users;

DELETE FROM users
WHERE name = "Anita";
SELECT * FROM users;

DELETE FROM users;
SELECT * FROM users;

