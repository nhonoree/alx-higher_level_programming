-- Task 20: Display the maximum temperature of each state, ordered by state name
-- This script calculates the maximum temperature for each state from the temperatures table,
-- and orders the result alphabetically by state name.

SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
