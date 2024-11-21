-- Script to list all cities in the database `hbtn_0d_usa` along with their corresponding states.
-- Each record displays: cities.id - cities.name - states.name.
-- Results are sorted in ascending order by cities.id.
-- Author: [Your Name]

SELECT 
    cities.id, 
    cities.name, 
    states.name 
FROM 
    cities 
JOIN 
    states 
ON 
    cities.state_id = states.id 
ORDER BY 
    cities.id ASC;
