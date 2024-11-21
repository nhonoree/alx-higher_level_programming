-- Script to list all genres by their total rating.
-- Results are sorted in descending order by rating.

SELECT 
    tv_genres.name, 
    SUM(ratings.rating) AS rating
FROM 
    tv_genres
JOIN 
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN 
    ratings ON tv_show_genres.show_id = ratings.show_id
GROUP BY 
    tv_genres.id
ORDER BY 
    rating DESC;
