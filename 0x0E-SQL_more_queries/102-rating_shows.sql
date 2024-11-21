-- Script to list all shows by their total rating.
-- Results are sorted in descending order by rating.

SELECT 
    tv_shows.title, 
    SUM(ratings.rating) AS rating
FROM 
    tv_shows
JOIN 
    ratings ON tv_shows.id = ratings.show_id
GROUP BY 
    tv_shows.id
ORDER BY 
    rating DESC;
