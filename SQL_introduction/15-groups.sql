-- Number by score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
GROUP BY number DESC;
