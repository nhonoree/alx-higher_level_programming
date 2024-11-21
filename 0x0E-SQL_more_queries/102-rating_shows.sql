-- Script to list all shows by their total rating.
-- The total rating is calculated by summing up the ratings for each show.
-- Results are sorted in descending order by the total rating.

SELECT 
    tv_shows.title, 
    SUM(ratings.score) AS rating -- Ensure 'score' is the correct column for ratings
FROM 
    tv_shows
JOIN 
    ratings ON tv_shows.id = ratings.show_id
GROUP BY 
    tv_shows.id, 
    tv_shows.title -- Include 'tv_shows.title' in the GROUP BY clause
ORDER BY 
    rating DESC; -- Sort by the calculated total rating in descending order
