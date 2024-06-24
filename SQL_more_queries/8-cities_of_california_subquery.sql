-- lists all the cities of california that can be found on a database
SELECT id, name FROM cities WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
