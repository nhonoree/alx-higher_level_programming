-- List records where name is not null, ordered by score (highest first)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
