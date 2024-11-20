-- Title: Cities by States
-- Script to list all cities and their corresponding states from the database `hbtn_0d_usa`
-- Each record displays: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
