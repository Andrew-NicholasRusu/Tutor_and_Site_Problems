# Select the name value for the oldest game under the alias oldest.

SELECT name AS oldest
FROM mario_games
WHERE release = 1983;

SELECT *
FROM flights
WHERE destination = 'Rome';

SELECT *
FROM flights
WHERE destination <> 'Rome';

# Code a condition to select all flights items where daily is not 1.

SELECT *
FROM flights
WHERE daily <> 1;

# Select the newest game's name under an alias, with SELECT name, AS and the alias newest.

SELECT name AS newest 
FROM mario_games
WHERE release = 1983;

SELECT name AS newest 
FROM mario_games
WHERE release = 2013;

# Code a comma (,) and then select the release column as well.

SELECT name AS newest, release
FROM mario_games
WHERE release = 2013;

SELECT name AS newest, release AS year # Renames the release column to year
FROM mario_games
WHERE release = 2013;

SELECT daily
FROM flights
WHERE destination <> 'Paris';

SELECT *
FROM chess_players
WHERE games_won < 1000;

SELECT *
FROM chess_players
WHERE games_won > 1000;

SELECT *
FROM chess_players
WHERE games_won <= 1162;



