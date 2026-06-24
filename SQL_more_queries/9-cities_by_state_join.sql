-- Cities by States
SELECT *
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
