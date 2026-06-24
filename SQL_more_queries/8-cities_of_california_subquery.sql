-- Cities of California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
      SELECT id FROM status WHERE name = 'California'
)
ORDER BY cities.id ASC;
